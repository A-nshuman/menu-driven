# Declaring dictonaries
basic_dict = {"Addition" : 1, "Subtraction" : 2, "Multiplication" : 3, "Division" : 4, "EXIT" : 5}
special_dict = {"Modulus" : 1, "Exponent" : 2, "Floor Division" : 3, "Square Root" : 4, "EXIT" : 5}
bitwise_dict = {"AND" : 1, "OR" : 2, "XOR" : 3, "NOT" : 4, "EXIT" : 5}

# Basic operations
def add(num1, num2):
    summ = num1 + num2
    print(f"Addition of {num1} and {num2} = {summ}")

def sub(num1, num2):
    diff = num1 - num2
    print(f"Subtraction of {num1} and {num2} = {diff}")

def multi(num1, num2):
    prod = num1 * num2
    print(f"Multiplication of {num1} and {num2} = {prod}")

def div(num1, num2):
    quo = num1 / num2
    print(f"Division of {num1} and {num2} = {quo}")

# Special operations
def modulus(num1, num2):
    mod = num1 % num2
    print(f"Modulus of {num1} and {num2} = {mod}")

def exponent(num1, num2):
    exp = num1 ** num2
    print(f"Exponentiation of {num1} and {num2} = {exp}")

def floor_division(num1, num2):
    fd = num1 // num2
    print(f"Floor Division of {num1} and {num2} = {fd}")

def rt(num):
    sqrt = num ** 0.5
    print(f"Square root of {num} = {round(sqrt, 3)}")

# Bitwise operations
def a_nd(num1, num2):
    nd = num1 & num2
    print(f"AND of {num1} and {num2} = {nd}")

def o_r(num1, num2):
    r = num1 | num2
    print(f"OR of {num1} and {num2} = {r}")

def x_o_r(num1, num2):
    xr = num1 ^ num2
    print(f"XOR of {num1} and {num2} = {xr}")

def n_o_t(num):
    nt = ~num
    print(f"NOT of {num} = {nt}")

# Program Start
while True:
    print("\nMenu")
    print("\n1.Basic Operations")
    print("2.Special Operations")
    print("3.Bitwise Operations")
    print("4.EXIT")
    choice = int(input("\nEnter your choice : "))

    if choice == 1:
        while True:
            print("\n",basic_dict)
            basic_choice = int(input("\nEnter your choice : "))
            if basic_choice == 1:
                num1 = int(input("\nEnter 1st number : "))
                num2 = int(input("Enter 2nd number : "))
                add(num1, num2)
            elif basic_choice == 2:
                num1 = int(input("\nEnter 1st number : "))
                num2 = int(input("Enter 2nd number : "))
                sub(num1, num2)
            elif basic_choice == 3:
                num1 = int(input("\nEnter 1st number : "))
                num2 = int(input("Enter 2nd number : "))
                multi(num1, num2)
            elif basic_choice == 4:
                num1 = int(input("\nEnter 1st number : "))
                num2 = int(input("Enter 2nd number : "))
                div(num1, num2)
            elif basic_choice == 5:
                print("You have exited basic operations")
                break
            else:
                print("Incorrect Choice")
                continue
        
    elif choice == 2:
        while True:
            print("\n",special_dict)
            special_choice = int(input("\nEnter your choice : "))
            if special_choice == 1:
                num1 = int(input("\nEnter 1st number : "))
                num2 = int(input("Enter 2nd number : "))
                modulus(num1, num2)
            elif special_choice == 2:
                num1 = int(input("\nEnter 1st number : "))
                num2 = int(input("Enter 2nd number : "))
                exponent(num1, num2)
            elif special_choice == 3:
                num1 = int(input("\nEnter 1st number : "))
                num2 = int(input("Enter 2nd number : "))
                floor_division(num1, num2)
            elif special_choice == 4:
                num = int(input("Enter a number : "))
                rt(num)
            elif special_choice == 5:
                print("You have exited special operations")
                break
            else:
                print("Incorrect Choice")
                continue
        
    elif choice == 3:
        while True:
            print("\n",bitwise_dict)
            bitwise_choice = int(input("\nEnter your choice : "))
            if bitwise_choice == 1:
                num1 = int(input("\nEnter 1st number : "))
                num2 = int(input("Enter 2nd number : "))
                a_nd(num1, num2)
            elif bitwise_choice == 2:
                num1 = int(input("\nEnter 1st number : "))
                num2 = int(input("Enter 2nd number : "))
                o_r(num1, num2)
            elif bitwise_choice == 3:
                num1 = int(input("\nEnter 1st number : "))
                num2 = int(input("Enter 2nd number : "))
                x_o_r(num1, num2)
            elif bitwise_choice == 4:
                num = int(input("Enter a number : "))
                n_o_t(num)
            elif bitwise_choice == 5:
                print("You have exited bitwise operations")
                break
            else:
                print("Incorrect Choice")
                continue
    
    elif choice == 4:
        print("\nYou have exited the program")
        break

    else:
        print("\nIncorrect Choice")
        continue
# Program End