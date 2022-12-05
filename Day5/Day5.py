def get_data(filename):
    with open(filename) as file:
        lines = file.readlines()

    split_index = lines.index('\n')

    raw_stacks = [line.strip('\n') for line in lines[:split_index]]
    raw_moves = [line.strip('\n') for line in lines[split_index + 1:]]

    #get stacks
    len_max_line = max(list(map(len, raw_stacks)))
    padded_stacks = [line.ljust(len_max_line) for line in raw_stacks]

    n_stacks = int(padded_stacks[-1].strip().split()[-1])

    stacks = []
    for i in range(n_stacks):
        stack = [line[4 * i + 1] for line in padded_stacks[:-1] if line[4 * i + 1]!=' ']
        stacks.append(stack)

    #get moves
    moves = []
    for line in raw_moves:
        moves.append((int(line.split()[1]), int(line.split()[3]), int(line.split()[5])))

    return stacks, moves


def move_crates_9000(stacks,n_crates,stack_from,stack_to):
    for i in range(n_crates):
        crate = stacks[stack_from-1].pop(0)
        stacks[stack_to-1].insert(0,crate)


def move_crates_9001(stacks, n_crates, stack_from, stack_to):
    removed_crates = []
    for i in range(n_crates):
        crate = stacks[stack_from - 1].pop(0)
        removed_crates.append(crate)
    stacks[stack_to - 1] = removed_crates + stacks[stack_to - 1]


if __name__=='__main__':
    #PART 1
    print('____PART1____')
    stacks, moves = get_data('input.txt')
    print('BEFORE')
    print(stacks)
    for move in moves:
        n_crates, stack_from, stack_to = move
        move_crates_9000(stacks, n_crates, stack_from, stack_to)

    print('AFTER')
    print(stacks)

    result = ''.join([stack[0]for stack in stacks])
    print(f'\nResult: {result}')

    #PART 2
    print('\n____PART2____')
    stacks, moves = get_data('input.txt')
    print('BEFORE')
    print(stacks)
    for move in moves:
        n_crates, stack_from, stack_to = move
        move_crates_9001(stacks, n_crates, stack_from, stack_to)

    print('AFTER')
    print(stacks)

    result = ''.join([stack[0] for stack in stacks])
    print(f'\nResult: {result}')
