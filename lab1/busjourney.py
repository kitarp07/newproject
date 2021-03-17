'''
You live 4 miles from university. The bus drives at 25 mph but spends 2 minutes at each of the 10 stops
on the way. How long will the bus journey take. Alternatively, you could run to university. You jog the first mile at a7mph;
then run the next two at 15mph; before jogging the last at 7mph again. Will this be quicker or slower than the bus.
'''

time_me = {(1/7) + (2/15) + (1/7)}
time_bus = {(4/25) - (1/3)}
if time_me > time_bus:
 print("i am quicker than bus")
else:
 print("i am slower than bus")
