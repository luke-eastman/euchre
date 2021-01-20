import random


def play_game():
    hands, kitty = deal()

    print(f'your hand: {hands[0]}')
    print(f'top card of kitty: {kitty[0]}')

    response = input('would you like to call trump?(y/n)')
    print(response)
    if response == 'y':
        trump = kitty[0][0]
    else:
        trump = ''

    print(trump)


def deal():
    deck = [('D', '9'), ('D', '10'), ('D', 'J'), ('D', 'Q'), ('D', 'K'), ('D', 'A'),
            ('H', '9'), ('H', '10'), ('H', 'J'), ('H', 'Q'), ('H', 'K'), ('H', 'A'),
            ('S', '9'), ('S', '10'), ('S', 'J'), ('S', 'Q'), ('S', 'K'), ('S', 'A'),
            ('C', '9'), ('C', '10'), ('C', 'J'), ('C', 'Q'), ('C', 'K'), ('C', 'A')]
    remaining_deck = deck
    hands = [[], [], [], []]
    player = 0
    hand_size = 0
    while len(remaining_deck) > 0 and hand_size < 5:
        index = random.randrange(len(remaining_deck))
        hands[player].append(remaining_deck[index])
        del remaining_deck[index]
        player += 1

        if player > 3:
            player = 0
            hand_size += 1

    return hands, remaining_deck


