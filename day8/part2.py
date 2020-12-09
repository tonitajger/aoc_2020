def run(instr_list: list):
    been = set()
    acc = 0
    pos = 0
    while pos < len(instr_list):
        if pos in been:
            return None

        been.add(pos)

        print(instr_list[pos])
        operation, val = instr_list[pos].split()
        val = int(val)

        if operation == 'jmp':
            pos += val

        elif operation == 'acc':
            acc += val
            pos += 1

        elif operation == 'nop':
            pos += 1

    return acc


def main():
    with open('input.txt', 'r') as f:
        lines = f.read().splitlines()

    for i, line in enumerate(lines):
        op, val = line.split()

        print([op + ' ' + val])
        if op == 'jmp':
            op = 'nop'
            acc = run(lines[:i] + [op + ' ' + val] + lines[i + 1:])
        elif op == 'nop':
            op = 'nop'
            acc = run(lines[:i] + [op + ' ' + val] + lines[i + 1:])
        else:
            acc = run(lines[:i] + [op + ' ' + val] + lines[i + 1:])
        if acc:
            return acc

if __name__ == '__main__':
    print(main())









