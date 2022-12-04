
def create_array(assigment):
    assigment = assigment.split("-")
    start, end = assigment
    return set([x for x in range(int(start), int(end) + 1)])


def check(first, second):
    first = create_array(first)
    second = create_array(second)
    intersection = first.intersection(second)
    if first == intersection or second == intersection:
        return True
    return False
    

f = open('input.txt')

reconsider = 0

for line in f: 
    line = line.strip().split(",")
    first, second = line
    if check(first, second):
        reconsider += 1

print(reconsider)