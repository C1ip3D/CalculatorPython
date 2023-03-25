import math
# Functions

def again():
    another = str(input("Have another calculation?"))
    another=another.replace(" ","")
    if another.lower() == 'yes':
        define()
    else:
        pass


def add(a, b):
    answer = str(input("How do you want your answer?"))
    answer=answer.replace(" ","")
    if answer.lower() == "absolutevalue":
        print("Your answer is ", abs(a + b))
        again()
    else:
        print(a + b)
        again()


def subtract(a, b):
    answer = str(input("How do you want your answer?"))
    answer=answer.replace(" ","")
    if answer.lower() == "absolutevalue":
        print("Your answer is ", abs(a - b))
        again()
    else:
        print(a - b)
        again()


def multiply(a, b):
    answer = str(input("How do you want your answer?"))
    answer=answer.replace(" ","")
    if answer.lower() == "absolutevalue":
        print("Your answer is ", abs(a * b))
        again()
    else:
        print(a * b)
        again()


def division(a, b):
    answer = str(input("How do you want your answer?"))
    answer=answer.replace(" ","")
    if answer.lower() == "absolutevalue":
        print("Your answer is ", abs(a / b))
        again()
    elif answer.lower() == "remainder":
        print("Your answer is ", (a % b))
        again()
    elif answer.lower() == "integer":
        print("Your answer is ", (a // b))
        again()
    else:
        print(a / b)
        again()


def aritmithic():
    a = int(input("So, what is the first number?"))
    b = int(input("Ok, what is the second number?"))
    print("The following will be the choices of arithmetic operations you can perform")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    operation = int(input("Which of the 4 choices of operation would you like to perform on these numbers? "))

    if operation == 1:
        add(a, b)
    elif operation == 2:
        subtract(a, b)
    elif operation == 3:
        multiply(a, b)
    elif operation == 4:
        division(a, b)
    else:
        print("Please enter a valid option")
        print("Please renter your numbers")
        aritmithic()

def area():
    shape=str(input("What shape is the problem ex.Square, triangle, circle, etc."))
    shape=shape.replace(" ","")
    if shape.lower()=="square" or shape.lower()=="rectangle" or shape.lower()=="parallelogram":
        side1=int(input("What is one side of the quadrilateral? "))
        side2=int(input("What is the second side of the quadrilateral? "))
        area=side1*side2
        print(f"The area of the quadrilateral is {area}")
    elif shape.lower()=="triangle":
        base=int(input("What is the base of the triangle? "))
        height=int(input("What is the height of the triangle? "))
        area=(base*height)/2
        print(f"The area of the triangle is {area}")
    elif shape.lower()=='circle':
        radius=int(input("What is the radius of the circle? "))
        area=math.pi*(radius**2)
        print(f"The area of the circle is {area}")
    else: 
        print("You did not enter a vaild shape!")
        area()

def perimeter():
    shape=str(input("What shape is the problem ex.Square, triangle, circle, etc."))
    shape=shape.replace(" ","")
    if shape.lower()=="square" or shape.lower()=="rectangle" or shape.lower()=="parallelogram":
        side1=int(input("What is one side of the quadrilateral? "))
        side2=int(input("What is the second side of the quadrilateral? "))
        peri=2*(side1+side2)
        print(f"The perimeter of the quadrilateral is {peri}")
    elif shape.lower()=='triangle':
        side1=int(input("What is the length of the first side? "))
        side2=int(input("What is the length of the second side? "))
        side3=int(input("What is the length of the third side? "))
        peri=side1+side2+side3
        print(f"The perimeter of the triangle is {peri}")
    elif shape.lower()=="circle":
        radius=int(input("What is the radius of the circle? "))
        peri=2*math.pi*radius
        print(f"The perimeter of the circle is {peri}")
    else:
        print("You did not enter a valid shape!")
        perimeter()


def define():
    print("Hi, I am an AI Calculator who can calculate extreme numbers. Feel free to enter any number you like!")
    global name
    name=str(input("Whats your name? "))
    print(f"Hi {name}!")
    print("By the way, I cannot calculate variables, only constants")
    print("I would also like to mention that everything must be spelled correctly or I am no use to you")
    print("The following will be the choices of mathematics you can perform")
    print("Enter only the numbers associated with")
    print("1. Aritmitic/Basic Operations")
    print("2. Area")
    print("3. Perimeter")
    definer=int(input("Which area of mathematics would you like to choose"))
    if definer==1:
        aritmithic()
    elif definer==2:
        area()
    elif definer==3:
        perimeter() 
# START
define()