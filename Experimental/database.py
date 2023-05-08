import pyrebase

# Firebase configuration
firebase_config = {
    "apiKey": "AIzaSyBFbZ4u6cDpEeY36_LicY0mbaG4LNivlRQ",
    "authDomain": "calculatorpy-b374f.firebaseapp.com",
    "databaseURL": "https://calculatorpy-b374f-default-rtdb.firebaseio.com",
    "projectId": "calculatorpy-b374f",
    "storageBucket": "calculatorpy-b374f.appspot.com",
    "messagingSenderId": "302531060792",
    "appId": "1:302531060792:web:df51bad7d75d73d7d032cd",
}

firebase = pyrebase.initialize_app(firebase_config)
db = firebase.database()

name ="Aanya"
def add(a, b):
    result = a + b
    data = {"operation": f"{a} + {b}", "result": result, "name": name}
    db.child("calculations").push(data)
    return result

def subtract(a, b):
    result = a - b
    data = {"operation": f"{a} - {b}", "result": result}
    db.child("calculations").push(data)
    return result

def multiply(a, b):
    result = a * b
    data = {"operation": f"{a} * {b}", "result": result}
    db.child("calculations").push(data)
    return result

def divide(a, b):
    result = a / b
    data = {"operation": f"{a} / {b}", "result": result}
    db.child("calculations").push(data)
    return result

# main calculator function
def calculator():
    while True:
        print("Select operation.")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")
        
        choice = input("Enter choice(1/2/3/4/5): ")
        
        if choice in ('1', '2', '3', '4'):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            
            if choice == '1':
                print(num1, "+", num2, "=", add(num1, num2))
            elif choice == '2':
                print(num1, "-", num2, "=", subtract(num1, num2))
            elif choice == '3':
                print(num1, "*", num2, "=", multiply(num1, num2))
            elif choice == '4':
                print(num1, "/", num2, "=", divide(num1, num2))
        elif choice == '5':
            break
        else:
            print("Invalid Input")

# run the calculator function
calculator()
