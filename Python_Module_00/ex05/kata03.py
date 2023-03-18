# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    kata03.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jihoolee <jihoolee@student.42SEOUL.kr>     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/12 16:24:25 by jihoolee          #+#    #+#              #
#    Updated: 2023/03/18 23:50:58 by jihoolee         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Put this at the top of your kata03.py file
kata = "The right format"


def main():
    year, month, date, hour, minute = kata
    print(f'{month:02}/{date:02}/{year:04} {hour:02}:{minute:02}')


if (__name__ == '__main__'):
    main()
