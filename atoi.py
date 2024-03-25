def main():
	strn1 = "12546"
	val = int(strn1)
	print("String value = ", strn1)
	print("Integer value = ", val)
	
	strn2 = "GeeksforGeeks"
	try:
		val = int(strn2)
	except ValueError:
		val = 0
		print("String value = ", strn2)
		print("Integer value = ", val)

main()