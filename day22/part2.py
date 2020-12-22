import copy

def play(deck1, deck2, depth=0):
    seen = set()
    cnt = 0
    while deck1 and deck2:
        if not depth:
            print(f'Round: {cnt}, deck1: {deck1}, deck2 {deck2}')
        if str(deck1) in seen:
            return [1], []
        seen.add(str(deck1))
        card1 = deck1.pop(0)
        card2 = deck2.pop(0)
        if card1 <= len(deck1) and card2 <= len(deck2):
            # print(depth)
            sub_result = play(copy.deepcopy(deck1[:card1]), copy.deepcopy(deck2[:card2]), depth=depth+1)
            if sub_result[0]:
                deck1.append(card1)
                deck1.append(card2)
            else:
                deck2.append(card2)
                deck2.append(card1)
        else:
            if card1 > card2:
                deck1.append(card1)
                deck1.append(card2)
            else:
                deck2.append(card2)
                deck2.append(card1)
        cnt+=1
    return deck1, deck2


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        _, p1, p2 = f.read().split(':')

    deck1 = list(map(int, p1.splitlines()[1:-2]))
    deck2 = list(map(int, p2.splitlines()[1:]))

    result = play(deck1, deck2)
    winner_deck = [deck for deck in result if deck][0]

    sum = 0
    scale = len(winner_deck)
    for el in winner_deck:
        sum += el * scale
        scale -= 1
    print(sum)


