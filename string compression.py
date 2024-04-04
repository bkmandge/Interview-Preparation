def string_compression(s):
    compressed = ""
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:    # if curr char is same as previous increase count
            count += 1
        else:
            # if different add to compressed result and reset count back to 1
            compressed += s[i - 1] + str(count) 
            count = 1
    # append last char to compressed result
    compressed += s[-1] + str(count)
    
    # if the compressed string is shorter than original then return it else return original
    return compressed if len(compressed) < len(s) else s


print(string_compression("aabcccccaaa"))  # Output: "a2b1c5a3"


# using hashmap
def compress(chars):
    # Check if the list is empty
    if len(chars) == 0:
        return 0

    # Initialize variables
    current_char = chars[0]  # Initialize the current character
    count = 1  # Initialize the count of the current character
    result_index = 0  # Initialize the index for the result array

    # Iterate through the characters starting from the second one
    for i in range(1, len(chars)):
        # If the current character is the same as the previous one, increase the count
        if chars[i] == current_char:
            count += 1
        else:
            # If the current character is different, update the result array
            chars[result_index] = current_char  # Store the current character in the result array
            result_index += 1  # Move to the next position in the result array

            # If the count is greater than 1, update the result array with the count
            if count > 1:
                for digit in str(count):
                    chars[result_index] = digit
                    result_index += 1
            
            # Update the current character and reset the count for the new character
            current_char = chars[i]
            count = 1

    # Add the last character and its count to the result array
    chars[result_index] = current_char
    result_index += 1
    if count > 1:
        for digit in str(count):
            chars[result_index] = digit
            result_index += 1

    # Return the length of the compressed array
    return result_index

# Test case
# chars = ["a", "a", "b", "b", "c", "c", "c"]  # Output: ["a", "2", "b", "2", "c", "3"]
chars = ["a","a","b","b","c","c","c"]
compressed_length = compress(chars)
print(compressed_length)  
print(chars[:compressed_length])  
