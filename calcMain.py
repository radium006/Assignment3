from calculator import add, subtract, multiply, divide

print("Welcome to Kev's simple calculator")
#cont = True
#while cont == True:

while True:
    while True:
        try:
            number_1 = int(input("Enter num1: "))
            break
        except ValueError:
            print("Incorrect input: Not a number, try again.")    
    
    while True:
        
        operand = input('Enter operand: ')

        if operand == '+' or operand == '-' or operand == '*' or operand == '/':
            break
        else:
            print("Not a valid input, enter a '+', '-', '*', or a '/'")

    while True:    
        try:
            number_2 = int(input('Enter num2: '))
            break
        except ValueError:
            print("Incorrect input: Not a number, try again.")      
    
    if operand == "+":
        result = add(number_1, number_2)
    elif operand == '-':
        result = subtract(number_1,number_2)
    elif operand == '*':
        result = multiply(number_1,number_2)
    elif operand == '/':
        result = divide(number_1,number_2)
    else:
        print("ERROR: INVALID OPERAND")    
    
    print("Your equation is {0} {1} {2} = {3}".format(number_1,operand,number_2,result))
    
    cont = input("Press 'q' to quit or any other key to continue")
    if cont == 'q':
        break
    
 