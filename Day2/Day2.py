def get_strategy(filename):
    with open(filename) as file:
        lines = file.readlines()
    opponent_moves = []
    your_moves = []
    for line in lines:
        opponent_move = line[0]
        your_move = line[2]
        opponent_moves.append(opponent_move)
        your_moves.append(your_move)

    return opponent_moves, your_moves

def get_scores_part1(opponent_moves, your_moves):
    play_score = {'X': 1, 'Y': 2, 'Z': 3}
    n_rounds = len(opponent_moves)
    scores = [0]*n_rounds
    for i in range(n_rounds):
        #Draws
        if (opponent_moves[i]== 'A') and (your_moves[i]=='X'):
            scores[i]=3
        if (opponent_moves[i] == 'B') and (your_moves[i] == 'Y'):
            scores[i] = 3
        if (opponent_moves[i] == 'C') and (your_moves[i] == 'Z'):
            scores[i] = 3
        #Wins
        if (opponent_moves[i]=='A') and (your_moves[i]=='Y'):
            scores[i] = 6
        if (opponent_moves[i]=='B') and (your_moves[i]=='Z'):
            scores[i] = 6
        if (opponent_moves[i]=='C') and (your_moves[i]=='X'):
            scores[i] = 6
        #Loses
        if (opponent_moves[i]=='A') and (your_moves[i]=='Z'):
            scores[i] = 0
        if (opponent_moves[i] == 'B') and (your_moves[i] == 'X'):
            scores[i] = 0
        if (opponent_moves[i] == 'C') and (your_moves[i] == 'Y'):
            scores[i] = 0

        #Adding strategy score
        scores[i] += play_score[your_moves[i]]

    return scores

def get_scores_part2(opponent_moves, your_moves):
    n_rounds = len(opponent_moves)
    scores = [0]*n_rounds
    for i in range(n_rounds):
        #Lose
        if your_moves[i]=='X':
            if opponent_moves[i]=='A':
                move_score = 3
            if opponent_moves[i]=='B':
                move_score = 1
            if opponent_moves[i]=='C':
                move_score = 2
            scores[i]=0+move_score
        #Draw
        if your_moves[i]=='Y':
            if opponent_moves[i]=='A':
                move_score = 1
            if opponent_moves[i]=='B':
                move_score = 2
            if opponent_moves[i]=='C':
                move_score = 3
            scores[i] = 3 + move_score
        #Win
        if your_moves[i]=='Z':
            if opponent_moves[i]=='A':
                move_score = 2
            if opponent_moves[i]=='B':
                move_score = 3
            if opponent_moves[i]=='C':
                move_score = 1
            scores[i] = 6 + move_score

    return scores

if __name__=='__main__':
    filename='input.txt'
    opponent_moves, your_moves = get_strategy(filename)

    your_scores1 = get_scores_part1(opponent_moves, your_moves)
    print('PART 1')
    print('Result:',sum(your_scores1))

    your_scores2 = get_scores_part2(opponent_moves, your_moves)
    print('\nPART 2')
    print('Result:', sum(your_scores2))
