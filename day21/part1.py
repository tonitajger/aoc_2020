from typing import Tuple, List, Any

def parse_inp(inp_file: str) -> Tuple[List, List]:
    with open(inp_file, 'r') as f:
        food_list = f.read().splitlines()

    ingr_list = []
    all_list = []
    for food in food_list:
        ingredients, allergenes = food.split('(')
        ingr_list.append(ingredients.strip().split())
        all_list.append(allergenes[:-1].replace(',', '').split()[1:])
    return  ingr_list, all_list



if __name__ == '__main__':
    ings, alls = parse_inp('input.txt')

    all_dict = {}
    all_ings = []
    for ingredients, allergenes in zip(ings, alls):
        all_ings.extend(ingredients)
        for a in allergenes:
            if a in all_dict:
                poss_ingr = all_dict[a]
                all_dict[a] = list(set(ingredients) & set(poss_ingr))
            else:
                all_dict[a] = ingredients

    already_assigned = set()


    contains_allergenes = []
    for key, val in all_dict.items():
        if len(val) == 1:
            already_assigned.add(val[0])
        else:
            val = [el for el in val if el not in already_assigned]
            all_dict[key] = val
            if len(val) == 1:
                already_assigned.add(val[0])
        contains_allergenes.extend(val)

    count = 0
    for ingr in all_ings:
        if ingr not in contains_allergenes:
            count += 1

    print(count)
    # all_are_len_one = False
    # while not all_are_len_one:
    #     all_are_len_one = True
    #     for key, val in all_dict.items():
    #         if len(val) == 1:
    #             already_assigned.add(val[0])
    #         else:
    #             val = [el for el in val if el not in already_assigned]
    #             all_dict[key] = val
    #             if len(val) == 1:
    #                 already_assigned.add(val[0])
    #             else:
    #                 all_are_len_one = False
    #         contains_allergenes.extend(val)
    #
    # all_dict.items()
    #
    #

