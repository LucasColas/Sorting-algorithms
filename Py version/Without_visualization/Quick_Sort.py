
def partition(Board, first, last):
    pivot = Board[last]
    i = first

    for j in range(first,last):
        if Board[j] < pivot:
            Board[i], Board[j] = Board[j], Board[i]
            i += 1

    Board[i], Board[last] = Board[last], Board[i]

    return i


def QuickSort(Board, first, last):
    if first < last:
        p = partition(Board, first, last)

        QuickSort(Board, first, p-1)
        QuickSort(Board, p+1, last)



Board = [3,2,9,6,11,4]

QuickSort(Board, 0, len(Board)-1)
print(Board)
