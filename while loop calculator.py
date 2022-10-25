dictonary = {"Addition" : 1, "Subtraction" : 2, "Multiplication" : 3, "Division" : 4, "EXIT" : 5}

while True:
    print(f"\n{dictonary}")
    opp = input("Which opperator do you want to use? : ")
    num1 = int(input("Enter 1st number : "))
    num2 = int(input("Enter 2nd number : "))
    
    if opp == '1':
        addition = num1 + num2
        print(f"{num1} + {num2} = {addition}")
    elif opp == '2':
        subtraction = num1 - num2
        print(f"{num1} - {num2} = {subtraction}")
    elif opp == '3':
        multiplication = num1 * num2
        print(f"{num1} x {num2} = {multiplication}")
    elif opp == '4':
        division = num1/num2
        print(f"{num1} / {num2} = {division}")
    else:
        break
