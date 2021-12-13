path_map = {}
with open('input.txt', 'r') as f:
    for line in f:
        (orig, dest) = line.strip().split('-')
        if orig not in path_map:
            path_map[orig] = set()
        if dest not in path_map:
            path_map[dest] = set()
        path_map[orig].add(dest)
        path_map[dest].add(orig)


current_position = 'start'

def calculate_paths(current_path):
    if current_path[-1] == 'end':
        return [current_path]

    paths = []
    next_steps = path_map[current_path[-1]]
    for next_step in next_steps:
        if next_step.isupper() or next_step not in current_path:
            new_path = current_path.copy()
            new_path.append(next_step)
            paths.extend(calculate_paths(new_path))

    return paths

paths = calculate_paths([current_position])
print(paths)
print(len(paths))