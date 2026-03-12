n = int(input("Enter the number of rows: "))

a = 1

for i in range(1,n+1):
    for j in range(i):
        a += 1
    print()