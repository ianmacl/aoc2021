with open('input.txt', 'r') as f:
    diagnostics = [x.strip() for x in f.readlines()]

diag_copy = [x for x in diagnostics]
str_len = len(diagnostics[0])
oxygen = None
for i in range(0, str_len):
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

diagnostics = diag_copy
co2 = None
for i in range(0, str_len):
    if co2 is not None:
        continue
    ones = 0
    zeros = 0
    for diagnostic in diagnostics:
        if diagnostic[i] == '0':
            zeros += 1
        else:
            ones += 1
    if ones >= zeros:
        value = '0'
    else:
        value = '1'

    diagnostics = [x for x in diagnostics if x[i] == value]
    if len(diagnostics) == 1:
        co2 = diagnostics[0]

print(int(''.join(oxygen), 2) * int(''.join(co2), 2))
