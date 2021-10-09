print("Welcome To DZ ATM..")
restart = ('y')
chances = 3
balance = 1000

while chances>=0:
    pin = int(input("please enter a 4 digit pin: "))
    if pin ==(1982):
        print("You Entered your pin correctly")
        print("press 1 for balace")
        print("press 2 for make a withdrawl")
        print("press 3 to make a pay in")
        print("press 4 to return card")
        option = int(input("what would you like to choose : "))
        if option ==1:
            print("your Balance is $",balance)
            restart = input("would you like to go back ??")
            if restart in ('n','NO','no','N'):
                print('THANK YOU')
                break
            else :
                restart = ('y')
        elif option ==2:
            option2 = ('y')
            withdrawl = float(input("how much would you like you withdrawl? "))
            if withdrawl:
                balance = balance-withdrawl
                print(f"your balace is now {balance}")
                restart = input("would you like to go back ??")
                if restart in ('n','no','NO','N'):
                    print("thank you")
                    break

        elif option ==3:
            pay_in = float(input("how much would you like to pay in ? "))
            balance = balance + pay_in
            print("your balance is now $",balance)
            restart = input("would you like to go back ??")
            if restart in ('n', 'no', 'NO', 'N'):
                print("thank you")
                break

        elif option ==4:
            print("please wait until you card returned ....")
            print("thank you for taking out service ....")
            break

        else:
            print("enter a correct pin number..")
            restart = ('y')
    elif pin != ('1982'):
        print("Invalid Password")
        chances = chances-1
        if chances ==0:
            print("no more tries")
            break

