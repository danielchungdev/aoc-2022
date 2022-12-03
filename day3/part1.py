


def letter_value(letter):
    if letter.isupper():
        return ord(letter) - ord('A') + 27
    return ord(letter) - ord('a') + 1

f = open('input.txt')

total = 0

for line in f:
    line = line.strip()
    seen = set()
    middle = len(line) // 2
    first = line[:middle]
    second = line[-middle:]
    repeated = set(first).intersection(set(second))
    for i in repeated:
        total += letter_value(i)

print(total)

