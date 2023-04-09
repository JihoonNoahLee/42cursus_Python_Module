# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    guess.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jihoolee <jihoolee@student.42SEOUL.kr>     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/09 16:25:11 by jihoolee          #+#    #+#              #
#    Updated: 2023/04/09 16:50:30 by jihoolee         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
from random import randint


SECRET_MSG = '''The answer to the ultimate question of life, \
the universe and everything is 42.
Congratulations! You got it on your first try!
'''


def exec_guess():
    trial = 0
    answer = randint(1, 99)
    guess = 0

    while (guess != answer):
        guess = input('What\'s your guess between 1 and 99?\n>> ')
        trial += 1
        if (guess == 'exit'):
            print('Goodbye!')
            return
        elif (int(guess) == 42 and trial == 1):
            print(SECRET_MSG)
            return
        if (int(guess) == answer):
            break
        elif (int(guess) < answer):
            print('Too low!')
        else:
            print('Too high!')
    print('Congratulations. you\'ve got it!')
    print(f'You won in {trial} attempts!')


def main(argv):
    assert (len(argv) == 1)

    print('''This is an interactive guessing game!
You have to enter a number between 1 and 99 to find out the secret number.
Type 'exit' to end the game.
Good luck!\n''')
    exec_guess()


if (__name__ == '__main__'):
    try:
        main(sys.argv)
    except Exception as e:
        print('ERROR')
