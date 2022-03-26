from random_word import RandomWords
from prettytable import PrettyTable

def word_of_day():
    while True:
        word = RandomWords().get_random_word(minLength = 5, maxLength=5)
        if word != None or '-' not in word:
            break
    return word.upper()

def letters_words(word):
    list_letters = []
    for letter_word in word:
        list_letters.append(letter_word)
    return list_letters

def main():
    while True:
        user_word = input('Enter a 5-letter Word: ').upper()
        if len(user_word) == 5 or user_word != '':
            break
    list_user_word = letters_words(user_word)
    list_main_word = letters_words(word_of_day())


main()