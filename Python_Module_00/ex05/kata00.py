# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    kata00.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jihoolee <jihoolee@student.42SEOUL.kr>     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/12 16:24:03 by jihoolee          #+#    #+#              #
#    Updated: 2023/03/18 23:40:50 by jihoolee         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Put this at the top of your kata00.py file
kata = (19, 42, 21)


def main():
    print(f'The {len(kata)} numbers are: {", ".join(map(str, kata))}')


if (__name__ == '__main__'):
    main()
