num=int(input('Enter the number of factorial: '))
product = 1
for i in range(1, num+1):
    product= (product * i)

print(f'THe factorial of {num} is {product}')


# Multiplication table (from 1 to 10) in Python

num = 12

# To take input from the user
# num = int(input("Display multiplication table of? "))

# Iterate 10 times from i = 1 to 10
for i in range(1, 11):
   print(num, 'x', i, '=', num*i)
