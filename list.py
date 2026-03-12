data = [120, 20, 25, 40, 200, 57, 150, 160, 90, 150, 85, 190, 20, 30, 205, 20]
fruits = ["Mango", "Banana", "Apple"]

print("Original list:",data)
print("Original list:",fruits)

#Append
data.append(200)
print("After append:", data)

fruits.append("Pineapple")
print("After append:", fruits)

#Extend
data.extend([300,400, 255, 625])
print("After extend", data)

fruits.extend(["Cherry", "Guava", "watermelon"])
print("After extend", fruits)


#Imsert
data.insert(2, 150)
print("After insert at index 2:", data)

# Remove
for num in data:
    if num == 150:
        data.remove(150)
print("After remove 150:", data)

# Pop
popped = data.pop()
print("After pop:", data, "I popped value:", popped)

# Index
if 200 in data:
    idx = data.index(200)
    print("Index of 200:", idx)

# Count
count_20 = data.count(20)
print("Count of 20:", count_20)