# hw1
COSC 4315 - Programming Languages and Paradigms - Homework 1

## Instructions:
    - The file can be called as specified on the pdf:
        >>  python3 freqnumber.py "k=<K_ELEMENTS_TO_OUTPUT>;input=<INPUT_FILE>;output=<OUTPUT_FILE>"  <<

## Specifications:
- The only sort algorithm used in this project was merge sort and its time complexity is O(n log n)
- No loops were used in any part of the code except for I/O operations
- Ties are handle as follows:
    > The program takes K most frequent elements and if there is a tie for the last k element. It will output all elements that have the same frequency. As an illustration of a tie:
            For illustration pusposes instead of numbers words will be used:
            - We have the following frequencies:
            "int"       15
            "double"    10
            "while"     10
            "float"     15
            "for"       7
            - Example with k = 2:
            Output:
            "int"       15
            "float"     15
            - Example with k = 3:
            "int"       15
            "float"     15
            "double"    10
            "while"     10

## Concern about test cases:
__Test #3__, does output order matter not for frequyencies but for the actual number, if it does what is the criteria decreasing, increasing or what?
|My Output|Test Output|
|---------|-----------|
|integer: |  integer: |
|0 9      |  0 9      |
|3 4      |  3 4      |
|2 3      |  -101 3   |
|-101 3   |  2 3      |
|real:    |  real:    |
|3.3 4    |  3.3 4    |
|-3.3 3   |  -3.3 3   |
|-2.2 2   |  -2.2 2   |

__Test #4__, does output order matter not for frequyencies but for the actual number, if it does what is the criteria decreasing, increasing or what?
|My Output|Test Output|
|---------|-----------|
|integer: |  integer: |
|1 6      |  1 6      |
|2 4      |  2 4      |
|real:    |  real:    |
|9.5 3    |  9.5 3    |
|-1.1 2   |  -1.1 2   |
|0.3 1    |  0.2 1    |
|0.2 1    |  0.3 1    |

__Test #5__, tests outputs more elements than asked for even though the extra element does not tie with the first 3 mos frequent elements?
|My Output|Test Output|
|---------|-----------|
|integer: |  integer: |
|1234 5   |  1234 5   |
|1234567 4|  3 4      |
|3 4      |  1234567 4|
|real:    |  293 3    |
|0.5 4    |  real:    |
|2.3 3    |  0.5 4    |
|96.6896 2|  2.3 3    |
|     -   |  96.6896 2|







