

def transform(val: int, subj: int = 7, today: int = 20201227) -> int:
    return (val * subj) % today


def calculate_loop(pub: int) -> int:
    loop = 0
    curr = 1
    while curr != pub:
        curr = transform(curr)
        loop += 1
    return loop


def transform_n(val: int, n: int, subj: int = 7) -> int:
    curr = val
    for i in range(n):
        curr = transform(curr, subj=subj)
    return curr


def calculate_encryption(card_pub: int, door_pub: int, card_loop: int, door_loop: int) -> int:
    enc1 = transform_n(1, door_loop, subj=card_pub)
    enc2 = transform_n(1, card_loop, subj=door_pub)
    if enc1 != enc2:
        print('mismatching encryption keys!')
        return
    return enc1


if __name__ == '__main__':
    with open('input.txt') as f:
        lines = f.read().splitlines()
    card_pub, door_pub = lines
    card_pub, door_pub = int(card_pub), int(door_pub)

    card_loop = calculate_loop(card_pub)
    door_loop = calculate_loop(door_pub)

    encryption_key = calculate_encryption(card_pub, door_pub, card_loop, door_loop)
    print(encryption_key)
