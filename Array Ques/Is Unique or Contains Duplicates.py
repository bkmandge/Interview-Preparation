myList = [1, 20, 30, 44, 5, 56, 57, 8, 19, 10, 31, 12, 13, 14, 35, 16, 27, 58, 19, 21]

def isUnique(list):
    new_list = []
    for i in list:
        if i in new_list:
            print(i)
            return "List is not unique!"
        else:
            new_list.append(i)
    return "List is unique!"


print(isUnique(myList))