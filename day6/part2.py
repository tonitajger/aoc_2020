with open('input.txt', 'r') as f:
    lines = f.read()

total_count = 0
for group in lines.split('\n\n'):
    group_dict = {}
    group_num = len(group.splitlines())
    for person in group.splitlines():
        for char in person:
            if char in group_dict:
                group_dict[char] += 1
            else:
                group_dict[char] = 1

    for key, val in group_dict.items():
        if val >= group_num:
            total_count += 1

print(total_count)
