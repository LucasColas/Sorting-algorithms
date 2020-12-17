import random

def Swap(Board,first, last, pivot):
    print("pivot", pivot)
    print("last", last)
    Board[pivot], Board[last] = Board[last], Board[pivot]

    j = first

    for i in range(last-1):
        if Board[i] <= Board[last]:
            Board[i], Board[j] = Board[j], Board[i]
            j += 1
    Board[last], Board[j] = Board[j], Board[last]

    return j

def select(Board, first, last):
    print("first", first)
    print("last", last)
    num = random.randrange(first, last)
    pivot = Board[num]

    return pivot


def QuickSort(Board, first, last):
    if first < last:
        pivot = select(Board, first, last)
        print("pivot : ", pivot)
        pivot = Swap(Board, first, last, pivot)

        QuickSort(Board, pivot-1)
        QuickSort(Board, pivot+1, last)



Board = [3,2,9,6,11,4]

QuickSort(Board, 0, len(Board)-1)
print(Board)
