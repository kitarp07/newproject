'''
wap to convert seconds to day, hour and minutes
'''
seconds = float(input("Enter the seconds: "))
day =(seconds)/(60*60*24)
print(f'{seconds} seconds equals to {day} days')
hour = seconds/(60*60)
print(f'{seconds} seconds equals to {hour} hours')
minutes = seconds/(60)
print(f'{seconds} seconds equals to {minutes}  minutes')