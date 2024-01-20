# list()

word = "hello"
print(list(word))

print(list(range(1, 101)))
# ----------------------------------------------------------------------------------------------
'''
                    range() - Starting from - Stopping to(not including) - Steps(default is 1)
'''

for num in range(1, 11):
    print(num)

print()

for num in range(1, 11, 2):
    print(num)

print()
# ----------------------------------------------------------------------------------------------
'''
                    zip() - Combines two lists together - creates zip object
-> maps only available range of items & ignores rest of values
-> Use FOR LOOP - returns Tuple
'''
num = [1, 2, 3, 4, 5, 6, 7, 8]
words = ['hello', 'my', 'name', 'is', 'Sony']

combinedItems = zip(num, words)
print("Zip object:", combinedItems)

for item in combinedItems:
    print(item)

print()
# ----------------------------------------------------------------------------------------------

'''
                    enumerate() - assigns default index to each item & returns index & value together in tuple form.
-> Trick:- assigns number to each value
-> Can assign index range starting from any number
-> Used with FOR LOOP
'''

words = ['hello', 'my', 'name', 'is', 'Sony']

for item in enumerate(words):
    print(item)

for item in enumerate(words, 1):
    print(item)



