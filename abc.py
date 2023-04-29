import math
def calculate_circle_area(radius):
    area = math.pi * radius ** 2
    return area
def print_file_extension(filename):
    extension = filename.split(".")[-1]
    print("The extension of the file is :", extension)
radius = float(input("Input the radius of the circle : "))
filename = input("Input the Filename: ")
area = calculate_circle_area(radius)
print("The area of the circle with radius", radius, "is:", area)

print_file_extension(filename)
