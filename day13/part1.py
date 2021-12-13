from collections import defaultdict

mode = 'coordinates'
coords = {}
max_x = 0
max_y = 0
folds = []

def set_point(coords, x, y, value):
    if x not in coords:
        coords[x] = {}
    coords[x][y] = value


def get_point(coords, x, y):
    if x not in coords:
        return '.'
    if y not in coords[x]:
        return '.'
    return '*' if coords[x][y] == '*' else '.'

with open('input.txt', 'r') as f:
    for line in f:
        if line.strip() == '':
            mode = 'folds'
        elif mode == 'coordinates':
            (x,y) = line.strip().split(',')
            x = int(x)
            y = int(y)
            max_x = max(x, max_x)
            max_y = max(y, max_y)
            set_point(coords, x, y, '*')
        else:
            (fold, along, dims) = line.strip().split()
            if fold != 'fold':
                print('BAD LINE: ', line)
            (axis, position) = dims.split('=')
            folds.append([axis, int(position)])

def do_fold(index, coords, folds):
    global max_x, max_y
    axis = folds[index][0]
    position = folds[index][1]
    if axis == 'x':
        print('x')
        for y in range(max_y + 1):
            for x in range(position + 1, max_x+1):
                left_x = position - (x - position)
                new_value = '*' if get_point(coords, left_x, y) == '*' or get_point(coords, x, y) == '*' else None
                set_point(coords, left_x, y, new_value)
                set_point(coords, x, y, None)
        max_x = position - 1

    else:
        print('y')
        print(folds[index][1])
        for x in range(max_x + 1):
            for y in range(position + 1, max_y+1):
                left_y = position - (y - position)
                new_value = '*' if get_point(coords, x, left_y) == '*' or get_point(coords, x, y) == '*' else None
                set_point(coords, x, left_y, new_value)
                set_point(coords, x, y, None)
        max_y = position - 1

for index in range(len(folds)):
    do_fold(index, coords, folds)
#do_fold(0, coords, folds)
dots = 0
for x in range(max_x + 1):
    for y in range(max_y + 1):
        if get_point(coords, x, y) == '*':
            dots += 1

print(dots)
for y in range(max_y + 1):
    for x in range(max_x + 1):
        print(get_point(coords, x, y), end='')
    print('')

