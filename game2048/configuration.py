# Frames per seconds
fps = 30
# Game matrix
game_matrix_size = [4, 4]
game_matrix = [[0 for _ in range(list(game_matrix_size)[1])] for _ in range(list(game_matrix_size)[0])]
# Blocks
block_size = 80
gap_block_size = 10
block_background_font_color = {
        0: ['#CAC2B2', None],
        2: ['#EDE6DA', '#7B7766'],
        4: ['#EAE1C6', '#7B7766'],
        8: ['#EFB27B', '#F1F5EB'],
        16: ['#F09A65', '#F1F5EB'],
        32: ['#F37D61', '#F1F5EB'],
        64: ['#F36241', '#F1F5EB'],
        128: ['#EACF76', '#F1F5EB'],
        256: ['#EDCA67', '#F1F5EB'],
        512: ['#E9C757', '#F1F5EB'],
        1024: ['#E8C356', '#F1F5EB'],
        2048: ['#E8C04E', '#F1F5EB'],
        4096: ['#EDE6DA', '#7B7766'],
        8192: ['#EAE1C6', '#7B7766'],
        16384: ['#EFB27B', '#F1F5EB'],
        32768: ['#F09A65', '#F1F5EB'],
        65536: ['#F37D61', '#F1F5EB'],
        131072: ['#F36241', '#F1F5EB'],
        262144: ['#EACF76', '#F1F5EB'],
        524288: ['#EDCA67', '#F1F5EB'],
        1048576: ['#E9C757', '#F1F5EB'],
        2097152: ['#E8C356', '#F1F5EB'],
        4194304: ['#E8C04E', '#F1F5EB'],
}
# Display
display_size_w = game_matrix_size[1] * block_size + (game_matrix_size[1] + 1) * gap_block_size
display_size_h = game_matrix_size[0] * block_size + (game_matrix_size[0] + 1) * gap_block_size
display_size = (display_size_w, display_size_h + 150)
display_background_color = '#B9AEA0'
