for i in range(5):
    for i in range(5):
      print ('3', end='')

    print()

for i in range (2):
    for i in range (3):
        print('2', end='')

    print()

for i in range(4):
    for j in range(i+1):
        print('*', end='')
    print()

a= 0
for i in range(4):
    for j in range(i+1):
        print(a, end='')
        a +=1
    print()

a= 0
for i in range(5):
    for j in range(i+1):
        print(a, end='')
    a+=1
    print()