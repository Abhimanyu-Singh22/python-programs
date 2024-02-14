import math
import numpy as np
from fractions import Fraction
import matplotlib.pyplot as plt

class EleganceMath:

    def __init__(self, number):
        self.number = number
    @staticmethod
    def is_prime(number):
        if number < 2:
            return False
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                return False
        return True
    @staticmethod
    def factorial(number):
        if number < 0:
            return "Factorial is not defined for negative numbers."
        result = 1
        for i in range(1, number + 1):
            result *= i
        return result
    @staticmethod
    def fibonacci(number):
        fib_sequence = [0, 1]
        while fib_sequence[-1] + fib_sequence[-2] < number:
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence


    #end-codeblock for elegance

    #start- codeblock for Surface area and volume    
    @staticmethod
    def cube_properties(side_length):
        total_surface_area = 6 * side_length**2
        curved_surface_area = 4 * side_length**2
        volume = side_length**3
        return total_surface_area, curved_surface_area, volume

    @staticmethod
    def cuboid_properties(length, width, height):
        total_surface_area = 2 * (length * width + length * height + width * height)
        curved_surface_area = 2 * (length * height + width * height)
        volume = length * width * height
        return total_surface_area, curved_surface_area, volume

    @staticmethod
    def cylinder_properties(radius, height):
        total_surface_area = 2 * math.pi * radius * (radius + height)
        curved_surface_area = 2 * math.pi * radius * height
        volume = math.pi * radius**2 * height
        return total_surface_area, curved_surface_area, volume

    @staticmethod
    def cone_properties(radius, height):
        slant_height = math.sqrt(radius**2 + height**2)
        total_surface_area = math.pi * radius * (radius + slant_height)
        curved_surface_area = math.pi * radius * slant_height
        volume = (1/3) * math.pi * radius**2 * height
        return total_surface_area, curved_surface_area, volume

    @staticmethod
    def sphere_properties(radius):
        total_surface_area = 4 * math.pi * radius**2
        curved_surface_area = 4 * math.pi * radius**2
        volume = (4/3) * math.pi * radius**3
        return total_surface_area, curved_surface_area, volume

    @staticmethod
    def hemisphere_properties(radius):
        total_surface_area = 2 * math.pi * radius**2
        curved_surface_area = 2 * math.pi * radius**2
        volume = (2/3) * math.pi * radius**3
        return total_surface_area, curved_surface_area, volume
    # end- codeblock for Surface area and volume    

#start- codeblock for hcf and lcm
def find_hcf(x, y):
    while y:
        x, y = y, x % y
    return x

def find_lcm(x, y):
    return (x * y) // find_hcf(x, y)
#end codeblock for lcm and hcf

#start codeblock for squareroot
def find_square_root(number):
    if number < 0:
        return "Square root is undefined for negative numbers."
    
    return number ** 0.5
#end codeblock for squareroot 

#start codeblock for irrational to rational with precision
def approximate_irrational(number, precision=10):
    return Fraction(number).limit_denominator(precision)
#end codeblock for irrational to rational with precision

#start codeblock for ploting graph
def Plote_Graph():
    n=int(input("Enter The Number of coordinates: "))
    x = []
    y = []

    for i in range(0,n):
        x1 = int(input("Enter x coordinate: "))
        y1 = int(input("Enter y coordinate: "))
        x.append(x1)
        y.append(y1)
    print(x)
    print(y)
    plt.plot(x, y)
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Cartesian Plane Graph')
    plt.show()

# -end start codeblock for ploting graph
    
# -start start codeblock for histogram
def Plote_Histogram():
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.title('Histogram')
    plt.show()
#-end start codeblock for histogram
    
def display_elegance(self):
            num = int(input("Enter a number for elegance: "))
            elegance_math = EleganceMath(num)
            elegance_math.display_elegance()
            print(f"Elegance with the number {self.number}:")

print("1. Elegant Numerics")
print("2. Non Terminating Numbers to Rational Numbers with Precision")
print("3. Find the HCF and LCM fo a number")
print("4. Arthematic Operations")
print("5. Finding Square Root of a Number")
print("6. Surface Area and Volume")
print("7. Co-ordinate Geometry")
print("8. Statistics(histograms)")
print("9. Enter 9 to exit the program \n")
 
choice = int(input("Choose an operation (1/2/3/4/5/6/7/8/9):"))



if choice == 1:
    if __name__ == "__main__":
                
        print("1. Prime Check")
        print("2. Factorial")
        print("3. Fibonacci Sequence")
        SubChoice = int(input("Choose an operation (1/2/3): "))

        if SubChoice == 1:
           number = int(input("enter the number for Prime Check: "))
           print(f"{number} is {'prime' if EleganceMath.is_prime(number) else ' not prime'}.")
        
        elif SubChoice == 2:
            number = int(input("enter the number for factorial: "))
            print(f"The factorial of {number} is {EleganceMath.factorial(number)}.")
            exit()

        elif SubChoice == 3:
            number = int(input("enter the number for Fibonacci Sequence: "))
            print(f"The Fibonacci sequence up to {number} is {EleganceMath.fibonacci(number)}.")

        else:
            print("Invalid choice. Please choose a valid option (1/2/3).")

if choice == 2:
    if __name__ == "__main__":
        try:
            irrational_number = float(input("Enter an irrational number to approximate: "))
            precision = int(input("Enter the precision (number of digits repetin after the decimal point): "))
            rational_approximation = approximate_irrational(irrational_number, 10**precision)       
            print(f"The rational approximation of {irrational_number} is: {rational_approximation}")
        
        except ValueError:
            print("Invalid input. Please enter a valid number and precision.")

if choice == 3:
    if __name__ == "__main__":
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        hcf = find_hcf(num1, num2)
        lcm = find_lcm(num1, num2)
        print(f"The LCM of {num1} and {num2} is: {lcm}")
        print(f"The HCF of {num1} and {num2} is: {hcf}")

if choice == 4: 
    if __name__ == "__main__":
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Remainder after division")

        choice == int(input(" Enter the number corresponding to your choice: "))

        if choice in range(1,6):
            if choice == 1:
                add1=float(input("Enter a Value: "))
                add2=float(input("Enter a Value: "))
                sum=(add1+add2)
                print("The Sum of the 2 numbers is", sum)
            
            if choice == 2:
                min1=float(input("Enter the Minued: "))
                min2=float(input("Enter a Subtrahend: "))
                sub=(min1-min2)
                print("The Difference of the 2 numbers is", sub)

            if choice == 3:
                mul1=float(input("Enter a Value: "))
                mul2=float(input("Enter a Value: "))
                pro=(mul1*mul2)
                print("The Product of the 2 numbers is", pro)

            if choice == 4:
                div1=float(input("Enter the Divident: "))
                div2=float(input("Enter the Divisor: "))
                div=(div1/div2)
                print("The Quotient of the Division is", div)

            if choice == 5:
                div3=float(input("Enter the Divident: "))
                div4=float(input("Enter the Divisor: "))
                div5=(div3%div4)
                print("The Remainder after division is", div5)
        else:print("Invalid choice. Please choose a number between 1 and 6.")

if choice == 5:
    if __name__ == "__main__":
        try:
            num = float(input("Enter a number to find its square root: "))
            
            root_result = find_square_root(num)
            
            print(f"The square root of {num} is: {root_result}")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if choice == 6:
    if __name__ == "__main__":
        print("Choose a 3D shape:")
        print("1. Cube")
        print("2. Cuboid")
        print("3. Cylinder")
        print("4. Cone")
        print("5. Sphere")
        print("6. Hemisphere")

        choice = int(input("Enter the number corresponding to your choice: "))


        if choice in range(1, 7):
            if choice == 1:
                side_length = float(input("Enter the side length of the cube: "))
                properties = EleganceMath.cube_properties(side_length)
            elif choice == 2:
                length = float(input("Enter the length of the cuboid: "))
                width = float(input("Enter the width of the cuboid: "))
                height = float(input("Enter the height of the cuboid: "))
                properties = EleganceMath.cuboid_properties(length, width, height)
            elif choice == 3:
                radius = float(input("Enter the radius of the cylinder: "))
                height = float(input("Enter the height of the cylinder: "))
                properties = EleganceMath.cylinder_properties(radius, height)
            elif choice == 4:
                radius = float(input("Enter the radius of the cone: "))
                height = float(input("Enter the height of the cone: "))
                properties = EleganceMath.cone_properties(radius, height)
            elif choice == 5:
                radius = float(input("Enter the radius of the sphere: "))
                properties = EleganceMath.sphere_properties(radius)
            elif choice == 6:
                radius = float(input("Enter the radius of the hemisphere: "))
                properties = EleganceMath.hemisphere_properties(radius)

            print("\nProperties of the selected shape:")
            print(f"Total Surface Area: {properties[0]}")
            print(f"Curved Surface Area: {properties[1]}")
            print(f"Volume: {properties[2]}")
        else:print("Invalid choice. Please choose a number between 1 and 6.")

if choice == 7:
     if __name__ == "__main__":
        try:
            print("this is the graph ")
            Plote_Graph()
           
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if choice == 8:
     if __name__ == "__main__":
        try:
            graph=np.random.normal(180,10,280)
            plt.hist(graph)
            plt.show()
           
        except ValueError:
            print("Invalid input. Please try again and enter a valid number. Thank you")
            
if choice == 9:
    print("Thank you for visting this program. :) ")
    exit()