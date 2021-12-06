class MoveBlocks:
    def __init__(self, game_matrix_size: list, game_matrix: list, move: str):
        self.game_matrix_size = game_matrix_size
        self.game_matrix = game_matrix
        self.move = move
        self.score = 0
        self.max_number2 = 4
        self.merge_is = False

    def move_blocks(self):
        move_cmd = {
            'up': 'self.move_up()',
            'down': 'self.move_down()',
            'left': 'self.move_left()',
            'right': 'self.move_right()',
        }
        try:
            eval(move_cmd[self.move])
        except:
            pass
        return self.game_matrix

    def move_up(self):
        game_matrix_new = []
        for arr in self.transpose(self.game_matrix):
            arr = self.merge(arr)
            arr = self.swap(arr)
            arr = arr + (self.game_matrix_size[0] - len(arr)) * [0]
            game_matrix_new.append(arr)
        self.game_matrix = self.transpose(game_matrix_new)

    def move_down(self):
        game_matrix_new = []
        for arr in self.transpose(self.game_matrix):
            arr = self.merge(list(reversed(arr)))
            arr = list(reversed(self.swap(arr)))
            arr = (self.game_matrix_size[0] - len(arr)) * [0] + arr
            game_matrix_new.append(arr)
        self.game_matrix = self.transpose(game_matrix_new)

    def move_left(self):
        game_matrix_new = []
        for arr in self.game_matrix:
            arr = self.merge(arr)
            arr = self.swap(arr)
            arr = arr + (self.game_matrix_size[1] - len(arr)) * [0]
            game_matrix_new.append(arr)
        self.game_matrix = game_matrix_new

    def move_right(self):
        game_matrix_new = []
        for arr in self.game_matrix:
            arr = self.merge(list(reversed(arr)))
            arr = list(reversed(self.swap(arr)))
            arr = (self.game_matrix_size[1] - len(arr)) * [0] + arr
            game_matrix_new.append(arr)
        self.game_matrix = game_matrix_new

    @staticmethod
    def transpose(matrix_arr: list) -> list:
        return list(map(list, zip(*matrix_arr)))

    def merge(self, arr: list) -> list:
        arr_merge = [arr[0]]
        count = 0
        for i in range(1, len(arr)):
            if arr[i] == arr_merge[count] and arr[i] != 0:
                arr_merge[count] += arr[i]
                self.score += arr_merge[count]
                self.merge_is = True
                arr_merge.append(0)
                count += 1
            elif arr[i] != arr_merge[count] and arr[i] != 0:
                arr_merge.append(arr[i])
                count += 1
        return arr_merge

    @staticmethod
    def swap(arr: list) -> list:
        arr_swap = []
        for i in arr:
            if i != 0:
                arr_swap.append(i)
        return arr_swap

    def getScore(self):
        return self.score

    def getMaxNumber(self):
        for arr in self.game_matrix:
            self.max_number2 = max(self.max_number2, max(arr))
        return self.max_number2

    def getMergeIs(self):
        return self.merge_is
