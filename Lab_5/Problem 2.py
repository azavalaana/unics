import heapq


class Element:
    def __init__(self, count, word):
        self.count = count
        self.word = word

    def __lt__(self, other):
        if self.count == other.count:
            return self.word > other.word
        return self.count < other.count

    def __eq__(self, other):
        return self.count == other.count and self.word == other.word


from collections import Counter


def count_list(word_set):
    # Create list of all the words in the string
    word_list = word_set.split()

    # Get the count of each word.
    word_counted = Counter(word_list)
    return word_counted


def heapify_word(word_count, k):
    freqs = []
    heapq.heapify(freqs)
    for word, count in word_count.items():
        heapq.heappush(freqs, (Element(count, word), count, word))
        if len(freqs) > k:
            heapq.heappop(freqs)

    res = []
    for _ in range(k):
        res.append(heapq.heappop(freqs)[2])
    return res[::-1]


def heapify_num(word_count, k):
    freqs = []
    heapq.heapify(freqs)
    for word, count in word_count.items():
        heapq.heappush(freqs, (Element(count, word), count, word))
        if len(freqs) > k:
            heapq.heappop(freqs)

    res = []
    for _ in range(k):
        res.append(heapq.heappop(freqs)[1])
    return res[::-1]


def print_freq(words, frqs):
    for i in range(len(words)):
        print(words[i], frqs[i])


def main():
    word_set = " This is a series of strings to count " \
               "many words . They sometime hurt and words sometime inspire " \
               "Also sometime fewer words convey more meaning than a bag of words " \
               "Be careful what you speak or what you write or even what you think of. " \

    word_count = count_list(word_set)

    k = int(input("Please type the k of frequent words:"))

    print("Type 1 to print using counter")
    option = input("Type 2 to print using heap \n")

    if option == '1':
        print(word_count.most_common(k))
    elif option == '2':
        res_w = heapify_word(word_count, k)
        res_n = heapify_num(word_count, k)
        print_freq(res_w, res_n)

    # print(res_w)
    # print(res_n)


main()
