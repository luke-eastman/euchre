import random


def play_game():
    scores = [0, 0]

    def play_hand():
        table = []
        hands, kitty = deal()
        print(kitty)
        print(f'your hand: {hands[0]}')
        print(f'top card of kitty: {kitty[0]}')

        trump = pick_trump(kitty[0], hands)
        print(f"trump is {trump}")

        def play_round():
            def play_card(player):
                if player == 0:
                    card_played = users_play_choice(hands[0], '', table)
                    table.append(card_played)

                else:
                    print(f"computer player {player}'s hand: {hands[player]}")

            for i in range(4):
                play_card(i)

        for play in range(5):
            print(f'play: {play}')
            play_round()

        scores[0] += 3

    while scores[0] < 10 and scores[1] < 10:
        play_hand()


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
    random.shuffle(remaining_deck)
    return hands, remaining_deck


def pick_trump(top_card, hands):
    def player_wants_trump(player):
        trump_count = 0
        for card in hands[player]:
            if card[0] == top_card[0]:
                trump_count += 1

        if trump_count < 2:
            return False
        else:
            return True

    response = input('would you like to call trump?(y/n)')
    trump = 'D'
    if response == 'y':
        trump = top_card[0]
    else:
        for i in range(1, 4):
            print(f'player: {i}')
            print(hands[i])
            print(player_wants_trump(i))
            if player_wants_trump(i):
                trump = top_card[0]
                break
    return trump


def users_play_choice(hand, lead_suit, current_plays):
    print(f'your hand: {hand}, {lead_suit} was lead')
    print(f'the table currently looks like this: {current_plays}')
    card = int(input('which card would you like to play?'))
    if hand[card][0] == lead_suit or lead_suit == '':
        card_to_play = hand[card]
        del hand[card]
        return card_to_play
