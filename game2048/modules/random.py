import random as rd


class RandomBlock:
    def __init__(self, game_matrix_size: list, game_matrix: list):
        self.game_matrix_size = game_matrix_size
        self.game_matrix = game_matrix

    def random_block(self):
        zero = self.zero()
        if zero != []:
            i, j = rd.choice(zero)
            if rd.random() < 0.8:
                self.game_matrix[i][j] = 2
            else:
                self.game_matrix[i][j] = 4
        return self.game_matrix

    def zero(self):
        zero = []
        for i in range(self.game_matrix_size[0]):
            for j in range(self.game_matrix_size[1]):
                if self.game_matrix[i][j] == 0:
                    zero.append([i, j])
        return zero
