"""
File: hangman.py
Name:Owen Zhangjian
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    I finished this program thanks to the discussion with  my TA HuaJung Chang.

    This program plays hangman game. The game starts with dashed line.
    Players inputs one letter for each chance, and they have N_TURNS chances to win this game
    If the input letter is in the word, the program will update the letter in the word.
    """
    a = random_word()
    ans = ''
    for i in range(len(a)):
        if a[i].isalpha:
            ans += '-'
    print('The word looks like ' + ans)
    print('You have ' + str(N_TURNS) + ' wrong guesses left.')

    while True:
        first_guess = input('Your guess: ')  # the first guess
        if first_guess.islower():  # case insensitive
            first_guess = first_guess.upper()
        if not first_guess.isalpha() or len(first_guess) != 1:
            print('Illegal format.')
        else:
            break

    if a.find(first_guess) == -1:
        print('There is no ' + first_guess + "'s" + ' in the word.')
        print('The word looks like ' + ans)
        print('You have ' + str(N_TURNS-1) + ' wrong guesses left.')
        count = N_TURNS  # This variable was introduced to calculate the times of guesses.

        for i in range(len(a)):
            guess = input('Your guess: ')  # the second guess if the first guess is not in a.
            if guess.islower():  # case insensitive
                guess = guess.upper()

            if a.find(guess) == -1:

                if i == (N_TURNS - 2):
                    print('There is no ' + guess + "'s" + ' in the word.')
                    print('You are completely hung : (')
                    print('The word was ' + a)
                    break

                else:
                    print('There is no ' + guess + "'s" + ' in the word.')
                    print('The word looks like ' + ans)
                    print('You have ' + str(count - 2) + ' wrong guesses left.')
                    count -= 1
            else:
                s = ''
                for j in range(len(a)):
                    alphabet = a[j]
                    if alphabet == guess:
                        s += guess
                    else:
                        s += ans[j]
                ans = s
                if ans == a:
                    print('You are correct!')
                    print('You win!!')
                    print('The word was ' + a)
                    break
                else:
                    print('You are correct!')
                    print('The word looks like ' + s)
                    print('You have ' + str(count - 1) + ' wrong guesses left.')

    else:
        print('You are correct!')
        s = ''
        for i in range(len(a)):
            alphabet = a[i]
            if alphabet == first_guess:
                s += first_guess
            else:
                s += ans[i]
        ans = s
        print('The word looks like ' + s)
        print('You have ' + str(N_TURNS) + ' wrong guesses left.')
        count = N_TURNS

        for i in range(len(a)):
            guess = input('Your guess: ')  # the second guess if the first guess is in a.
            if guess.islower():  # case insensitive
                guess = guess.upper()

            if a.find(guess) == -1:

                if i == (N_TURNS - 1):
                    print('There is no ' + guess + "'s" + ' in the word.')
                    print('You are completely hung : (')
                    print('The word was ' + a)
                    break
                else:
                    print('There is no ' + guess + "'s" + ' in the word.')
                    print('The word looks like ' + ans)
                    print('You have ' + str(count-1) + ' wrong guesses left.')
                    count -= 1

            else:
                s = ''
                for j in range(len(a)):
                    alphabet = a[j]
                    if alphabet == guess:
                        s += guess
                    else:
                        s += ans[j]
                ans = s
                if ans == a:
                    print('You are correct!')
                    print('You win!!')
                    print('The word was ' + a)
                    break

                else:
                    print('You are correct!')
                    print('The word looks like ' + s)
                    print('You have ' + str(count) + ' wrong guesses left.')


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
