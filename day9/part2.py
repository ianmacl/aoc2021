lines = []
with open('input.txt', 'r') as f:
    for line in f:
        lines.append([int(char) for char in line.strip()])


max_y = len(lines)
max_x = len(lines[0])

def fill_basin(lines, basin_number, y, x, basin_count):
    lines[y][x] = basin_number
    basin_count += 1
    if y > 0:
        if lines[y-1][x] < 9:
            basin_count = fill_basin(lines, basin_number, y-1, x, basin_count)
    if x > 0:
        if lines[y][x-1] < 9:
            basin_count = fill_basin(lines, basin_number, y, x-1, basin_count)
    if y < max_y - 1:
        if lines[y+1][x] < 9:
            basin_count = fill_basin(lines, basin_number, y+1, x, basin_count)
    if x < max_x - 1:
        if lines[y][x+1] < 9:
            basin_count = fill_basin(lines, basin_number, y, x+1, basin_count)

    return basin_count

total_risk = 0
basin_number = 65
basin_counts = {}
for y in range(0, len(lines)):
    for x in range(0, len(lines[y])):
        if lines[y][x] < 9:
            basin_counts[basin_number] = fill_basin(lines, basin_number, y, x, 0)
            basin_number += 1

for y in lines:
    print("".join(['.' if x == 9 else chr(x) for x in y]))

counts = [basin_counts[x] for x in basin_counts]
print(basin_counts)
counts.sort()
print(counts)
print(counts[-1] * counts[-2] * counts[-3])