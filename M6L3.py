import pygame
import time
pygame.init()

back = (200, 255, 255)
mw = pygame.display.set_mode((500, 500))
mw.fill(back)
clock = pygame.time.Clock()

class Area():
    def __init__(self, x=0, y=0, width=10, height=10, color=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.fill_color = color
    def color(self, new_color):
        self.fill_color = new_color
    def fill(self):
        pygame.draw.rect(mw, self.fill_color, self.rect)
    def outline(self, frame_color, thickness):
        pygame.draw.rect(mw, frame_color, self.rect, thickness)

class Label(Area):
    def set_text(self, text, fsize=12, text_color=(0, 0, 0))
        self.image = pygame.font.SysFont('verdana', fsize).render(text, True, text_color)
                 
while True:
    pygame.display.update()
    clock.tick(40)

    