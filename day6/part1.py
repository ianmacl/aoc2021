with open('input_test2.txt', 'r') as f:
    fish = [int(x) for x in f.readline().strip().split(',')]
    print(fish)

number_of_days = 256

## number of n days:
#In n days, a single fish will hatch:
#floor((n - start) / 6)

#Con


for i in range(0, number_of_days):
    print(f'Day {i}')
    print(len(fish))
    for j in range(0, len(fish)):
        if fish[j] == 0:
            fish.append(8)
            fish[j] = 6
        else:
            fish[j] -= 1

print(len(fish))
