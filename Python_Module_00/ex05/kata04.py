# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    kata04.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jihoolee <jihoolee@student.42SEOUL.kr>     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/12 16:24:31 by jihoolee          #+#    #+#              #
#    Updated: 2023/03/12 16:24:32 by jihoolee         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

kata = (2019, 9, 25, 3, 30)


def main():
    year, month, date, hour, minute = kata
    print(f'{month:02}/{date:02}/{year:04} {hour:02}:{minute:02}')


if (__name__ == '__main__'):
    main()
