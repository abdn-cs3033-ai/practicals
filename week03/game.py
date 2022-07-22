#!/usr/bin/env python
# Four spaces as indentation [no tabs]
import sys
import pygame
from pygame.locals import (QUIT, KEYDOWN, K_SPACE, K_ESCAPE)
from common import *
from player import *

# ==========================================
# Game
# ==========================================


class Game:

    # ------------------------------------------
    # Initialize
    # ------------------------------------------

    def __init__(self, map_name):
        # Setup
        self.map = read_map(map_name)
        pygame.init()
        screen = pygame.display.set_mode((TILE_WIDTH * self.map.width, TILE_HEIGHT * self.map.height))
        pygame.display.set_caption("[T1a]   A Link to the Path")
        background = pygame.Surface(screen.get_size()).convert()
        self.load_tileset(TILESET, 3, 1)
        self.draw_map(background)
        self.player = Player(self.map, self.load_image(PLAYER), 4, 8 / ZOOM)
        # Loop
        clock = pygame.time.Clock()
        game_over = False
        while not game_over:
            screen.blit(background, (0, 0))
            self.player.update(screen)
            pygame.display.flip()
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == QUIT:
                    game_over = True
                elif event.type == KEYDOWN:
                    if event.key == K_SPACE: # Reset this map
                        self.player.setup(self.map)
                    elif event.key == K_ESCAPE: # Load map
                        map_name = input('Load map: ')
                        self.map = read_map(map_name)
                        if screen.get_size() != (TILE_WIDTH * self.map.width, TILE_HEIGHT * self.map.height):
                            del screen
                            del background
                            screen = pygame.display.set_mode((TILE_WIDTH * self.map.width, TILE_HEIGHT * self.map.height))
                            background = pygame.Surface(screen.get_size()).convert()
                        self.draw_map(background)
                        self.player.setup(self.map)

    # ------------------------------------------
    # Draw map
    # ------------------------------------------

    def draw_map(self, surface):
        map_y = 0
        for y in range(self.map.height):
            map_x = 0
            for x in range(self.map.width):
                tile = self.map.data[y][x]
                if tile == TILE_CLEAR or tile == TILE_CLOSED or tile == TILE_GOAL:
                    surface.blit(self.tileset[tile], (map_x, map_y))
                else:
                    raise Exception("Unknown tile", tile, (map_x, map_y))
                map_x += TILE_WIDTH
            map_y += TILE_HEIGHT

    # ------------------------------------------
    # Load image
    # ------------------------------------------

    def load_image(self, filename):
        img = pygame.image.load(os.path.join(PATH, "sprites", filename)).convert()
        img.set_colorkey((0, 128, 128))
        if ZOOM > 1:
            return pygame.transform.scale(img, (img.get_width() * ZOOM, img.get_height() * ZOOM))
        return img

    # ------------------------------------------
    # Load tileset
    # ------------------------------------------

    def load_tileset(self, filename, width, height):
        image = self.load_image(filename)
        self.tileset = []
        tile_y = 0
        for y in range(height):
            tile_x = 0
            for x in range(width):
                self.tileset.append(image.subsurface((tile_x, tile_y, TILE_WIDTH, TILE_HEIGHT)))
                tile_x += TILE_WIDTH
            tile_y += TILE_HEIGHT

# ==========================================
# Main
# ==========================================


if __name__ == "__main__":
    if len(sys.argv) == 2:
        map_name = sys.argv[1]
    else:
        map_name = DEFAULT_MAP
    print("Loading map: " + map_name)
    Game(map_name)