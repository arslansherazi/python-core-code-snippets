def division(num1, num2):
    try:
        ans = num1 / num2
    except ZeroDivisionError as error:
        print('Exception::', error)
        return 0
    else:
        print('This block executes if no exception occurs')
        return ans
    finally:
        print('This block executes either exception occurs or not')


if __name__ == '__main__':
    num1 = input('Enter number1::')
    num2 = input('Enter number2::')

    ans = division(int(num1), int(num2))

    if ans:
        print(ans)