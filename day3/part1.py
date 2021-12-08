with open('input.txt', 'r') as f:
    diagnostics = [x.strip() for x in f.readlines()]


gamma = []
epsilon = []
for i in range(0, len(diagnostics[0])):
    if oxygen is not None:
        continue
    ones = 0
    zeros = 0
    for diagnostic in diagnostics:
        if diagnostic[i] == '0':
            zeros += 1
        else:
            ones += 1
    if ones >= zeros:
        value = '1'
    else:
        value = '0'

    diagnostics = [x for x in diagnostics if x[i] == value]
    if len(diagnostics) == 1:
        oxygen = diagnostics[0]

print(int(''.join(gamma), 2) * int(''.join(epsilon), 2))
