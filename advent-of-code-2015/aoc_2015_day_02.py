"""Calculates amount of wrapping paper and ribbon required for 
the christmas presents."""

from os import path

# Specify the location of data here
# Leave blank to default to `input.txt`
input_file = "input.txt"


def import_data(file_name):
    """Imports and formats data from text file.

    Defaults to "input.txt" if no other path is specified.

    Line breaks are removed and each element is added to a list.
    
    """

    if path.exists(file_name):
        with open(file_name) as f:
            raw_data = f.read()
            input_data = raw_data.split("\n")
            return input_data

    # Handles blank or incorrect file path, defaults to input.txt
    else:
        print ("File not found \'" + file_name + "\', defaulting to \'input.txt\'")

        if path.exists(".\input.txt") == False:
            with open("input.txt", 'w') as f:
                print("Creating new file \'input.txt\' as file did not exist.")

        return import_data(".\input.txt")


def parse_numbers(input_string):
    """Separates each number from an input string and returns
    a sorted list.
    
    """

    separated_numbers = []
    split_string = input_string.split('x')

    for number in split_string:
        separated_numbers.append(int(number))

    separated_numbers.sort()

    return separated_numbers


def calculate_area(dimensions, type):
    """Calculates the total area of a cuboid when given a
    sorted list of the dimensions.

    If `type` "paper" or "ribbon" is passed, total area will include
    the area of extra provisioned material.
    
    """

    total = 0

    height = dimensions[0]
    width = dimensions[1]
    length = dimensions[2]

    small_area = height * width
    mid_area = height * length
    large_area = width * length
    
    if type == "paper":
        total = (3 * small_area) + (2 * mid_area) + (2 * large_area)
    
    elif type == "ribbon":
        volume = height * width * length
        total = volume + (2 * height) + (2 * width)

    return total


def calculate_result(file_path):
    """Calculates the total sum of paper and ribbon needed from
    a given data set.
    
    """
    
    shield = []
    wire = []

    data = import_data(file_path)

    # Handles empty files
    if len(data[0]) < 1:
        print ("No data found in \"input.txt\"")
        return None

    for item in data:
        shield.append(calculate_area(parse_numbers(item), "paper"))
        wire.append(calculate_area(parse_numbers(item), "ribbon"))
    
    total_paper = sum(shield)
    total_ribbon = sum(wire)

    print ("Total paper area:\n" + str(total_paper) + "\n")
    print ("Total ribbon area:\n" + str(total_ribbon) + "\n\n")

    return total_paper, total_ribbon


# Execute program
calculate_result (input_file)
