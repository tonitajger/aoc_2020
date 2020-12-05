with open('input.txt', 'r') as f:
    str_list = f.read().splitlines()
int_list = [int(el) for el in str_list]
print(int_list)


for i, el1 in enumerate(int_list):
    for j in range(i, len(int_list)):
        el2 = int_list[j]
        if el1 + el2 < 2020:
            for k in range(j, len(int_list)):

                el3 = int_list[k]
                if el1 + el2 + el3 == 2020:
                    print(el1, el2, el3)
                    print(el1 * el2 * el3)
                    break


