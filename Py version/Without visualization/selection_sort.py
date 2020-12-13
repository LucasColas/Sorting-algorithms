def selection_sort(board):

  for i in range(len(board)):
    min = i
    for j in range(i+1, len(board)):
      if board[j] < board[min]:
        min = j

    temp = board[min]
    board[min] = board[i]
    board[i] = temp

  return board

trial = [4,3,6,11,2,5]
print(selection_sort(trial))
