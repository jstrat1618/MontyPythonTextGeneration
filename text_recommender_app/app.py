import re
import os
import json
from word_suggestion import WordSuggestion

#Print Header
def header():
    print("------------------------------------")
    print("              WELCOME!")
    print("------------------------------------")


def load_data():
    data_path = os.path.abspath("../data/monty_python_holy_grail_word_data.json")

    with open(data_path) as file:
        data = json.load(file)

    return data

def process_word_data(data):
    word_data = {}

    for key,val in data.items():
        word_data[key] = WordSuggestion(key, val[0], val[1])

    return word_data





def first_input():

    user_input = input("Start Typing: ")

    user_input = user_input.strip()

    if user_input == "1":
        user_input = 'of'
    elif user_input == "2":
        user_input = "the"
    elif user_input == "3":
        user_input = 'because'

    return user_input

def clean_word(word):

    #Replace all punctuation
    word = re.sub(r'[^\w\s]', '', word)

    return word



def extract_last_word(text):
    words = text.split(" ")

    return words[-1]

def append_text(next_text, text_so_far):
    if next_text in ['.', '?', '!', ',', "'", '"']:
        text = text_so_far + next_text

    else:
        text = text_so_far + " " + next_text

    return text

def generic_suggestion():
    print("Press: [1] of [2] the [3] because  [Q]uit")
    user_input = input("Keep typing: ")

    user_input = user_input.strip()

    if user_input == "1":
        user_input = 'of'
    elif user_input == "2":
        user_input = "the"
    elif user_input == "3":
        user_input = 'because'

    return user_input

def get_next_word_with_data(last_word, word_data):
    word = word_data[last_word]

    display = word.show_suggestions()

    print(display)

    user_input = input("Keep typing: ")

    if user_input == "1":
        user_input = word.suggestions[0]
    elif user_input == "2":
        user_input = word.suggestions[1]
    elif user_input == "3":
        user_input = word.suggestions[2]

    return user_input

def next_text(last_word, word_data):

    if last_word in word_data.keys():
        next_text = get_next_word_with_data(last_word, word_data)

    else:
        next_text = generic_suggestion()

    return next_text


def main_loop(text_so_far, word_data):

    last_word = extract_last_word(text_so_far)

    while last_word != "Q":
        print(text_so_far)

        last_word = clean_word(last_word)

        next_input = next_text(last_word, word_data)

        text_so_far = append_text(next_input, text_so_far)

        last_word = extract_last_word(text_so_far)


    return text_so_far



def main():

    #Load Data
    data = load_data()

    #Process Data
    word_data = process_word_data(data)

    #print header
    header()

    #Ask user to start typing
    text = first_input()

    #Enter loop
    main_text = main_loop(text_so_far=text, word_data = word_data)

    print("You Wrote: ")
    print(main_text)


if __name__ == '__main__':
    main()

