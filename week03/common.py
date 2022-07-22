#!/usr/bin/env python
# Four spaces as indentation [no tabs]
import os, inspect
from collections import namedtuple

PATH        = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
DEFAULT_MAP = "easy.txt"
DEBUG       = False

# Frames per second (more means faster)
FPS         = 30

# Image files
# Zelda
PLAYER = "link.bmp"
TILESET = "link_tiles.bmp"
# Pokemon
# PLAYER = "red.png"
# TILESET = "red_tiles.png"

# Map (map values must match the following)
TILE_CLEAR  = 0
TILE_CLOSED = 1
TILE_GOAL   = 2
# Tileset (pixels of image)
ZOOM        = 2
TILE_WIDTH  = 16 * ZOOM
TILE_HEIGHT = 16 * ZOOM
# Player (directions in the image)
MOVE_RIGHT  = 0
MOVE_LEFT   = 1
MOVE_UP     = 2
MOVE_DOWN   = 3
# Pixels per frame, must match tile size (TILE_WIDTH % MOVE_SPEED == 0 and TILE_HEIGHT % MOVE_SPEED == 0)
MOVE_SPEED  = 4 * ZOOM

# Immutable structures
Point = namedtuple('Point', ['x', 'y'])


class Map:
    def __init__(self, sx, sy, gx, gy, map_width, map_height, map_data):
        self.start = Point(sx, sy)
        self.goal = Point(gx, gy)
        self.width = map_width
        self.height = map_height
        self.data = map_data

    # ------------------------------------------
    # Successors
    # ------------------------------------------

    def successors(self, x, y):
        n = []
        if x - 1 >= 0 and self.data[y][x - 1] != TILE_CLOSED:
            n.append(Point(x - 1, y))
        if x + 1 < self.width and self.data[y][x + 1] != TILE_CLOSED:
            n.append(Point(x + 1, y))
        if y - 1 >= 0 and self.data[y - 1][x] != TILE_CLOSED:
            n.append(Point(x, y - 1))
        if y + 1 < self.height and self.data[y + 1][x] != TILE_CLOSED:
            n.append(Point(x, y + 1))
        return n


# ------------------------------------------
# Read map
# ------------------------------------------

def read_map(filename):
    with open(os.path.join(PATH, "maps", filename)) as map_file:
        sx = int(map_file.readline())
        sy = int(map_file.readline())
        data = [[int(cell) for cell in row.rstrip()] for row in map_file]
        width = len(data[0])
        height = len(data)
        if sx < 0 or sx >= width:
            raise Exception("Player outside map width", width, sx)
        elif sy < 0 or sy >= height:
            raise Exception("Player outside map height", height, sy)
        for row in data:
            if len(row) != width:
                raise Exception("Map width does not match", width, len(row))
        gx = None
        gy = None
        for y in range(height):
            for x in range(width):
                cell = data[y][x]
                if cell != TILE_CLEAR and cell != TILE_CLOSED:
                    if cell == TILE_GOAL:
                        if gx is None:
                            gx = x
                            gy = y
                        else:
                            raise Exception("Goal already defined", (x, y), (gx, gy))
                    else:
                        raise Exception("Unknown tile", cell)
        if gx is None:
            raise Exception("Goal not found in map")
        return Map(sx, sy, gx, gy, width, height, data)


# ------------------------------------------
# Direction
# ------------------------------------------

def direction(p1, p2):
    if p1.x < p2.x:
        return MOVE_RIGHT
    elif p1.x > p2.x:
        return MOVE_LEFT
    elif p1.y < p2.y:
        return MOVE_DOWN
    elif p1.y > p2.y:
        return MOVE_UP
    raise Exception("Unknown direction", p1.x, p1.y, p2.x, p2.y)
