

from os import remove


with open('./4/input.txt') as f:
    board_array=[[0]*5]*5
    boards = board_array*100
    answers = f.readline()
    list = [line.rstrip().strip() for line in f]
    list.pop(0)
    for line in list:
        for i,number in enumerate(line):
            board_array[i%5] = number
    print(board_array)
    

