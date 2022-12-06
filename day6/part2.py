

f = open('input.txt')

start = 0
end = 14

flag = True

returnval = 0

for line in f: 
    while(end < len(line) and flag):
        four = set(line[start:end])
        if len(four) == 14:
            returnval = end
            flag = False
        else:
            start += 1
            end += 1

print(returnval)