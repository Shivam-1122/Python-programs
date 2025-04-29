def add():
    print(f"The result is: {num1 + num2}")
def sub():
    print(f"The result is: {num1 - num2}")
def mul():
    print(f"The result is: {num1 * num2}")
def div():
    if num2 != 0:
        print(f"The result is: {num1 / num2}")
    else:
        print("Error: Division by zero is not allowed.")
print("Select operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

choice = input("Enter choice (1/2/3/4): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == '1':
    add()
elif choice == '2':
    sub()
elif choice == '3':
    mul()
elif choice == '4':
    div()
else:
    print("Invalid input")