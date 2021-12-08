counts = {}
total = 0

def increment_counts(counts, x, y):
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
        if x0 == x1:
            if y1 > y0:
                startY = y0
                endY = y1
            else:
                startY = y1
                endY = y0
            for i in range(startY, endY + 1):
                total += increment_counts(counts, x0, i)
        elif y0 == y1:
            if x1 > x0:
                startX = x0
                endX = x1
            else:
                startX = x1
                endX = x0
            for i in range(startX, endX + 1):
                total += increment_counts(counts, i, y0)

    print(total)

