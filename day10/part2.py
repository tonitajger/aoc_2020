from collections import Counter
import random

with open('input.txt') as f:
    lines = f.read().splitlines()

adap_list = [int(el) for el in lines]


def get_valids(adap_list):
    valid_list = []
    for i, el in enumerate(adap_list):
        diff = 0
        j = i + 1
        valids = []
        if i == 0:
            valid_list.append([(el, 0, el)])
        while diff < 3 and j < len(adap_list):
            new_el = adap_list[j]
            diff = new_el - el
            if diff <= 3:
                valids.append((new_el, el,  diff))
            j += 1
        if valids:
            valid_list.append(valids)

    valid_list.append([(max(adap_list) + 3, max(adap_list), 3)])
    return valid_list


# def get_combo(adap_list):
#     if len(adap_list) <= 1:
#         print(adap_list)
#         if adap_list == []:
#             return 1
#         return len(adap_list[0])
#
#     sum = 0
#     for i, el in enumerate(adap_list[0]):
#         print(el)
#         term = get_combo(adap_list[i+1:])
#         print(term)
#         sum += term
#     return sum
adap_list.append(0)
adap_list.sort()

print(adap_list, 1)

adap_max = max(adap_list)
valids = get_valids(adap_list)


# print(get_combo(valids))
valids.reverse()

adap_list.reverse()
num_comb = {}
for i, el in enumerate(valids):
    print(i, el)
    if el[0][1] == adap_max:
        num_comb[adap_max] = 1
    else:
        sum = 0
        for subel in el:
            sum += num_comb[subel[0]]
        num_comb[el[0][1]] = sum
print(num_comb)


