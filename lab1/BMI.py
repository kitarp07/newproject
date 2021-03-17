#Solve each of the problems solving python scripts. Make sure you use appropriate variable names and comments. When there
# is a final answer, have python print it to the screen.
#A person's body mass index(BMI) is defined as: BMI= mass in kg / (height in m)**2

mass = float(input("Enter the mass in kg: "))
height = float(input("Enter the height in meter: "))
BMI = (mass/(height**2))
print(f'The BMI of the person is {BMI}')

