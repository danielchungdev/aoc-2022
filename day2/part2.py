
# A for Rock, B for Paper, and C for Scissors.
# X for Rock, Y for Paper, and Z for Scissors.
# (1 for Rock, 2 for Paper, and 3 for Scissors)

values = {'X': 1, 'Y': 2, 'Z': 3}

#X = lose
#Y = draw
#Z = Win

def declare_winner (elf, human):
    #rock vs scissor
    if elf == "A" and human == "X":
        return 3
    #rock vs rock
    if elf == "A" and human == "Y":
        return 1 + 3
    #rock vs paper
    if elf == "A" and human == "Z": 
        return 2 + 6

    #paper vs rock
    if elf == "B" and human == "X":
        return 1
    #paper vs paper
    if elf == "B" and human == "Y":
        return 2 + 3
    #paper vs scissors
    if elf == "B" and human == "Z": 
        return 3 + 6

    #scissors
    if elf == "C" and human == "X":
        return 2
    #scissors
    if elf == "C" and human == "Y":
        return 3 + 3
    #scissors
    if elf == "C" and human == "Z": 
        return 1 + 6

f = open('input.txt')

total = 0

for i in f: 
    round = 0
    elf, human = i.strip().split(" ")
    print(declare_winner(elf, human))
    total += declare_winner(elf, human)

print(total)