fruits = {"apple", "banana", "cherry"}
for x in fruits:
    if x == "banana":
        continue
    print(x)
print('end')

fruits = {"apple", "banana", "cherry"}
for x in fruits:
    print(x)
    if x == "banana":
        break