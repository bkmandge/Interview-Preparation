# Calculate and return square root of given number
# 25 -> 5, 100 -> 10


def square_root(X):
    if X < 0:
        raise ValueError("Enter non-negative number.")

    if X in [0, 1]:
        return X

    low = 0
    high = X

    while low <= high:
        mid = low + (high - low) // 2
        mid_squared = mid * mid

        if mid_squared > X:
            high = mid - 1
        elif mid_squared < X:
            low = mid + 1
        else:
            return mid


print(square_root(49))
print(square_root(0))





