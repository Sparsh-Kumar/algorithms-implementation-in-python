
def calcFibbonaaci (number = None):
    if not number:
        return False
    if number == 0:
        return 0;
    elif number == 1:
        return 1;
    else:
        return calcFibbonaaci (number - 1) + calcFibbonaaci (number - 2)


def main ():
    number = 4
    result = calcFibbonaaci (number)
    if not result:
        print ('error')
    else:
        print (result)

if __name__ == '__main__':
    main ()