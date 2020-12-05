
mandatory_fields = {
    'byr',
    'iyr',
    'eyr',
    'hgt',
    'hcl',
    'ecl',
    'pid'
}

valid_hcl_chars = {
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f'
}

valid_ecl = {
    'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'
}


def is_year_between(year: str, lo: int, hi: int):
    if len(year) != 4:
        return False
    if lo <= int(year) <= hi:
        return True
    return False


def is_valid_hgt(hgt: str):
    if hgt[-2:] == 'in':
        if 59 <= int(hgt[:-2]) <= 76:
            return True
    elif hgt[-2:] == 'cm':
        if 150 <= int(hgt[:-2]) <= 193:
            return True
    return False


def is_valid_hcl(hcl: str):
    if hcl[0] == '#' and len(hcl) == 7:
        for char in hcl[1:]:
            if char not in valid_hcl_chars:
                return False
        return True
    return False


def is_valid_ecl(ecl: str):
    if ecl in valid_ecl:
        return True
    return False


def is_valid_pid(pid: str):
    try:
        if len(pid) == 9:
            a = int(pid)
            return True
        return False
    except ValueError:
        return False


def is_valid(passport):
    passport_dict = {}
    for el in passport.replace('\n', ' ').split():
        key, value = el.split(':')
        passport_dict[key] = value
    if mandatory_fields.issubset(passport_dict.keys()):
        if not is_year_between(passport_dict['byr'], 1920, 2002):
            return False
        if not is_year_between(passport_dict['iyr'], 2010, 2020):
            return False
        if not is_year_between(passport_dict['eyr'], 2020, 2030):
            return False
        if not is_valid_hgt(passport_dict['hgt']):
            return False
        if not is_valid_hcl(passport_dict['hcl']):
            return False
        if not is_valid_ecl(passport_dict['ecl']):
            return False
        if not is_valid_pid(passport_dict['pid']):
            return False
        return True


def main():
    with open('input.txt', 'r') as f:
        lines = f.read().split('\n\n')
    valid_count = 0
    for passport in lines:
        if is_valid(passport):
            valid_count += 1
    print(valid_count)


if __name__ == '__main__':
    main()
