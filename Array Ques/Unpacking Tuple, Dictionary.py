# Unpacking means getting data in more readable form from tuple, dictionary
# Uses FOR LOOP
# Unpacking List of Tuples

people = [("Sid", 10000), ("Shiv", 20000), ("chiku", 30000), ("kuhu", 40000)]
print("Unpacking List of Tuples:-")
for name,sal in people:
    print(name)
    print(sal)
    print()


# unpacking Dictionary
people = {"Sid": 10000, "Shiv": 20000, "chiku": 30000, "kuhu": 40000}
print("Key-Value pairs:-")
for key, value in people.items():
    print(key, value)


print()

# getting only keys
print("Keys:-")
for key in people:
    print(key)

print()

print("Getting Keys in another way:-")
for k in people.keys():
    print(k)

print()
print("Values:- ")
for v in people.values():
    print(v)
