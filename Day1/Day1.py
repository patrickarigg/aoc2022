def get_calories_per_elf(data='real'):
    if data=='real':
        filename = 'input.txt'
    else:
        filename = 'test_input.txt'

    with open(filename) as file:
        lines = file.readlines()
    calorie_list = [line[:-1] for line in lines]

    calories_per_elf = []
    calorie_count = 0
    for line in calorie_list:
        if line!='':
            calorie_count += int(line)
        else:
            calories_per_elf.append(calorie_count)
            calorie_count = 0

    return calories_per_elf

def sum_top_three_elves(calories_per_elf):
    c_calories_per_elf = calories_per_elf.copy()
    top_three_calories = []
    for i in range(3):
        max_calorie_value = max(c_calories_per_elf)
        top_three_calories.append(max_calorie_value)
        c_calories_per_elf.remove(max_calorie_value)
    return sum(top_three_calories)

def part1():
    calories_per_elf = get_calories_per_elf()
    print(max(calories_per_elf))

def part2():
    calories_per_elf = get_calories_per_elf()
    sum_top_three = sum_top_three_elves(calories_per_elf)
    print(sum_top_three)


if __name__=="__main__":
    print('PART 1:')
    part1()

    print('\nPART 2:')
    part2()

sum_top_three_elves
