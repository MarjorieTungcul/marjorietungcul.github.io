print("AREA OF SHAPES CALCULATOR")
print(" ")
print("==SQUARE==")

s= int (input("Enter the Side Length of Square:"))
area_of_square_formula=s**2

decimal_point="{:.1f}".format(area_of_square_formula)
print("Area of a Square is=",decimal_point)

print(" ")
print("==TRIANGLE==")

a= int(input("Enter value for A:"))
b= int(input("Enter value for B:"))
c= int(input("Enter value for C:"))
semiperimeter_of_a_triangle = sp = (a+b+c)/2

area_of_triangle_formula=(sp*(sp-a)*(sp-b)*(sp-c))**0.5
decimal_point="{:.2f}".format(area_of_triangle_formula)
print("Area of a Triangle is:", decimal_point)

print(" ")
print("==CIRCLE==")

r=int(input("Enter the radius of the given circle:"))

area_of_the_given_circle_formula=3.14*(r**2)
decimal_point="{:.2f}".format(area_of_the_given_circle_formula)
print("The area of the given circle is:", decimal_point)

print(" ")
print("==RECTANGLE==")

length= int(input("Enter the length of a Rectangle:"))
breadth= int(input("Enter the breadth of a Rectangle:"))

area_of_a_rectangle_formula= length*breadth
decimal_point="{:.2f}".format(area_of_a_rectangle_formula)
print("Area of a Rectangle is:", decimal_point)

print(" ")
print("==PARALLELOGRAM==")

base=int(input("Enter the length of base:"))
height=int(input("Enter the measurement of height:"))

area_of_a_parallelogram_formula= base*height
decimal_point="{:.1f}".format(area_of_a_parallelogram_formula)
print("Area of a Parallelogram is:", decimal_point)

print(" ")
print("==TRAPEZOID==")

h=int(input("Enter the height of trapezoid:"))
b1=int(input("Enter the base one value:"))
b2=int(input("Enter the base two value:"))

area_of_a_trapezoid_formula=(1/2)*(b1+b2)*h
decimal_point="{:.1f}".format(area_of_a_trapezoid_formula)
print("Area of a Parallelogram is:", decimal_point)

print(" ")
print("==ELLIPSE==")

ma=int(input("Enter the length of major axis:"))
mi=int(input("Enter the length of minor axis:"))

area_of_an_ellipse_formula=3.141592*ma*mi
decimal_point="{:.6f}".format(area_of_an_ellipse_formula)
print("Area of an Ellipse is:", decimal_point)









