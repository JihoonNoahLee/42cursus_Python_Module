# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    filterwords.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jihoolee <jihoolee@student.42SEOUL.kr>     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/28 20:34:50 by jihoolee          #+#    #+#              #
#    Updated: 2023/03/28 21:10:51 by jihoolee         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys


def get_things_done(string: str, word_len: int):
    return [word for word in string.split() if len(word) > word_len]


def main(argv):
    assert len(argv) == 3
    # TODO: Think about punctuaction

    print(f'argv[1]: {argv[1]}')
    print(get_things_done(argv[1], int(argv[2])))



if (__name__ == '__main__'):
    try:
        main(sys.argv)
    except Exception as e:
        print('ERROR')
