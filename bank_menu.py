import webbrowser

# Declaring Dictonaries
user_list = []
pass_list = []
dash_dict = {"Deposit Amount" : 1, "Withdraw Amount" : 2, "Transfer amount" : 3, "Logout" : 4}

balance = 1000

break_flag = False

# Program Start
while True:
    print("\nMenu")
    print("\n1.Login")
    print("2.Register")
    print("3.Support")
    print("4.EXIT")
    choice = int(input("\nEnter your choice : "))

    if choice == 1:
        while True:
            username = input("\nEnter username : ")
            password = input("Enter password : ")
            if username in user_list and password in pass_list:
                print("\nSuccessfully logged in")

                while True:
                    print("\n", dash_dict)
                    print(f"\nYour current balance is ${balance}")
                    dash_choice = int(input("\nEnter your choice : "))
                    if dash_choice == 1:
                        dep_am = float(input("Enter amount to be deposited : "))
                        balance += dep_am
                    elif dash_choice == 2:
                        with_am = float(input("Enter amount to be withdrawn : "))
                        if with_am > balance:
                            print("\nNot enough balance in your account.")
                        else:
                            balance -= with_am
                    elif dash_choice == 3:
                        tran_am = float(input("Enter amount to be transfered : "))
                        tran_user = input("Enter person's name to be tranfered to : ")
                        y_pass = input("Enter your password : ")
                        if y_pass in pass_list:
                            if tran_am > balance:
                                print("\nNot enough balance in your account.")
                                break
                            else:
                                balance -= tran_am
                                print(f"\nSuccessfully transfered {tran_am} to {tran_user}")
                        else:
                            print("\nIncorrect password, pls try again")
                    elif dash_choice == 4:
                        print("Successfully logged out")
                        break_flag = True
                        break
                    else:
                        print("Incorrect choice")
                if break_flag:
                    break

            else:
                print("\nIncorrect username or password. Pls try again")
                break
                

    elif choice == 2:
        while True:
            username = input("\nEnter username : ")
            password = input("Enter password : ")
            if username in user_list:
                print("User already exists.")
                continue
            else:
                user_list.append(username)
                pass_list.append(password)
                print("\nSuccessfully created your account.")
                print("Please login.")
                break

    elif choice == 3:
        webbrowser.open_new("https://safe-bank.netlify.app")

    elif choice == 4:
        print("Successfully Exited")
        break

    else:
        print("Incorrect choice")