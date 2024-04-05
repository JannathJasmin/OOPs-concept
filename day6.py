# 1. Create a class circle and initialise it with radius . Make two methods get_Area and get_circumference inside the class
class Circle():
    def __init__(self, radius):
        self.radius = radius
    
    def get_area(self):
        return 3.14 * (self.radius ** 2)
    
    def get_circumference(self):
        return 2 * 3.14 * self.radius
radius = float(input("Enter the radius of the circle: "))
circle = Circle(radius)
print("Area:", circle.get_area())
print("Circumference:", circle.get_circumference())

# 2.Create a class to find area and perimeter of triangle
class Triangle:
    def __init__(self, base, height, side1, side2, side3):
        self.base = base
        self.height = height
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
    
    def get_area(self):
        area = 0.5 * self.base * self.height
        return area
    
    def get_perimeter(self):
        perimeter = self.side1 + self.side2 + self.side3
        return perimeter
base = float(input("Enter the length of the base: "))
height = float(input("Enter the height of the triangle: "))
side1 = float(input("Enter the length of side 1: "))
side2 = float(input("Enter the length of side 2: "))
side3 = float(input("Enter the length of side 3: "))

triangle = Triangle(base, height, side1, side2, side3)
print("Area:", triangle.get_area())
print("Perimeter:", triangle.get_perimeter())

# 3.Create a Temprature class. Make two methods :**
# 1. convertFahrenheit - It will take celsius and will print it into Fahrenheit.
# 2. convertCelsius - It will take Fahrenheit and will convert it into Celsius
# give the simplest code
class Temperature:
    def convert_fahrenheit(celsius):
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius} degrees Celsius is equal to {fahrenheit} degrees Fahrenheit.")
    def convert_celsius(fahrenheit):
        celsius = (fahrenheit - 32) * 5/9
        print(f"{fahrenheit} degrees Fahrenheit is equal to {celsius} degrees Celsius.")
temperature = float(input("Enter the temperature value: "))
Temperature.convert_fahrenheit(temperature)  
Temperature.convert_celsius(temperature)

# 4.Create a student class and initialize it with and roll number.Make methods to 
#   * It should display all information of student
#   * It should assign age to student
#   * it should assign marks to the student
class Student:
    def __init__(self, roll_number):
        self.roll_number = roll_number
        self.age = None
        self.marks = {}

    def display_info(self):
        print("Student Roll Number:", self.roll_number)
        print("Student Age:", self.age)
        print("Student Marks:", self.marks)

    def assign_age(self, age):
        self.age = age

    def assign_marks(self, subject, marks):
        self.marks[subject] = marks
student1 = Student(101)
student1.assign_age(20)
student1.assign_marks("Math", 95)
student1.assign_marks("Science", 88)
student1.display_info()

# 5. Create a Time class and initialize it with hours and minutes
#   * Make a method add time which should take time object and add them
       
#        Eg:- (2hr and 50 min)+(1 hr and 20 min) is (4hr 10min)
#   * Make a method display which should print the time
#   * Make a method Display minute which should display minutes in the time
  
#       Eg:- 1 hr 2 min should display 62 min
class Time:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def add_time(self, other_time):
        total_minutes = self.hours * 60 + self.minutes + other_time.hours * 60 + other_time.minutes
        hours = total_minutes // 60
        minutes = total_minutes % 60
        return Time(hours, minutes)

    def display(self):
        print(f"{self.hours} hr {self.minutes} min")

    def display_minutes(self):
        print(f"{self.hours * 60 + self.minutes} min")

# Take user input for the first time
hours1 = int(input("Enter hours for the first time: "))
minutes1 = int(input("Enter minutes for the first time: "))
time1 = Time(hours1, minutes1)

# Take user input for the second time
hours2 = int(input("Enter hours for the second time: "))
minutes2 = int(input("Enter minutes for the second time: "))
time2 = Time(hours2, minutes2)

# Add times
result_time = time1.add_time(time2)

# Display result
print("Result of addition:")
result_time.display()

# Display total minutes
print("Total minutes:")
result_time.display_minutes()

# 6.convert minutes to second
class MinutesConverter:
    def __init__(self, minutes):
        self.minutes = minutes

    def to_seconds(self):
        return self.minutes * 60
minutes = float(input("Enter the number of minutes: "))
converter = MinutesConverter(minutes)
seconds = converter.to_seconds()
print(f"{minutes} minutes is equal to {seconds} seconds.")

# 7. Fill in the Line class methods to accept coordinates as a pair of tuples and return the slope and distance of the line.
class Line:
    def __init__(self, coord1, coord2):
        self.coord1 = coord1
        self.coord2 = coord2
    
    def slope(self):
        x1, y1 = self.coord1
        x2, y2 = self.coord2
        if x2 - x1 == 0:
            return "Undefined"  # Vertical line, slope is undefined
        return (y2 - y1) / (x2 - x1)
    
    def distance(self):
        x1, y1 = self.coord1
        x2, y2 = self.coord2
        return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
coordinate1 = (5, 2)
coordinate2 = (8, 10)
li = Line(coordinate1, coordinate2)
# calculate and print distance
distance = li.distance()
print("Distance:", distance)

# Calculate and print slope
slope = li.slope()
print("Slope:", slope)


# 8. Find the volume and surface area of a cylinder using class methods
class Cylinder:
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height
    
    def volume(self):
        return 3.14159 * self.radius ** 2 * self.height
    
    def surface_area(self):
        return 2 * 3.14159 * self.radius * (self.height + self.radius)
c = Cylinder(2, 3)
print("Volume of the cylinder:", c.volume())
print("Surface area of the cylinder:", c.surface_area())


