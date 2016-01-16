__author__ = 'wangyu'

from SimpleGraphics import *


'''
logic decision depending on student Id (for example if last four digit number is 9171 it's odd
so it should be logical "and" as assignment indicated)
and user input's true or false condition

'''

def evaluateMyCircuit(boolValues):
    return ((boolValues[1] and boolValues[2]) and (boolValues[3] and boolValues[4])) and (not boolValues[0])


# get input True or False, or T for True and F for False
def getUserBooleanValues():
    boolValues = []
    while True:
        userValue = input("input five boolean values (typing T or True and F or False)")
        if userValue == 'T' or userValue == 'True':
            boolValues.append(True)
        elif userValue == 'F' or userValue == 'False':
            boolValues.append(False)
        else:
            print("invaild input\nplease try again!")
        if len(boolValues) == 5:
            break
    return boolValues


# draw the circuit graph
def drawCircuit(boolValues, result):

    # draw the first input circuit boolean value
    for i, v in enumerate(boolValues):
        if v:
            textV = 'T'
        else:
            textV = 'F'
        setColor("white")
        ellipse(100, 200+i*50, 30, 30)
        setColor("black")
        text(100+15, 200+15+i*50, textV)
        line(130, 215+i*50, 200, 215+i*50)
        ellipse(200, 210+i*50, 10, 10)

    # draw the conditional circuit
    setColor("white")
    rect(250, 250, 40, 80)
    ellipse(260, 250, 60, 80)

    rect(250, 350, 40, 80)
    ellipse(260, 350, 60, 80)

    rect(380, 300, 40, 80)
    ellipse(390, 300, 60, 80)

    rect(490, 250, 40, 80)
    ellipse(500, 250, 60, 80)

    ellipse(630, 275, 30, 30)

    polygon(380, 245, 380, 215, 410, 230)
    ellipse(410, 225, 10, 10)

    setColor("black")
    line(560, 290, 630, 290)
    ellipse(580, 285, 10, 10)
    if result:
        text(645, 290, 'T')
    else:
        text(645, 290, 'F')

    line(450, 340, 465, 340)
    line(465, 310, 465, 340)
    line(465, 310, 490, 310)
    ellipse(460, 305, 10, 10)
    ellipse(460, 335, 10, 10)

    line(420, 230, 465, 230)
    line(465, 230, 465, 260)
    line(465, 260, 490, 260)
    ellipse(460, 225, 10, 10)
    ellipse(460, 255, 10, 10)

    line(200, 215, 350, 215)
    line(350, 230, 380, 230)
    line(350, 215, 350, 230)
    ellipse(345, 210, 10, 10)
    ellipse(345, 225, 10, 10)

    line(200, 265, 250, 265)
    line(200, 315, 250, 315)
    line(200, 365, 250, 365)
    line(200, 415, 250, 415)

    line(320, 390, 350, 390)
    line(350, 365, 380, 365)
    line(350, 365, 350, 390)
    ellipse(345, 360, 10, 10)
    ellipse(345, 385, 10, 10)
    line(320, 290, 350, 290)
    line(350, 315, 380, 315)
    line(350, 290, 350, 315)
    ellipse(345, 285, 10, 10)
    ellipse(345, 310, 10, 10)


# start function
def main():
    print("the last four digit student numbers are 6 1 7 2")
    boolValues = getUserBooleanValues()
    result = evaluateMyCircuit(boolValues)
    print("your circuit result is ", result)
    drawCircuit(boolValues, result)


if __name__ == "__main__":
    main()
