def triangleArea(base,height):
    area = (base*height)/2
    return area
def squareArea(side):
    area = side ** 2
    return area
def rectangleArea(lenght,width):
    area = lenght ** width
    return area
def circleArea(radius):
    area = 3.14159 * radius ** 2
    return area

print("Area Calculator")
print("Choose a shape: ")
print("1.Rectangle")
print("2.Triangle")
print("3.Square")
print("4.Circle")

choice = input("Enter your choice from (1/2/3/4): ")

if choice == "1":
    l = float(input("Enter the lenght of rectangle: "))
    w = float(input("Enter the width of rectangle: "))
    print("The area of rectangle is: ", rectangleArea(l,w))


elif choice == "2":
    b = float(input("Enter the base of triangle: "))
    h = float(input("Enter the height of triangle: "))
    print("The area of triangle is: ", triangleArea(b,h))

elif choice == "3":
    s = float(input("Enter a side of square: "))
    print("The area of square is: ", squareArea(s))

elif choice == "4":
    r = float(input("Enter the radius of circle: "))
    print("The area of circle is: ", circleArea(r))