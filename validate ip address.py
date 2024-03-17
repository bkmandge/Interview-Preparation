def is_valid_ip(s):
	n = len(s)

	# for test cases like 1...1 or something lesser than 7
	if n < 7:
		return False

	# Using split to separate all the strings from '.'
	# and create a list like for example -
	# "222.111.111.111" becomes ["222", "111", "111", "111"]
	substrings = s.split(".")
	count = 0

	for substr in substrings:
		count += 1

		# If the substring size is greater than 1 and the first character is '0', return false
		if len(substr) > 1 and substr[0] == '0':
			return False

		# For substrings like a.b.c.d, checking if any character is non-numeric
		if not substr.isdigit():
			return False

		# Check if the number is greater than 255
		if int(substr) > 255:
			return False

	# If the count of substrings is not 4, return false
	if count != 4:
		return False

	return True


# Driver code
s1 = "128.0.0.1"
s2 = "125.16.100.1"
s3 = "125.512.100.1"
s4 = "125.512.100.abc"

print("Valid" if is_valid_ip(s1) else "Not valid")
print("Valid" if is_valid_ip(s2) else "Not valid")
print("Valid" if is_valid_ip(s3) else "Not valid")
print("Valid" if is_valid_ip(s4) else "Not valid")
