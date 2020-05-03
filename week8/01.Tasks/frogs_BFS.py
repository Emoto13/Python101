import time


def legal_moves(board):
    moves = []
    for index, piece in enumerate(board):
        jump_move = index + (piece * 2)
        move = index + piece
        if piece == 0:
            continue
        if not ((jump_move < 0) or (jump_move >= len(board))):
            if board[jump_move] == 0:
                new_position = list(board)
                new_position[index] = 0
                new_position[jump_move] = piece
                moves.append(new_position)
        if not ((move < 0) or (move >= len(board))):
            if board[move] == 0:
                new_position = list(board)
                new_position[index] = 0
                new_position[move] = piece
                moves.append(new_position)
    return moves


def get_moves(tree, final):
    next_moves = []
    for node in tree:
        new_nodes = legal_moves(node[-1])
        for new_node in new_nodes:
            next_move = list(node)
            next_move.append(new_node)
            if new_node == final:
                return next_move
            next_moves.append(next_move)
    return next_moves


def serialize_data(frogs):
    lst = []

    dicts = {'_': 0,
             '>': 1,
             '<': -1
             }
    for i in frogs:
        lst.append(dicts[i])
    return lst


def deserialize_data(positions):
    dicts = {0: '_',
             1: '>',
             -1: '<'
             }

    res = []
    for position in positions:
        current_position = []
        for piece in position:
            current_position.append(dicts[piece])
        current_position.append('\n')
        res.append("".join(current_position))
    return "".join(res)


def solve(frogs):
    if frogs.count('>') != frogs.count('<') or frogs.count('_') != 1:
        raise ValueError('Wrong swamp')

    frog_list = serialize_data(frogs)

    positions = [[frog_list]]
    end_position = list(frog_list)
    end_position.reverse()
    while positions[-1] != end_position:
        positions = get_moves(positions, end_position)
    positions = deserialize_data(positions)
    print(positions)


def main():
    start_time = time.time()
    solve('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>_'
          '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
    print(time.time() - start_time)


if __name__ == '__main__':
    main()
