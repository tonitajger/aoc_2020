
if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        cups = [int(char) for char in f.read()]

    max_label = max(cups)
    min_label = min(cups)
    curr = cups[0]
    idx = 0
    no_cups = len(cups)

    for i in range(100):
        pick_idx = idx
        if idx + 1 == no_cups:
            pick_idx = -1
            pick_up = cups[pick_idx + 1: pick_idx + 4]
            cups = cups[:pick_idx + 1] + cups[pick_idx + 4:]
        else:
            if idx + 4 >= no_cups:
                pick_up = cups[pick_idx + 1: no_cups] + cups[0: idx + 4 - no_cups]
                cups = cups[idx + 4 - no_cups:pick_idx + 1]
            else:
                pick_up = cups[pick_idx + 1: pick_idx + 4]
                cups = cups[:pick_idx + 1] + cups[pick_idx + 4:]

        destination = curr - 1
        while destination not in cups:
            destination -= 1
            if destination < min_label:
                destination = max_label

        dest_idx = cups.index(destination)
        cups = cups[:dest_idx + 1] + pick_up + cups[dest_idx + 1:]

        idx = cups.index(curr)
        if idx + 1 == no_cups:
            idx = 0
        else:
            idx += 1

        curr = cups[idx]

    one_idx = cups.index(1)
    cups.pop(one_idx)
    outp = cups[one_idx:] + cups[:one_idx]
    print(''.join(str(x) for x in outp))




