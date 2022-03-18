import sys
from functions import *
from errorhandler import *
from task import *

def readandadd(file, list):
    try:
        with open(file) as f:
            for line in f:
                line = line.strip().split(", ") # split line into list of three things

                #setup task structure
                name = line[0]
                try:
                    priority = int(line[1])
                    burst = int(line[2])
                except ValueError:
                    #current Task has bad inputs, skip it and go to next
                    print(f"Bad Input in Task {name}, skipping it and moving on")
                    continue

                task = Task(name, priority, burst)

                #add task to list
                add(list, task)
    except:
        error("File does not exist.")
    
    return list
    

