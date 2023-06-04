# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    filterwords.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jihoolee <jihoolee@student.42SEOUL.kr>     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/28 20:34:50 by jihoolee          #+#    #+#              #
#    Updated: 2023/04/16 12:33:10 by jihoolee         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
from string import punctuation


def split_longer(string: str, word_len: int):
    string = string.translate(str.maketrans('', '', punctuation))
    return [word for word in string.split() if len(word) > word_len]


def main(argv):
    assert len(argv) == 3

    print(split_longer(argv[1], int(argv[2])))


if (__name__ == '__main__'):
    try:
        main(sys.argv)
    except Exception as e:
        print('ERROR')
