import copy
import math
import numpy as np


def lcm(a):
    lcm = a[0]
    for i in a[1:]:
      lcm = lcm*i//math.gcd(lcm, i)
    return lcm


def get_ts(bus_list):
    ts = 100000000000000
    ts = math.ceil(ts / bus_list[0]) * bus_list[0]
    max_bus = max(bus_list)
    max_bus_i = bus_list.index(max_bus)

    while True:
        # max_step = bus_list[0]
        if not ts % 1000000:
            print(ts)
        is_valid = True
        valids = []

        for i, bus in enumerate(bus_list):
            if bus != 0:
                # if (ts + max_bus_i) % max_bus:
                #     is_valid = False
                #     break
                if (ts + i) % bus:
                    is_valid = False
                    break
                valids.append(bus)
                # max_step = max(bus, max_step)
        if is_valid:
            return ts

        if valids == []:
            step = 1
        else:
            prod = 1
            for fac in valids:
                prod *= fac
            step = prod

        ts += step



def main():
    with open('input.txt', 'r') as f:
        earliest, buses = f.read().splitlines()
    earliest = int(earliest)
    bus_list = []
    for bus in buses.split(','):
       if bus == 'x':
           bus_list.append(0)
       else:
           bus_list.append(int(bus))

    print(get_ts(bus_list))


if __name__ == '__main__':
    main()