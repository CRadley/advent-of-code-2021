def is_winning(board, combination):
    for j in range(5):
        if set(board[j * 5 if j else 0:(j+ 1) *5]).issubset(set(combination)):
            return [int(x) for x in board[j * 5 if j else 0:(j+ 1) *5]]
        elif set([board[j], board[j + 5], board[j + 10], board[j + 15], board[j + 20]]).issubset(set(combination)):
            return [int(x) for x in [board[j], board[j + 5], board[j + 10], board[j + 15], board[j + 20]]]

def part_one(draws, boards):
    for i in range(len(draws)):
        if i < 5: 
            continue
        for b in boards:
            winning_combination = is_winning(b, draws[0:i+1])
            if winning_combination:
                return int(draws[i]) * sum([int(y) for y in b if y not in draws[0:i+1]])

def part_two(draws, boards):
    round_2_winners = []
    for i in range(len(draws)):
        if i < 5: 
            continue
        for b in boards:
            if b in round_2_winners:
                continue
            winning_combination = is_winning(b, draws[0:i+1])
            if winning_combination:
                if len(round_2_winners) == len(boards) - 1:
                    return int(draws[i]) * sum([int(y) for y in b if y not in draws[0:i+1]])
                round_2_winners.append(b)

def determine_inputs(filepath):
    with open(filepath, 'r') as f:
        lines = f.read()
    draws = lines.split('\n')[0].split(',')
    boards_unparsed = lines.split('\n\n')[1:]
    boards = [b.split() for b in boards_unparsed]
    return draws, boards
