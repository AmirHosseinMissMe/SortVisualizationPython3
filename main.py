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


def drawLines():
    line_x = 2
    index = 0
    for line in vet:
        pygame.draw.rect(win, colors[index], (line_x, 500, lineWidth, line - 500))
        line_x += lineWidth + 5
        index += 1
    pygame.display.update()


def clearScreen():
    pygame.draw.rect(win, (0, 0, 20), (0, 0, 800, 501))


def refreshLines():
    clearScreen()
    global vet, lineWidth, colors
    vet = []
    while len(vet) < arraySize:
        r2 = random.randint(10, 500)
        if r2 not in vet:
            vet.append(r2)
    lineWidth = int(round((800 - (arraySize - 1) * 5 - 2 - 5) / arraySize))
    colors = [BLUE for _ in range(arraySize)]
    for i2 in range(0, len(colors)):
        colors[i2] = BLUE
    drawLines()


def swapPos(pos1, pos2):
    global vet
    vet[pos1], vet[pos2] = vet[pos2], vet[pos1]


def slowDown():
    if sortSpeed == 2:
        pygame.time.delay(5)
    if sortSpeed == 3:
        pygame.time.delay(20)
    if sortSpeed == 4:
        pygame.time.delay(100)


def showOff():
    vet2 = vet.copy()
    vet2.sort(reverse=True)
    if vet == vet2:
        for index in range(len(vet)):
            pygame.event.get()
            setLineColor(index, BLUE)
            slowDown()
        for index in range(len(vet)):
            pygame.event.get()
            if index+1 < len(vet):
                setLineColor(index+1, PURPLE)
            setLineColor(index, PURPLE)
            slowDown()
            setLineColor(index, GREEN)


def sort():
    global startTime
    startTime = time.time()
    if sortSpeed == 0:
        vet.sort(reverse=True)
        for i2 in range(0, len(colors)):
            colors[i2] = GREEN
        clearScreen()
        drawLines()
        return
    if algorithm == 0:
        bubbleSort()
    elif algorithm == 1:
        selectionSort()
    elif algorithm == 2:
        quickSort(vet, 0, len(vet)-1)
    elif algorithm == 3:
        mergeSort(vet, 0, len(vet)-1)
    elif algorithm == 4:
        heapSort(vet)
    startTime = 0
    if algorithm != 3:
        showOff()


def bubbleSort():
    for i in range(len(vet) - 1, -1, -1):
        for j in range(i):
            pygame.event.get()
            setLineColor(j, RED)
            setLineColor(j + 1, RED)
            slowDown()
            if vet[j] < vet[j + 1]:
                swapPos(j, j + 1)
                clearScreen()
                drawLines()
            setLineColor(j, BLUE)
            setLineColor(j + 1, BLUE)
            drawTimer()
        setLineColor(i, PURPLE)


def selectionSort():
    for i in range(len(vet) - 1, -1, -1):
        max_index = 0
        for j in range(i + 1):
            pygame.event.get()
            setLineColor(j, RED)
            slowDown()
            if vet[j] < vet[max_index] or j == 0:
                setLineColor(max_index, BLUE)
                max_index = j
                setLineColor(max_index, (200, 200, 255))
            else:
                setLineColor(j, BLUE)
            drawTimer()
        setLineColor(max_index, BLUE)
        swapPos(i, max_index)
        setLineColor(i, PURPLE)
        clearScreen()
        drawLines()


def quickSort(array, low, high):
    if low < high:
        q = quick(array, low, high)
        quickSort(array, low, q - 1)
        quickSort(array, q + 1, high)
    clearScreen()
    drawLines()


def quick(array, low, high):
    i = low-1
    pivot = array[high]
    for j in range(low, high):
        setLineColor(j, RED)
        setLineColor(i+1, RED)
        drawTimer()
        slowDown()
        if array[j] >= pivot:
            i = i + 1
            setLineColor(i, BLUE)
            swapPos(i, j)
        setLineColor(i+1, BLUE)
        setLineColor(j, BLUE)
        clearScreen()
        drawLines()
    swapPos(i+1, high)
    setLineColor(i+1, PURPLE)
    return i+1


def mergeSort(array, left, right):
    drawTimer()
    slowDown()
    middle = (left + right) // 2
    if left < right:
        mergeSort(array, left, middle)
        mergeSort(array, middle + 1, right)
        merge(array, left, middle, middle + 1, right)


def merge(array, left, middle, middle2, right):
    i, j = left, middle2
    temp = []
    pygame.event.get()
    while i <= middle and j <= right:
        setLineColor(i, RED)
        setLineColor(j, RED)
        clearScreen()
        drawLines()
        slowDown()
        drawTimer()
        setLineColor(i, BLUE)
        setLineColor(j, BLUE)
        if array[i] > array[j]:
            temp.append(array[i])
            i += 1
        else:
            temp.append(array[j])
            j += 1
    while i <= middle:
        setLineColor(i, RED)
        clearScreen()
        drawLines()
        slowDown()
        drawTimer()
        setLineColor(i, BLUE)
        temp.append(array[i])
        i += 1
    while j <= right:
        setLineColor(j, RED)
        clearScreen()
        drawLines()
        slowDown()
        drawTimer()
        setLineColor(j, BLUE)
        temp.append(array[j])
        j += 1
    j = 0
    for i in range(left, right + 1):
        pygame.event.pump()
        array[i] = temp[j]
        j += 1
        setLineColor(i, PURPLE)
        clearScreen()
        drawLines()
        slowDown()
        drawTimer()
        if right - left == len(array) - 2:
            setLineColor(i, BLUE)
        else:
            setLineColor(i, GREEN)


def heapSort(array):
    drawTimer()
    clearScreen()
    drawLines()

    size = len(array)
    for i in range(size, -1, -1):
        drawTimer()
        maxHeapify(array, i, size)

    size -= 1
    while size > 0:
        pygame.event.get()
        setLineColor(0, RED)
        setLineColor(size, RED)
        if size+1 < len(array):
            setLineColor(size+1, PURPLE)
        drawTimer()
        slowDown()
        slowDown()
        swapPos(0, size)
        slowDown()
        setLineColor(0, BLUE)
        setLineColor(size, BLUE)
        maxHeapify(array, 0, size)
        size -= 1

    clearScreen()
    drawLines()


def maxHeapify(array, i, size):
    largest = i
    left_child = (i * 2) + 1
    right_child = (i * 2) + 2

    clearScreen()
    drawLines()

    if left_child < size and array[left_child] < array[largest]:
        largest = left_child
    if right_child < size and array[right_child] < array[largest]:
        largest = right_child

    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        maxHeapify(array, largest, size)

    clearScreen()
    drawLines()


def setLineColor(index, color):
    line_x = 2 + index * (5 + lineWidth)
    pygame.draw.rect(win, color, (line_x, vet[index] - 1, lineWidth, 500 - vet[index] + 2))
    pygame.display.update()
    colors[index] = color


def drawTimer():
    global elapsedTime
    pygame.event.get()
    elapsedTime = time.time() - startTime
    pygame.draw.rect(win, (0, 0, 20), (640, 615, 160, 15))
    win.blit(ARIAL12.render('Elapsed time: ' + str(round(elapsedTime, 2)) + ' seconds', False, (255, 255, 255)), (640,
                                                                                                                   615))


def drawText():
    win.blit(ARIAL14.render('Speed:', False, (255, 255, 255)), (5, 505))  # Speed Title
    win.blit(ARIAL12.render('Instant', False, (255, 255, 255)), (25, 528))  # Speed 0 - Instant
    win.blit(ARIAL12.render('Fast', False, (255, 255, 255)), (25, 548))  # Speed 1 - Fast
    win.blit(ARIAL12.render('Normal', False, (255, 255, 255)), (25, 568))  # Speed 2 - Normal
    win.blit(ARIAL12.render('Slow', False, (255, 255, 255)), (25, 588))  # Speed 3 - Slow
    win.blit(ARIAL12.render('Very slow', False, (255, 255, 255)), (25, 608))  # Speed 4 - Very slow

    win.blit(ARIAL14.render('Array Size:', False, (255, 255, 255)), (95, 505))  # Array Size Title
    win.blit(ARIAL12.render('Huge', False, (255, 255, 255)), (115, 528))  # Size 5 - Huge
    win.blit(ARIAL12.render('Big', False, (255, 255, 255)), (115, 548))  # Size 6 - Big
    win.blit(ARIAL12.render('Medium', False, (255, 255, 255)), (115, 568))  # Size 7 - Medium
    win.blit(ARIAL12.render('Small', False, (255, 255, 255)), (115, 588))  # Size 8 - Small
    win.blit(ARIAL12.render('Very small', False, (255, 255, 255)), (115, 608))  # Size 9 - Very small

    win.blit(ARIAL14.render('Algorithm:', False, (255, 255, 255)), (190, 505))  # Algorithm Title
    win.blit(ARIAL12.render('Bubble Sort', False, (255, 255, 255)), (210, 528))  # Algorithm 10 - Bubble Sort
    win.blit(ARIAL12.render('Selection Sort', False, (255, 255, 255)), (210, 548))  # Algorithm 11 - Selection Sort
    win.blit(ARIAL12.render('Quick Sort', False, (255, 255, 255)), (210, 568))  # Algorithm 12 - Quick Sort
    win.blit(ARIAL12.render('Merge Sort', False, (255, 255, 255)), (210, 588))  # Algorithm 13 - Merge Sort
    win.blit(ARIAL12.render('Heap Sort', False, (255, 255, 255)), (210, 608))  # Algorithm 14 - Heap Sort


def drawCircles():
    for num in range(len(CIRCLE_POS)):
        pygame.draw.circle(win, (255, 255, 255), CIRCLE_POS[num], 5)  # main circle
        pygame.draw.circle(win, (255, 255, 255), CIRCLE_POS[num], 3)  # smaller circle

    if sortSpeed == 0:
        pygame.draw.circle(win, (0, 0, 0), (CIRCLE_POS[0][0], CIRCLE_POS[0][1]), 3)
    elif sortSpeed == 1:
        pygame.draw.circle(win, (0, 0, 0), (CIRCLE_POS[1][0], CIRCLE_POS[1][1]), 3)
    elif sortSpeed == 2:
        pygame.draw.circle(win, (0, 0, 0), (CIRCLE_POS[2][0], CIRCLE_POS[2][1]), 3)
    elif sortSpeed == 3:
        pygame.draw.circle(win, (0, 0, 0), (CIRCLE_POS[3][0], CIRCLE_POS[3][1]), 3)
    elif sortSpeed == 4:
        pygame.draw.circle(win, (0, 0, 0), (CIRCLE_POS[4][0], CIRCLE_POS[4][1]), 3)

    if arraySize == 100:
        pygame.draw.circle(win, (0, 0, 0), (CIRCLE_POS[5][0], CIRCLE_POS[5][1]), 3)
    elif arraySize == 80:
        pygame.draw.circle(win, (0, 0, 0), (CIRCLE_POS[6][0], CIRCLE_POS[6][1]), 3)
    elif arraySize == 40:
        pygame.draw.circle(win, (0, 0, 0), (CIRCLE_POS[7][0], CIRCLE_POS[7][1]), 3)
    elif arraySize == 20:
        pygame.draw.circle(win, (0, 0, 0), (CIRCLE_POS[8][0], CIRCLE_POS[8][1]), 3)
    elif arraySize == 10:
        pygame.draw.circle(win, (0, 0, 0), (CIRCLE_POS[9][0], CIRCLE_POS[9][1]), 3)

    pygame.draw.circle(win, (0, 0, 0), (CIRCLE_POS[algorithm+10][0], CIRCLE_POS[algorithm+10][1]), 3)

    pygame.display.update()


def checkDistance(x, y, x2, y2):
    return math.sqrt((x - x2) ** 2 + (y - y2) ** 2)


def markCircle():
    global sortSpeed, arraySize, algorithm
    for num in range(5):
        if checkDistance(mouseX, mouseY, int(CIRCLE_POS[num][0]), int(CIRCLE_POS[num][1])) < 5:
            sortSpeed = num
            return num
    for num in range(5):  # loop through speed buttons
        if checkDistance(mouseX, mouseY, int(CIRCLE_POS[num + 5][0]), int(CIRCLE_POS[num + 5][1])) < 5:
            if num + 5 == 5:
                arraySize = 100
            elif num + 5 == 6:
                arraySize = 80
            elif num + 5 == 7:
                arraySize = 40
            elif num + 5 == 8:
                arraySize = 20
            elif num + 5 == 9:
                arraySize = 10
            refreshLines()
            return num + 5
    for num in range(5):  # loop through algorithm buttons
        if checkDistance(mouseX, mouseY, int(CIRCLE_POS[num + 10][0]), int(CIRCLE_POS[num + 10][1])) < 5:
            if num + 10 == 10:
                algorithm = 0
            elif num + 10 == 11:
                algorithm = 1
            elif num + 10 == 12:
                algorithm = 2
            elif num + 10 == 13:
                algorithm = 3
            elif num + 10 == 14:
                algorithm = 4
            return num + 10
    return False


def draw_buttons():
    if mark_button() == 1:
        pygame.draw.rect(win, LIGHT_BLUE, BUTTONS_POS[0])
        pygame.draw.rect(win, BLUE, BUTTONS_POS[1])
    elif mark_button() == 2:
        pygame.draw.rect(win, LIGHT_BLUE, BUTTONS_POS[1])
        pygame.draw.rect(win, BLUE, BUTTONS_POS[0])
    else:
        pygame.draw.rect(win, BLUE, BUTTONS_POS[0])
        pygame.draw.rect(win, BLUE, BUTTONS_POS[1])
    win.blit(IMPACT20.render('SORT!', False, DARK_BLUE),
             (BUTTONS_POS[0][0] + 20, BUTTONS_POS[0][1] + 10))
    win.blit(ARIAL12.render('or press s', False, (255, 255, 255)), (BUTTONS_POS[0][0] + 20, BUTTONS_POS[0][1] + 55))
    win.blit(IMPACT20.render('REFRESH', False, DARK_BLUE),
             (BUTTONS_POS[1][0] + 10, BUTTONS_POS[1][1] + 10))
    win.blit(ARIAL12.render('or press r', False, (255, 255, 255)), (BUTTONS_POS[1][0] + 20, BUTTONS_POS[1][1] + 55))
    pygame.display.update()


def mark_button():
    global mouseX, mouseY
    mouseX, mouseY = pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]
    for num in range(len(BUTTONS_POS)):
        if BUTTONS_POS[num][0] < mouseX < BUTTONS_POS[num][0] + BUTTONS_POS[num][2] and \
                BUTTONS_POS[num][1] < mouseY < BUTTONS_POS[num][1] + BUTTONS_POS[num][3]:
            return num + 1
    return False


def reset_timer():
    global elapsedTime, startTime
    elapsedTime = 0
    startTime = time.time()
    drawTimer()


draw_buttons()
drawLines()
drawText()
drawCircles()
reset_timer()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEMOTION:
            draw_buttons()
        if event.type == pygame.MOUSEBUTTONUP:
            pygame.event.get()
            mouseX, mouseY = pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]
            markCircle()
            drawCircles()
            if mark_button() == 1:
                sort()
            elif mark_button() == 2:
                reset_timer()
                refreshLines()
                clearScreen()
                drawLines()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r and rPressed is False:
                rPressed = True
                reset_timer()
                refreshLines()
                clearScreen()
                drawLines()
            if event.key == pygame.K_s and sPressed is False:
                sPressed = True
                sort()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_r:
                rPressed = False
            if event.key == pygame.K_s:
                sPressed = False
            if event.key == pygame.K_e:
                e_pressed = False

pygame.quit()
