map = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>',
}

illegal_map = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}

score = 0
scores = []
with open('input.txt', 'r') as f:
    for line in f:
        stack = []
        chars_seen = []

        for char in line.strip():
            chars_seen.append(char)
            if char == '{' or char == '[' or char == '(' or char == '<':
                stack.append(map[char])
            elif char == stack[-1]:
                stack.pop()
            else:
                print("".join(chars_seen))
                print(char)
                score += illegal_map[char]
                break

print(score)

