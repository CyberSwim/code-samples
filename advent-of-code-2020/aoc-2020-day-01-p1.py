# ADVENT OF CODE 2020 DAY 1
# Find the two entries that sum to 2020; what do you get if you multiply them together?

# Open file stream (assumes input.txt is in the same folder as script)
inputfile = open("input.txt").readlines()

# Converts each number from file into int and adds to list
numbers = []
for item in inputfile:
    numbers.append (int(item))

numbers.sort()

# Search for answers
def numberFinder (number_list, target_sum):
    
    # will remove previously searched values without modifying list
    search_adjustment = 0

    # loops through the list
    for number in number_list:

        # the number we are looking for; number + target number = 2020
        target_number = target_sum - number
        
        # initialise search properties
        low_value = 0 + search_adjustment
        high_value = len(number_list) - 1
        mid_value = int((low_value + high_value) / 2)

        # binary search
        while (low_value <= high_value):
            test_number = number_list[mid_value]

            if (test_number == target_number):
                return [number, test_number]

            if (test_number > target_number):
                high_value = mid_value
                mid_value = int((low_value + mid_value) / 2)

            if (test_number < target_number):
                low_value = mid_value
                mid_value = int((mid_value + high_value) / 2)

            # break out of loop if we cannot find the target number
            if (low_value == mid_value or mid_value == high_value):
                search_adjustment += 1
                low_value = high_value + 1
    
    return "null"



    
part_one_result = numberFinder(numbers, int(2020))

for number in numbers:
    part_two_result = numberFinder(numbers, (2020 - number))
    if (part_two_result == "null"):
        continue
    else:
        part_two_result.append(number)
        break


print ("Part One\nNumbers: " + str(part_one_result))
print ("Final Answer: " + str(part_one_result[0] * part_one_result[1]))
print ("Part Two\nNumbers: " + str(part_two_result))
print ("Final Answer: " + str(part_two_result[0] * part_two_result[1] * part_two_result [2]))
