import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import praw

reddit = praw.Reddit(client_id='naQfnUORqi03oQ',
                     client_secret='ZgMm3ScA_gzTvFcJ8_w8vnwagro',
                     user_agent='frstdengineer'
                     )

nltk.download('vader_lexicon')
sid = SentimentIntensityAnalyzer()


def get_text_negative_proba(text):
    return sid.polarity_scores(text)['neg']


def get_text_neutral_proba(text):
    return sid.polarity_scores(text)['neu']


def get_text_positive_proba(text):
    return sid.polarity_scores(text)['pos']


def get_submission_comments(url):
    submission = reddit.submission(url=url)
    submission.comments.replace_more()

    return submission.comments


def process_comments(comments, pos, neg, neu):
    for subreply in comments:
        if len(subreply.replies) > 0:
            process_comments(subreply.replies, pos, neg, neu)
        if get_text_negative_proba(subreply.body) > 0.5:
            neg.append(subreply)
        elif get_text_positive_proba(subreply.body) > 0.5:
            pos.append(subreply)
        elif get_text_neutral_proba(subreply.body) > 0.5:
            neu.append(subreply)

    return


def main():
    comments = get_submission_comments(
        'https://www.reddit.com/r/learnprogramming/comments/5w50g5/eli5_what_is_recursion/')

    pos_replies = []
    neg_replies = []
    neu_replies = []

    process_comments(comments, pos_replies, neg_replies, neu_replies)

    print(comments[0].body, '\n')

    print('After traversing the whole post there were:')
    print(len(neg_replies), 'Negative Comments')
    print(len(pos_replies), 'Positive Comments')
    print('And, ', len(neu_replies), 'Neutral Comments')

    comments = get_submission_comments(
        'https://www.reddit.com/r/StarWars/comments/3qvj6w/theory_jar_jar_binks_was_a_trained_force_user/')

    pos_replies = []
    neg_replies = []
    neu_replies = []

    process_comments(comments, pos_replies, neg_replies, neu_replies)

    print(comments[0].body, '\n')

    print('After traversing the whole post there were:')
    print(len(neg_replies), 'Negative Comments')
    print(len(pos_replies), 'Positive Comments')
    print('And, ', len(neu_replies), 'Neutral Comments')

main()
