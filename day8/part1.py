ones = 0
fours = 0
sevens = 0
eights = 0

# counts:
# 1 - 2
# 7 - 3
# 4 - 4
# 5 - 5
# 2 - 5
# 3 - 5
# 0 - 6
# 6 - 6
# 9 - 6
# 8 - 7

def find_mapping(digits):
    one = list([x for x in digits if len(x) == 2][0])
    seven = list([x for x in digits if len(x) == 3][0])
    four = list([x for x in digits if len(x) == 4][0])
    nine = list([x for x in digits if len(x) == 6 and x.issuperset(four)][0])
    six = list([x for x in digits if len(x) == 6 and not x.issuperset(one)][0])
    zero = list([x for x in digits if len(x) == 6 and not x.issuperset(six) and not x.issuperset(nine)][0])
    eight = list([x for x in digits if len(x) == 7][0])
    three = list([x for x in digits if len(x) == 5 and x.issuperset(one)][0])
    five = list([x for x in digits if len(x) == 5 and x.union(one).issuperset(nine)][0])
    two = list([x for x in digits if len(x) == 5 and not x.union(one).issuperset(nine) and not x.issuperset(three)][0])

    output_list = [one, two, three, four, five, six, seven, eight, nine, zero]
    for x in output_list:
        x.sort()

    print(output_list)

    print(one)
    print(two)
    print(three)
    print(four)
    print(five)
    print(six)
    print(seven)
    print(eight)
    print(nine)
    print(zero)

    return {
        "".join(one): 1,
        "".join(two): 2,
        "".join(three): 3,
        "".join(four): 4,
        "".join(five): 5,
        "".join(six): 6,
        "".join(seven): 7,
        "".join(eight): 8,
        "".join(nine): 9,
        "".join(zero): 0,
    }

total = 0
with open('input.txt', 'r') as f:
    for line in f:
        print(line)
        (patterns, whole_output) = line.split("|")
        digits = [frozenset(x) for x in patterns.strip().split()]
        outputs = [list(x) for x in whole_output.split()]
        for output in outputs:
            output.sort()
        mappings = find_mapping(digits)
        print(mappings)
        real_digits = [mappings["".join(x)] for x in outputs]
        print(real_digits)
        output_number = real_digits[0] * 1000 + real_digits[1] * 100 + real_digits[2] * 10 + real_digits[3]
        print(output_number)
        total += output_number


print(total)