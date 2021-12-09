lines = []
with open('input.txt', 'r') as f:
    for line in f:
        lines.append([int(char) for char in line.strip()])

print(lines)

max_y = len(lines)
max_x = len(lines[0])

def is_low_point(lines, y, x):
    current_height = lines[y][x]
    if y > 0:
        if current_height >= lines[y-1][x]:
            return False
    if x > 0:
        if current_height >= lines[y][x-1]:
            return False
    if y < max_y - 1:
        if current_height >= lines[y+1][x]:
            return False
    if x < max_x - 1:
        if current_height >= lines[y][x+1]:
            return False
    return True



total_risk = 0

for y in range(0, len(lines)):
    for x in range(0, len(lines[y])):
        adjacents = []
        if is_low_point(lines, y, x):
            total_risk += lines[y][x] + 1

print(total_risk)