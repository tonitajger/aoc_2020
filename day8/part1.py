



def main():
    with open('input.txt', 'r') as f:
        lines = f.read().splitlines()

    been = set()
    acc = 0
    pos = 0
    while True:
        if pos in been:
            return acc

        been.add(pos)

        operation, val = lines[pos].split()
        val = int(val)

        if operation == 'jmp':
            pos += val

        elif operation == 'acc':
            acc += val
            pos += 1

        elif operation == 'nop':
            pos += 1


if __name__ == '__main__':
    print(main())












