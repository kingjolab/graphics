__author__ = 'wangyu'

from SimpleGraphics import *

class ArtGenerator:

    '''
    init:
        color from light to black
    '''
    def __init__(self):
        self.color = ['.', ',', '`', '^', ':', ';', '!', '_', '-', '?', '>', '+', '=', '*', '$', '#']
        self.value = []

    # getting user input
    def userInput(self):
        try:
            filename = input("input your image name: ")
            backcolor = input("you want black background or white background\ninput 1 for black\ninput 2 for white\nyour choosen background color is : ")
            image = loadImage(filename)
            if getWidth(image) > 80:    # draw a big one will be too long
                print(" too boarder , width greater than 80 pixel\t try again !")
                return self.userInput()
            if backcolor not in ('1', '2'):
                print("input your background color number again")
                return self.userInput()
            return image, backcolor
        except Exception as error:
            print(error)
            return self.userInput()

    # convert image pixel to character (a string)
    def conversion(self, image):
        valueY = []
        for y in range(0, getHeight(image)):
            valueX = []
            for x in range(0, getWidth(image)):
                r, g, b = getPixel(image, x, y)
                valueX.append(self.pixelToColor(r, g, b))
            valueY.append(valueX)
        return valueY

    # a simple algorithm for separating image pixel into a range of char, 16 is the art color amount
    def pixelToColor(self, r, g, b):
        return self.color[int((r+g+b) / (3 * 16))]

    # display the converted image
    def display(self, image, backColor):
        try:
            if backColor == '1':
                background(0, 0, 0)
                setColor('white')
            else:
                background(255, 255, 255)
                self.color.reverse()
                setColor('black')
            self.value = self.conversion(image)
            for j, y in enumerate(self.value):
                for i, x in enumerate(y):
                    text(i, j, x)
        except Exception as error:
            print(error)

if __name__ == '__main__':
    art = ArtGenerator()
    image, backColor = art.userInput()
    art.display(image, backColor)
