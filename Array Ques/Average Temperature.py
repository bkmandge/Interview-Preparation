'''
Calculate avg temperature:-

1. ask user:- How many day's temperature?
2. declare total var to sum up all days' temperature
3. ask for each day's temperature
4. sum up all days' temperature
5. calculate average with round() & print it

Find the days above average temperature:-
1. need to use list or array data structure
2. array index starts from 0, so range (numDays)
3. add all temperatures to temp[]
'''

numDays = int(input("How many day's temperature? "))
total = 0
for i in range(1, numDays + 1):
    nextDay = int(input("Day "+ str(i) +"'s high temp:"))
    total += nextDay
avg = round(total/numDays, 2)

print("Average temperature is "+ str(avg))

#============================================================#

numDays = int(input("How many day's temperature? "))
total = 0
temp = []
for i in range(numDays):
    nextDay = int(input("Day " + str(i + 1) +"'s high temp: "))
    temp.append(nextDay)
    total += temp[i]

avg = round(total / numDays, 2)
print("Average temperature is "+ str(avg))

above = 0
for i in temp:
    if i > avg:
        above += 1

print(str(above) + " day[s] above average.")