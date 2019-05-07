from PIL import Image, ImageColor

# Usage:
#   pip install pillow
#   python checkerboard-fp.py

def buildBoard(columns, color1, color2):
    # build a row of color1, color2 values based on even/odd
    row = list(map(lambda x: color1 if x % 2 == 0 else color2, range(columns)))

    # build a row of color2, color1 values based on even/odd
    altRow = list(map(lambda x: color2 if x % 2 == 0 else color1, range(columns)))

    # join multiple rows of the above based on even/odd rows
    board = list(map(lambda x: row if x % 2 == 0 else altRow, range(columns)))
    return board

def drawBoard(board, pixelSize, image):
    for x, row in enumerate(board):
        for y, columnColor in enumerate(row):
            image = drawSquare(x * pixelSize, y * pixelSize, columnColor, pixelSize, image)
    return image

def drawSquare(xStart, yStart, color, pixelSize, image):
    for i in range(pixelSize):
        for j in range(pixelSize):
            image.putpixel((xStart + i, yStart + j), ImageColor.getrgb(color))
    return image

if __name__ == '__main__':

    columns = 10
    pixelSize = 10
    color1, color2 = 'black', 'red'

    image = Image.new('RGB', (pixelSize * columns, pixelSize * columns))
    board = buildBoard(columns, color1, color2)
    image = drawBoard(board, pixelSize, image)
    image.save('output.png')

# Debug
#print('Board looks like this:', *board, sep='\n ')