counts = {}
total = 0

def increment_counts(counts, xIn, yIn):
    x = int(xIn)
    y = int(yIn)
    print(f'Marking point {x},{y}')
    total = 0
    if not x in counts:
        counts[x] = {}
    if not y in counts[x]:
        counts[x][y] = 0
    elif counts[x][y] == 1:
        total += 1
    counts[x][y] += 1

    return total

with open('input.txt', 'r') as f:
    total = 0
    for line in f.readlines():
        pairs = line.split(" -> ")
        (x0, y0) = tuple(int(num) for num in pairs[0].split(","))
        (x1, y1) = tuple(int(num) for num in pairs[1].split(","))
        xDistance = abs(x1 - x0)
        yDistance = abs(y1 - y0)
        distance = max(xDistance, yDistance)
        xDelta = (x1 - x0) / distance
        yDelta = (y1 - y0) / distance
        print(f'Line is {x0:d},{y0:d} to {x1},{y1} has xDelta {xDelta} and yDelta {xDelta} and distance {distance}')
        for i in range(0, distance + 1):
            total += increment_counts(counts, x0 + xDelta * i, y0 + yDelta * i)


    print(total)

