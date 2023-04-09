# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    sos.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jihoolee <jihoolee@student.42SEOUL.kr>     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/09 15:05:02 by jihoolee          #+#    #+#              #
#    Updated: 2023/04/09 16:23:06 by jihoolee         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

MORSE_CODE = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', ' ': '/'
}


def encode(string: str, dictionary: dict) -> str:
    return ' '.join([dictionary[char] for char in string.upper()])


def main(argv):
    if (len(argv) == 1):
        print('At least one argument expected for this python script')
        print('usage: python3 sos.py [string]..')
    string = ' '.join(argv[1:])
    print(encode(string, MORSE_CODE))


if (__name__ == '__main__'):
    try:
        main(sys.argv)
    except Exception as e:
        print('ERROR')
