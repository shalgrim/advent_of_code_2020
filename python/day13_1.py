from math import prod

ARRIVAL_TIME = 1003681
LINE_TWO = '23,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,37,x,x,x,x,x,431,x,x,x,x,x,x,x,x,x,x,x,x,13,17,x,x,x,x,19,x,x,x,x,x,x,x,x,x,x,x,409,x,x,x,x,x,x,x,x,x,41,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,29'
BUSES_IN_SERVICE = [int(bus) for bus in LINE_TWO.split(',') if bus != 'x']

if __name__ == '__main__':
    wait_times = {}
    for bus in BUSES_IN_SERVICE:
        wait_times[bus] = bus - (ARRIVAL_TIME % bus)

    shortest_tuple = sorted(
        [tuple(item) for item in wait_times.items()], key=lambda x: x[1]
    )[0]
    print(prod(shortest_tuple))
