# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    kata02.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jihoolee <jihoolee@student.42SEOUL.kr>     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/12 16:24:18 by jihoolee          #+#    #+#              #
#    Updated: 2023/03/18 23:50:46 by jihoolee         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Put this at the top of your kata02.py file
kata = (2019, 9, 25, 3, 30)


def main():
    year, month, date, hour, minute = kata
    print(f'{month:02}/{date:02}/{year:04} {hour:02}:{minute:02}')


if (__name__ == '__main__'):
    main()
