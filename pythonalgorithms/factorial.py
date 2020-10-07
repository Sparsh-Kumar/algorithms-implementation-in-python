

def CalcFactorial (number):
    if number == 1:
        return 1;
    elif number <= 0:
        return -1;
    else:
        return number * CalcFactorial (number - 1)

def main ():
    result = CalcFactorial (6)
    if result == -1:
        print ('Error')
    else:
        print (result)

if __name__ == '__main__':
    main()