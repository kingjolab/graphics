__author__ = 'wangyu'

import os

class ArtGenerator:

    '''
    init:
        color from light to black
    '''
    def __init__(self):
        self.color = ['.', ',', '`', '^', ':', ';', '!', '_', '-', '?', '>', '+', '=', '*', '$', '#']
        self.colorMap = {'.': 0, ',': 1, '`': 2, '^': 3, ':': 4, ';': 5, '!': 6, '_': 7, '-': 8, '?': 9, '>': 10,
                         '+': 11, '=': 12, '*': 13, '$': 14, '#': 15}
        self.colorValue = []
        self.filename = ''

    # getting input 
    def userInput(self):
        try:
            filename = input("input your file name: ")
            try:
                fileHandler = open(filename, 'r')
            except FileNotFoundError as notfound:
                print(notfound)
                return self.userInput()
            invalueLine = fileHandler.readline()
            if invalueLine[0] != '.':
                print("it's not the file you saved at Q2 \ninput a valid filename !")
                return self.userInput()
            while True:
                charLine = fileHandler.readline()
                if not charLine:
                    break
                if charLine[-1] == os.linesep:
                    charLine = charLine[:-1]
                self.colorValue.append([x for x in charLine])
            self.filename = filename
            fileHandler.close()
        except Exception as error:
            print(error)
            return self.userInput()

    # rotate image using a simple turning, making the origin horizontal line to a new vertical line and the origin vertical one to a new horizontal line
    def rotateImage(self):
        width = len(self.colorValue[0])
        height = len(self.colorValue)
        # determine it is wider or higher, if w > h -> width > height so make the new one height > width, or vise versa.
        # initialize the template X and Y line
        newDirection = [['0' for i in range(height)] for j in range(width)]
        for i in range(0, width):
            for j in range(0, height):
                newDirection[i][height-j-1] = self.colorValue[j][i]
        self.colorValue = newDirection
        self.printOut()

    # flip image vertically
    def flipVertical(self):
        newDirection = []
        for colorLine in self.colorValue:
            length = len(colorLine)
            middle = int(length/2)
            for i in range(0, middle):
                tempC = colorLine[i]
                colorLine[i] = colorLine[length-1]
                colorLine[length-1] = tempC
                length -= 1
            newDirection.append(colorLine)
        self.colorValue = newDirection
        self.printOut()

    # flip image horizontally
    def flipHorizontal(self):
        length = len(self.colorValue)
        middle = int(length/2)
        for i in range(0, middle):
            temp = self.colorValue[i]
            self.colorValue[i] = self.colorValue[length-1]
            self.colorValue[length-1] = temp
            length -= 1
        self.printOut()

    # invert the image
    def invertImage(self):
        newDirectionY = []
        for y in self.colorValue:
            newDirectionX = []
            for x in y:
                z = self.color[15 - self.colorMap[x]]
                newDirectionX.append(z)
            newDirectionY.append(newDirectionX)
        self.colorValue = newDirectionY
        self.printOut()

    # save the image
    def saveImage(self):
        with open(self.filename, 'w') as f:
            for y in self.colorValue:
                tempLine = ''
                for c in y:
                    tempLine += c
                f.write(tempLine)

    def printOut(self):
        for y in self.colorValue:
            tempS = ''
            for x in y:
                tempS += x
            print(tempS)

    # display the converted image
    def display(self):
        while True:
            userInput = input("---------------------------------\n\
                input 1 for flip the image horizontally \n\
                input 2 for flip the image vertically \n\
                input 3 for rotate the image by 90 degrees clockwise\n\
                input 4 for invert the image\n\
                input 5 for save the new image and end\n\
                your input is : ")
            if userInput not in ('1', '2', '3', '4', '5'):
                print("you could input a number from 1 to 5\ntry again!")
                return self.display()
            elif userInput == '1':
                self.flipHorizontal()
            elif userInput == '2':
                self.flipVertical()
            elif userInput == '3':
                self.rotateImage()
            elif userInput == '4':
                self.invertImage()
            elif userInput == '5':
                self.saveImage()
                break

if __name__ == '__main__':
    try:
        art = ArtGenerator()
        art.userInput()
        art.display()
    except Exception as error:
        print(error)
