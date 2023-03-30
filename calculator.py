#Librarys
import math
import fractions

# Functions

def again():
    another = str(input("Have another calculation? "))
    another=another.replace(" ","")
    if another.lower() == 'yes':
        define()
    else:
        pass


def add(a, b):
    answer = str(input("How do you want your answer? "))
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
    answer = str(input("How do you want your answer? "))
    answer=answer.replace(" ","")
    if answer.lower() == "absolutevalue":
        print("Your answer is ", abs(a * b))
        again()
    elif answer.lower()=='fraction' or answer.lower()=='fractions':
        print("Your answer is: ", fractions.Fraction(a*b).limit_denominator(100))
        again()
    else:
        print(a * b)
        again()


def division(a, b):
    answer = str(input("How do you want your answer? "))
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
    elif answer.lower()=='fraction' or answer.lower()=='fractions':
        print("Your answer is: ", fractions.Fraction(a/b).limit_denominator(100))
        again()
    else:
        print(a / b)
        again()

def exponents(a, b):
    answer=str(input("How do you want your answer? "))
    answer=answer.replace(" ", "")
    result=a**b
    if answer.lower()=='absolutevalue':
        print(f"Your answer is {abs(result)}")
        again()
    elif answer.lower()=="percentage" or answer.lower()=="percent" and b<0:
        print("Your answer is: ", result, "%")
    elif answer.lower()=='fraction' or answer.lower()=='fractions':
        print("Your answer is: ", fractions.Fraction(result).limit_denominator(100))
        again()
    else: 
        print(f"Your answer is: {result}")
        again()



def aritmithic():
    a = str(input("So, what is the first number? (Base of the exponent)? "))
    b = str(input("Ok, what is the second number? (exponent of the exponents)? "))
    a=fractions.Fraction(a)
    b=fractions.Fraction(b)
    print("The following will be the choices of arithmetic operations you can perform")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exponents")
    operation = int(input("Which of the 5 choices of operation would you like to perform on these numbers? "))

    if operation == 1:
        add(a, b)
    elif operation == 2:
        subtract(a, b)
    elif operation == 3:
        multiply(a, b)
    elif operation == 4:
        division(a, b)
    elif operation == 5:
        exponents(a,b)
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
    shape=str(input("What shape is the problem? ex.Square, triangle, circle, etc. "))
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
        radius=str(input("What is the radius of the circle? "))
        radius=fractions.Fraction(radius)
        peri=2*math.pi*radius
        answer= input("How do you want your answer? ")
        answer=answer.replace(" ","")
        print(f"The perimeter of the circle is {peri}")
    else:
        print("You did not enter a valid shape!")
        perimeter()


def define():
    
    print("The following will be the choices of mathematics you can perform")
    print("Enter only the numbers associated with")
    print("1. Aritmitic/Basic Operations")
    print("2. Area")
    print("3. Perimeter")
    definer=int(input("Which area of mathematics would you like to choose? "))
    if definer==1:
        aritmithic()
    elif definer==2:
        area()
    elif definer==3:
        perimeter() 
# START
print("Hi, I am an AI Calculator who can calculate extreme numbers. Feel free to enter any number you like!")
name=str(input("Whats your name? "))
print(f"Hi {name}!")
print("By the way, I cannot calculate variables, only constants")
print("I would also like to mention that everything must be spelled correctly or I am no use to you")
define()
while (True):
    try: KeyboardInterrupt
    
    except:
        print("1 - Horrible")
        print("2 - Bad")
        print("3 - Okay")
        print("4 - Good")
        print("5. Excellent")
        rate = int(input("How well do you rate this calculator on a scale of 1-5"))
        if rate<=5 and rate == 1 or rate == 2 and rate>=0:
            input("Why do you rate this calculator so low? ")
        elif rate<=5 and rate == 3 and rate >=0:
            input("What can I do to improve your rating? ")
        elif rate<=5 and rate>=0 and rate>=4:
            input("Anything I can do to improve the calculator in the future? ")
        else:
            print("Please enter a positive rating that is greater than 0 and less than 6")