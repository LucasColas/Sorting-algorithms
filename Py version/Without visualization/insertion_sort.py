def InsertionSort(Board):
    for i in range(1, len(Board)):
        mem = Board[i]
        j = i-1
        while j >= 0 and Board[j] > mem:
            Board[j+1] = Board[j]

        Board[j+1] = mem
    return Board
