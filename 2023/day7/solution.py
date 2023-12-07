def card_strength(card_dict):
    if len(card_dict) == 5:
        return 1
    elif len(card_dict) == 4:
        return 2
    elif len(card_dict) == 3:
        if sorted(card_dict.values()) == [1, 2, 2]:
            return 3
        elif sorted(card_dict.values()) == [1, 1, 3]:
            return 4
    elif len(card_dict) == 2:
        if sorted(card_dict.values()) == [2, 3]:
            return 5
        elif sorted(card_dict.values()) == [1,4]:
            return 6
    elif len(card_dict) == 1:
        return 7

def get_card_type(cards):
    card_dict = {}
    for card in cards:
        if card not in card_dict:
            card_dict[card] = 1
        else:
            card_dict[card] += 1
    return card_strength(card_dict),card_dict

def key_order(cards):
    card_order = {'A':13, 'K':12, 'Q':11, 'J':10, 'T':9, '9':8, '8':7, '7':6, '6':5, '5':4, '4':3, '3':2, '2':1}
    return [card_order[card] for card in cards]

def key_order_joker(cards):
    card_order = {'A':13, 'K':12, 'Q':11, 'T':10, '9':9, '8':8, '7':7, '6':6, '5':5, '4':4, '3':3, '2':2, 'J':1,}
    return [card_order[card] for card in cards]

def order_cards(card_list, joker):
    if joker:
        return sorted(card_list, key=key_order_joker)
    return sorted(card_list, key=key_order)

def get_type_joker(cards):
    card_dict = get_card_type(cards)[1]
    if 'J' in cards and cards != 'JJJJJ':
        max_value = max(value for key, value in card_dict.items() if key != 'J')
        max_key = next(key for key in card_dict.keys() if card_dict[key] == max_value and key != 'J')
        card_dict[max_key] += card_dict['J']
        del card_dict['J']
    return card_strength(card_dict)

def get_final_order(card_ranks, joker):
    final_order = []
    for item, cards in card_ranks.items():
        if len(cards) == 0:
            continue
        elif len(cards) == 1:
            final_order.append(cards[0])
        else:
            final_order += order_cards(cards, joker)
    return final_order

with open("input.txt") as file:
    hands = file.read().strip().split('\n')

card_bids = {}
for hand in hands:
    card_bids[hand.split(' ')[0]] = int(hand.split(' ')[1])

card_ranks = {key:[] for key in range(1,8)}

for cards in card_bids.keys():
    card_ranks[get_card_type(cards)[0]].append(cards)

final_order = get_final_order(card_ranks, joker = False)

total_winnings = 0

for i, card in enumerate(final_order):
    total_winnings += (i+1)*card_bids[card]

print(total_winnings)

card_ranks_joker = {key:[] for key in range(1,8)}

for cards in card_bids.keys():
    card_ranks_joker[get_type_joker(cards)].append(cards)
        
final_order = get_final_order(card_ranks_joker, joker = True)

total_winnings = 0
for i, card in enumerate(final_order):
    total_winnings += (i+1)*card_bids[card]

print(total_winnings)