import copy

def get_combos(bin_str: str):
    combos = []
    temp_combos = []
    new_str = [char for char in bin_str]
    for i, char in enumerate(bin_str):
        if char == 'X':
            new_str[i] = 0
            temp_combos.append(new_str)
            new_str[i] = 1
            temp_combos.append(new_str)



def get_combos_r(bin_list: list, combos: list):
    if 'X' not in bin_list:
        joined = ''.join(bin_list)
        if joined not in combos:
            combos.append(''.join(bin_list))
        return
    x_ind = bin_list.index('X')
    bin_list_copy = copy.deepcopy(bin_list)
    bin_list[x_ind] = '0'
    get_combos_r(bin_list, combos)
    bin_list_copy[x_ind] = '1'
    get_combos_r(bin_list_copy, combos)



with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

mem = {}
for line in lines:
    instr, val = line.split(' = ')
    if instr == 'mask':
        mask = val
    else:
        mem_loc = int(instr.split('[')[-1][:-1])
        mem_loc_bin = '{:036b}'.format(int(mem_loc))
        bin_val = '{:036b}'.format(int(val))
        masked_mask = ['0'] * 36
        for i, char in enumerate(mask):
            if char == 'X' or char == '1':
                masked_mask[i] = char
            elif char == '0':
                masked_mask[i] = mem_loc_bin[i]
        combos = []
        get_combos_r(masked_mask, combos)
        mem_locs = [int(bin_str,2) for bin_str in combos]
        for mem_loc in mem_locs:
            mem[mem_loc] = int(bin_val, 2)


sum = 0
for key, val in mem.items():
    sum += val
print(sum)