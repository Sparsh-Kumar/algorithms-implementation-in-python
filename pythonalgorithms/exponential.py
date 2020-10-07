

def CalcExponential (number, power):
    if power == 1:
        return number
    elif power == 0:
        return 1;
    elif power < 0:
        return -1;
    else:
        return number * CalcExponential (number, power - 1)

def main ():
    number, power = 3, 5;
    result = CalcExponential (number, power)
    if result == -1:
        print ('Not a valid power')
    else:
        print (result)

if __name__ == '__main__':
    main ()