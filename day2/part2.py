with open('input.txt', 'r') as f:
    str_list = f.read().splitlines()

valid_list = []
for line in str_list:
    line_split = line.split()
    ind1, ind2 = line_split[0].split('-')
    ind1, ind2 = int(ind1), int(ind2)
    char = line_split[1][0]
    passw = line_split[2]

    if bool(passw[ind1-1] == char) != bool(passw[ind2-1] == char):
        valid_list.append(passw)
print(valid_list)
print(len(valid_list))

