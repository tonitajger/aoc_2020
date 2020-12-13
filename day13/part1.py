import copy


def get_dep(earliest, buses):
    timestamp = copy.deepcopy(earliest)
    while True:
        for bus in buses:
            print(timestamp, timestamp % bus)
            if not timestamp % bus:
                return timestamp, bus
        timestamp += 1




def main():
    with open('input.txt', 'r') as f:
        earliest, buses = f.read().splitlines()
    earliest = int(earliest)
    buses = [int(bus) for bus in buses.split(',') if bus != 'x']
    ts, bus = get_dep(earliest, buses)
    print((ts-earliest)*bus)


if __name__ == '__main__':
    main()