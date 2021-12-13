with open('input.txt') as file:
    file = [x.strip() for x in file.readlines()]


class Board:
    def __init__(self, rows):
        self.rows = rows
        self.win_score = 0
        self.win_turn = None
        self.win_value = 0
        self.final_score = 0


def setup_boards(rows):
    boards = []
    for index, row in enumerate(rows, 0):
        if index + 5 > len(rows):
            break
        if row == '':
            card_rows = rows[index + 1: index + 6]
            card = [number.split() for number in card_rows]
            boards.append(Board(card))
    return boards


def calculate_score(board):
    sum = 0
    for row in board.rows:
        for element in row:
            if element != 'x':
                sum += int(element)
    return sum


def determine_winner(boards):
    winning_board = boards[0]
    for board in boards:
        if board.win_turn < winning_board.win_turn:
            winning_board = board

    return winning_board


def determine_loser(boards):
    losing_board = boards[0]
    for board in boards:
        if board.win_turn > losing_board.win_turn:
            losing_board = board
    return losing_board


def print_results(board):
    print("win turn: " + str(board.win_turn))
    print("win val: " + str(board.win_val))
    print("win score: " + str(board.win_score))
    print("** final score **: " + str(int(board.win_score) * int(board.win_val)))


def play_bingo(board, numbers):
    win = ['x', 'x', 'x', 'x', 'x']

    for turn, drawn in enumerate(numbers):
        for index, row in enumerate(board.rows):
            board.rows[index] = ['x' if item ==
                                 drawn else item for item in row]

        for row in board.rows:
            if row == win:
                board.win_turn = turn
                board.win_val = drawn
                board.win_score = calculate_score(board)
                return board

        for i in range(len(board.rows[0])):
            col = []
            for j in range(len(board.rows)):
                col.append(board.rows[j][i])
            if col == win:
                board.win_turn = turn
                board.win_val = drawn
                board.win_score = calculate_score(board)
                return board

    return board


def d04(file):
    drawn_numbers = file[0].split(',')
    board_numbers = file[1::]
    boards = setup_boards(board_numbers)

    result_boards = [play_bingo(board, drawn_numbers) for board in boards]

    print("== Winning board ==")
    print_results(determine_winner(result_boards))

    print("== Losing Board ==")
    print_results(determine_loser(result_boards))


d04(file)
