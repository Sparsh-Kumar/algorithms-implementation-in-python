

def gcd (number1, number2):

    reminder = number1 % number2
    if reminder == 0:
        return number2
    else:
        return gcd (number2, reminder)

def main ():

    number1, number2 = 8, 12
    result = gcd (number1, number2)
    if result == -1:
        print ('Error')
    else:
        print (result)

if __name__ == '__main__':
    main ()