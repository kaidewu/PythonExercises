from random_word import RandomWords

def word_of_day():
    while True:
        word = RandomWords().get_random_word(minLength = 5, maxLength=5).upper()
        if word != None or '-' not in word:
            break
    return word

def main():
    while True:
        user_word = input('Enter a 5-letter Word: ').upper()
        if len(user_word) == 5 or user_word != '':
            pass
    list_user_word = []
    for letter_user_word in user_word:
        list_user_word.append(letter_user_word)


main()