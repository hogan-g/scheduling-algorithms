# Made by Gareth Hogan
# Student Num: 20379616
# I have read and acknowledge the DCU Academic Integrity and Plagiarism Policy.

import sys
import os

def error(message): # general error message to stop program gracefully
    print(f'Error Caught. Terminating Program\nError : {message}')
    sys.exit()

def checkfiletype(file):
    splitfile = file.split(".")
    if splitfile[1] != "txt":
        error("File given is not a txt file.")

def emptycheck(file):
    if os.stat(file).st_size == 0:
        error('File is empty')


def checkforfile(): # function to check if the file given to program actually exists
    try:
        schedulefile = sys.argv[1]
    except:
        error("No File Given!")
    finally:
        checkfiletype(schedulefile)
        emptycheck(schedulefile)
        return schedulefile


