#  question 1 ;
""" Find the maximum element present in a list.
First, you have to take 5 inputs from the user and store it in a list.
 Then, find the maximum number present in it."""

a=int(input ("enter first number: "))
b= int(input("enter second number: "))
c= int(input ("enter third number: "))
def greater(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c
print(greater(a,b,c))
# question 2 ;
"""Write a Python class named Rectangle constructed by a length and width and a method which will compute the area of a rectangle."""
class Rectangle():
    def __init__(self,l,W):
        self.length = l
        self.width = W
    def rectangle_area(self):
        return self.length*self.width
newRectangle = Rectangle(4,8)
print(newRectangle.rectangle_area()) 


# question 3;
# Write a Python class named Circle constructed by a radius and two methods which will compute the area and the perimeter of a circle

class Circle():
    def __init__(self, r):
        self.radius = r

    def area(self):
        return self.radius**2*3.14

    def perimeter(self):
        return 2*self.radius*3.14

NewCircle = Circle(9)
print(NewCircle.area())
print(NewCircle.perimeter())

# question 4 ;
# Check if the first and last number of a list is the same.

li=[10,20,30,40,100]
if li[0]==li[-1]:
    print("True")
else:
    print("False")







