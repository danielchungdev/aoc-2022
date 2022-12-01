
f = open('input.txt')

biggest_cal_deer = 0
current = 0

for i in f:
    if i == "\n":
        biggest_cal_deer = max(biggest_cal_deer, current)
        current = 0
    else:
        current += int(i)


print(biggest_cal_deer)