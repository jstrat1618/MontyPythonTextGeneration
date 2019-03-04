import re


#Print Header
def header():
    print("------------------------------------")
    print("              WELCOME!")
    print("------------------------------------")


def first_input():
    user_input = input("Start Typing: ")

    return user_input

def clean_word(word):

    word = word.lower()

    #Replace all punctuation
    word = re.sub(r'[^\w\s]', '', word)

    return word



def extract_last_word(text):
    words = text.split(" ")

    return words[-1]



def main():
    #print header
    header()

    #Ask user to start typing
    text = first_input()

    last_word = extract_last_word(text)

    last_word = clean_word(last_word)

    print(last_word)

    #Enter loop

    #make recommendations

    #show final text


if __name__ == '__main__':
    main()

