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

legal_map = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
}

score = 0
scores = []
with open('input.txt', 'r') as f:
    for line in f:
        stack = []
        chars_seen = []
        illegal = False

        for char in line.strip():
            chars_seen.append(char)
            if char == '{' or char == '[' or char == '(' or char == '<':
                stack.append(map[char])
            elif char == stack[-1]:
                stack.pop()
            else:
                score += illegal_map[char]
                illegal = True
                break

        if not illegal:
            legal_score = 0
            for char in reversed(stack):
                legal_score *= 5
                legal_score += legal_map[char]
            scores.append(legal_score)

scores.sort()
print(score)
print(scores[int((len(scores) - 1) / 2)])

