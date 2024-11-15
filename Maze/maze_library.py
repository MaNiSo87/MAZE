from PIL import Image, ImageDraw

def first_output(matrix, row, column, explored, start, end):
    cell_size = 50
    cell_border = 2

    img = Image.new(
        "RGBA",
        (column * cell_size, row * cell_size),
        "black"
    )
    draw = ImageDraw.Draw(img)

    for i in range(row):
        for j in range(column):
            if matrix[i][j] == '#':
                fill = (40, 40, 40)
            elif (i,j) not in explored and matrix[i][j] == ' ':
                fill = (0,0,0)
            elif (i, j) == start :
                fill = (255, 0, 0)
            elif (i, j) == end:
                fill = (0, 171, 28)
            else:
                fill = (0,0,0)
            draw.rectangle(
                ([(j * cell_size + cell_border, i * cell_size + cell_border),
                    ((j + 1) * cell_size - cell_border, (i + 1) * cell_size - cell_border)]),
                fill=fill
            )
    img.save('themaze.png')

def second_output(matrix, row, column, explored, start, end, way):
    cell_size = 50
    cell_border = 2

    img = Image.new(
        "RGBA",
        (column * cell_size, row * cell_size),
        "black"
    )
    draw = ImageDraw.Draw(img)

    for i in range(row):
        for j in range(column):
            if (i,j) in way and (i, j) != start:
                fill = (128, 159, 255)
            elif matrix[i][j] == '#':
                fill = (40, 40, 40)
            elif (i,j) not in explored and matrix[i][j] == ' ':
                fill = (0,0,0)
            elif (i, j) == start :
                fill = (255, 0, 0)
            elif (i, j) == end:
                fill = (0, 171, 28)
            else:
                fill = (220, 235, 113)
            draw.rectangle(
                ([(j * cell_size + cell_border, i * cell_size + cell_border),
                    ((j + 1) * cell_size - cell_border, (i + 1) * cell_size - cell_border)]),
                fill=fill
            )
    img.save('maze.png')

def the_end(matrix, row, column, explored, start, end, p):
    for i in range(row):
        for j in range(column):
            o = (i,j)
            if o not in explored and matrix[i][j] != 'A' and matrix[i][j] != 'B' and matrix[i][j] != ' ':
                print("█", end='')
            elif o not in explored and matrix[i][j] == ' ':
                print(' ', end='')
            elif matrix[i][j] == 'A':
                print('A', end='')
            elif matrix[i][j] == 'B':
                print('B', end='')
            else:
                matrix[i][j] = '.'
                print('.',end='')
        print()
    p = False
    return p

def aliii(x,reminder,fway,index,trash,matrix):
    if reminder == []:
        if fway != []:
            if len(trash) > 0:
                o = trash[len(trash)-1]
                if matrix[o[0]-1][o[1]] == '.' or matrix[o[0]][o[1]+1] == '.' or matrix[o[0]][o[1]-1] == '.' or matrix[o[0]+1][o[1]] == '.':
                    return True
    return False

            


        


        
        

        
    