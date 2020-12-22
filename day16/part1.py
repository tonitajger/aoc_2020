with open('input.txt', 'r') as f:
    inp_str = f.read()

spec_list = inp_str.split('your ticket:')[0].splitlines()
tickets = inp_str.split('nearby tickets:')[-1].splitlines()

all_intervals = []
spec_dict = {}

for spec in spec_list[:-1]:

    intervals = spec.split(':')[-1].split('or')

    intervals = [interval.strip().split('-') for interval in intervals]
    all_intervals .append(intervals)
    spec_dict[spec.split(':')[0]] = intervals

invalid_count = 0
invalid_sum = 0
for ticket in tickets[1:]:

    for val in ticket.split(','):
        is_valid = False
        for intervals in all_intervals:
            for interval in intervals:
                if int(interval[0]) <= int(val) <= int(interval[1]):
                    is_valid = True
                    break
        if not is_valid:
            invalid_count += 1
            invalid_sum += int(val)
print(invalid_count, invalid_sum)