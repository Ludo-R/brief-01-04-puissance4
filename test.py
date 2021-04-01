


case = '-'
rows = 6
cols = 7

board = [[case] * rows for i in range(cols)]

for r in range(rows):
    print(' '.join(str(board[c][r]) for c in range(cols)))

print("\n\n")

play = input("play col:")

col = board[int(play)]

i = 1

while col[i] != case:
    i = i -1
col[i] = "X"

for r in range(rows):
    print(' '.join(str(board[c][r]) for c in range(cols)))

print("\n\n")