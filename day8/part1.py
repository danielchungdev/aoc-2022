



def determine_tree_visible(mapping, column, row):
    visible_left = visible_right = visible_up = visible_down = True
    current_tree_height = mapping[row][column]
    length = len(mapping[0])
    height = len(mapping)
    if column == 0 or row == 0:
        return True
    if column == height - 1 or row == height - 1:
        return True
    #left
    left_y = right_y = column
    up_x = down_x = row
    while(left_y > 0):
        left_y -= 1
        current_left_side = mapping[row][left_y]
        if current_left_side >= current_tree_height:
            visible_left = False
    #right
    while(right_y < length - 1):
        right_y += 1
        current_right_side = mapping[row][right_y]
        if current_right_side >= current_tree_height:
            visible_right = False
    #up
    while(up_x > 0):
        up_x -= 1
        current_up_side = mapping[up_x][column]
        if current_up_side >= current_tree_height:
            visible_up = False
    #bottom
    while(down_x < height - 1):
        down_x += 1
        current_down_side = mapping[down_x][column]
        if current_down_side >= current_tree_height:
            visible_down = False

    if visible_left or visible_right or visible_up or visible_down:
        return True
    else:
        return False
    

f = open('input.txt')

mapping = []

all_visibles = 0

for line in f: 
    line = line.strip()
    temp_arr = []
    for i in line:
        temp_arr.append(int(i))
    mapping.append(temp_arr)

for row in range(len(mapping)):
    for column in range(len(mapping[row])):
        current_tree = mapping[row][column]
        if determine_tree_visible(mapping, column, row):
            all_visibles += 1

print(all_visibles)