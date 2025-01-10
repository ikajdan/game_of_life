import random
from os import environ

environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"

import pygame


class GameOfLife:
    """
    A class that implements Conway's Game of Life using the Pygame library.
    """

    def __init__(self):
        self.fps = 60
        self.update_frequency = 60
        self.width = 600
        self.height = 600
        self.tile_size = 20
        self.grid_width = self.width // self.tile_size
        self.grid_hight = self.height // self.tile_size
        self.grid_color = (60, 60, 60)
        self.cell_color = (255, 255, 255)
        self.background_color = (0, 0, 0)

        pygame.init()  # pylint: disable=no-member
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Game of Life")
        self.clock = pygame.time.Clock()
        self.running = True
        self.playing = False
        self.positions = set()
        self.update_counter = 0

    def generate_random_positions(self, num_cells):
        return {
            (
                random.randint(0, self.grid_width - 1),
                random.randint(0, self.grid_hight - 1),
            )
            for _ in range(num_cells)
        }

    def draw_grid_and_cells(self):
        self.screen.fill(self.background_color)
        for row in range(self.grid_hight):
            pygame.draw.line(
                self.screen,
                self.grid_color,
                (0, row * self.tile_size),
                (self.width, row * self.tile_size),
            )
        for col in range(self.grid_width):
            pygame.draw.line(
                self.screen,
                self.grid_color,
                (col * self.tile_size, 0),
                (col * self.tile_size, self.height),
            )
        for col, row in self.positions:
            center_x = col * self.tile_size + self.tile_size // 2
            center_y = row * self.tile_size + self.tile_size // 2
            pygame.draw.circle(
                self.screen, self.cell_color, (center_x, center_y), self.tile_size // 3
            )

    def adjust_grid(self):
        new_positions = set()
        potential_positions = set()
        for position in self.positions:
            neighbors = self.get_neighbors(position)
            live_neighbors = self.positions.intersection(neighbors)
            if len(live_neighbors) in {2, 3}:
                new_positions.add(position)
            potential_positions.update(neighbors - self.positions)
        for position in potential_positions:
            if len(self.positions.intersection(self.get_neighbors(position))) == 3:
                new_positions.add(position)
        return new_positions

    def get_neighbors(self, position):
        x, y = position
        return {
            (x + dx, y + dy)
            for dx in [-1, 0, 1]
            for dy in [-1, 0, 1]
            if (dx != 0 or dy != 0)
            and 0 <= x + dx < self.grid_width
            and 0 <= y + dy < self.grid_hight
        }

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.MOUSEBUTTONDOWN and not self.playing:
                col, row = (
                    event.pos[0] // self.tile_size,
                    event.pos[1] // self.tile_size,
                )
                cell = (col, row)
                if cell in self.positions:
                    self.positions.remove(cell)
                else:
                    self.positions.add(cell)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.playing = not self.playing
                if event.key == pygame.K_c and not self.playing:
                    self.positions.clear()
                    self.update_counter = 0
                if event.key == pygame.K_r and not self.playing:
                    self.positions = self.generate_random_positions(200)

    def run(self):
        while self.running:
            self.clock.tick(self.fps)
            pygame.display.set_caption(
                "Game of Life" if self.playing else "Game of Life [Paused]"
            )
            if self.playing:
                self.update_counter += 1
            if self.update_counter >= self.update_frequency:
                self.positions = self.adjust_grid()
                self.update_counter = 0
            self.handle_events()
            self.draw_grid_and_cells()
            pygame.display.flip()
        pygame.quit()  # pylint: disable=no-member


if __name__ == "__main__":
    game = GameOfLife()
    game.run()
