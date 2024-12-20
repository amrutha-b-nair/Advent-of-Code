import re

with open('input.txt') as file:
    lines = file.read().strip().split('\n')

total_score = 0
card_pile = {key : 1 for key in range(1, len(lines) + 1)}
for line in lines:
    card = re.split(r'[:|]', line)
    card_id = int(card[0].split(' ')[-1])
    card_winning = card[1].strip().split(' ')
    card_elf = card[2].strip().split(' ')
    winning_numbers = sum(1 for number in card_elf if number in card_winning and number != '')
    if winning_numbers != 0:
        total_score += 2**(winning_numbers- 1)
    for i in range(winning_numbers):
        card_pile[card_id + i + 1] += 1*card_pile[card_id]

print("Part 1: ",total_score)

card_total = sum(value for value in card_pile.values())
print("Part 2: ",card_total)