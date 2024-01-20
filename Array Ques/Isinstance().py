def sumNumbers(num1, num2):
    if isinstance(num1, int) and isinstance(num2, int):
        print(num1 + num2)
    else:
        print("Not of integer types")


sumNumbers(5, 'sid')
sumNumbers(5, 10)