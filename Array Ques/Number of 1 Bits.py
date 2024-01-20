'''
WAP to return number of 1 bits, also known as "Hamming weight"

1. Using & operator
2. Using bit manipulation

1. set result bits counter var to 0
2. check while num != 0
3. mod num by 2 to get 1 bit from given 32 bits integer & add it to result counter
4. num = num >> 1 shift all remaining integer bits to right
5. finally return result

'''


def hammingWeight(num):
    res = 0  # bit counter variable
    while num:  # while n != 0
        res += num % 2  # to get 1 bit from given 32 bits integer & add it to res counter
        num = num >> 1  # shift all remaining integer bits to right
    return res


print(hammingWeight(1011))

