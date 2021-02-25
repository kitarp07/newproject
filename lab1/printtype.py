name = input ("Enter your name:")
age  = int (input ("Enter your age:"))

print("hello my name is" + name +  " and i am" + str(age) + " years old")
print("hello my name is", name, "and i am", age, "years old")
print("hello my nam is %s and i am %d years old" % (name, age))
print("hello mt nam is {} and i am {} years old".format(name, age))
print(f"hello my nam is {name} and i am {age} years old")