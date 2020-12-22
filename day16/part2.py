

def parse_spec(spec_list):
    all_intervals = []
    spec_dict = {}

    for spec in spec_list[:-1]:

        intervals = spec.split(':')[-1].split('or')

        intervals = [interval.strip().split('-') for interval in intervals]
        all_intervals .append(intervals)
        spec_dict[spec.split(':')[0]] = intervals
    return all_intervals, spec_dict


def get_valids(tickets, all_intervals):
    valids = []
    for ticket in tickets[1:]:
        is_valid = False
        for val in ticket.split(','):
            is_valid_val = False
            for intervals in all_intervals:
                for interval in intervals:
                    if int(interval[0]) > int(val) or int(interval[1]) < int(val):
                        pass
                    else:
                        is_valid_val = True
                        break
            if not is_valid_val:
                is_valid = False
                break
        if is_valid_val:
            is_valid = True
        if is_valid:
            valids.append(ticket)
    return valids


def get_fields(tickets, spec_dict):
    confirmed_fields = {}
    for ticket_idx, ticket in enumerate(tickets):
        possible_fields = {}
        for i, val in enumerate(ticket.split(',')):
            for key, intervals in spec_dict.items():
                for interval in intervals:

                    if int(interval[0]) <= int(val) <= int(interval[1]):
                        if i in possible_fields:
                            if key not in possible_fields[i]:

                                possible_fields[i].append(key)
                        else:

                            possible_fields[i] = [key]

        if ticket_idx == 0:
            confirmed_fields = possible_fields
        else:
            for key, val in confirmed_fields.items():
                for poss in val:
                    if not poss in possible_fields[key]:
                        val.remove(poss)

    return confirmed_fields



if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        inp_str = f.read()

    spec_list = inp_str.split('your ticket:')[0].splitlines()
    my_ticket = inp_str.split('ticket')[1].splitlines()[1].split(',')
    tickets = inp_str.split('nearby tickets:')[-1].splitlines()
    all_intervals, spec_dict = parse_spec(spec_list)
    valid_tickets = get_valids(tickets, all_intervals)
    fields = get_fields(valid_tickets, spec_dict)

    all_is_one = False
    purged_idxs = []
    while not all_is_one:
        for field, val in fields.items():
            if len(val) == 1 and field not in purged_idxs:
                for field2, val2 in fields.items():
                    if val[0] in val2 and field != field2:
                        val2.remove(val[0])
                purged_idxs.append(field)
                break
        for field, val in fields.items():
            if len(val) != 1:
                all_is_one = False
                break
            all_is_one = True

    departure_idxs = [int(key) for key, val in fields.items() if 'departure' in val[0]]
    print(departure_idxs)
    print(my_ticket)

    prod = 1
    for idxs in departure_idxs:
        prod *= int(my_ticket[idxs])
    print(prod)

