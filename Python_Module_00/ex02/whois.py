# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    whois.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jihoolee <jihoolee@student.42SEOUL.kr>     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/12 16:17:50 by jihoolee          #+#    #+#              #
#    Updated: 2023/04/15 19:55:15 by jihoolee         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys


def print_whois(num_str):
    try:
        num = int(num_str)
    except Exception as e:
        raise AssertionError('argument is not an integer')
    if (num == 0):
        print("I'm Zero.")
    elif (num % 2):
        print("I'm Odd.")
    else:
        print("I'm Even.")


def main(argv):
    if (len(argv) == 1):
        print('One argument expected for this python script')
        print('usage: python whois.py [number]')
        return
    assert len(argv) == 2, 'more than one argument are provided'

    print_whois(argv[1])


if __name__ == '__main__':
    try:
        main(sys.argv)
    except Exception as e:
        print(f'{type(e).__name__}: {e.args[0]}')
