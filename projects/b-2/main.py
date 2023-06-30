# function to read all words in words.txt
import random

def get_words():
    temp = []
    try:
        with open("words.txt","r")as f:
            temp +=[x.strip() for x in f.readlines()]
    except:
        temp+=["test","sample","random","words"]
    return temp


if __name__ == '__main__':

    user_name = input("Enter your name: ")
    print("Welcome to the game",user_name)
    print("You have 12 chances to guess the word")

    # get all words from words.txt
    words = get_words()
    # select a random word from words
    word:str = random.choice(words)
    # print(word)
    # create a list of underscores
    guess_word = ["_"]*len(word)
    # print(guess_word)
    # create a list of guessed letters
    guessed_letters = []
    # create a list of wrong letters
    wrong_letters = []
    # create a list of correct letters
    correct_letters = []
    # create a list of chances
    chances = 12

    # print(hints)

    while chances > 0:

        print("Chances left: ",chances)
        print("Guessed letters: ",guessed_letters)
        print("Wrong letters: ",wrong_letters)
        print("Correct letters: ",correct_letters)
        print("Guess word: ",guess_word)
        print("--------------------------------------------------")
        # take input from user
        user_input = input("Enter a letter: ")
        # check if user input is a letter
        if not user_input.isalpha():
            print("Enter a letter")
            continue
        # check if user input is already guessed
        if user_input in guessed_letters:
            print("Already guessed")
            continue
        # check if user input is in word
        if user_input in word:
            # add user input to guessed letters
            guessed_letters.append(user_input)
            # add user input to correct letters
            correct_letters.append(user_input)
            # find index of user input in word
            for i in range(len(word)):
                if word[i] == user_input:
                    # replace underscore with user input
                    guess_word[i] = user_input


            # check if guess word is equal to word
            if "".join(guess_word) == word:
                print("You won")
                break
            else:
                continue
        else:
            # add user input to guessed letters
            guessed_letters.append(user_input)
            # add user input to wrong letters
            wrong_letters.append(user_input)
            # decrease chances by 1
            chances -= 1
            continue
    else:
        print("You lost")
        print("Word was",word)
