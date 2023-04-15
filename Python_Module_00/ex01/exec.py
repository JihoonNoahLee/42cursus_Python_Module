# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    exec.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jihoolee <jihoolee@student.42SEOUL.kr>     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/12 15:56:26 by jihoolee          #+#    #+#              #
#    Updated: 2023/04/15 19:58:08 by jihoolee         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys


def revert_case(string: str) -> str:
    return ''.join([
        char.lower() if char.isupper() else
        char.upper() for char in string])


def main(argv):
    argc = len(argv)

    if (argc == 1):
        print('Argument expected for this python script')
        print('Usage: python3 exec.py [string]')
        return
    string = ' '.join(argv[1:])
    print(revert_case(string[::-1]))


if (__name__ == '__main__'):
    main(sys.argv)
