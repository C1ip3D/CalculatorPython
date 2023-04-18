# Librarys
import math
import fractions

# Functions


def code():

    def again():
        another = input("Have another calculation? ")
        another = another.replace(" ", "").lower()

        if another == 'yes':
            define()
        else:
            pass

    def add(a, b):
        answer = input("How do you want your answer? ")
        answer = answer.replace(" ", "").lower()

        if answer == "absolutevalue":
            print("Your answer is ", abs(a + b))
            again()
        elif answer == 'round' or answer == 'rounded':
            print("Your answer is: ", round(a+b))
            again()
        else:
            print(a + b)
            again()

    def subtract(a, b):
        answer = input("How do you want your answer?")
        answer = answer.replace(" ", "").lower()
        if answer == "absolutevalue":
            print("Your answer is ", abs(a - b))
            again()
        elif answer == 'round' or answer == 'rounded':
            print("Your answer is: ", round(a-b))
            again()
        else:
            print(a - b)
            again()

    def multiply(a, b):
        answer = input("How do you want your answer? ")
        answer = answer.replace(" ", "").lower()
        if answer == "absolutevalue":
            print("Your answer is ", abs(a * b))
            again()
        elif answer == 'fraction' or answer == 'fractions':
            print("Your answer is: ", fractions.Fraction(
                a*b).limit_denominator(100))
            again()
        elif answer == 'round' or answer == 'rounded':
            print("Your answer is: ", round(a*b))
            again()
        else:
            print(a * b)
            again()

    def division(a, b):
        answer = input("How do you want your answer? ")
        answer = answer.replace(" ", "").lower()
        if answer == "absolutevalue":
            print("Your answer is ", abs(a / b))
            again()
        elif answer == "remainder":
            print("Your answer is ", (a % b))
            again()
        elif answer == "integer":
            print("Your answer is ", (a // b))
            again()
        elif answer == 'round' or answer == 'rounded':
            print("Your answer is: ", round(a/b))
            again()
        elif answer == 'fraction' or answer == 'fractions':
            print("Your answer is: ", fractions.Fraction(
                a/b).limit_denominator(100))
            again()
        else:
            print(a / b)
            again()

    def exponents(a, b):
        answer = str(input("How do you want your answer? "))
        answer = answer.replace(" ", "")
        result = a**b
        if answer.lower() == 'absolutevalue':
            print(f"Your answer is {abs(result)}")
            again()
        elif answer.lower() == "percentage" or answer.lower() == "percent":
            print("Your answer is: ", result/100, "%")
        elif answer.lower() == 'fraction' or answer.lower() == 'fractions':
            print("Your answer is: ", fractions.Fraction(
                result).limit_denominator(100))
            again()
        elif answer.lower() == 'round' or answer.lower() == 'rounded':
            print("Your answer is: ", round(result))
            again()
        else:
            print(f"Your answer is: {result}")
            again()

    def aritmithic():
        a = str(input("So, what is the first number? (Base of the exponent)? "))
        b = str(input("Ok, what is the second number? (exponent of the exponent)? "))
        a = fractions.Fraction(a)
        b = fractions.Fraction(b)
        print("The following will be the choices of arithmetic operations you can perform")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exponents")
        operation = input(
            "Which of the 5 choices of operation would you like to perform on these numbers? ")

        if operation == 1:
            add(a, b)
        elif operation == 2:
            subtract(a, b)
        elif operation == 3:
            multiply(a, b)
        elif operation == 4:
            division(a, b)
        elif operation == 5:
            exponents(a, b)
        else:
            print("Please enter a valid option")
            print("Please renter your numbers")
            aritmithic()

    def area():
        shape = str(
            input("What shape is the problem ex.Square, triangle, circle, etc."))
        shape = shape.replace(" ", "")
        if shape.lower() == "square":
            side1 = int(
                input("What is the measure of one side of the square? "))
            unit = str(input("In what units are the measures? "))
            area = side1**2
            print(f"The area of the quadrilateral is {area} {unit} squared")
            again()
        elif shape.lower() == "rectangle" or shape.lower() == "parallelogram":
            side1 = int(input("What is one side of the parallelogram? "))
            side2 = int(
                input("What is the second side of the parallelogram? "))
            unit = str(input("What unit are the measures? "))
            area = side1*side2
            print(f"The area of the parallelogram is {area} {unit} squared")
        elif shape.lower() == "triangle":
            base = int(input("What is the base of the triangle? "))
            height = int(input("What is the height of the triangle? "))
            area = (base*height)/2
            print(f"The area of the triangle is {area}")
            again()
        elif shape.lower() == 'circle':
            radius = int(input("What is the radius of the circle? "))
            area = math.pi*(radius**2)
            print(f"The area of the circle is {area}")
            again()
        else:
            print("You did not enter a vaild shape!")
            area()

    def perimeter():
        shape = str(
            input("What shape is the problem? ex.Square, triangle, circle, etc. "))
        shape = shape.replace(" ", "")
        if shape.lower() == "square" or shape.lower() == "rectangle" or shape.lower() == "parallelogram":
            side1 = int(input("What is one side of the quadrilateral? "))
            side2 = int(
                input("What is the second side of the quadrilateral? "))
            peri = 2*(side1+side2)
            print(f"The perimeter of the quadrilateral is {peri}")
            again()

        elif shape.lower() == 'triangle':
            side1 = int(input("What is the length of the first side? "))
            side2 = int(input("What is the length of the second side? "))
            side3 = int(input("What is the length of the third side? "))
            peri = side1+side2+side3
            print(f"The perimeter of the triangle is {peri}")
        elif shape.lower() == "circle":
            radius = str(input("What is the radius of the circle? "))
            radius = fractions.Fraction(radius)
            peri = 2*math.pi*radius
            answer = input("How do you want your answer? ")
            answer = answer.replace(" ", "")
            print(f"The perimeter of the circle is {peri}")
        else:
            print("You have entered a shape that is not yet supported by our system!")
            perimeter()

    def conv():
        def distance():
            startUnit = str(input("What is the starting unit? "))
            startNum = str(input("What is the starting number? "))
            endUnit = str(input("What is the ending unit"))

            startUnit = startUnit.replace(" ", "")
            startUnit = startUnit.lower()
            endUnit = endUnit.replace(" ", "")
            endUnit = endUnit.lower()

            startNum = fractions.Fraction(startNum)

            if startUnit == "miles" or startUnit == "mile" or startUnit == "mi":

                if endUnit == 'feet' or endUnit == 'foot' or endUnit == "ft":

                    answer = str(input("How do you want your answer? "))
                    answer = answer.replace(" ", "")
                    answer = answer.lower()

                    if answer == 'round' or answer == 'rounded':
                        print("The approximate measurement is now: ",
                              round(startNum*5280))
                        again()
                    else:
                        print("The exact measurement is now: ", startNum*5280)
                        again()

                elif endUnit == "kilometers" or endUnit == 'kilometer' or startUnit == "km":

                    answer = str(input("How do you want your answer? "))
                    answer = answer.replace(" ", "")
                    answer = answer.lower()

                    if answer == 'round' or answer == 'rounded':
                        print("The approximate measurement is now: ",
                              round(startNum*1.60934))
                        again()
                    else:
                        print("The exact measurement is now: ", startNum*1.60934)
                        again()

                elif endUnit == 'yards' or endUnit == 'yard' or endUnit == 'yd':
                    answer = str(input("How do you want your answer? "))
                    answer = answer.replace(" ", "").lower()

                    if answer == 'round' or answer == 'rounded':
                        print("The approximate measurement is now: ",
                              round(startNum*1760))
                        again()
                    else:
                        print("The exact measurement is now: ", startNum*1760)
                        again()
                else:
                    print("You have entered a unit that is not supported! ")
                    distance()

            elif startUnit == 'kilometers' or startUnit == 'kilometer' or startUnit == 'km':

                if endUnit == 'miles' or endUnit == 'mi' or endUnit == 'mile':

                    answer = str(input("How do you want your answer? "))
                    answer = answer.replace(" ", "")
                    answer = answer.lower()

                    if answer == 'round' or answer == 'rounded':
                        print("The approximate measurement is now: ",
                              round(startNum*1.609344))
                        again()
                    else:
                        print("The measurement is now: ", startNum*1.609344)
                        again()

                elif endUnit == 'foot' or endUnit == 'feet' or endUnit == 'ft':

                    answer = str(input("How do you want your answer? "))
                    answer = answer.replace(" ", "")
                    answer = answer.lower()

                    if answer == 'round' or answer == 'rounded':
                        print("The approximate measurement is now: ",
                              round(startNum*3280.84))
                        again()
                    else:
                        print("The measurement is now: ", startNum*3280.84)
                        again()

                elif endUnit == 'yard' or endUnit == 'yards' or endUnit == 'yd':

                    answer = str(input(" How do you want your answer? "))
                    answer = answer.replace(" ", "")
                    answer = answer.lower()

                    if answer == 'round' or answer == 'rounded':
                        print("The approximate measurement is now: ",
                              round(startNum*1093.61))
                        again()
                    else:
                        print("The measurement is now: ", startNum*1093.61)
                        again()
                else:
                    print("You have entered a unit that is not supported! ")
                    distance()
            elif startUnit == 'yards' or startUnit == 'yd' or startUnit == 'yard':
                if endUnit == 'miles' or endUnit == 'mi' or endUnit == 'mile':
                    answer = str(input(" How do you want your answer? "))
                    answer = answer.replace(" ", "")
                    answer = answer.lower()

                    if answer == 'round' or answer == 'rounded':
                        print("The approximate measurement is now: ",
                              round(startNum/1760))
                        again()
                    else:
                        print("The measurement is now: ", startNum/1760)
                        again()
                elif endUnit == 'feet' or endUnit == 'ft' or endUnit == 'foot':

                    answer = str(input(" How do you want your answer? "))
                    answer = answer.replace(" ", "")
                    answer = answer.lower()

                    if answer == 'round' or answer == 'rounded':
                        print("The approximate measurement is now: ",
                              round(startNum*3))
                        again()
                    else:
                        print("The measurement is now: ", startNum*3)
                        again()
                elif endUnit == 'in' or endUnit == 'inches' or endUnit == 'inch':

                    answer = str(input(" How do you want your answer? "))
                    answer = answer.replace(" ", "")
                    answer = answer.lower()

                    if answer == 'round' or answer == 'rounded':
                        print("The approximate measurement is now: ",
                              round(startNum*36))
                        again()
                    else:
                        print("The measurement is now: ", startNum*36)
                        again()
                else:
                    print("You have entered a unit that is not supported! ")
                    distance()
            else:
                print("You have entered a unit that is not supported yet! ")
                distance()

        def temp():
            startUnit = str(
                input("What is the starting unit: Fahrenheit, Celsius, or Kelvin?"))
            startNum = str(input("What is the starting number?"))
            startNum = fractions.Fraction(startNum)

            startUnit = startUnit.replace(" ", "").lower()

            if startUnit == "fahrenheit":
                endNumC = (startNum-32)/1.8
                endNumK = endNumC + 273.15
                print("The temperature in Celsius is: ", endNumC, "°C")
                print("The temperature in Kelvin is: ", endNumK, "K")
            elif startUnit == "celsius" or startUnit == "centigrade":
                endNumF = (1.8)*startNum + 32
                endNumK = startNum + 273.15
                print("The temperature in Fahrenheit is: ", endNumF, "°F")
                print("The temperature in Kelvin is: ", endNumK, "K")
            elif startUnit == "kelvin":
                endNumC = startNum - 273.15
                endNumF = endNumC * 1.8 + 32
                print("The temperature in Celsius is: ", endNumC, "°C")
                print("The temperature in Fahrenheit is: ", endNumF, "°F")

        answer = str(
            input("Do you want to calculate distances or temperatures? "))
        answer = answer.replace(" ", "").lower()

        if answer == 'distance' or answer == 'distances':
            distance()
        elif answer == 'temperature' or answer == 'temperatures':
            temp()

    def geo():
        what = input("What would you like to do in the geometry section? ")
        what = what.replace(" ", "").lower()

        if what == 'pythagoras' or what == 'pythagoreantheorem' or what == 'pythagorean':
            missing = input(
                "What is the missing side of the right triangle? If none, type no ")
            missing = missing.replace(" ", "").lower()

            if missing == "no" or missing == 'none':
                a = int(
                    input("What is the measurement of side A in the right triangle? "))
                b = int(
                    input("What is the measurement of side B in the right triangle? "))
                c = int(
                    input("What is the measurement of side C in the right triangle? "))
                ab = a**2 + b**2

                if ab == c**2:
                    print("TRUE, the triangle is a right triangle!")
                    again()
                else:
                    print("FALSE, the triangle is not a right triangle!")
                    again()

            elif missing == 'a':
                b = int(input("Which side is B in the right triangle? "))
                c = int(input("Which side is C in the right triangle? "))
                a = math.sqrt(c**2 - b**2)
                print(f"Side a is {a}")
                again()

            elif missing == 'b':
                a = int(input("Which side is A in the right triangle? "))
                c = int(input("Which side is C in the right triangle? "))
                b = math.sqrt(c**2 - a**2)
                print(f"Side b is {b}")
                again()

            elif missing == 'c':
                b = int(input("Which side is B in the right triangle? "))
                a = int(input("Which side is A in the right triangle? "))
                c = math.sqrt(a**2 + b**2)
                print(f"Side c is {c}")
                again()

            else:
                print("Invalid input!")
                again()

        else:
            print("Invalid input!")
            geo()

    def define():

        print("The following will be the choices of mathematics you can perform")
        print("Enter only the numbers associated with")
        print("1 - Aritmitic/Basic Operations")
        print("2 - Area")
        print("3 - Perimeter")
        print("4 - Conversions")
        print("5 - Geometry")
        definer = int(
            input("Which area of mathematics would you like to choose? "))
        if definer == 1:
            aritmithic()
        elif definer == 2:
            area()
        elif definer == 3:
            perimeter()
        elif definer == 4:
            conv()
        elif definer == 5:
            geo()
        else:
            print("Enter a valid number")
            define()

    # START
    print("Hi, I am an AI Calculator who can calculate extreme numbers. Feel free to enter any number you like!")
    print("By the way, I cannot calculate variables, only constants")
    print("I would also like to mention that everything must be spelled correctly or I am no use to you")
    name = str(input("Whats your name? "))
    print(f"Hi {name}!")
    print("By the way, I cannot calculate variables, only constants")
    print("I would also like to mention that everything must be spelled correctly or I am no use to you")
    define()


try:
    code()
except KeyboardInterrupt:
    print("1 - Horrible")
    print("2 - Bad")
    print("3 - Okay")
    print("4 - Good")
    print("5. Excellent")
    rate = int(input("How well do you rate this calculator on a scale of 1-5? "))
    if rate <= 5 and rate == 1 or rate == 2 and rate >= 0:
        input("Why do you rate this calculator so low? ")
    elif rate <= 5 and rate == 3 and rate >= 0:
        input("What can I do to improve your rating? ")
    elif rate <= 5 and rate >= 0 and rate >= 4:
        input("Anything I can do to improve the calculator in the future? ")
    else:
        print("Please enter a positive rating that is greater than 0 and less than 6")
