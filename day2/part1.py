
# A for Rock, B for Paper, and C for Scissors.
# X for Rock, Y for Paper, and Z for Scissors.
# (1 for Rock, 2 for Paper, and 3 for Scissors)


def declare_winner (elf, human):
    #rock vs rock
    if elf == "A" and human == "X":
        return "Tie"
    #rock vs paper
    if elf == "A" and human == "Y":
        return "Win"
    #rock vs scissor
    if elf == "A" and human == "Z": 
        return "Loss"

    #paper vs rock
    if elf == "B" and human == "X":
        return "Loss"
    #paper vs paper
    if elf == "B" and human == "Y":
        return "Tie"
    #paper vs scissors
    if elf == "B" and human == "Z": 
        return "Win"

    if elf == "C" and human == "X":
        return "Win"
    if elf == "C" and human == "Y":
        return "Loss"
    if elf == "C" and human == "Z": 
        return "Tie"

values = {'X': 1, 'Y': 2, 'Z': 3}

f = open('input.txt')

total = 0

for i in f: 
    round = 0
    elf, human = i.strip().split(" ")
    if declare_winner(elf, human) == "Win":
        round = values[human] + 6
    if declare_winner(elf, human) == "Loss":
        round = values[human]
    if declare_winner(elf, human) == "Tie":
        round = values[human] + 3
    print(round)
    total += round

print(total)