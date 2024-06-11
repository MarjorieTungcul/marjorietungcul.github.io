# These are the functions for calculating the area of each shape.
def area_of_the_square(side_length):
    return side_length ** 2

def area_of_the_rectangle(length, width):
    return length * width

def area_of_the_triangle(base, height):
    return (1 / 2) * base * height

def area_of_the_trapezoid(base1, base2, height):
    return (1 / 2) * (base1 + base2) * height

def area_of_the_hexagon(side_length):
    return (3 * (3 ** 0.5)) * (1 / 2) * (side_length ** 2)

def area_of_the_octagon(side_length):
    return 2 * (1 + (2 ** 0.5)) * (side_length ** 2)

def area_of_the_circle(radius):
    pi = 3.141592653589793
    return (pi) * (radius ** 2)

# This is the function for displaying a menu that includes options for each shape, allowing the user to select the shape for which they want to calculate the area.
def printShapes(*shapes):
    print("""Here are the shapes that you can calculate its area by using this calculator:""")
    i = 1
    for name in shapes:
        print(f"{i}. {name}")
        i += 1

# This is the function that handles the cases where the user enters invalid values.
def print_Error_Message(name):
    print(f"""Error: The {name} cannot be a negative number or zero. Please enter a valid number.
▢ ===========▭ ===========△ ===========⏢ ===========⬡ ===========🛑 ===========◯ ==========""")

# This is the function that handles the user input and calculates the area for the chosen shape .
def calculating_the_shape_area():
    # This tests a block of code for errors. If the user inputted the needed data correctly, then those block of codes here will run.
    try:
        # This is a divider that separates every section of the program to have an organized and readable output.
        print("▢ ===========▭ ===========△ ===========⏢ ===========⬡ ===========🛑 ===========◯ ==========")

        # The user is prompt to input the number corresponding to the shape they want to calculate.
        chosen_shape_number = int(
            input("Enter the number of the shape you want to calculate its area (1/2/3/4/5/6/7): "))

        # Initialization of variables for measurements.
        side_length, length, width, base, height, base1, base2, radius = 0, 0, 0, 0, 0, 0, 0, 0

        # This is the list of shape names.
        chosen_shape_name = ( "Square ▢", "Rectangle ▭", "Triangle △", "Trapezoid ⏢", "Hexagon ⬡", "Octagon 🛑", "Circle ◯")

        # This checks if the number of the chosen shape is within the valid range.
        if 1 <= chosen_shape_number <= 7:

            # This checks if the chosen shape number is 1, 5, 6.
            if chosen_shape_number in [1, 5, 6]:

                # This is the loop that executes until a valid side length is provided.
                while True:

                    # The user is prompt to input the measurement of the side length of the specific shape.
                    side_length = float(input(f"Enter the side length of the {chosen_shape_name[chosen_shape_number - 1]} in cm: "))

                    # This checks if the side length is less than or equal to 0.
                    if side_length <= 0:

                        # This function prints the error message for an invalid side length.
                        print_Error_Message("side length")

                    else:
                        # These calculates the area based on the chosen shape number and side length.
                        if chosen_shape_number == 1:
                            area = area_of_the_square(side_length)
                            break
                        elif chosen_shape_number == 5:
                            area = area_of_the_hexagon(side_length)
                            break
                        else:
                            area = area_of_the_octagon(side_length)
                            break

            # This checks if the chosen number is 2.
            elif chosen_shape_number == 2:

                # This is the loop that executes until a valid length and width are provided.
                while True:

                    # The user is prompt to input the measurement of the length of the specific shape.
                    length = float(input(f"Enter the length of the {chosen_shape_name[1]} in cm: "))

                    # This checks if the length is greater than 0.
                    if length > 0:

                        # The user is prompt to input the measurement of the width of the specific shape.
                        width = float(input(f"Enter the width of the {chosen_shape_name[1]} in cm: "))

                        # This checks if the width is greater than 0.
                        if width > 0:

                            # This calculates the area of the rectangle.
                            area = area_of_the_rectangle(length, width)
                            break

                        else:
                            # This function prints the error message for an invalid width.
                            print_Error_Message("width")
                    else:
                        # This function prints the error message for an invalid length.
                        print_Error_Message("length")

            # This checks if the chosen shape number is 3.
            elif chosen_shape_number == 3:

                # This is the loop that executes until a valid base, and height  are provided.
                while True:

                    # The user is prompt to input the measurement of the base of the specific shape.
                    base = float(input(f"Enter the base of the {chosen_shape_name[2]} in cm: "))

                    # This checks if the base is greater than 0.
                    if base > 0:

                        # The user is prompt to input the measurement of the height of the specific shape.
                        height = float(input(f"Enter the height of the {chosen_shape_name[2]} in cm: "))

                        # This checks if the height is greater than 0.
                        if height > 0:

                            # This calculates the area of the triangle.
                            area = area_of_the_triangle(base, height)
                            break

                        else:
                            # This function prints the error message for an invalid height.
                            print_Error_Message("height")
                    else:
                        # This function prints the error message for an invalid base.
                        print_Error_Message("base")

            # This checks if the chosen shape number is 4.
            elif chosen_shape_number == 4:

                # This is the loop that executes until a valid base 1, base 2, and height  are provided.
                while True:

                    # The user is prompt to input the measurement of the base 1 of the specific shape.
                    base1 = float(input(f"Enter the base 1 of the {chosen_shape_name[3]} in cm: "))

                    # This checks if the base1 is greater than 0.
                    if base1 > 0:

                        # The user is prompt to input the measurement of the base 2 of the specific shape.
                        base2 = float(input(f"Enter the base 2 of the {chosen_shape_name[3]} in cm: "))

                        # This checks if the base 2 is greater than zero.
                        if base2 > 0:

                            # The user is prompt to input the measurement of the hegith of the specific shape.
                            height = float(input(f"Enter the height of the {chosen_shape_name[3]} in cm: "))

                            # This checks if the height is greater than zero.
                            if height > 0:

                                # This calculates the area of the trapezoid.
                                area = area_of_the_trapezoid(base1, base2, height)
                                break

                            else:
                                # This function prints the error message for an invalid height.
                                print_Error_Message("height")
                        else:
                            # This function prints the error message for an invalid base 2.
                            print_Error_Message("base 2")
                    else:
                        # This function prints the error message for an invalid base 1.
                        print_Error_Message("base 1")

            # This checks if the chosen shape number is 7.
            elif chosen_shape_number == 7:

                # This is the loop that executes until a valid radius is provided.
                while True:

                    # The user is prompt to input the measurement of the radius of the specific shape.
                    radius = float(input(f"Enter the radius of the {chosen_shape_name[6]} in cm: "))

                    # This checks if the radius is greater than 0.
                    if radius > 0:

                        # This calculates the area of the circle.
                        area = area_of_the_circle(radius)
                        break

                    else:
                        # This function prints the error message for an invalid radius.
                        print_Error_Message("radius")

            # This displays the calculated area with the chosen shape name.
            print(f"The area of the {chosen_shape_name[chosen_shape_number - 1]} is {area:.2f} cm².")
            print("▢ ===========▭ ===========△ ===========⏢ ===========⬡ ===========🛑 ===========◯ ==========")
        else:
            # In the lines 61 and 62, it handles invalid input number and repeatedly call the function for another attempt.
            print("Invalid input number.Please enter a valid number.")
            calculating_the_shape_area()

    # This handles the error. If the user inputted the needed data incorrectly (e.g. characters), then this will run.
    except ValueError:
        print("""Invalid Input. Please enter a number.
▢ ===========▭ ===========△ ===========⏢ ===========⬡ ===========🛑 ===========◯ ==========""")

# This displays a header for the Shape Area Calculator, and providing clear instructions for the user.
print("""===================================Shape Area Calculator===================================    

▢ ===========▭ ===========△ ===========⏢ ===========⬡ ===========🛑 ===========◯ ==========
In this calculator, you can easily calculate the area of the given shape by only inputting
the exact measurement of its side length, base, height, etc. 
▢ ===========▭ ===========△ ===========⏢ ===========⬡ ===========🛑 ===========◯ ==========""")

# This initializes a variable to control the continuation of the calculation loop.
continue_calculation = True

# This executes the calculation loop as long as the user chooses to continue.
while continue_calculation:

    # This displays a menu of shapes for the user to choose from.
    printShapes("Square ▢", "Rectangle ▭", "Triangle △", "Trapezoid ⏢", "Hexagon ⬡", "Octagon 🛑", "Circle ◯")

    # This calls the function for calculating the area of the chosen shape.
    calculating_the_shape_area()

    # The user is prompt to decide whether to try again or exit the program.
    while True:
        question = input("Do you want to try again?(Yes / No):")
        if question == "Yes":
            # This breaks out the inner loop to restart the calculation.
            print("▢ ===========▭ ===========△ ===========⏢ ===========⬡ ===========🛑 ===========◯ ==========")
            break

        elif question == "No":
            # This exits the program and display a closing message.
            print("▢ ===========▭ ===========△ ===========⏢ ===========⬡ ===========🛑 ===========◯ ==========")
            print("Thank you for using this Shape Area Calculator!")
            continue_calculation = False
            break

        else:
            # This handles invalid input and the user is prompt to enter Yes or No only.
            print("Invalid input. Please enter Yes or No only. ")
            print("▢ ===========▭ ===========△ ===========⏢ ===========⬡ ===========🛑 ===========◯ ==========")


