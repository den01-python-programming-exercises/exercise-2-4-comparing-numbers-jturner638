def main():
    #write your code below this line
    number1 = int(input())
    number2 = int(input())

    if number1 > number2:
        print("{} is greater than {}.".format(number1, number2))
    elif number1 < number2:
        print("{} is smaller than {}.".format(number1, number2))
    else:
        print("{} is equal to {}.".format(number1, number2))

if __name__ == '__main__':
    main()
