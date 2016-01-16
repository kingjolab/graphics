__author__ = 'wangyu'

from SimpleGraphics import *
from random import randrange
from math import *

'''
    this program will show a pie chart with legend or sector label
'''

print("========================\n\tChart Creator Menu\n========================")

# choose prefered chart
def userPreferedChartform():
    preferedChart = input("Choose 1) a legend, or 2) sector labels?")
    while True:
        try:
            if preferedChart in ['1', '2']:
                return preferedChart
            preferedChart = input("Invalid selection. Please enter either 1 or 2:")
        except Exception:
            pass


''' for each sector if the sum of it great than total then reset
    params sectorNum (the number of sector)
    params total (total value)

    return list of name and value for each sector
'''


def enterSector(sectorNum, total):
    sectorValue = []
    sectorName = []
    for i in range(1, sectorNum + 1):
        sectorN = input("Enter the label for sector %s" % i)
        sectorV = int(input("Enter the value for the '%s' sector:" % sectorN))
        sectorName.append(sectorN)
        sectorValue.append(sectorV)
    # ensure input sum of value(sum of real value) doesn't greater than input total
    if not checkTotal(total, sectorValue):
        print("make sure your input value less than or equal to your total value\ntry again!")
        sectorName, sectorValue = enterSector(sectorNum, total)
    return sectorName, sectorValue


'''
    draw a pie chart with legend

    params total (total value)
    params sepName (list of name)
    params sepVal (list of value)
    params chartTitle (title of the pie chart)
    params x (the start x location of chart)
    params y (the start y location of chart)
    params h (high of pie chart)
    params w (width of pie chart)

'''


def drawPieChartWithLegend(total, sepName, sepVal, chartTitle, x, y, w, h):
    location = 0
    each = 360 / total
    rectIncrease = (getWidth() - 100) / (len(sepName) * 3)
    rectx = rectIncrease
    recty = 600

    # draw the title while reset text format
    setFont("Helvetica", 20, "bold italic")
    text(350, 100, chartTitle)
    setFont()

    for n, v in enumerate(sepVal):
        setColor(randrange(0, 255), randrange(0, 255), randrange(0, 255))
        pieSlice(x, y, w, h, location, each * v)
        rect(rectx, recty, 50, 50)
        setColor('black')
        text(rectx + 20, recty + 70, sepName[n])
        rectx += (rectIncrease + 50)
        location += each * v
    if location < 360:
        setColor("grey")
        pieSlice(x, y, w, h, location, 360 - location)
        rect(rectx, recty, 50, 50)
        text(rectx + 20, recty + 70, "unused")


'''
    draw a pie chart with sector label

    params total (total value)
    params sepName (list of name)
    params sepVal (list of value)
    params chartTitle (title of the pie chart)
    params x (the start x location of chart)
    params y (the start y location of chart)
    params h (high of pie chart)
    params w (width of pie chart)

'''


def drawPieChartWithSectorLabel(total, sepName, sepVal, chartTitle, x, y, w, h):
    location = 0
    each = 360 / total

    # draw the title while reset text format
    setFont("Helvetica", 20, "bold italic")
    text(350, 40, chartTitle)
    setFont()

    for n, v in enumerate(sepVal):
        setColor(randrange(0, 255), randrange(0, 255), randrange(0, 255))
        pieSlice(x, y, w, h, location, each * v)
        angle = radians(location + (each * v) / 2)
        drawIndication(x, y, w, h, angle, sepName[n])
        location += each * v
    if location < 360:
        setColor("grey")
        pieSlice(x, y, w, h, location, 360 - location)
        angle = radians(location + (360 - location) / 2)
        drawIndication(x, y, w, h, angle, "unused")


''' draw indication for each piece of pie
    params x (the start x location of text and rect)
    params y (the start y location of text and rect)
    params h (high of pie chart)
    params w (width of pie chart)
    params angle (slice location)
    params word (text word)
'''


def drawIndication(x, y, w, h, angle, word):
    x1 = 250 * cos(angle)
    y1 = -250 * sin(angle)
    rect(x + w / 2 + x1 - 40, y + h / 2 + y1 - 15, 100, 30)
    line(x + w / 2, y + h / 2, x + w / 2 + x1, y + h / 2 + y1)
    setColor("black")
    text(x + w / 2 + x1 - 30, y + h / 2 + y1, word)


# check the sum of input value
# if greater means invalid return False else True
def checkTotal(total, sepNum):
    if sum(sepNum) > total:
        return False
    return True


if __name__ == "__main__":
    resize(800, 700)      # resize in case different screen shows different window size that will effect the location of graph

    preferedChart = userPreferedChartform()

    chartTitle = input("Enter a title for the chart:")

    sectorNum = int(input("Enter the number of sectors:"))

    total = int(input("Enter the total:"))

    sectorName, sectorValue = enterSector(sectorNum, total)

    if preferedChart == "1":
        drawPieChartWithLegend(total, sectorName, sectorValue, chartTitle, getWidth() / 4, getHeight() / 4, 300, 300)
    else:
        drawPieChartWithSectorLabel(total, sectorName, sectorValue, chartTitle, getWidth() / 4, getHeight() / 4, 300, 300)
