with open('day6/input.txt', 'r') as f:
    lines = f.read()

total_count = 0
for group in lines.split('\n\n'):
    group_set = set()
    for person in group.splitlines():
        for char in person:
            group_set.add(char)
    total_count += len(group_set)
print(total_count)
