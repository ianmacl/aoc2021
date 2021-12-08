with open('input.txt', 'r') as f:
    numbers = [int(x.strip()) for x in f.readlines()]

print(numbers)
increase = 0
decrease = 0
last_number = None

for i in range(3, len(numbers)):
    if sum(numbers[i-3:i]) > sum(numbers[i-4:i-1]):
        increase += 1

print(increase)