with open('input.txt', 'r') as f:
    str_list = f.read().splitlines()

valid_list = []
for line in str_list:
    line_split = line.split()
    lo, hi = line_split[0].split('-')
    lo, hi = int(lo), int(hi)
    char = line_split[1][0]
    passw = line_split[2]

    char_count = 0
    for c in passw:
        if c == char:
            char_count += 1
    if lo <= char_count <= hi:
        valid_list.append(passw)
    char_count = 0
print(valid_list)
print(len(valid_list))

