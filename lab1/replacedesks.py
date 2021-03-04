#A school decided to replace the desks in threee classrooms.  Each desk sits two students. Given the number
# of students in each class, print the smallest possible number of desks that can be purchased.

S_one = int(input("Enter the number of students in class 1: "))
S_two = int(input("Enter the number of students in class 2: "))
S_three = int(input("Enter the number of students in class 3: "))
desks_one = (S_one//2)
desks_two = (S_two//2)
desks_three = (S_three//2)
total_desks = (desks_one + desks_two + desks_three)
remainder = (S_one + S_two + S_three)%(total_desks)


print(f'The smallest number possible number of desks that can be purchased is {(total_desks) + (remainder)}')

