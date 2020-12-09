with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

input_list = [int(el) for el in lines]


def get_first_invalid():
    for i, el in enumerate(input_list):
        if i + 25 >= len(input_list):
            break
        preamb = input_list[i:i+25]
        curr = input_list[i+25]

        is_valid = False
        for j, el2 in enumerate(preamb):
            for k, el3 in enumerate(preamb[j:]):

                if el2 + el3 == curr and el2 != el3:
                    is_valid = True
                    break

        if not is_valid:
            return curr


a = get_first_invalid()
print(a)
for i, el in enumerate(input_list):
    cont = []
    cont.append(el)
    j=1
    while sum(cont) != a and  i+j+1<len(input_list):
        cont.append(input_list[i+j])
        j+=1

    if sum(cont) == a:
        print(min(cont)+max(cont))
        print(sum(cont))
        break
