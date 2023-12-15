# Check if given number is palindrome or not
# Palindrome:- original and reverse order of number is same


def palindrome_number(num):
    temp_num = num
    ans = 0
    while num:
        rem = num % 10
        num = num // 10
        ans = ans * 10 + rem

    if ans == temp_num:
        return True
    return False


number = int(input("Enter any number: "))
print(f"Original number: {number}")
print("Is palindrome or not: ", palindrome_number(number))
