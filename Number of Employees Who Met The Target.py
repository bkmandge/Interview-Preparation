"""
                Number of Employees Who Met The Target

Input: hours = [0,1,2,3,4], target = 2
Output: 3

"""


def numberOfEmployeesWhoMetTarget(hours, target):
    emp_count = 0
    for i in range(len(hours)):
        if hours[i] >= target:
            emp_count += 1
    return emp_count


hours = [0,1,2,3,4]
target = 2

print(numberOfEmployeesWhoMetTarget(hours, target))