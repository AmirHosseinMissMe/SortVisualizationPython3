import random
import pygame
import math
import time
from constants import *

pygame.init()

win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(CAPTION)
pygame.draw.rect(win, (0, 0, 20), (0, 0, 800, 630))

elapsedTime, startTime = 0, 0

mouseX, mouseY = pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]

arraySize = 40  # default, 100 = huge, 80 = big, 40 = medium, 20 = small, 10 = very small
sortSpeed = 2  # 0 = instant, 1 = fast, 2 = normal, 3 = slow, 4 = very slow
algorithm = 0  # 0 = Bubble Sort, 1 = Selection Sort, 2 = Quick Sort, 3 = Merge Sort, 4 = Heap Sort

lineWidth = int(round((800 - (arraySize - 1) * 5 - 2 - 5) / arraySize))

vet = []
while len(vet) < arraySize:
    r = random.randint(10, 500)
    if r not in vet:
        vet.append(r)

colors = [BLUE for _ in range(arraySize)]

rPressed = False
sPressed = False



