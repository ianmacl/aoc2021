with open('input.txt', 'r') as f:
    instructions = [x.strip() for x in f.readlines()]


horizontal = 0
depth = 0
aim = 0

for instruction in instructions:
    (direction, distance) = instruction.split(" ")
    distance_int = int(distance)
    if direction == "up":
        aim -= distance_int
    elif direction == "down":
        aim += distance_int
    elif direction == "forward":
        horizontal += distance_int
        depth += distance_int * aim
    else:
        print("bad direction!")

print(horizontal * depth)