from tqdm import tqdm

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


i_start = i + 1
i += 1
prev = el

for i in tqdm(range(i_start+1, 30000000+1)):
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

print(prev)


