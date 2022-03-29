from random_word import RandomWords
from colorama import Fore, Style

def word_of_day():
    while True:
        word = RandomWords().get_random_word(minLength = 5, maxLength=5)
        word = str(word)
        if word != 'None' and '-' not in word:
            break
    return word.upper()

def letters_words(word):
    list_letters = []
    for letter_word in word:
        list_letters.append(letter_word)
    return list_letters

def termtables(list_words):
    import termtables
    termtables.print(list_words)

def main():
    num_attempts = 0
    list_words = []
    word_day = word_of_day()
    list_main_word = letters_words(word_day)
    while num_attempts < 6:
        if num_attempts == 5:
                print(f'Almost!! The word of the day is {word_day}')
                break
        user_word = input('Enter a 5-letter Word: ').upper()
        if len(user_word) == 5 and user_word != '':
            num_attempts += 1
            list_user_word = letters_words(user_word)
            for i in range(5):
                if list_user_word[i] == list_main_word[i]:
                    list_user_word[i] = Fore.GREEN + list_user_word[i] + Style.RESET_ALL
                elif list_user_word[i] in list_main_word:
                    list_user_word[i] = Fore.YELLOW + list_user_word[i] + Style.RESET_ALL
            list_words.append(list_user_word)
            termtables(list_words)
            if user_word == word_day:
                print('Well done!! You find the word of the day!!')
                break
if __name__ == '__main__':
    main()