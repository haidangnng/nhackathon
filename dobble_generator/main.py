with open("./input.txt", "r") as f:
    input = f.read()


def build_deck(sym_len):
    card = []
    cards = []

    for i in range(1, sym_len + 1):
        card.append(i)
    cards.append(card)

    for j in range(1, sym_len):
        card = []
        card.append(1)

        for k in range(1, sym_len):
            card.append((sym_len - 1) * j + k + 1)
        cards.append(card)

    for i in range(1, sym_len):
        for j in range(1, sym_len):
            card = []
            card.append(i + 1)

            for k in range(1, sym_len):
                card.append(
                    sym_len
                    + 1
                    + (sym_len - 1) * (k - 1)
                    + (((i - 1) * (k - 1) + j - 1) % (sym_len - 1))
                )
            cards.append(card)

    print(sym_len)
    for index_card, card in enumerate(cards):
        print(f"{index_card + 1} - [{', '.join(str(x) for x in card)}]")
        if index_card == len(cards) - 1:
            print()


for i in input.split():
    if i.isnumeric():
        build_deck(int(i))
    else:
        print(f"{i}\ninvalid")
