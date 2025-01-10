import random
from os import environ

environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"

import pygame

FPS = 60
UPDATE_FREQUENCY = 60
WIDTH = 600
HEIGHT = 600
TILE_SIZE = 20
GRID_WIDTH = WIDTH // TILE_SIZE
GRID_HEIGHT = HEIGHT // TILE_SIZE
GRID_COLOR = (60, 60, 60)
CELL_COLOR = (255, 255, 255)
BACKGROUND_COLOR = (0, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game of Life")
clock = pygame.time.Clock()


def generate_random_positions(num_cells):
    return {
        (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
        for _ in range(num_cells)
    }


def draw_grid_and_cells(positions):
    screen.fill(BACKGROUND_COLOR)

    for row in range(GRID_HEIGHT):
        pygame.draw.line(
            screen, GRID_COLOR, (0, row * TILE_SIZE), (WIDTH, row * TILE_SIZE)
        )

    for col in range(GRID_WIDTH):
        pygame.draw.line(
            screen, GRID_COLOR, (col * TILE_SIZE, 0), (col * TILE_SIZE, HEIGHT)
        )

    for col, row in positions:
        center_x = col * TILE_SIZE + TILE_SIZE // 2
        center_y = row * TILE_SIZE + TILE_SIZE // 2
        pygame.draw.circle(screen, CELL_COLOR, (center_x, center_y), TILE_SIZE // 3)


def adjust_grid(positions):
    new_positions = set()
    potential_positions = set()

    for position in positions:
        neighbors = get_neighbors(position)
        live_neighbors = positions.intersection(neighbors)

        if len(live_neighbors) in {2, 3}:
            new_positions.add(position)

        potential_positions.update(neighbors - positions)

    for position in potential_positions:
        if len(positions.intersection(get_neighbors(position))) == 3:
            new_positions.add(position)

    return new_positions


def get_neighbors(position):
    x, y = position
    return {
        (x + dx, y + dy)
        for dx in [-1, 0, 1]
        for dy in [-1, 0, 1]
        if (dx != 0 or dy != 0)
        and 0 <= x + dx < GRID_WIDTH
        and 0 <= y + dy < GRID_HEIGHT
    }


def main():
    running = True
    playing = False
    positions = set()
    update_counter = 0

    while running:
        clock.tick(FPS)

        if playing:
            pygame.display.set_caption("Game of Life")
            update_counter += 1
        else:
            pygame.display.set_caption("Game of Life [Paused]")

        if update_counter >= UPDATE_FREQUENCY:
            positions = adjust_grid(positions)
            update_counter = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN and not playing:
                col, row = event.pos[0] // TILE_SIZE, event.pos[1] // TILE_SIZE
                cell = (col, row)
                if cell in positions:
                    positions.remove(cell)
                else:
                    positions.add(cell)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    playing = not playing

                if event.key == pygame.K_c:
                    positions.clear()
                    playing = False
                    update_counter = 0

                if event.key == pygame.K_g and not playing:
                    positions = generate_random_positions(200)

        draw_grid_and_cells(positions)
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
