from PIL import Image, ImageColor

# Usage:
#   pip install pillow
#   python checkerboard.py

class CheckerBoard:

    def __init__(self, columns, pixelSize, color1, color2):
        self.image = Image.new('RGB', (pixelSize * columns, pixelSize * columns))
        self.columns = columns
        self.pixelSize = pixelSize
        self.currentColor = color1
        self.color1 = color1
        self.color2 = color2

        for x in range(self.columns):
            for y in range(self.columns):
                self.drawSquare(x * self.pixelSize, y * self.pixelSize, self.currentColor)
                self.swapColor() # Swap color for each column
            self.swapColor() # Swap starting color each new set of columns

    def swapColor(self):
        if (self.currentColor == self.color1):
            self.currentColor = self.color2
        else:
            self.currentColor = self.color1

    def drawSquare(self, x_start, y_start, color):
        for i in range(self.pixelSize):
            for j in range(self.pixelSize):
                self.image.putpixel((x_start + i, y_start + j), ImageColor.getrgb(color))

    def render(self, filename):
        self.image.save(filename)

if __name__ == '__main__':

    columns = 10
    pixelSize = 10
    color1, color2 = 'black', 'red'

    cb = CheckerBoard(columns, pixelSize, color1, color2)
    cb.render('output.png')