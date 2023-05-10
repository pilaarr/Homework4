import requests
import string

Q = requests.get("https://www.gutenberg.org/cache/epub/996/pg996.txt")
with open("quixote.txt", "w", encoding='utf-8') as Quixote:
    Quixote.write(Q.text)
H = requests.get("https://www.gutenberg.org/files/27761/27761-0.txt")
with open("hamlet.txt", "w", encoding='utf-8') as Hamlet:
    Hamlet.write(H.text)


def count_words_quixote(filename="quixote.txt"):
    """
    Count the words in the book
    :param filename:
    :return: a dictionary
    """
    words_dict_quixote = {}
    with open("quixote.txt", "r", encoding="utf-8") as f:
        for line in f:
            # remove punctuation from the line
            for p in string.punctuation:
                line = line.replace(p, "")
            line_words = line.split()
            for word in line_words:
                words_dict_quixote[word] = words_dict_quixote.get(word, 0) + 1  # to add the word to the dict and give it a value based on how many times it appears
    return words_dict_quixote

def count_words_hamlet(filename="hamlet.txt"):
    """
    Count the words in the book
    :param filename:
    :return: a dictionary
    """
    words_dict_hamlet = {}
    with open("hamlet.txt", "r", encoding="utf-8") as g:
        for line in g:
            # remove punctuation from the line
            for q in string.punctuation:
                line = line.replace(q, "")
            line_words = line.split()
            for word in line_words:
                words_dict_hamlet[word] = words_dict_hamlet.get(word, 0) + 1  # to add the word to the dict and give it a value based on how many times it appears
    return words_dict_hamlet

words_dict_quixote = count_words_quixote()
# print(words_dict_quixote)
# print(len(words_dict_quixote))
words_dict_hamlet = count_words_hamlet()
# print(words_dict_hamlet)
# print(len(words_dict_hamlet))
print(f"'Don Quixote has {len(words_dict_quixote)} unique words, while 'Hamlet' has {len(words_dict_hamlet)} unique words.")

# compare unique words
if len(words_dict_quixote) < len(words_dict_hamlet):
    print("Thus, 'Don Quixote' has less unique words than 'Hamlet'.")
elif len(words_dict_quixote) > len(words_dict_hamlet):
    print("Thus, 'Don Quixote' has more unique words than 'Hamlet'.")
else:
    print("Thus, 'Don Quixote' has the same number of unique words than 'Hamlet'.")

# compare ratio
ratio_quixote = len(words_dict_quixote)/sum(words_dict_quixote.values())
ratio_hamlet = len(words_dict_hamlet)/sum(words_dict_hamlet.values())
print(f"'Don Quixote has a ratio of unique words/total words of {ratio_quixote}, while that of 'Hamlet' is {ratio_hamlet}.")

if ratio_quixote < ratio_hamlet:
    print("Thus, 'Don Quixote' has a lower ratio of unique words/total words than 'Hamlet'.")
elif ratio_quixote > ratio_hamlet:
    print("Thus, 'Don Quixote' has a higher ratio of unique words/total words than 'Hamlet'.")
else:
    print("Thus, 'Don Quixote' has the same ratio of unique words/total words than 'Hamlet'.")