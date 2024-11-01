import pygame
import random
from collections import deque

# Initialize Pygame
pygame.init()

# Constants
WINDOW_SIZE = 400
GRID_SIZE = 20
GRID_COUNT = WINDOW_SIZE // GRID_SIZE
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Direction constants
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Set up display
screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption("AI Snake Game")
clock = pygame.time.Clock()
SNAKE_SPEED = 10  # Control game speed

class SnakeAI:
    def __init__(self):
        self.reset()

    def reset(self):
        self.length = 1
        self.positions = [(GRID_COUNT // 2, GRID_COUNT // 2)]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.food = None
        self.place_food()
        self.score = 0

    def place_food(self):
        while True:
            self.food = (random.randint(0, GRID_COUNT - 1), random.randint(0, GRID_COUNT - 1))
            if self.food not in self.positions:
                break

    def find_path_to_food(self):
        start = self.positions[0]
        goal = self.food
        queue = deque([[start]])
        visited = set([start])

        while queue:
            path = queue.popleft()
            row, col = path[-1]
            if (row, col) == goal:
                return path
            
            for dr, dc in [UP, DOWN, LEFT, RIGHT]:
                r, c = row + dr, col + dc
                
                if (0 <= r < GRID_COUNT and
                        0 <= c < GRID_COUNT and
                        (r, c) not in visited and
                        (r, c) not in self.positions[1:]):
                    
                    queue.append(path + [(r, c)])
                    visited.add((r, c))
        
        return None

    def get_next_move(self):
        path = self.find_path_to_food()
        if not path or len(path) < 2:
            # If no path is found, try to avoid obstacles
            head = self.positions[0]
            possible_moves = []

            for dr, dc in [UP, DOWN, LEFT, RIGHT]:
                r, c = head[0] + dr, head[1] + dc
                if (0 <= r < GRID_COUNT and
                        0 <= c < GRID_COUNT and
                        (r, c) not in self.positions):
                    possible_moves.append((r, c))

            if possible_moves:
                return random.choice(possible_moves)
            return None
        
        return path[1]

    def check_collision(self):
        head = self.positions[0]
        # Check wall collisions
        if (head[0] < 0 or head[0] >= GRID_COUNT or
                head[1] < 0 or head[1] >= GRID_COUNT):
            return True
        if head in self.positions[1:]:
            return True
        return False

    def update(self):
        next_move = self.get_next_move()
        if next_move is None or self.check_collision():
            return False
        
        self.positions.insert(0, next_move)
        if self.positions[0] == self.food:
            self.score += 1
            self.place_food()
        else:
            self.positions.pop()
        
        return True

    def draw(self, screen):
        # Draw snake
        for position in self.positions:
            rect = pygame.Rect(position[1] * GRID_SIZE, position[0] * GRID_SIZE,
                               GRID_SIZE - 2, GRID_SIZE - 2)
            pygame.draw.rect(screen, GREEN, rect)

        # Draw food
        rect = pygame.Rect(self.food[1] * GRID_SIZE, self.food[0] * GRID_SIZE,
                           GRID_SIZE - 2, GRID_SIZE - 2)
        pygame.draw.rect(screen, RED, rect)

        # Draw grid lines (optional)
        for x in range(0, WINDOW_SIZE, GRID_SIZE):
            pygame.draw.line(screen, (40, 40, 40), (x, 0), (x, WINDOW_SIZE))
            pygame.draw.line(screen, (40, 40, 40), (0, x), (WINDOW_SIZE, x))

def main():
    snake = SnakeAI()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        if not snake.update():
            print(f"Game Over! Final Score: {snake.score}")  # Show final score
            snake.reset()

        screen.fill(BLACK)
        snake.draw(screen)

        # Draw score
        font = pygame.font.Font(None, 36)
        score_text = font.render(f'Score: {snake.score}', True, WHITE)
        screen.blit(score_text, (10, 10))

        pygame.display.flip()
        clock.tick(SNAKE_SPEED)  # Control game speed
    
    pygame.quit()

if __name__ == "__main__":
    main()
