with open('input.txt', 'r') as f:
    numbers = [int(x.strip()) for x in f.readlines()]

print(numbers)
increase = 0
decrease = 0
last_number = None

for number in numbers:
    if last_number is None:
        last_number = number
        continue

    if number > last_number:
        increase += 1

    if number < last_number:
        decrease += 1

    last_number = number

print(increase)