import pygame
import numpy as np

# Initialize the game window size and colors
WINDOW_SIZE = (1000, 1000)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRID_COLOR = (50, 50, 50)

# Set the size of the grid and the cells
CELL_SIZE = 8
GRID_WIDTH = WINDOW_SIZE[0] // CELL_SIZE
GRID_HEIGHT = WINDOW_SIZE[1] // CELL_SIZE

# Function to initialize the grid with random live and dead cells
def draw_grid(screen, grid):
    for x in range(GRID_WIDTH):
        for y in range(GRID_HEIGHT):
            rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            if grid[x, y] == 1:
                pygame.draw.rect(screen, WHITE, rect)
            else:
                pygame.draw.rect(screen, BLACK, rect)
            pygame.draw.rect(screen, GRID_COLOR, rect, 1)

def game_of_life():
    pygame.init()
    screen = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption("Conway's Game of Life")
    
    clock = pygame.time.Clock()

    # Initialize the grid
    grid = initialize_grid(randomize=True)

    running = True
    paused = False

    while running:
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    paused = not paused
                if event.key == pygame.K_r:
                    grid = initialize_grid(randomize=True)
                if event.key == pygame.K_c:
                    grid = initialize_grid(randomize=False)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    x, y = pygame.mouse.get_pos()
                    grid[x // CELL_SIZE, y // CELL_SIZE] = 1 - grid[x // CELL_SIZE, y // CELL_SIZE]  # Toggle cell state

        if not paused:
            grid = update_grid(grid)

        draw_grid(screen, grid)

        pygame.display.update()
        clock.tick(10)

    pygame.quit()
