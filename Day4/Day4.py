def get_data(filename):
    with open(filename) as file:
        lines = file.readlines()
    elf_pairs = []
    for line in lines:
        elf1_data,elf2_data = line.split(',')
        elf1_min, elf1_max = list(map(int,elf1_data.split('-')))
        elf2_min, elf2_max = list(map(int,elf2_data.split('-')))
        elf1 = list(range(elf1_min,elf1_max+1))
        elf2 = list(range(elf2_min,elf2_max+1))

        elf_pairs.append([elf1,elf2])
    return elf_pairs

def n_fully_overlapping_pairs(elf_pairs):
    n_fully_overlapping_pairs = 0
    for elf_pair in elf_pairs:
        if is_fully_overlapping(elf_pair[0],elf_pair[1]):
            n_fully_overlapping_pairs+=1
    return n_fully_overlapping_pairs


def n_overlapping_pairs(elf_pairs):
    n_overlapping_pairs = 0
    for elf_pair in elf_pairs:
        if is_overlapping(elf_pair[0], elf_pair[1]):
            n_overlapping_pairs += 1
    return n_overlapping_pairs


def is_fully_overlapping(list1,list2):
    if all(item in list1 for item in list2) or all(item in list2 for item in list1):
        return True
    return False


def is_overlapping(list1, list2):
    if any(item in list1 for item in list2) or any(item in list2 for item in list1):
        return True
    return False

if __name__=='__main__':
    elf_pairs = get_data('input.txt')
    print(elf_pairs)
    print('PART1')
    print(n_fully_overlapping_pairs(elf_pairs))
    print('PART2')
    print(n_overlapping_pairs(elf_pairs))
