def get_rucksacks_by_compartments(filename):
    with open(filename) as file:
        lines = file.readlines()
    rucksacks = []
    for line in lines:
        contents = line.strip('\n')
        mid_index = int(len(contents)/2)
        compartment1 = contents[:mid_index]
        compartment2 = contents[mid_index:]
        rucksacks.append([compartment1, compartment2])
    return rucksacks

def get_elf_groups(filename):
    with open(filename) as file:
        lines = file.readlines()

    rucksacks = [line.strip('\n') for line in lines]
    n_groups = int(len(rucksacks)/3)

    elf_groups = []
    for i in range(n_groups):
        elf_groups.append(rucksacks[3*i:3*i+3])

    return elf_groups

def find_group_badges_and_priorities(elf_groups):
    group_badges = []
    group_priorities = []
    for group in elf_groups:
        elf1_rucksack = group[0]
        elf2_rucksack = group[1]
        elf3_rucksack = group[2]
        for letter in elf1_rucksack:
            if (letter in elf2_rucksack) and (letter in elf3_rucksack):
                group_badges.append(letter)
                group_priorities.append(priority_of(letter))
                break
    return group_badges, group_priorities



def priority_of(character):
    if character.isupper():
        return ord(character) - 38
    if character.islower():
        return ord(character) - 96

def get_all_priorities(rucksacks):
    priorities = []
    for rucksack in rucksacks:
        compartment1 = rucksack[0]
        compartment2 = rucksack[1]

        for letter in compartment1:
            if letter in compartment2:
                priorities.append(priority_of(letter))
                break
    return priorities

if __name__=='__main__':
    print("PART1")
    rucksacks = get_rucksacks_by_compartments('input.txt')
    print(rucksacks)
    priorities = get_all_priorities(rucksacks)
    print(priorities)
    print(sum(priorities))

    print('PART2')
    elf_groups = get_elf_groups('input.txt')
    group_badges, group_priorities = find_group_badges_and_priorities(elf_groups)
    print(group_priorities)
    print(sum(group_priorities))
