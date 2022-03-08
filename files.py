import sys
from lists import *
from task import *

def readandadd(file, list):
    with open(file) as f:
        for line in f:
            line = line.strip().split(", ") # split line into list of three things

            #setup task structure
            name = line[0]
            priority = int(line[1])
            burst = int(line[2])
            task = Task(name, priority, burst)

            #add task to list
            add(list, task)

    return list
    

