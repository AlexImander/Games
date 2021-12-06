from game2048.modules.move import MoveBlocks


def game_over(game_matrix_size: list, game_matrix: list) -> bool:
    game_over_is = []
    moves = ['up', 'down', 'left', 'right']
    for move in moves:
        move_matrix = MoveBlocks(game_matrix_size, game_matrix, move)
        game_matrix_new = move_matrix.move_blocks()
        if game_matrix_new == game_matrix:
            game_over_is.append(True)
        else:
            game_over_is.append(False)
    return all(game_over_is)
