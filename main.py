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


