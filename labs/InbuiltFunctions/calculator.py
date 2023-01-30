
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def power(x, y):
    return x ** y

print("1.Add \n2.Subtract \n3.Multiply \n4.Divide \n5.Power")

choice = int(input("Select between 1-5: "))
num1 = int(input("Enter first number: "))
num2 = int(input("Enter Second number: "))

if choice == 1:
    print(num1, "+", num2, "=", add(num1, num2))
elif choice == 2:
    print(num1, "-", num2, "=", subtract(num1, num2))
elif choice == 3:
    print(num1, "*", num2, "=", multiply(num1, num2))
elif choice == 4:
    print(num1, "/", num2, "=", divide(num1, num2))
elif choice == 5:
    print(num1, "^", num2, "=", power(num1, num2))
else:
    print("Invalid choice. Please enter a number between 1 and 5.")
