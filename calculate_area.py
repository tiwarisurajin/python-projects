

# rectanglw and triangle
import turtle
def calculate_area(shape= "triangle" ,*args) :
    if shape == "triangle" or shape ==  "" :
        base_input =int(input("Enter the base: "))
        height_input = int(input("Enter the height: "))
        area_of_triangle = (1/2)*base_input  * height_input
        print(f"Area of triangle is {area_of_triangle}.")
    elif shape == "rectangle" :
         length = int(input("Enter the base: "))
         breadth = int(input("Enter the height: "))
         area_of_rectangle = (1/2)*base_input  * height_input
         print(f"Area of rectangle is {area_of_rectangle}.")
    


calculate_area() 

