# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    count.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jihoolee <jihoolee@student.42SEOUL.kr>     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/12 16:18:13 by jihoolee          #+#    #+#              #
#    Updated: 2023/04/16 12:16:12 by jihoolee         ###   ########.fr        #
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
    assert type(string) is str, 'agrument type is not str'

    print(f"""The text contains {len(string)} character(s):
- {len([char for char in string if char.isupper()])} upper letter(s)
- {len([char for char in string if char.islower()])} lower letter(s)
- {len([char for char in string if char in punctuation])} punctuation mark(s)
- {len([char for char in string if char.isspace()])} space(s)""")


def main(argv):
    assert len(argv) <= 2, 'one argument must be provided'

    if (len(argv) == 1):
        text_analyzer()
    else:
        text_analyzer(argv[1])


if (__name__ == '__main__'):
    try:
        main(sys.argv)
    except Exception as e:
        print(f'{type(e).__name__}: {e.args[0]}')
