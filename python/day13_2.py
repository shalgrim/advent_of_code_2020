from day13_1 import LINE_TWO
import math
import datetime


def does_work(minutes_past, bus, t):
    if minutes_past == 0:
        return t % bus == 0
    return bus - minutes_past == t % bus


def main(line):
    minutes_past_t = [
        (minute, int(bus)) for minute, bus in enumerate(line.split(',')) if bus != 'x'
    ]
    print(minutes_past_t)
    lowest_bus = min([tup[1] for tup in minutes_past_t])
    minutes_past_for_lowest_bus = [t[0] for t in minutes_past_t if t[1] == lowest_bus][
        0
    ]
    print(lowest_bus, minutes_past_for_lowest_bus)
    highest_bus = max([tup[1] for tup in minutes_past_t])
    minutes_past_for_highest_bus = [t[0] for t in minutes_past_t if t[1] == highest_bus][
        -1
    ]

    t = highest_bus - minutes_past_for_highest_bus
    # t = minutes_past_for_lowest_bus
    log_len = 0
    start = datetime.datetime.now()

    while True:
        if all(does_work(*tup, t) for tup in minutes_past_t if tup[1] != highest_bus):
            break
        t += highest_bus
        # t += lowest_bus
        # print(t)

        if int(math.log10(t)) > log_len:
            td = datetime.datetime.now() - start
            log_len = int(math.log10(t))
            print(math.log10(t), t, td.seconds)

    return t


if __name__ == '__main__':
    print(main(LINE_TWO))  # 1068792 is too low
