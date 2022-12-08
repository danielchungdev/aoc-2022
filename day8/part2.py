




def determine_tree_scenic_score(mapping, column, row):
    visible_left = visible_right = visible_up = visible_down = 0
    current_tree_height = mapping[row][column]
    length = len(mapping[0])
    height = len(mapping)
    #left
    left_y = right_y = column
    up_x = down_x = row
    while(left_y > 0):
        left_y -= 1
        if left_y < 0:
            break
        current_left_side = mapping[row][left_y]
        visible_left += 1
        if current_left_side >= current_tree_height:
            break
    #right
    while(right_y < length - 1):
        right_y += 1
        if right_y == length:
            break
        current_right_side = mapping[row][right_y]
        visible_right += 1
        if current_right_side >= current_tree_height:
            break
    #up
    while(up_x > 0):
        up_x -= 1
        if up_x < 0:
            break
        current_up_side = mapping[up_x][column]
        visible_up += 1
        if current_up_side >= current_tree_height:
            break
    #bottom
    while(down_x < height - 1):
        down_x += 1
        if down_x == height:
            break
        current_down_side = mapping[down_x][column]
        visible_down += 1
        if current_down_side >= current_tree_height:
            break
    return visible_left * visible_down * visible_up * visible_right

f = open('input.txt')

mapping = []

highest_scenic_score = 0

for line in f: 
    line = line.strip()
    temp_arr = []
    for i in line:
        temp_arr.append(int(i))
    mapping.append(temp_arr)

for row in range(len(mapping)):
    for column in range(len(mapping[row])):
        current_tree = mapping[row][column]
        highest_scenic_score = max(highest_scenic_score, determine_tree_scenic_score(mapping, column, row))

print(highest_scenic_score)