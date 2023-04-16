# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    operations.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jihoolee <jihoolee@student.42SEOUL.kr>     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/12 16:18:36 by jihoolee          #+#    #+#              #
#    Updated: 2023/04/16 11:52:39 by jihoolee         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
from operator import add, sub, mul, truediv, mod


def calc(operator, num1, num2):
    try:
        return operator(num1, num2)
    except Exception as e:
        return f'ERROR ({e.args[0]})'


def print_operations(arg1, arg2):
    print(f'Sum:\t\t{calc(add, arg1, arg2)}')
    print(f'Difference:\t{calc(sub, arg1, arg2)}')
    print(f'Product:\t{calc(mul, arg1, arg2)}')
    print(f'Quotient:\t{calc(truediv, arg1, arg2)}')
    print(f'Remainder:\t{calc(mod, arg1, arg2)}')


def main(argv):
    if (len(argv) == 1):
        print('Usage: python3 operations.py [num1] [num2]')
        print('Example:\n\tpython3 operations.py 10 3')
        return
    assert len(argv) == 3, 'two arguments are expected for this script'

    try:
        print_operations(int(argv[1]), int(argv[2]))
    except Exception as e:
        raise AssertionError('only integers')


if (__name__ == '__main__'):
    try:
        main(sys.argv)
    except Exception as e:
        print(f'{type(e).__name__}: {e.args[0]}')
