
# Udemy course - Complete Python Bootcamp
# Section 8 Homework Assignment


# Problem 1
# Create the Line class methods to accept corrdinates as a pair of tuples and
# return the slope and distance of the Line
class Line:

    def __init__(self, coord1, coord2):
        self.coord1 = coord1
        self.coord2 = coord2

    def distance(self):
        x1,y1 = self.coord1
        x2,y2 = self.coord2
        return (((x2-x1)**2)+((y2-y1)**2))**(0.5)

    def slope(self):
        x1,y1 = self.coord1
        x2,y2 = self.coord2
        return (y2-y1)/(x2-x1)

coordinate1 = (3,2)
coordinate2 = (8,10)
li = Line(coordinate1, coordinate2)
print(li.distance())
print(li.slope())


# Problem 2
# Same with a cylinder
class Cylinder:
    pi = 3.14159
    def __init__(self,height=1,radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        return (Cylinder.pi*(self.radius**2))*self.height

    def surface_area(self):
        return (2*Cylinder.pi*self.radius*self.height) + (2*Cylinder.pi*(self.radius**2))

c = Cylinder(2,3)
print(c.volume())
print(c.surface_area())
