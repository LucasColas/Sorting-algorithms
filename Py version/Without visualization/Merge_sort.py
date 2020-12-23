def Mergesort(Board):
  if len(Board) <= 1:
    return Board

  else:
    #print(len(Board)//2)
    return Merge(Mergesort(Board[0:len(Board)//2]), Mergesort(Board[len(Board)//2:len(Board)]))



def Merge(Board_A,Board_B):
  #print("Board B" ,Board_B)
  #print("Board A ", Board_A)

  if len(Board_A) <= 0:
    return Board_B

  if len(Board_B) <= 0:
    return Board_A

  if Board_A[0] <= Board_B[0]:

    return [Board_A[0]] + Merge(Board_A[1:], Board_B)

  else:

    return [Board_B[0]] + Merge(Board_A, Board_B[1:])

Board = [20,5,1,15,9,3, 100, 50,32,33,10,7,8,25,42,19,18,77,88]
print(Mergesort(Board))
