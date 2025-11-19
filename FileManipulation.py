# File Manipulation - Count word occurrences in a file

from collections import Counter
import re

# Function to count words in a file
def count_words(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            text = f.read().lower()
            words = re.findall(r'\b\w+\b', text)
            word_count = Counter(words)
            for word in sorted(word_count):
                print(f"{word}: {word_count[word]}")
    except FileNotFoundError:
        print("File not found. Please check the file name or path.")

# Main program
filename = input("Enter the filename (with path if needed): ")
count_words(filename)
