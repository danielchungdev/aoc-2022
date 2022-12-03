


def letter_value(letter):
    if letter.isupper():
        return ord(letter) - ord('A') + 27
    return ord(letter) - ord('a') + 1

f = open('input.txt')

total = 0
current = []
for line in f:
    line = line.strip()
    current.append(line)
    if len(current) == 3:
        badge = set(current[0]).intersection(set(current[1]), set(current[2]))
        total += letter_value(list(badge)[-1])
        current = []

print(total)

