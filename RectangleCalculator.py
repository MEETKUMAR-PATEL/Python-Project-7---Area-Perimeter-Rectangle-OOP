# This is where your code for the RectangleCalculator program will go.
# Name:                 RectangleCalculator.py
# Author:               Meetkumar Patel
# Date Created:         March 25, 2022
# Date Last Modified:   March 25, 2022 

# Purpose:
#This program Will calculate the area and perimeter of rectangle by the use of class and objects 
class Rectangle:
    #Intiating
    def __init__(self, width, height):
        self.width = width
        self.height = height
    #class for calculating the area
    def calculateArea(self):
        area = self.width * self.height
        return area
    #Class for calculating the perimeter
    def calculatePerimeter(self):
        perimeter = 2*(self.width + self.height)
        return perimeter
    #class for getting the display
    def displayInfo(self):
        print("\n{0:}{1:>15}{2:>25}".format("The Area of The Rectangle is: ", self.calculateArea(), "Square Centimeters."))
        print("{0:}{1:>10}{2:>20}".format("The Perimeter of The Rectangle is: ", self.calculatePerimeter(), "Centimeters."))
        print("Thank you!")

print("Hello!In this program you wil be able to caluclate the area and perimeter of a rectangle in centimeters.\n")

width = float(input("Enter the Width of the object in cm [Centimeters]: "))
height = float(input("Enter the Height of the object in cm [Centimeters]: "))

rectangleCalculator = Rectangle(width,height)

rectangleCalculator.displayInfo()


