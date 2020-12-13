def BubbleSort(board):
  for i in range(len(board)-1, 1, -1):
    for j in range(0, i):
      if board[j] > board[j+1]:
        temp = board[j]
        board[j] = board[j+1]
        board[j+1] = temp

  return board

def BubbleSort2(Board):
  for i in range(len(Board)):
    for j in range(0,len(Board)-1):
      if Board[j] > Board[j+1]:
        Board[j], Board[j+1] = Board[j+1], Board[j]

  return Board

board = [4,5,1,2,99,9,7,11,3]
print(board)
print(BubbleSort2(board))
