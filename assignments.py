import random
 
def ex2():
    width = float(input("Enter width:"))
    height = float(input("Enter height:"))
    length = float(input("Enter length:"))
 
    volume = width * height * length
    print (f"Volume is: {volume}")
 
def ex4():
    txt = "Python was conceived in the late 1980s by Guido van Rossum at Centrum Wiskunde & Informatica (CWI) in the Netherlands as a successor to ABC programming language, which was inspired by SETL capable of exception handling and interfacing with the Amoeba operating system. Its implementation began in December 1989. Van Rossum shouldered sole responsibility for the project, as the lead developer, until 12 July 2018, when he announced his permanent vacation from his responsibilities as Python's Benevolent Dictator For Life, a title the Python community bestowed upon him to reflect his long-term commitment as the project's chief decision-maker. In January 2019, active Python core developers elected a 5-member Steering Council to lead the project. As of 2021, the current members of this council are Barry Warsaw, Brett Cannon, Carol Willing, Thomas Wouters, and Pablo Galindo Salgado."
    tokens = txt.split()
    count = 0
    for word in tokens:
        if word == "Python":
            count = count + 1
    print(count)
 
def ex6():
    myList = []
    myList.append(11)
    myList.append(100)
    myList.append(101)
    myList.append(999)
    myList.append(1001)
    myList.append(1)
    myList.reverse()
    print(myList)


def ex8():
    myList = [6,2,7,3,77,7,1]
    min = myList[0]
    for num in myList:
        if num < min:
            min = num
    print(min)

def ex10():
    txt = input("Enter string: ")
    count = 0
    count2 = 0
    for i in txt:
        if i == "a" or i == "e" or i == "i" or i == "o" or  i == "u" or i == "A" or i == "E" or i == "I" or  i == "O" or i == "U":
            count = count + 1
        else:
            count2 = count2 + 1
    print(f"Vowels: {count}")
    print(f"Consonants: {count2}")

def ex12():
    num = input("Enter Integer: ")
    if(num.count(".") == 1):
        print(f"ERROR: {num} is not an integer")
    else:
        print(int(num)*-1)

ex12()