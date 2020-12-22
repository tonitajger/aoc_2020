with open('input.txt', 'r') as f:
    lines = f.read().splitlines()


def calc_sub(expr_str):
    expr = expr_str.split()

    new_val = None
    i = 0
    while i < len(expr):

        if not expr[i].isnumeric():
            if expr[i] == '+':
                new_val = int(expr[i - 1]) + int(expr[i + 1])

            if new_val:
                expr = expr[:i - 1] + expr[i + 2:]

                expr.insert(i - 1, str(new_val))

                new_val = None
                i -= 1

        i += 1

    new_val = None
    i = 0
    while i < len(expr):

        if not expr[i].isnumeric():
            if expr[i] == '*':
                new_val = int(expr[i - 1]) * int(expr[i + 1])

            if new_val:
                expr = expr[3:]
                expr.insert(0, str(new_val))
                i -= 1
        i += 1
    print(expr)
    return expr[0]


sum = 0
for line in lines:

    new_str = ''
    i = 0
    has_more_par = False
    while i < len(line) or has_more_par:

        if i == len(line):
            i = 0
            has_more_par = False

        char = line[i]
        par_begin = None
        if char == '(':
            par_begin = i
            new_i = i
            while line[new_i] != ')':
                if line[new_i] == '(':
                    has_more_par = True
                    par_begin = new_i
                new_i += 1
            new_str = line[:par_begin] + str(calc_sub(line[par_begin + 1:new_i])) + line[new_i + 1:]
            line = new_str
        i += 1

    sum += int(calc_sub(line))
print(sum)
