import datetime
a = datetime.datetime.now()

number_of_days = 128

results = []
for start_num in range(0,9):
    fish = [start_num]
    for i in range(0, number_of_days):
        print(f'Day {i}')
        print(len(fish))
        for j in range(0, len(fish)):
            if fish[j] == 0:
                fish.append(8)
                fish[j] = 6
            else:
                fish[j] -= 1
    results.append(len(fish))

fish = init_fish
for i in range(0, number_of_days):
    print(f'Day {i}')
    print(len(fish))
    for j in range(0, len(fish)):
        if fish[j] == 0:
            fish.append(8)
            fish[j] = 6
        else:
            fish[j] -= 1

total_fish = 0
for this_fish in init_fish:
    total_fish += results[this_fish]
b = datetime.datetime.now()

print(b-a)
print(total_fish)
