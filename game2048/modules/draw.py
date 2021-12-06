import pygame as pg
import game2048.configuration as cfg


class Draw:
    def __init__(self, display, game_matrix_size, game_matrix, score):
        self.display = display
        self.game_matrix_size = game_matrix_size
        self.game_matrix = game_matrix
        self.score = score

    def draw_blocks(self):
        for i in range(self.game_matrix_size[0]):
            for j in range(self.game_matrix_size[1]):
                number = self.game_matrix[i][j]
                x = cfg.gap_block_size * (j + 1) + cfg.block_size * j
                y = cfg.gap_block_size * (i + 1) + cfg.block_size * i + 150
                pg.draw.rect(self.display, pg.Color(cfg.block_background_font_color[number][0]), (x, y, cfg.block_size, cfg.block_size))
                if number != 0:
                    text_str = str(number)
                    text_pos = [x + cfg.block_size / 2, y + cfg.block_size / 2]
                    text_font = 20
                    text_color = cfg.block_background_font_color[number][1]
                    self.display.blit(*self.draw_text(text_str, text_pos, text_font, text_color))

    def draw_score(self):
        text_str = f'Score: {self.score}'
        text_pos = [cfg.display_size_w / 2, 50]
        text_font = 32
        text_color = (255, 255, 255)
        self.display.blit(*self.draw_text(text_str, text_pos, text_font, text_color))

    def draw_restart(self):
        text_str = 'Press R to restart'
        text_pos = [cfg.display_size_w / 2, 100]
        text_font = 28
        text_color = (255, 255, 255)
        self.display.blit(*self.draw_text(text_str, text_pos, text_font, text_color))

    @staticmethod
    def draw_text(text_str, text_pos, text_font, text_color):
        font = pg.font.Font('resources/font/Excelorate-Font.otf', text_font)
        text = font.render(text_str, True, pg.Color(text_color))
        text_rect = text.get_rect()
        text_rect.centerx, text_rect.centery = text_pos
        return text, text_rect
