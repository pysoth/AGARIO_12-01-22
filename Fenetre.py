import random
from pygame.math import Vector2
import core



def setup():
    print("Setup START---------")
    core.fps = 30
    core.WINDOW_SIZE = [700, 700]

def show () :
    COLOURS = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (0, 255, 255), (255, 0, 255)]

    pygame.init()

    SCREEN_SIZE = (1000, 500)
    FONT = pygame.font.Font(None, 14)
    FEED = []
    ADERSARS = []