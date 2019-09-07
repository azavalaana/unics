from operator import attrgetter
from datetime import datetime

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
    # method to travers the list of comments and subcomments recursively
    for subreply in comments:
        # check if there is a subreply to get into the comment's subreplies list
        if len(subreply.replies) > 0:
            process_comments(subreply.replies, pos, neg, neu)
        # check whether the comment is negative positive or neutral and get it to corresponding list
        if get_text_negative_proba(subreply.body) > 0.5:
            neg.append(subreply)
        elif get_text_positive_proba(subreply.body) > 0.5:
            pos.append(subreply)
        elif get_text_neutral_proba(subreply.body) > 0.5:
            neu.append(subreply)

    return


def print_comments(test, comments, pos_replies, neg_replies, neu_replies):
    # print method: to  show the data collected from the lists of comments
    print('Test case No.', test)
    print('The total amount of comments is:', len(comments), 'and they have, \n')

    # print the number of negative, positive and neutral comments and subcomments
    print(len(neg_replies), 'Negative (Sub)comments')
    print(len(pos_replies), 'Positive (Sub)comments')
    print('And, ', len(neu_replies), 'Neutral (Sub)comments \n')


def oldest_comment(comments, n):
    comments.sort(key=attrgetter('created_utc'))
    if n >= len(comments):
        print('that\'s all the comments in this category!')
        return
    else:
        print('No.', n+1, 'Oldest Comment:', comments[n].body)
        print('Date posted:', datetime.utcfromtimestamp(comments[n].created_utc).strftime('%Y-%m-%d %H:%M:%S'))
        print('Want to see the next oldest? (y/n)')
        x = str(input())
        if x == 'y':
            n = n + 1
            oldest_comment(comments, n)
        else:
            return


def menu(pos_replies, neg_replies):
    print('Want to see the oldest positive comment? (y/n)')
    x = str(input())
    if x == 'y':
        n = 0
        oldest_comment(pos_replies, n)

    print('Want to see the oldest negative comment? (y/n)')
    x = str(input())
    if x == 'y':
        n = 0
        oldest_comment(neg_replies, n)


def next_test():
    print('Want to see our next test case? (y/n)')
    x = str(input())
    if x == 'y':
        return
    else:
        exit(0)

def main():
    test_case = 1
    # Test Case #1: Default test case of the Lab #
    comments = get_submission_comments(
        'https://www.reddit.com/r/learnprogramming/comments/5w50g5/eli5_what_is_recursion/')

    pos_replies = []
    neg_replies = []
    neu_replies = []

    process_comments(comments, pos_replies, neg_replies, neu_replies)
    print_comments(test_case, comments, pos_replies, neg_replies, neu_replies)
    menu(pos_replies, neg_replies)
    next_test()
    test_case += 1

    # Test Case #2: Considerable amount of comments and replies to practice and interesting topic #
    comments = get_submission_comments(
        'https://www.reddit.com/r/productivity/comments/cyqk6p/i_figured_out_why_i_cant_sit_and_focus_on_one/')

    pos_replies = []
    neg_replies = []
    neu_replies = []

    process_comments(comments, pos_replies, neg_replies, neu_replies)
    print_comments(test_case, comments, pos_replies, neg_replies, neu_replies)
    menu(pos_replies, neg_replies)
    next_test()
    test_case += 1

    # Test Case #3: High Probability of Positive Comments test case #
    comments = get_submission_comments(
        'https://www.reddit.com/r/productivity/comments/aa305p/tips_and_life_hacks_for_staying_motivated_and/')

    pos_replies = []
    neg_replies = []
    neu_replies = []

    process_comments(comments, pos_replies, neg_replies, neu_replies)
    print_comments(test_case, comments, pos_replies, neg_replies, neu_replies)
    menu(pos_replies, neg_replies)
    next_test()
    test_case += 1

    # Test Case #4 High Probability of Negative Comments test case #
    print('This post is a little long so it may take a couple of seconds \n Please wait.')
    comments = get_submission_comments(
        'https://www.reddit.com/r/worldnews/comments/cvnm3y/donald_trump_skips_g7_talks_on_climate_crisis_and/')

    pos_replies = []
    neg_replies = []
    neu_replies = []

    process_comments(comments, pos_replies, neg_replies, neu_replies)
    print_comments(test_case, comments, pos_replies, neg_replies, neu_replies)
    menu(pos_replies, neg_replies)
    test_case += 1

    print('Lab 1 Finished Successfully. Have a Good Day!')

main()
