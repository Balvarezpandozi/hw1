# Imports
import sys
import re

# CONSTANTS
    # Used to classify each number from the input
INTEGER_NUM = 1
REAL_NUM = 2
INVALID_STRING = 0

# Lambda functions
    # Merge sort lambdas
get_middle = lambda x: x // 2
compare_less_or_equal = lambda x,y: x <= y
compare_greater = lambda x,y: x > y
compare_occurrences_greater_or_equal = lambda x,y: x[1] >= y[1]
compare_occurrences_less = lambda x,y: x[1] < y[1]
    # General purpose lambdas
compare_x_equals_y_minus_z = lambda x,y,z: x <= y+z
compare_x_greater_or_equal_to_y = lambda x, y: x >= y
compare_x_less_or_equal_to_1 = lambda x: x <= 1
compare_x_equals_y = lambda x,y: x == y
compare_x_equals_0 = lambda x: x == 0
compare_x_and_y_equal_0 = lambda x, y: x == 0 and y == 0
compare_is_x_less_than_2 = lambda x: x < 2
compare_x_equals_y_minus_1 = lambda x,y: x == (y-1)
    # Clasifying input lambdas
compare_is_x_dot = lambda x: x == '.'
compare_is_digit = lambda x: x >= '0' and x <= '9'
compare_is_x_minus_sign = lambda x: x == '-'
compare_is_x_integer = lambda x: x == INTEGER_NUM
compare_is_x_real = lambda x: x == REAL_NUM
compare_is_x_invalid = lambda x: x == INVALID_STRING
filter_data_by_type = lambda x,y: list(filter(lambda z: isinstance(z, x), y))
    # Frecuency count related lambdas
compare_is_frequency_equal_to_prev = lambda list, k, step: compare_x_equals_y(list[k+step][1], list[k+step-1][1])
compare_list_length_greater_k_plus_step = lambda list, k, step: len(list) > k+step
not_end_of_list_and_curr_and_prev_same_frequency = lambda list, k, step: compare_list_length_greater_k_plus_step(list, k, step) and compare_is_frequency_equal_to_prev(list, k, step)



# Main function
def main():
    ##INPUT##
        # Parse command line arguments
    try:
        arguments = sys.argv[1].split(';')
        k = int(arguments[0].split('=')[1])
        input_file = arguments[1].split('=')[1]
        output_file = arguments[2].split('=')[1]
    except:
        print("====================================================================================\n")
        print("Expected arguements to be the following format:\n")
        print("\"k=<K elements to output>;input=<Input File Name>;output=<Output File Name>.txt\"\n")
        print("Ex. python3 freqnumber.py \"k=3;input=input.txt;output=output.txt\"\n")
        print("Try running again using the format described.\n")
        print("====================================================================================\n")

        return
    
        # Read input file
    with open(input_file, 'r') as input_file:
        input_data = input_file.read()
        # Separate input file by commas, spaces, new lines
    input_data_list = re.split(",| |\n", input_data)
    # print("\nInput: " , input_data_list)
    ##/INPUT##

    ##PROCESS DATA##
        # Discard invalid strings and sorts all numbers
    filtered_and_sorted_input = filter_and_sort_input(input_data_list)
    # print("\nFiltered and sorted: " , filtered_and_sorted_input)
        # Get only integers
    integers = get_numbers_of_specific_type(filtered_and_sorted_input, INTEGER_NUM)
    # print("\nOnly integers: " , integers)
        # Count each integer occurrances
    integers_count = count_instances_of_all_elements(integers)
    # print("\nIntegers count: " , integers_count)
        # Sort integers by amount of occurrances
    sorted_integers_count = sort_by_occurrances(integers_count)
    # print("\nSorted integers count: " , sorted_integers_count)
        # Get k most repeated integers
    k_most_repeated_integers = get_most_repeated(sorted_integers_count, k)
    # print("\nK most repeated integers: " , k_most_repeated_integers)

        # Get only real numbers
    reals = get_numbers_of_specific_type(filtered_and_sorted_input, REAL_NUM)
    # print("\nOnly reals: " , reals)
        # Count each real occurrances
    reals_count = count_instances_of_all_elements(reals)
    # print("\nReals count: " , reals_count)
        # Sort reals by amount of occurrances
    sorted_reals_count = sort_by_occurrances(reals_count)
    # print("\nSorted reals count: " , sorted_reals_count)
        # Get k most repeated reals
    k_most_repeated_reals = get_most_repeated(sorted_reals_count, k)
    # print("\nK most repeated reals: " , k_most_repeated_reals)
    ##/PROCESS DATA##

    ##OUTPUT##
    output_results(k_most_repeated_integers, k_most_repeated_reals, output_file)
    ##/OUTPUT##

# Functions

# Discards invalid strings and sorts numbers through MERGE SORT. This way there is not list mutation and no loops are used.
def filter_and_sort_input(input_list):
    # Base case: the input_list is only 1 element
    if compare_x_less_or_equal_to_1(len(input_list)):
        # Find out if element is float, integer, or an invalid string
        valid_string_flag = get_string_type(input_list[0])
        # Case 1: invalid string
        if compare_x_equals_y(valid_string_flag, INVALID_STRING):
            return []

        # Case 2: integer
        elif compare_x_equals_y(valid_string_flag, INTEGER_NUM):
            list = [int(input_list[0])]
            return list

        # Case 3: floating point
        elif compare_x_equals_y(valid_string_flag, REAL_NUM):
            list = [float(input_list[0])]
            return list

    # Find middle of the array
    middle = get_middle(len(input_list))
    # Copy left half of the array and call recursion
    left = filter_and_sort_input(input_list[:middle])
    # Copy right half of the array and call recursion
    right = filter_and_sort_input(input_list[middle:])

    # Call merge to join the two arrays into a new one
    return merge_recursively(left, right)
     
# Merge arrays: loop through both arrays recursively and compare elements according to the comaprison arguments so that the function can adapt to the list it is receiving
def merge_recursively(left, right, left_index=0, right_index=0, sorted=None):
    # Base case: one of the arrays is empty
    if compare_x_equals_0(len(left)):
        return right
    elif compare_x_equals_0(len(right)):
        return left
    # Base case: both arrays are empty
    elif compare_x_and_y_equal_0(len(left), len(right)):
        return []
    
    # Base Cases
        # Reached end of left array
    if compare_x_equals_y(left_index, len(left)):
        return sorted + right[right_index:]
        
        # Reached end of right array
    elif compare_x_equals_y(right_index, len(right)):
        return sorted + left[left_index:]
    
    # Sorting
    if compare_less_or_equal(left[left_index], right[right_index]):
        if sorted != None:
            result = sorted.copy() + [left[left_index]]
        else:
            result = [left[left_index]]
        new_left_index = left_index + 1
        new_right_index = right_index
    elif compare_greater(left[left_index], right[right_index]):
        if sorted != None:
            result = sorted.copy() + [right[right_index]]
        else:
            result = [right[right_index]]
        new_left_index = left_index
        new_right_index = right_index + 1
    
    return merge_recursively(left, right, new_left_index, new_right_index, result)

# Returns 0 for invalid strings, 1 for integers, 2 for floats
    # Checks for a valid start of the string (a digit or a minus sign) then calls check_rest_of_string to validate the rest
def get_string_type(str):
    # Case 1: string is empty
    if compare_x_equals_0(len(str)):
        return 0

    # Case 1: first char is a number
    if compare_is_digit(str[0]):
        return check_rest_of_string(str)

    # Case 2: first char is a minus
    if compare_is_x_minus_sign(str[0]):
        # Case 2.1: the string is just a minus
        if compare_is_x_less_than_2(len(str)):
            return 0
        # Case 2.2: second char is a number
        if compare_is_digit(str[1]):
            return check_rest_of_string(str[1:])

        # Case 2.3: second char is not a number
        else:
            return 0
    
    # Case 3: first char is not a number nor a minus
    else:
        return 0

# Returns 0 for invalid strings, 1 for integers, 2 for floats
    # Recursively loops through the string to check if it is a valid number (integer or real number)
def check_rest_of_string(str, index=0, hasDot=False):
    if compare_is_digit(str[index]):
        if compare_x_equals_y_minus_1(index, len(str)):
            if hasDot:
                return 2
            else:
                return 1
        else:
            return check_rest_of_string(str, index+1, hasDot)
    elif compare_is_x_dot(str[index]):
        if hasDot:
            return 0
        return check_rest_of_string(str, index+1, True)
    else:
        return 0

# Filters list to return the specified type of values (integers or real numbers)
def get_numbers_of_specific_type(input_data, integers_or_real):
    if compare_is_x_integer(integers_or_real):
        comparing_type = int
    elif compare_is_x_real(integers_or_real):
        comparing_type = float
    
    filtered_data = filter_data_by_type(comparing_type, input_data)

    return filtered_data

# Loops recursively through a sorted list to count number of instances of every number. 
# Returns a 2-dimensional array where the first element is the number and the second element is the occurrences of said number
def count_instances_of_all_elements(list, index=0, counter=[]):
    # Base case: list is empty
    if compare_x_equals_0(len(list)):
        return []
    # Reached end of the list
    if compare_x_greater_or_equal_to_y(index, len(list)):
        return counter

    occurrances = count_instances(list, list[index])
    occurrances_counter = [list[index], occurrances]
    result = [occurrances_counter] + counter

    return count_instances_of_all_elements(list, index+occurrances, result)

# Counts the number of instances of a specific number in a list recursively
def count_instances(list, element, instances=0, index=0):
    # If the index is at the end of the list, return the current instances of the number
    if compare_x_equals_y(len(list), index):
        return instances

    # If the element is found, increment the create a new instances value to avoid mutation and call the function again
    if compare_x_equals_y(element, list[index]):
        new_instances = instances + 1
        return count_instances(list, element, new_instances, index+1)
    return count_instances(list,element, instances, index+1)

# Sorts 2-dimensional array in decreasing order by the frequency of each element
def sort_by_occurrances(list):
    # Base case: the input_list is only 1 element
    if compare_x_less_or_equal_to_1(len(list)):
            return list

    # Find middle of the array
    middle = get_middle(len(list))
    # Copy left half of the array and call recursion
    left = sort_by_occurrances(list[:middle])
    # Copy right half of the array and call recursion
    right = sort_by_occurrances(list[middle:])

    # Call merge to join the two arrays into a new one
    return merge_occurrences_recursively(left, right)

# Merge arrays: loop through both arrays recursively and compare elements according to their repetitions in case of tie compare the integer and retrieve the smallest first
def merge_occurrences_recursively(left, right, left_index=0, right_index=0, sorted=None):
    # Base case: one of the arrays is empty
    if (lambda x: x == 0)(len(left)):
        return right
    elif (lambda x: x == 0)(len(right)):
        return left
    # Base case: both arrays are empty
    elif (lambda x, y: x == 0 and y == 0)(len(left), len(right)):
        return []
    
    # Base Cases
        # Reached end of left array
    if compare_x_equals_y(left_index, len(left)):
        return sorted + right[right_index:]
        
        # Reached end of right array
    elif compare_x_equals_y(right_index, len(right)):
        return sorted + left[left_index:]
    
    # Sorting
    #if left occurrances is greater than right occurrances
    if (lambda x,y: x[1] > y[1])(left[left_index], right[right_index]):
        if sorted != None:
            result = sorted.copy() + [left[left_index]]
        else:
            result = [left[left_index]]
        new_left_index = left_index + 1
        new_right_index = right_index
        
    #if left occurrances is less than right occurrances
    elif (lambda x,y: x[1] < y[1])(left[left_index], right[right_index]):
        if sorted != None:
            result = sorted.copy() + [right[right_index]]
        else:
            result = [right[right_index]]
        new_left_index = left_index
        new_right_index = right_index + 1
    
    #if left and right occurrances are the same compare integers
    else:
        if (lambda x,y: x[0] > y[0])(left[left_index], right[right_index]):
            if sorted != None:
                result = sorted.copy() + [right[right_index]]
            else:
                result = [right[right_index]]
            new_left_index = left_index
            new_right_index = right_index + 1
        else:
            if sorted != None:
                result = sorted.copy() + [left[left_index]]
            else:
                result = [left[left_index]]
            new_left_index = left_index + 1
            new_right_index = right_index
    
    return merge_occurrences_recursively(left, right, new_left_index, new_right_index, result)

#Gets k most repeated elements from a two dimensional list where the second element is the number of occurrences
def get_most_repeated(list, k, step=0, most_repeated=[]):
    # Handling ties: grab k elements plus all ties of the lowest occurrances of the k elements
    
    #Base cases:
        #If list is less than k elements return the whole list
    if compare_x_greater_or_equal_to_y(k, len(list)):
        return list
        
        #If next index to check is out of bounds return current most repeated elements
    if compare_x_equals_y_minus_z(len(list), step, k):
        return most_repeated
    
    #If there are no current most repeated elements, add the first k elements to the list
    if compare_x_equals_0(len(most_repeated)):
        minimum_elements = list[:k]

    #Else, copy most repeated elements to a new variable minimum elemenets to avoid mutation
    else:
        minimum_elements = most_repeated.copy()
    
    # Check whether the last element added and the current element have the same frequency. If so, add the current element to the new most repeated list
    if  not_end_of_list_and_curr_and_prev_same_frequency(list, k, step):
        new_most_repeated = minimum_elements + [list[k+step]]
        #Call function again with the next index and the new most repeated elements
        return get_most_repeated(list, k, step+1, new_most_repeated)

    #If end of the list or the current and previous elements have different frequency return minimum elements
    else:
        return minimum_elements

#Outputs the results to a file  
def output_results(integers, reals, output_file_name):
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

if __name__ == '__main__':
    main()

