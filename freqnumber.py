# Imports
import sys
import re

# CONSTANTS
    # Used to classify each number in the input
INTEGER_NUM = 1
REAL_NUM = 2
INVALID_STRING = 0


# Main function
def main():

    ##INPUT##
        # Parse command line arguments
    arguments = sys.argv[1].split(';')
    k = int(arguments[0].split('=')[1])
    input_file = arguments[1].split('=')[1]
    output_file = arguments[2].split('=')[1]
        # Read input file
    with open(input_file, 'r') as input_file:
        input_data = input_file.read()
        # Separate input file by commas, spaces, new lines (maybe more this is not specified. Ask TAs or in class)
    input_data_list = re.split(",| |\n", input_data)
    ##/INPUT##

    ##PROCESS DATA##
        # Discard invalid strings and sorts all numbers
    sorted_and_processed_input = filter_and_sort_input(input_data_list)
        # Get only integers
    integers = get_specific_type(sorted_and_processed_input, INTEGER_NUM)
        # Count each integer occurrances
    integers_count = count_instances_of_all_elements(integers)
        # Get only real numbers
    reals = get_specific_type(sorted_and_processed_input, REAL_NUM)
        # Count each real occurrances
    reals_count = count_instances_of_all_elements(reals)
    ##/PROCESS DATA##

    ##OUTPUT##
    output_results(integers_count, reals_count, output_file, k)
    ##/OUTPUT##

# Functions

# Discards invalid strings and sorts numbers (Merge sort creating different lists in every recursion)
def filter_and_sort_input(input_list):
    # Base case: the input_list is only 1 element
    if (lambda x: x <= 1)(len(input_list)):
        # Find out if element is float, integer, or an invalid string
        valid_string_flag = get_string_type(input_list[0])

        # Case 1: invalid string
        if (lambda x,y: x == y)(valid_string_flag, INVALID_STRING):
            return []

        # Case 2: integer
        elif (lambda x,y: x == y)(valid_string_flag, INTEGER_NUM):
            array = [int(input_list[0])]
            return array

        # Case 3: floating point
        elif (lambda x,y: x == y)(valid_string_flag, REAL_NUM):
            array = [float(input_list[0])]
            return array

    # Find middle of the array
    get_middle = lambda x: x // 2
    middle = get_middle(len(input_list))
    # Copy left half of the array and call recursion
    left = filter_and_sort_input(input_list[:middle])
    # Copy right half of the array and call recursion
    right = filter_and_sort_input(input_list[middle:])

    # Call merge to join the two arrays into a new one
    return merge(left, right)

# Merges and sorts two arrays
def merge(left, right):
    # Base case: one of the arrays is empty
    if (lambda x: x == 0)(len(left)):
        return right
    elif (lambda x: x == 0)(len(right)):
        return left
    # Base case: both arrays are empty
    elif (lambda x, y: x == 0 and y == 0)(len(left), len(right)):
        return []

    # Loop through both arrays recursively and compare elements
    # (lambda x,y: merge_recursively(x, y))(left, right) Should I call it like this?  
    return merge_recursively(left, right)
     

def merge_recursively(left, right, left_index=0, right_index=0, sorted=None):
    is_x_equal_to_y = lambda x,y: x == y
    
    # Base Cases
    if is_x_equal_to_y(left_index, len(left)):
        return sorted + right[right_index:]
    elif is_x_equal_to_y(right_index, len(right)):
        return sorted + left[left_index:]
    
    if (lambda x,y: x <= y)(left[left_index], right[right_index]):
        if sorted != None:
            result = sorted.copy() + [left[left_index]]
        else:
            result = [left[left_index]]
        new_left_index = left_index + 1
        new_right_index = right_index
    elif (lambda x,y: x > y)(left[left_index], right[right_index]):
        if sorted != None:
            result = sorted.copy() + [right[right_index]]
        else:
            result = [right[right_index]]
        new_left_index = left_index
        new_right_index = right_index + 1
    
    return merge_recursively(left, right, new_left_index, new_right_index, result)

# Returns 0 for invalid strings, 1 for integers, 2 for floats
    # Checks for a valid start of the string then calls check_rest_of_string to validate the rest
def get_string_type(str):
    # Case 1: string is empty
    if (lambda x,y: x == y)(0, len(str)):
        return 0

    # Case 1: first char is a number
    if (lambda x: x >= '0' and x <= '9')(str[0]):
        return check_rest_of_string(str)

    # Case 2: first char is a minus
    if (lambda x: x == '-')(str[0]):
        # Case 2.1: the string is just a minus
        if (lambda x: x < 2)(len(str)):
            return 0
        # Case 2.2: second char is a number
        if (lambda x: x >= '0' and x <= '9')(str[1]):
            return check_rest_of_string(str[1:])

        # Case 2.3: second char is not a number
        else:
            return 0
    
    # Case 3: first char is not a number nor a minus
    else:
        return 0

# Returns 0 for invalid strings, 1 for integers, 2 for floats
    # Recursively loops through the string to check if it is a valid number
def check_rest_of_string(str, index=0, hasDot=False):
    if (lambda x: x >= '0' and x <= '9')(str[index]):
        if (lambda x,y: x == (len(str)-1))(index, len(str)):
            if hasDot:
                return 2
            else:
                return 1
        else:
            return check_rest_of_string(str, index+1, hasDot)
    elif (lambda x: x == '.')(str[index]):
        if hasDot:
            return 0
        return check_rest_of_string(str, index+1, True)
    else:
        return 0

# Returns a list of integers or floats
def get_specific_type(input_data, integers_or_real):
    if (lambda x: x == INTEGER_NUM)(integers_or_real):
        comparing_type = int
    elif (lambda x: x == REAL_NUM)(integers_or_real):
        comparing_type = float
    
    filtered_data = list(filter(lambda x: isinstance(x, comparing_type), input_data))

    return filtered_data

# Loops through a sorted list to count number of instances of every number
def count_instances_of_all_elements(list, index=0, counter=[]):
    # Base case: list is empty
    if (lambda x: x == 0)(len(list)):
        return []
    # Reached end of the list
    if (lambda x,y: x >= y)(index, len(list)):
        return counter

    occurrances = count_instances(list, list[index])
    occurrances_counter = [list[index], occurrances]
    result = [occurrances_counter] + counter

    return count_instances_of_all_elements(list, index+occurrances, result)

# Counts the number of instances of a specific number in a list recursively
def count_instances(list, element, instances=0, index=0):
    if (lambda x,y: x==y)(len(list), index):
        return instances
    if (lambda x,y: x==y)(element, list[index]):
        new_instances = instances + 1
        return count_instances(list, element, new_instances, index+1)
    return count_instances(list,element, instances, index+1)

def output_results(integers, reals, output_file_name, k):
    # Write output to file
    with open(output_file_name, 'w') as output_file:
        output_file.write("integer:\n")
        for number, occurrances in integers:
            output = str(number) + " " + str(occurrances)
            output_file.write(output + "\n")
        output_file.write("real:\n")
        for number, occurrances in reals:
            output = str(number) + " " + str(occurrances)
            output_file.write(output + "\n")
    return None

if __name__ == '__main__':
    main()

