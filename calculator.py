title = "!!!! CALCULATOR !!!!"
def calculator():
    print(title.center(30))
    try:
        a = int(input("Enter first number\n"))
        b = int(input("Enter second number\n"))
        c = input("Enter operator\n")
    except:
        print("enter valid value an integer")
        exit()
    add = "+"
    sub = "-"
    mul = "*"
    div = "/"
    if c == add: 
        print(a,"+",b,"is",a+b)
    elif c == sub:
        print(a,"-",b,"is",a-b)
    elif c == mul:
        print(a,"*",b,"is",a*b)
    elif c == div:
        print(a,"/",b,"is",a/b)
    else:
        print("choose a valid operator")
 
if __name__ == '__main__':
    calculator()