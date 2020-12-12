from collections import Counter

with open('input.txt') as f:
    lines = f.read().splitlines()

adap_list = [int(el) for el in lines]

outlet = 0
curr = outlet

device = max(adap_list) + 3


def find_diff(adap_list, curr, diff):
    for el in adap_list:
        if el - curr == diff:
            return el
    return None

diff_count = Counter()
while curr < device - 3:
    for diff in range(1, 4):
        new = find_diff(adap_list, curr, diff)
        if new:
            diff_count[diff] += 1
            curr = new
            break



diff_count[3] += 1
print(diff_count)
print(diff_count[1] * diff_count[3])


def get_valids(adap_list):
    valid_list = []
    for i, el in enumerate(adap_list):
        diff = 0
        j = i + 1
        valids = []
        if i == 0:
            valid_list.append([(el,el)])
        while diff < 3 and j < len(adap_list):
            new_el = adap_list[j]
            diff = new_el - el
            if diff  <= 3:
                valids.append((new_el, diff))
            j += 1
        if valids:
            valid_list.append(valids)
    return valid_list
