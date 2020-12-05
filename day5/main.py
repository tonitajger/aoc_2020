with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

id_list = []
max_id = 0
for line in lines:
    row = int(line[:-3].replace('F', '0').replace('B', '1'), 2)
    col = int(line[-3:].replace('L', '0').replace('R', '1'), 2)
    seat_id = row * 8 + col
    if seat_id > max_id:
        max_id = seat_id
    id_list.append(seat_id)

id_list.sort()

my_seat = None
for i, seat_id in enumerate(id_list):
    if i or i+1 > len(id_list):
        if seat_id - id_list[i-1] != 1:
            my_seat = seat_id - 1
            break
        elif id_list[i+1] - seat_id != 1:
            my_seat = seat_id + 1
            break

print(my_seat)



