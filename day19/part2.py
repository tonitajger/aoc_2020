from typing import List, Tuple
import tqdm


def divide_inp(lines: List[str]) -> Tuple[List[str], List[str]]:
    for i, line in enumerate(inp_list):
        if line == '':
            return lines[:i], lines[i + 1:]


def get_patterns(rule: int, rule_dict: dict) -> List:
    rules = rule_dict[rule]
    first_rule = rules[0].strip()
    if first_rule == '"a"' or first_rule == '"b"':
        return [first_rule[1]]

    possible = []
    for sub_rule in rules:
        sub_rules = sub_rule.strip().split()
        if len(sub_rules) == 3:
            fst, scd, trd = sub_rules
            pattern_fst = get_patterns(int(fst), rule_dict)
            pattern_scd = get_patterns(int(scd), rule_dict)
            pattern_trd = get_patterns(int(trd), rule_dict)
            for f in pattern_fst:
                for s in pattern_scd:
                    for t in pattern_trd:
                        possible.append(f + s + t)
        elif len(sub_rules) == 2:
            fst, scd = sub_rules
            pattern_fst = get_patterns(int(fst), rule_dict)
            pattern_scd = get_patterns(int(scd), rule_dict)
            for f in pattern_fst:
                for s in pattern_scd:
                    possible.append(f + s)
        elif len(sub_rules) == 1:
            fst = sub_rules[0]
            pattern_fst = get_patterns(int(fst), rule_dict)
            for f in pattern_fst:
                possible.append(f)

    return possible


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        inp_list = f.read().splitlines()

    rule_list, strs = divide_inp(inp_list)

    rule_dict = {}
    for rule in rule_list:
        rule_dict[int(rule.split(':')[0])] = rule.split(':')[1].split('|')

    patterns = get_patterns(0, rule_dict)

    rule_dict[8] = ['42', '42 8']
    rule_dict[11] = ['42 31', '42 11 31']
    pattern_42 = get_patterns(42, rule_dict)
    pattern_31 = get_patterns(31, rule_dict)

    p_len = len(patterns[0])
    p42_len = len(pattern_42[0])
    p31_len = len(pattern_31[0])
    print(p42_len, p31_len)
    prefix_len = p_len - p42_len
    prefix_len_31 = p_len - p31_len

    valids = []
    cnt = 0
    for el in tqdm.tqdm(strs):
        if el == 'aaaabbaaaabbaaa':
            print(1)
        valid = False
        for pattern in patterns:
            if pattern == el:
                valid = True
                cnt += 1
                valids.append(el)
                break

        if valid:
            continue

        cnt_42 = 0
        idx = 0
        while idx + p42_len <= len(el):
            window = el[idx: idx + p42_len]
            if window in pattern_42:
                idx += p42_len
                cnt_42 += 1
            else:
                break

        cnt_31 = 0
        while idx + p42_len <= len(el):
            window = el[idx: idx + p31_len]
            if window in pattern_31:
                idx += p31_len
                cnt_31 += 1
            else:
                break

        if idx == len(el) and cnt_42 > cnt_31 and cnt_31:
            valids.append(el)
            cnt += 1

    print(cnt)
    print(len(valids))
    # print('\n'.join(valids))
