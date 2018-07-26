#!/home/pyrax/anaconda3/bin/python
"""
Learning Series: Network Programmability basics
Module: Programming fundamentals
Lesson: Python lecture 2
Author: Joseph ngugi Muiruri

code2.py
Illustrate the following concepts:
-Reading from and writting to files
-The "with" statement
-Writting to command line
-Requesting interactive user input
"""

__author__ = "Ngugi Joseph"
__author__email__ = "joseph.ngugi@ditag.eu"
__copyright__ = "Python programming for Network Engineers"
__license__ = "MIT"

from datetime import datetime


log_file = "code2.log"


def read_log(log):
	"""
	Open the log file and print contents to the terminal
	"""
	with open(log, "r") as f:
		print(f.read())

def write_log(log, name):
	"""
	Add new log to the file
	"""
	#Get current date and time
	log_time = str(datetime.now())
	with open(log, "a") as f:
		f.writelines("Entry logged at {} by {}\n".format(log_time, name))

#Entry point for program
if __name__ == "__main__":
	#Get users name
	name = input("what is your name? ")


	#Add entry to the log file
	print("")
	print("Adding new log entry...")
	print("")
	print("Successfuly added!!!")
	write_log(log_file, name)
	print("")

	#Access starting log file
	print("Log file contents")
	print("=================")
	read_log(log_file)