#CALCULATOR
def powered(x,y):
    return x**y
def multi(x,y):
    return x*y
def add(x,y):
    return x+y
def Root(x):
    return (x**0.5)
def sub(x,y):
    return(x-y)
def calculator():
    print("Welcome For Calculation :")
    print("Click 1. for Addition :")
    print("Click 2. for Subtraction :")
    print("Click 3. for Powering :")
    print("Click 4. for UnderRoot :")
    print("Click 5. for Multipy")
    print("6. OFF :")
while True:
    choice=int(input('''Welcome For Calculation !
    Click 1. for Addition :
    Click 2. for Subtraction :
    Click 3. for Powering :
    Click 4. for Under Root :
    Click 5. for Multipy :
    Click 6. OFF :
    Enter following number 1 to 6 :'''))
    if choice == 1:
        first_no=float(input("enter first no. :"))
        sec_no=float(input("Enter second no :"))
        print(add(first_no,sec_no))
    elif choice==2:
        first_no=float(input("Enter first no :"))
        sec_no=float(input("enter second no. to subtract :"))
        print(sub(first_no,sec_no))
    elif choice==3:
        first_no=float(input("Enter base no. :"))
        sec_no=float(input("Enter power no : "))
        print(powered(first_no,sec_no))
    elif choice==4:
        num=float(input("Enter base No. :"))
        print(Root(num))
    elif choice==5:
        firstnum=("Enter first Number :")
        secnum=("Enter second Number :")
        print(multi(first_no,secnum))
    elif choice==6:
        break
    else:
        print("The number is incorrect. Try Again ! ")
print("THANK YOU")
