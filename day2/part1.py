with open('input.txt', 'r') as f:
    instructions = [x.strip() for x in f.readlines()]


horizontal = 0
depth = 0

for instruction in instructions:
    (direction, distance) = instruction.split(" ")
    distance_int = int(distance)
    if direction == "up":
        depth -= distance_int
    elif direction == "down":
        depth += distance_int
    elif direction == "forward":
        horizontal += distance_int
    else:
        print("bad direction!")

print(horizontal * depth)