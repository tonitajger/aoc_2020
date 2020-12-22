with open('input.txt', 'r') as f:
    start = f.read().split(',')

start = [int(el) for el in start]
prev = None
memory = {}

for i, el in enumerate(start):
    if el not in memory:
        memory[el] = [i + 1]
    else:
        memory[el].append(i + 1)

print(memory)
i += 1
prev = el
print(el)
while i < 2020:

    i += 1
    prev_idxs = memory[prev]
    last_idx = None
    if len(prev_idxs) >= 2:
        last_idx = prev_idxs[-2]
    if last_idx:
        new_val = i - last_idx - 1
    else:
        new_val = 0
    if new_val not in memory:
        memory[new_val] = [i]
    else:
        memory[new_val].append(i)
    prev = new_val
    print(i, prev)

print(prev)


