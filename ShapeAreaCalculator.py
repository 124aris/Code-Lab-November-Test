# Create a Python program to calculate the area of geometric shapes (circle, rectangle, or
# triangle, etc.):
# 1. Define a function that takes command line arguments for the shape type and its
# corresponding dimensions.
# 2. Create a library named "area_calculator" containing functions for calculating the
# area of each shape.
# 3. Implement 'if' statements within the function to identify the shape and call the
# corresponding area calculation function from the library.
# 4. Display the calculated area.
# 5. Allow users to specify the shape and dimensions through command line
# arguments. Ensure dimensions are provided in the required format (e.g., radius
# for a circle, length and width for a rectangle).
# Include a document providing usage examples and test cases.
# *Write program in file ShapeAreaCalculator.py*

import ShapeAreaCalculatorLibrary;

def CalculateArea(Shape):
    while True: 
        if Shape == "circle":
            Radius = int(input("Enter The Radius Of The Circle:"));
            return ShapeAreaCalculatorLibrary.CircleArea(Radius);
        elif Shape == "rectangle":
            Length = int(input('Enter The Length of The Rectangle:'));
            Width = int(input('Enter The Width Of The Rectangle:'));
            return ShapeAreaCalculatorLibrary.RectangleArea(Length, Width);
        elif Shape == "triangle":
            Base = int(input('Enter The Base Of The Triangle:'));
            Height = int(input('Enter The Height of The Triangle:'));
            return ShapeAreaCalculatorLibrary.TriangleArea(Base, Height);
        else:
           return print('Please Choose Correct Shape');

Shape = input('Enter Name Of A Shape:');
CalculateArea(Shape);