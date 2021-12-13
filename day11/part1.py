lines = []
with open('input.txt', 'r') as f:
    for line in f:
        lines.append([int(char) for char in line.strip()])

def increase_energy(lines, y, x):
    if y < 0 or y >= len(lines):
        return 0
    if x < 0 or x >= len(lines[0]):
        return 0
    flashes = 0
    lines[y][x] += 1
    if lines[y][x] == 10:
        flashes += 1
        for add_y in range(-1, 2):
            for add_x in range(-1, 2):
                if add_y == 0 and add_x == 0:
                    continue
                flashes += increase_energy(lines, y + add_y, x + add_x)

    return flashes

flashes = 0

def print_lines(lines, step):
    print("After step " + str(step+1))
    for line in lines:
        print("".join([str(x) for x in line]))
    print()


for step in range(0, 100):
    for y in range(0, len(lines)):
        for x in range(0, len(lines[y])):
            flashes += increase_energy(lines, y, x)

    for y in range(0, len(lines)):
        for x in range(0, len(lines[y])):
            if lines[y][x] > 9:
                lines[y][x] = 0
    print_lines(lines, step)

print(flashes)