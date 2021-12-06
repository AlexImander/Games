import pygame as pg
import configuration as cfg
from modules.move import MoveBlocks
from modules.random import RandomBlock
from modules.draw import Draw
from modules.game_over import game_over


pg.init()


# Start game
class Game:
    def __init__(self):
        self.display = pg.display.set_mode(cfg.display_size)
        self.clock = pg.time.Clock()
        self.game_matrix_size = cfg.game_matrix_size
        self.game_matrix = cfg.game_matrix
        self.score = 0
        self.max_number2 = 4
        self.move = None

    def run_game(self):
        game_open = True

        # Start game matrix
        self.getStartMatrix()

        # Open loop game
        while game_open:
            for event in pg.event.get():  # Game quit
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()
                elif event.type == pg.KEYDOWN:  # Game move
                    if event.key in [pg.K_UP, pg.K_DOWN, pg.K_LEFT, pg.K_RIGHT]:
                        self.move = {pg.K_UP: 'up', pg.K_DOWN: 'down', pg.K_LEFT: 'left', pg.K_RIGHT: 'right'}[event.key]
                        # Move blocks
                        moveblocks = MoveBlocks(self.game_matrix_size, self.game_matrix, self.move)
                        game_matrix_new = moveblocks.move_blocks()
                        self.score += moveblocks.getScore()
                        self.max_number2 = moveblocks.getMaxNumber()
                        if moveblocks.getMergeIs():
                            pg.mixer.music.load(r'resources/audio/merge.mp3')
                            pg.mixer.music.set_volume(0.5)
                            pg.mixer.music.play()
                        # Random block
                        if game_matrix_new != self.game_matrix:
                            randomblock = RandomBlock(self.game_matrix_size, game_matrix_new)
                            self.game_matrix = randomblock.random_block()
                        self.game_matrix = game_matrix_new
                        self.move = None

            # Create display
            pg.display.set_caption('2048')
            self.display.fill(cfg.display_background_color)

            # Draw
            draw = Draw(self.display, self.game_matrix_size, self.game_matrix, self.score)
            # Draw blocks
            draw.draw_blocks()
            # Draw score
            draw.draw_score()

            # Update display
            pg.display.update()
            self.clock.tick(cfg.fps)

            # Game over
            if game_over(self.game_matrix_size, self.game_matrix):
                # Draw restart
                draw.draw_restart()
                game_over_is = True
                while game_over_is:
                    for event in pg.event.get():
                        if event.type == pg.QUIT:
                            pg.quit()
                            quit()
                        if event.type == pg.KEYDOWN:
                            if event.key == pg.K_r:
                                self.game_matrix_size = cfg.game_matrix_size
                                self.game_matrix = cfg.game_matrix
                                self.getStartMatrix()
                                self.score = 0
                                self.max_number2 = 4
                                game_over_is = False
                    # Update display
                    pg.display.update()
                    self.clock.tick(cfg.fps)

    def getStartMatrix(self):
        # Start game matrix
        per = int(self.game_matrix_size[0] * self.game_matrix_size[1] * 20 / 100)
        for _ in range(per):
            startblock = RandomBlock(self.game_matrix_size, self.game_matrix)
            startblock.random_block()
        cfg.game_matrix = [[0 for _ in range(list(cfg.game_matrix_size)[1])] for _ in range(list(cfg.game_matrix_size)[0])]


if __name__ == "__main__":
    game = Game()
    game.run_game()
