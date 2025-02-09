'''
Exercise 1: Playing around with Geometry.
To implement the classes representing: equilateral triangles, circles, rectangles, squares and pentagons with the following
characteristics/properties/capabilities.

1. they should understand the calculate_area() and calculate_perimeter() messages with the obvious meaning
2. the state must be private
3. a list of geometric shapes must be sortable by area and by perimeter (not at the same time, of course)
4. to add an hexagon class should maintain all the capabilities of the existing classes and correctly interact with them
5. to write a iterator that permits to return the elements of a list of geometric shapes sorted by increasing areas.
'''

import math

def create_polygon(p_type, p_number, p_number2=None):
    class _polygon:
        def __init__(self, length):
            self.length = length
        def calculate_area(self):
            return .25*p_number*self.length**2*(math.tan(math.pi/p_number))**-1
        def calculare_perimeter(self):
            return self.length * p_number
        def __str__(self):
            return f"{p_type}: {p_number} of length {self.length}. Area: {self.calculate_area()}"
    return _polygon

triangle = create_polygon("triangle", 3)
square = create_polygon("square", 4)
pentagon = create_polygon("pentagon", 5)
hexagon = create_polygon("hexagon", 6)


t = triangle(4) # class
s = square(4) # class
p = pentagon(4) # class
h = hexagon(4) # class

sorted_area = sorted([t,s,p,h], key = lambda x: x.calculate_area())
sorted_perimeter = sorted([t,s,p,h], key = lambda x: x.calculare_perimeter())

print(*sorted_area)
print(*sorted_perimeter)

class iterator_area:
        def __init__(self, data_list):
            self.index = -1
            self.data_list = data_list

        def __iter__(self):
            return self

        def __next__(self):
            if self.index == len(self.data_list):
                raise StopIteration
            self.index = self.index + 1
            return self.data_list[self.index]

i_a = iterator_area(sorted_area)
print(next(i_a))
print(next(i_a))
print(next(i_a))
print(next(i_a))
