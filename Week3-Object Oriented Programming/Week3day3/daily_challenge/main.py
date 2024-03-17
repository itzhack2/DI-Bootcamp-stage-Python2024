# Daily Challenge - Circle
# import math
# class Circle:
#     def __init__(self, radius=None, diameter=None):
#         if radius is not None:
#             self.radius = radius
#             self.diameter = radius * 2
#         elif diameter is not None:
#             self.diameter = diameter
#             self.radius = diameter / 2
#         else:
#             raise ValueError("Either radius or diameter must be specified.")
#     @property
#     def area(self):
#         return math.pi * self.radius ** 2
    
#     def __str__(self):
#         return f"Circle(radius={self.radius}, diameter={self.diameter})"
    
#     def __add__(self, other):
#         return Circle(radius=self.radius + other.radius)
    
#     def __lt__(self, other):
#         return self.radius < other.radius
    
#     def __eq__(self, other):
#         return self.radius == other.radius
    
#     def __gt__(self, other):
#         return self.radius > other.radius
    
#     def __le__(self, other):
#         return self.radius <= other.radius
    
#     def __ge__(self, other):
#         return self.radius >= other.radius
    
#     def __ne__(self, other):
#         return self.radius != other.radius

# circle1 = Circle(radius=3)
# circle2 = Circle(diameter=6)

# print("Circle 1 radius:", circle1.radius)
# print("Circle 2 diameter:", circle2.diameter)

# print("Circle 1 area:", circle1.area)
# print("Circle 2 area:", circle2.area)

# print("Circle 1:", circle1)
# print("Circle 2:", circle2)

# circle3 = circle1 + circle2
# print("Circle 3 radius (circle1 + circle2):", circle3.radius)
# print("Is Circle 1 bigger than Circle 2?", circle1 > circle2)
# print("Are Circle 1 and Circle 2 equal?", circle1 == circle2)
# circle_list = [circle1, circle2, circle3]
# sorted_circles = sorted(circle_list)
# print("Sorted circles:", sorted_circles)
