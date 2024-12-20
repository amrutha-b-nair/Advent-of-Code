with open('input.txt') as file:
    game_choices = file.read().strip().split('\n')



score_win = 6
score_draw = 3

# rock_elf, rock = 'A', 'X'
# paper_elf, paper = 'B', 'Y' 
# scissors_elf, scissors = 'C', 'Z'

score_option = {
    'X': 1,
    'Y': 2,
    'Z': 3
}

win_pair = ['A Y', 'B Z', 'C X']
lose_pair = ['A Z', 'B X', 'C Y']
draw_pair = ['A X', 'B Y', 'C Z']


score = 0

for choice in game_choices:
    score += score_option[choice[-1]]
    if choice in win_pair:
        score += score_win
    elif choice in draw_pair:
        score += score_draw

print("Part 1:", score)

win = {'A': 'Y', 'B': 'Z', 'C': 'X'}
lose = {'A': 'Z', 'B': 'X', 'C': 'Y'}
draw = {'A': 'X', 'B': 'Y', 'C': 'Z'}

#X--> lose
#Y--> draw
#Z--> win

new_score = 0

for choice in game_choices:
    if choice[-1] == 'X':
        new_score += score_option[lose[choice[0]]]
    elif choice[-1] == 'Y':
        new_score += (score_option[draw[choice[0]]] + score_draw)
    elif choice[-1] == 'Z':
        new_score += (score_option[win[choice[0]]] + score_win)

print("Part 2:", new_score)

