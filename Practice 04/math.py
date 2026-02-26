import math

# 1. Convert degree to radian
degree = float(input("Input degree: "))
radian = math.radians(degree)
print("Output radian:", radian)


# 2. Area of trapezoid
height = float(input("\nHeight: "))
base1 = float(input("Base, first value: "))
base2 = float(input("Base, second value: "))

area_trapezoid = 0.5 * height * (base1 + base2)
print("Area of trapezoid:", area_trapezoid)


# 3. Area of regular polygon
n = int(input("\nInput number of sides: "))
side = float(input("Input the length of a side: "))

area_polygon = (n * side ** 2) / (4 * math.tan(math.pi / n))
print("The area of the polygon is:", area_polygon)


# 4. Area of parallelogram
base = float(input("\nLength of base: "))
height = float(input("Height of parallelogram: "))

area_parallelogram = base * height
print("Area of parallelogram:", area_parallelogram)