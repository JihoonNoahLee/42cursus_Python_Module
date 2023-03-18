# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    kata01.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jihoolee <jihoolee@student.42SEOUL.kr>     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/12 16:24:11 by jihoolee          #+#    #+#              #
#    Updated: 2023/03/18 23:48:50 by jihoolee         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Put this at the top of your kata01.py file
kata = {
    'Python': 'Guido van Rossum',
    'Ruby': 'Yukihiro Matsumoto',
    'PHP': 'Rasmus Lerdorf',
}


def main():
    for language, creator in kata.items():
        print(f'{language} was created by {creator}')


if (__name__ == '__main__'):
    main()
