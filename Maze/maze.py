import sys
from PIL import Image, ImageDraw
import maze_library as mani

column = 0
index = (-1, -1)
queue = []
explored = []
start = (1,1)
end = (1,1)
matrix = []
p = True
b = ()
row = int(input("Enter the number of rows:"))
for i in range(row):
    a = input()
    column = len(a)
    matrix.append(list(a))


for i in range(row):
    for j in range(column):
        if matrix[i][j] == 'A':
            start = (i, j)
            index = (i,j)
            b = index
        elif matrix[i][j] == 'B':
            end = (i, j)

mani.first_output(matrix, row, column, explored, start, end)

if index[0] > 0:
    if matrix[index[0]-1][index[1]] == ' ':
        if (index[0]-1, index[1]) not in explored:
            queue.append((index[0]-1, index[1]))
if index[1] > 0:
    if matrix[index[0]][index[1]-1] == ' ':
        if (index[0], index[1]-1) not in explored:
            queue.append((index[0], index[1]-1))
if index[0] <= row - 2:
    if matrix[index[0]+1][index[1]] == ' ':
        if (index[0]+1, index[1]) not in explored:
            queue.append((index[0]+1, index[1]))
if index[0] <= column - 2:
    if matrix[index[0]][index[1]+1] == ' ':
        if (index[0], index[1]+1) not in explored:
            queue.append((index[0], index[1]+1))


while index != end and p:
    if p:
        if queue[0] not in explored:
            explored.append(queue[0])
            index = queue[0]
            queue = queue[1:]
            if index[0] > 0:
                if matrix[index[0]-1][index[1]] == ' ':
                    if (index[0]-1, index[1]) not in explored:
                        queue.append((index[0]-1, index[1]))
                elif matrix[index[0]-1][index[1]] == 'B':
                    p = mani.the_end(matrix, row, column, explored, start, end, p)
            if index[1] > 0:
                if matrix[index[0]][index[1]-1] == ' ':
                    if (index[0], index[1]-1) not in explored:
                        queue.append((index[0], index[1]-1))
                elif matrix[index[0]][index[1]-1] == 'B':
                    p = mani.the_end(matrix, row, column, explored, start, end, p)
            if index[0] <= row - 2:
                if matrix[index[0]+1][index[1]] == ' ':
                    if (index[0]+1, index[1]) not in explored:
                        queue.append((index[0]+1, index[1]))
                elif matrix[index[0]+1][index[1]] == 'B':
                    p = mani.the_end(matrix, row, column, explored, start, end, p)
            if index[0] <= column - 2:
                if matrix[index[0]][index[1]+1] == ' ':
                    if (index[0], index[1]+1) not in explored:
                        queue.append((index[0], index[1]+1))
                elif matrix[index[0]][index[1]+1] == 'B':
                    p = mani.the_end(matrix, row, column, explored, start, end, p)
        else:
            queue = queue[1:]



trash = []
way = []
fway = []
reminder = []
index = start
while True:
    t = True
    x = 0
    v= False
    if index[0] > 0:
        if matrix[index[0]-1][index[1]] == '.':
            if (index[0]-1,index[1]) not in trash:
                x += 1
    if index[1] > 0:
        if matrix[index[0]][index[1]-1] == '.':
           if (index[0],index[1]-1) not in trash:
                x += 1
    if index[0] <= row - 2:
        if matrix[index[0]+1][index[1]] == '.':
           if (index[0]+1,index[1]) not in trash:
                x += 1
    if index[0] <= column - 2:
        if matrix[index[0]][index[1]+1] == '.':
            if (index[0],index[1]+1) not in trash:
                x += 1
    if index[0] > 0:
        if matrix[index[0]-1][index[1]] == 'B':
            if fway == []:
                fway = trash
                fway.append(index)
            else:
                if len(fway) > len(trash):
                    fway = trash
                    fway.append(index)
    if index[1] > 0:
        if matrix[index[0]][index[1]-1] == 'B':
            if fway == []:
                fway = trash
                fway.append(index)
            else:
                if len(fway) > len(trash):
                    fway = trash
                    fway.append(index)
    if index[0] <= row - 2:
        if matrix[index[0]+1][index[1]] == 'B':
            if fway == []:
                fway = trash
                fway.append(index)
            else:
                if len(fway) > len(trash):
                    fway = trash
                    fway.append(index)
    if index[0] <= column - 2:
        if matrix[index[0]][index[1]+1] == 'B':
            if fway == []:
                fway = trash
                fway.append(index)
            else:
                if len(fway) > len(trash):
                    fway = trash
                    fway.append(index)

    if x == 0:
        if reminder == []:
            v = True
            break
        while True:
            o = trash[len(trash)-1]
            i = reminder[0]
            if (o[0] == i[0] and o[1]-1 == i[1]) or (o[0]-1 == i[0] and o[1] == i[1]) or (o[0] == i[0] and o[1] == i[1]-1) or (o[0] == i[0]-1 and o[1] == i[1]):
                break
            else:
                trash = trash[:-1]
        index = reminder[0]
        reminder = reminder[1:]
        t = False
    elif x > 1:
        if index[0] > 0:
            if matrix[index[0]-1][index[1]] == '.':
                if (index[0]-1,index[1]) not in trash:
                    reminder.reverse()
                    reminder.append((index[0]-1,index[1]))
                    reminder.reverse()
        if index[1] > 0:
            if matrix[index[0]][index[1]-1] == '.':
                if (index[0],index[1]-1) not in trash:
                    reminder.reverse()
                    reminder.append((index[0],index[1]-1))
                    reminder.reverse()
        if index[0] <= row - 2:
            if matrix[index[0]+1][index[1]] == '.':
                if (index[0]+1,index[1]) not in trash:
                    reminder.reverse()
                    reminder.append((index[0]+1,index[1]))
                    reminder.reverse()
        if index[0] <= column - 2:
            if matrix[index[0]][index[1]+1] == '.':
                if (index[0],index[1]+1) not in trash:
                    reminder.reverse()
                    reminder.append((index[0],index[1]+1))
                    reminder.reverse()
        way.append(reminder[0])
        reminder = reminder[1:]

    else:
        if index[0] > 0:
            if matrix[index[0]-1][index[1]] == '.':
                if (index[0]-1,index[1]) not in trash:
                    way.append((index[0]-1,index[1]))
            elif matrix[index[0]-1][index[1]] == 'B':
                if fway == []:
                    fway = trash
                else:
                    if len(fway) > len(trash):
                        fway = trash
        if index[1] > 0:
            if matrix[index[0]][index[1]-1] == '.':
                if (index[0],index[1]-1) not in trash:
                    way.append((index[0],index[1]-1))
            elif matrix[index[0]][index[1]-1] == 'B':
                if fway == []:
                    fway = trash
                else:
                    if len(fway) > len(trash):
                        fway = trash
        if index[0] <= row - 2:
            if matrix[index[0]+1][index[1]] == '.':
                if (index[0]+1,index[1]) not in trash:
                    way.append((index[0]+1,index[1]))
            if matrix[index[0]+1][index[1]] == 'B':
                if fway == []:
                    fway = trash
                else:
                    if len(fway) > len(trash):
                        fway = trash
        if index[0] <= column - 2:
            if matrix[index[0]][index[1]+1] == '.':
                if (index[0],index[1]+1) not in trash:
                    way.append((index[0],index[1]+1))
            elif matrix[index[0]][index[1]+1] == 'B':
                if fway == []:
                    fway = trash
                else:
                    if len(fway) > len(trash):
                        fway = trash
    trash.append(index)
    if t:
        index = way[len(way)-1]
    if (fway != [] and reminder == []) and mani.aliii(x,reminder,fway,index,trash,matrix):
        break
    #print(trash)
    #print(reminder)
    #print(index)
    #print('///////////////')
mani.second_output(matrix, row, column, explored, start, end, fway)

                


    




