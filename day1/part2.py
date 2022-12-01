
f = open('input.txt')

top = []
current = 0

for i in f:
    if i == "\n":
        top.append(current)
        current = 0
    else:
        current += int(i)

top.sort(reverse = True)

total = 0

for i in top[:3]:
    total += i

print(total)