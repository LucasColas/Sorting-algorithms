import pygame

from Algorithms.Bubble_sort import BubbleSort
from Algorithms.insertion_sort import InsertionSort
from Algorithms.Merge_sort import Mergesort
from Algorithms.Quick_Sort import QuickSort
from Algorithms.selection_sort import selection_sort

Width, Height = 1500,700

Window = pygame.display.set_mode((Width, Height))

def update_window(Window):
    Window.fill((255,255,255))
    pygame.display.update()



def main():

    run = True

    while run:
        update_window(Window)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
                run = False

main()

BubbleSort([3,4,1,9,11,7])
