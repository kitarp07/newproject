#Given the integer N - the number of minutes that is passed since midnight - how many hours and minutes
# are displayed on the 24 h digital clock?

N = int(input("Enter the minutes passed since midnight:"))
hours = (N//60)
minutes = (N%60)



print(f'The hour displayed in the 24 h digital clock is {hours}')
print(f'The minutes displayed in the 24 h digital clock is {minutes}')
