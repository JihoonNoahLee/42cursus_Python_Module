# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    count.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jihoolee <jihoolee@student.42SEOUL.kr>     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/12 16:18:13 by jihoolee          #+#    #+#              #
#    Updated: 2023/03/12 16:18:18 by jihoolee         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
from string import punctuation


def text_analyzer(string=None):
    """
    This function counts the number of upper characters, lower characters,
    punctuation and spaces in a given text.

    when the string is not provieded or None, prompt user to provide a string

    Args:
        string(str, optional): a string to be counted.

    Returns:
        None
    """
    if (string is None):
        string = input('What is the text to analyze?\n>> ')
    try:
        if (type(string) is not str):
            raise AssertionError('argument type is not a string')
    except Exception as e:
        print(f'{type(e).__name__}: {e.args[0]}')
        return
    print(f"""The text contains {len(string)} character(s):
- {len([char for char in string if char.isupper()])} upper letter(s)
- {len([char for char in string if char.islower()])} lower letter(s)
- {len([char for char in string if char in punctuation])} punctuation mark(s)
- {len([char for char in string if char.isspace()])} space(s)""")


def main(argv):
    try:
        if len(argv) == 0 or len(argv) > 2:
            raise AssertionError('one argument must be provided')
        text_analyzer(argv[1])
    except Exception as e:
        print(f'{type(e).__name__}: {e.args[0]}')


if (__name__ == '__main__'):
    main(sys.argv)
