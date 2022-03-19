# Made by Gareth Hogan
# Student Num: 20379616
# I have read and acknowledge the DCU Academic Integrity and Plagiarism Policy.

import sys

def error(message):
    print(f'Error Caught. Terminating Program\nError : {message}')
    sys.exit()

def checkforfile():
    try:
        schedulefile = sys.argv[1]
        return schedulefile
    except:
        error("No File Given!")