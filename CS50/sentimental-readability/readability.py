import re
from cs50 import get_string


def count_letters(text):
    count = 0
    for letter in text:
        if letter.isalpha():
            count += 1
    # print (count)
    return count


def count_words(text):
    # print((text.split(' ')))
    return len(text.split(' '))


def count_sentences(text):
    # print((re.split('[?.!]',text)))
    return len((re.split('[?.!]', text))) - 1
    

def main():
    text = get_string("Text: ")
    letters = count_letters(text)
    words = count_words(text)
    sen = count_sentences(text)
    index = index = round(0.0588 * letters / words * 100 -
                          0.296 * sen / words * 100 - 15.8)
    print(index)
    if index < 1:
        print("Before Grade 1")
    elif index >= 1 and index <= 16:
        print(f"Grade {index}")
    else:
        print("Grade 16+")


main()