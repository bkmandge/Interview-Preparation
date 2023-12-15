# print numbers from 1 to N

# When only target N is given - using for loop (iterative way)
def print_numbers(N):
    for i in range(1, N + 1):
        print(i)


# print_numbers(5)


# When starting num and target N is given
def print_nums(num, target_N):
    if num == target_N:
        print(num)
        return
    print(num)
    print_nums(num + 1, target_N)


# print_nums(1, 5)


# When only target N is given.
# 1. Base condition, 2. recursive call to N - 1 -> print previous numbers first then next number, 3. printing N
def print_n(N):
    if N == 1:
        print(N)
        return
    print_n(N - 1)
    print(N)


print_n(5)
