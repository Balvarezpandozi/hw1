# hw1
COSC 4315 - Programming Languages and Paradigms - Homework 1

## Instructions:
    - The file can be called as specified on the pdf:
        >>  python3 freqnumber.py "k=<K_ELEMENTS_TO_OUTPUT>;input=<INPUT_FILE>;output=<OUTPUT_FILE>"  <<

## Specifications:
- The only sort algorithm used in this project was merge sort and its time complexity is O(n log n)
- No loops were used in any part of the code except for I/O operations
- Ties are handle as follows:
    > The program takes K most frequent elements and if there is a tie for the last k element. It will output all elements that have the same frequency. As an illustration of a tie:<br/>

    For illustration pusposes the integers from the file will be represented with quotes("19") and only integers will be shown. However, functionality for reals is the same:<br/>

    - We have the following frequencies:<br/>
    "19"    15<br/>
    "5"     10<br/>
    "8"     10<br/>
    "29"    15<br/>
    "0"     7<br/>

    > If the frequencies are tied the lowest integer will appear first<br/>
    - Example with k = 2:<br/>
    Output:<br/>
    "19"    15<br/>
    "29"    15<br/>

    > If there is a tie with the lowest frequencies, all of the tied elements are shown<br/>
    - Example with k = 3:<br/>
    "19"    15<br/>
    "29"    15<br/>
    "5"     10<br/>
    "8"     10<br/>

    > If k is greater than the amount of elements it will output them all:<br/>
    - Example with k = 8:<br/>
    "19"    15<br/>
    "29"    15<br/>
    "5"     10<br/>
    "8"     10<br/>
    "0"     7<br/>

## Concern about test cases:
__Test #3__, does output order matter not for frequencies but for the actual number, if it does what is the criteria decreasing or increasing? 

I solved this issue by sorting by the smallest integer first when the occurrences were tied.

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

__Test #4__, does output order matter not for frequencies but for the actual number, if it does what is the criteria decreasing or increasing?

I solved this issue by sorting by the smallest integer first when the occurrences were tied.

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
    