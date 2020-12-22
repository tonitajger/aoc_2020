from typing import List, Tuple
import tqdm

def divide_inp(lines: List[str]) -> Tuple[List[str], List[str]]:
    for i, line in enumerate(inp_list):
        if line == '':
            return lines[:i], lines[i+1:]


def get_patterns(rule: str, rule_dict: dict, max_depth: int, depth=0) -> str:
    print(depth)
    rules = rule_dict[rule]
    first_rule = rules[0].strip()
    if depth == max_depth:
        return ''
    if first_rule == '"a"' or first_rule == '"b"':
        return [first_rule[1]]

    possible = []
    for sub_rule in rules:
        sub_rules = sub_rule.strip().split()
        if len(sub_rules) == 3:
            fst, scd, trd = sub_rules
            pattern_fst = get_patterns(int(fst), rule_dict, max_depth, depth=depth + 1)
            pattern_scd = get_patterns(int(scd), rule_dict, max_depth, depth=depth + 1)
            pattern_trd = get_patterns(int(trd), rule_dict, max_depth, depth=depth + 1)
            for f in pattern_fst:
                for s in pattern_scd:
                    for t in pattern_trd:
                        possible.append(f+s+t)
        elif len(sub_rules) == 2:
            fst, scd = sub_rules
            pattern_fst = get_patterns(int(fst), rule_dict, max_depth, depth=depth + 1)
            pattern_scd = get_patterns(int(scd), rule_dict, max_depth, depth=depth + 1)
            for f in pattern_fst:
                for s in pattern_scd:
                    possible.append(f+s)
        elif len(sub_rules) == 1:
            fst = sub_rules[0]
            pattern_fst = get_patterns(int(fst), rule_dict, max_depth, depth=depth + 1)
            for f in pattern_fst:
                possible.append(f)

    return possible



if __name__ == '__main__':
    with open('mock2.txt', 'r') as f:
        inp_list = f.read().splitlines()

    rule_list, strs = divide_inp(inp_list)

    max_depth = max(map(len, strs))
    rule_dict = {}
    for rule in tqdm.tqdm(rule_list):
        rule_dict[int(rule.split(':')[0])] = rule.split(':')[1].split('|')
    rule_dict[8] = ['42', '42 8']
    rule_dict[11] = ['42 31', '42 11 31']




    patterns = get_patterns(0, rule_dict, max_depth)

    cnt = 0
    for el in tqdm.tqdm(strs):
        for pattern in patterns:
            if pattern == el:
                cnt += 1
                break
    print(cnt)
