import pygame
import random
import sys

# Oyun ayarları
SIZE = 4
TILE_SIZE = 100
MARGIN = 5
WIDTH = SIZE * TILE_SIZE + (SIZE+1) * MARGIN
HEIGHT = WIDTH
FONT_SIZE = 40

# Renkler
BACKGROUND_COLOR = (187, 173, 160)
EMPTY_COLOR = (205, 193, 180)
TILE_COLORS = {
    2: (238, 228, 218),
    4: (237, 224, 200),
    8: (242, 177, 121),
    16: (245, 149, 99),
    32: (246, 124, 95),
    64: (246, 94, 59),
    128: (237, 207, 114),
    256: (237, 204, 97),
    512: (237, 200, 80),
    1024: (237, 197, 63),
    2048: (237, 194, 46),
}

# Pygame başlat
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2048")
font = pygame.font.SysFont("arial", FONT_SIZE)

# Tahta oluştur
def new_board():
    board = [[0]*SIZE for _ in range(SIZE)]
    add_new_tile(board)
    add_new_tile(board)
    return board

def add_new_tile(board):
    empty = [(r,c) for r in range(SIZE) for c in range(SIZE) if board[r][c] == 0]
    if empty:
        r,c = random.choice(empty)
        board[r][c] = random.choice([2,4])

def draw_board(board):
    screen.fill(BACKGROUND_COLOR)
    for r in range(SIZE):
        for c in range(SIZE):
            value = board[r][c]
            rect_x = MARGIN + c * (TILE_SIZE + MARGIN)
            rect_y = MARGIN + r * (TILE_SIZE + MARGIN)
            rect = pygame.Rect(rect_x, rect_y, TILE_SIZE, TILE_SIZE)
            color = TILE_COLORS.get(value, EMPTY_COLOR)
            pygame.draw.rect(screen, color, rect)
            if value != 0:
                text = font.render(str(value), True, (0,0,0))
                text_rect = text.get_rect(center=rect.center)
                screen.blit(text, text_rect)
    pygame.display.flip()

# Ana döngü
board = new_board()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    draw_board(board)

pygame.quit()
sys.exit()
