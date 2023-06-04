# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    loading.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jihoolee <jihoolee@student.42SEOUL.kr>     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/09 16:51:26 by jihoolee          #+#    #+#              #
#    Updated: 2023/06/05 00:30:28 by jihoolee         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import time


def get_ETA(cur_it: int, total_it: int, elapsed_time: float) -> float:
    time_per_it = elapsed_time / cur_it
    remaining_it = total_it - cur_it
    return time_per_it * remaining_it


def print_progress(cur_it: int, total_it: int, elapsed_time: float) -> None:
    eta = get_ETA(cur_it, total_it, elapsed_time)
    progress_percent = int(cur_it / total_it * 100)
    progress_bar = "=" * ((progress_percent - 1) // 5) + ">"

    status = (
        f'\rETA: {eta:.2f}s [{progress_percent:>3}%] [{progress_bar:<20}] '
        f'{cur_it}/{total_it} | elapsed time {elapsed_time:.2f}s'
    )

    print(status, end='')


def ft_progress(iterable, interval: float = 0.1):
    cur_it = 0
    start_time = time.time()
    prev_time = start_time
    try:
        total_it = len(iterable)
    except TypeError as e:
        total_it = None

    for i in iterable:
        cur_it += 1
        now = time.time()
        if (now - prev_time < interval):
            yield i
            continue
        prev_time = now
        elapsed_time = now - start_time
        if (total_it):
            print_progress(cur_it, total_it, elapsed_time)
        else:
            print(f'\r{cur_it}it | elapsed time {elapsed_time:.2f}s', end='')
        yield i
    print()


def main():
    from time import sleep

    def temp_generator():
        for i in range(1000):
            yield i

    # listy = range(1000)
    listy = temp_generator()
    ret = 0
    for elem in ft_progress(listy):
        ret += (elem + 3) % 5
        sleep(0.01)
    print()
    print(ret)


if (__name__ == '__main__'):
    main()
