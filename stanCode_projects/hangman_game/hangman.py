"""
File: hangman.py
Name: Coco
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
    This program is a hangman game.
    """
    word = random_word()
    length = '-' * len(word)
    print('The word looks like ' + length)
    print('You have ' + str(N_TURNS) + ' wrong guesses left.')
    n = N_TURNS

    while n > 0 or not length.isalpha():
        w = upper(input('Your guess: '))
        if not w.isalpha() or len(w) > 1:
            print('Illegal format.')
        elif word.find(w) == -1:
            n -= 1
            print('There is no ' + w + '\'s in the word.')
            if n > 0:
                print('The word looks like ' + length)
                print('You have ' + str(n) + ' wrong guesses left.')
            else:
                break
        else:
            length_n = ''
            if w == word[0]:
                length_n += w
            else:
                length_n += length[0]
            a = 1
            for i in range(1, len(word)):
                k = 0
                if w == word[i]:
                    k += i
                for j in range(a, k + 1):
                    ch = length[j]
                    if j == k:
                        length_n += w
                        a = k + 1
                    else:
                        length_n += ch
            mid_n = len(length_n)
            for i in range(mid_n, len(word)):
                ch = length[i]
                length_n += ch
            length = length_n
            print('You are correct!')
            print('The word looks like ' + length)
            if not length.isalpha():
                print('You have ' + str(n) + ' wrong guesses left.')
            else:
                break

    if length.isalpha():
        print('You win!!')
        print('The word was: ' + word)
    else:
        print('You are completely hung : (')
        print('The word was: ' + word)


def upper(w):
    """
    :param w: string
    :return: upper letter string
    """
    ans = ''
    for i in range(len(w)):
        ch = w[i]
        if ch.islower():
            ans += ch.upper()
        else:
            ans += ch
    return ans


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
