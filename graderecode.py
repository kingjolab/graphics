__author__ = 'wangyu'

from SimpleGraphics import *

'''
    Student class
    initialize student attributes like number photo name major and grade
    providing set and get group methods for access and modify the class attributes and print the object
'''


class Students:
    def __init__(self):
        self.__number = ''
        self.__photo = ''
        self.__name = ''
        self.__major = ''
        self.__grade = ''

    def setNumber(self, number):
        self.__number = number

    def setName(self, name):
        self.__name = name

    def setPhoto(self, photo):
        self.__photo = photo

    def setMajor(self, major):
        self.__major = major

    def setGrade(self, grade):
        self.__grade = grade

    def setStudentRecords(self, infoList):
        self.setNumber(infoList[0].strip())
        self.setPhoto(infoList[1].strip())
        self.setName(infoList[2].strip())
        self.setGrade(infoList[3].strip())
        self.setMajor(infoList[4].strip())

    def getNumber(self):
        return self.__number

    def getName(self):
        return self.__name

    def getPhoto(self):
        return self.__photo

    def getMajor(self):
        return self.__major

    def getGrade(self):
        return self.__grade

    def image(self):
        image = loadImage(self.__photo)
        drawImage(image, 0, 0)

    def __str__(self):
        return "%s,%s,%s,%s,%s" % (str(self.getNumber()), self.getPhoto(), self.getName(), self.getMajor(), self.getGrade())

'''
    Records class
    initialize a dictionary for storing records
    providing storing(save) and receive methods and iteratively get item, also delete item
'''


class Records:
    def __init__(self, file="record.txt"):
        self.__record = {}
        self.saveFile = file

    def save(self):
        with open(self.saveFile, "w") as f:
            for s in self.__record:
                f.write(str(self.__record[s]))

    def receive(self):
        try:
            with open(self.saveFile, "r") as f:
                while True:
                    studentInfo = f.readline()
                    if not studentInfo:
                        break
                    infoList = studentInfo.split(',')
                    student = Students()
                    student.setStudentRecords(infoList)
                    self.__record[infoList[0].strip()] = student
        except Exception:
            pass

    def __iter__(self):
        for s in self.__record:
            yield self.__record[s]

    def __getitem__(self, item):
        if self.__record.get(item):
            return self.__record.get(item)
        return None

    def __setitem__(self, key, value):
        self.__record[key] = value

    def __delitem__(self, key):
        self.__record.pop(key)


# menu function for print options
def menu():
    print("----------MENU------------\n"
          "1, add a student\n"
          "2, remove a student\n"
          "3, search a signal record of a student\n"
          "4, search whole record of a student\n"
          "5, quit")
    return input("input your choose (e.g. 1) : ")


# main function
def main():
    records = Records()
    records.receive()
    while True:
        try:
            number = menu()
            if number == '5':
                break
            elif number == '4':
                for s in records:
                    print(s)
                    s.image()
            elif number == '3':
                studentId = input("input the student number that you are looking for (e.g. 123456): ")
                if records[studentId]:
                    print(records[studentId])
                    records[studentId].image()
                else:
                    print("this student do not exist")
            elif number == '2':
                studentId = input("input the student number that you want to remove (e.g. 123456): ")
                if records[studentId]:
                    del records[studentId]
            elif number == '1':
                studentInfo = input("input the student info that you want to add \n"
                                        "your input must include at least a number and photo name\n"
                                        "Or full information in order: number, photo name, name, grade, major\n"
                                        "E.g. 123456, user.png, , , or 123456, user.png, bill, A, cs or 123456, user.png, ,A, : ")
                if studentInfo:
                    infoList = studentInfo.split(',')
                    if len(infoList) == 5 and infoList[0].strip() and infoList[1].strip():
                        if records[infoList[0].strip()]:
                            print("this student exist")
                            continue
                        student = Students()
                        student.setStudentRecords(infoList)
                        records[infoList[0].strip()] = student
                    else:
                        print("input format error \n please notice the comma\nE.g. 123456, user.png, , , Or 123456, user.png, bill, A, cs Or 123456, user.png, ,A, etc")
            else:
                print("your input must be (1 to 5)")
        except Exception as error:
            print(error)
    records.save()

if __name__ == "__main__":
    main()
