

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        _, p1, p2 = f.read().split(':')

    deck1 = list(map(int, p1.splitlines()[1:-2]))
    deck2 = list(map(int, p2.splitlines()[1:]))

    while deck1 and deck2:
        card1 = deck1.pop(0)
        card2 = deck2.pop(0)
        if card1 > card2:
            deck1.append(card1)
            deck1.append(card2)
        else:
            deck2.append(card2)
            deck2.append(card1)
    print(deck1,deck2)
    len1 = len(deck1)
    score = 0
    for el in deck1:
        score += len1 * el
        print(el, len1)
        len1 -= 1
    print(score)


