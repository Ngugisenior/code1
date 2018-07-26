#!/home/pyrax/anaconda3/bin/python
"""
Lesson Series: Network Programmability
Module: programming fundamentals
Lesson: python part 1
Author: Joseph Ngugi Muiruri <joseph.ngugi@ditag.eu>


code1.py
illustrate the following concepts:
-script structure and format
-importing and using packages
-variable declaration and usage
-function creation and usage
-Basic error handling
"""

_author_ ="Joseph Ngugi Muiruri"
_author_email_ ="joseph.ngugi@ditag.eu"
_copyright_ = "Python programming for Network engineers"
_license_ = "MIT"

import sys


def doubler(number):
    """
    Given a number, double it and return the value
    """
    result = number*2
    return result

#Entry of the program
if __name__ == '__main__':
    #Retrieve the line input
    try:
        input = float(sys.argv[1])
    except(IndexError, ValueError) as e:
        #Indicates no command line parameters was provided
        print("you must provide a number as a parameter to this script")
        print("example: ")
        print("code1.py 12")
        sys.exit(1)

    #double the provided number and print out
    answer = doubler(input)
    print(answer)
