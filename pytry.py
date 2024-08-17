problem = 0
number1 = ''
number2 = ''
sign = ''

def entry():
    number1 = input('first number')
    sign = input ('what to do')
    number2 = input ('second number')
    which_sign()

def which_sign():
    if sign == '+':
        add()
    elif sign == '-':
        subtract ()
    elif sign == '*':
        multiply()
    elif sign == '/':
        divide ()
    else:
        entry()
        

            

        
    
    