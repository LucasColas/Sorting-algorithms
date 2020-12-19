import random

def partition(Board, first, last):
    pivot = Board[last]
    i = first

    for j in range(first,last):
        if Board[j] < pivot:
            Board[i], Board[j] = Board[j], Board[i]
            i += 1

    Board[i], Board[last] = Board[last], Board[i]

def select(Board, first, last):
    print("first", first)
    print("last", last)
    num = random.randrange(first, last)
    pivot = Board[num]

    return pivot


def QuickSort(Board, first, last):
    if first < last:
        get = Swap

        QuickSort(Board, first, pivot-1)
        QuickSort(Board, pivot+1, last)



Board = [3,2,9,6,11,4]

QuickSort(Board, 0, len(Board)-1)
print(Board)
