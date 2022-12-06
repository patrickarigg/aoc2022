def get_data(filename):
    with open(filename) as file:
        input = file.read().strip('\n')
    return input

def find_start_of_packet_marker(input):
    marker_index=0
    for i in range(len(input)-4):
        sequence = input[i:i+4]
        char_counts = [sequence.count(char) for char in sequence]
        if sum(char_counts)==4:
            marker_index=i+3
            print(f'last char: {sequence[-1]}')
            break
    return marker_index

def find_start_of_message_marker(input):
    marker_index = 0
    for i in range(len(input) - 4):
        sequence = input[i:i + 14]
        char_counts = [sequence.count(char) for char in sequence]
        if sum(char_counts) == 14:
            marker_index = i + 13
            print(f'last char: {sequence[-1]}')
            break
    return marker_index

if __name__=='__main__':
    input = get_data('input.txt')
    print(input)

    print('\n-----PART1-----')
    start_of_packet_marker_index = find_start_of_packet_marker(input)
    print('first marker after character:', start_of_packet_marker_index + 1)

    print('\n-----PART2-----')
    start_of_message_marker_index = find_start_of_message_marker(input)
    print('first marker after character:', start_of_message_marker_index + 1)
