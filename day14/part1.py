with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

mem = {}
for line in lines:
    instr, val = line.split(' = ')
    if instr == 'mask':
        mask = val
        print(mask)
    else:
        mem_loc = int(instr.split('[')[-1][:-1])
        bin_val = '{:036b}'.format(int(val))
        masked_val = ['0'] * 36
        for i, char in enumerate(mask):
            if char == 'X':
                masked_val[i] = bin_val[i]
            else:
                masked_val[i] = char

        mem[mem_loc] = int(''.join(masked_val), 2)

sum = 0
for key, val in mem.items():
    sum += val
print(sum)