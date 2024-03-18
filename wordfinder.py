"""Word Finder: finds random words from a dictionary."""
import random

# file = open('words.txt','r')
# newfile= repr(file)
# lines = file.read().split("\n")
# random_word = random.choice(lines)
# print(random_word)

# class WordFinder:
#  # read the file
#     def __init__ (self, fileName):
#         self.file = fileName
class WordFinder:
    def __init__(self, fileName):
        self.fileName = fileName
        self.words = []
        self.read_words()
        self.print_word_count()

    def read_words(self):
        with open(self.fileName, 'r') as file:
            self.words = file.read().splitlines()

    def print_word_count(self):
        num_of_words = len(self.words)
        print(f"{num_of_words} words read")

    def random_word(self):
        return random.choice(self.words)

wf = WordFinder("words.txt")
print(wf.random_word())
print(wf.random_word())
print(wf.random_word())
print(wf.random_word())




