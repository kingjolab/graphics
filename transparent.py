__author__ = 'wangyu'

from SimpleGraphics import *

'''
   getting user input, if input is invalid the user should re-input
   providing extra picture for user choose
'''

def userInput():
    while True:
        backgroundName = input("input the name of the background : ")
        if backgroundName in ['hallway-1-of-3', 'hallway-2-of-3', 'hallway-3-of-3', 'hallway-1-of-3.gif', 'hallway-2-of-3.gif', 'hallway-3-of-3.gif']:
            if backgroundName.find('.') < 0:
                backgroundName += '.gif'
            break
        print("unfortunately we have only three background images you can choose\nhallway-1-of-3 hallway-2-of-3 hallway-3-of-3")
    while True:
        monsterName = input("input the name of the monster images : ")
        if monsterName in ['unsparkling-vampire', 'pumpkin', 'bat', 'unsparkling-vampire.gif', 'pumpkin.gif', 'bat.gif']:
            if monsterName.find('.') < 0:
                monsterName += '.gif'
            break
        print("unfortunately we have only three monster images you can choose\nunsparkling-vampire pumpkin bat")
    backgroundImg = loadImage(backgroundName)
    monsterImg = loadImage(monsterName)
    while True:
        xLocaltion = input("input the x co-ordinates of monster : ")
        yLocaltion = input("input the y co-ordinates of monster : ")
        # in case the locations that user choose beyond the location of background and the transparent monster
        if xLocaltion and yLocaltion and int(xLocaltion) in range(100, getWidth(backgroundImg) - getWidth(monsterImg)) and int(yLocaltion) in range(175, getHeight(backgroundImg) - getHeight(monsterImg)):
            break
        else:
            print("invalid input\n in order to display your image in the background your input x should be 100 ~ 700, y should be 175 ~ 425 \n Reminder: if you want the ghost image to display at the top of background, your y should be 175 \n try again please!")
    return backgroundName, monsterName, int(xLocaltion) - 100, int(yLocaltion) - 175


# draw background image
def drawBackgroundImage(backgroundName):
    backgroundImg = loadImage(backgroundName)
    drawImage(backgroundImg, 0, 0)

# draw the transparent monster-image in the background image
def drawTransparentImage(backgroundName, monsterName, xLocation=0, yLocation=0):
    backgroundImg = loadImage(backgroundName)
    monsterImg = loadImage(monsterName)
    for x in range(0, getWidth(monsterImg)):
        for y in range(0, getHeight(monsterImg)):
            r, g, b = getPixel(monsterImg, x, y)
            # approximate 2 units are allowed to track pure background
            if (r <= 2 and g >= 253 and b <= 2) or (r <= 2 and g <= 2 and b <= 2) or (r >= 253 and g >= 253 and b >= 253):
                r, g, b = getPixel(backgroundImg, x + xLocation, y + yLocation)
            else:
                br, bg, bb = getPixel(backgroundImg, x + xLocation, y + yLocation)
                r = (r + br) / 2
                g = (g + bg) / 2
                b = (b + bb) / 2
            putPixel(monsterImg, x, y, r, g, b)

    drawImage(monsterImg, xLocation, yLocation)

# start function
def main():
    backgroundName, monsterName, xLocation, yLocation = userInput()
    drawBackgroundImage(backgroundName)
    drawTransparentImage(backgroundName, monsterName, xLocation, yLocation)


if __name__ == "__main__":
    main()
