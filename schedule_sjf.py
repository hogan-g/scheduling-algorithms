import sys
from files import *
from lists import *
from task import *
from errorhandler import *
from CPU import *

cputime = 0
tasklist = [] # list with no real ordering just with all tasks
average_turnaround = 0

schedulefile = checkforfile()

readandadd(schedulefile, tasklist) #reads file and adds all task to list

schedule = sorted(tasklist, key=lambda x: x.burst) # list where tasks will be ordered in the way they need to be, for FCFS it is the same

for task in schedule:
    cputime = run(task, cputime)
    average_turnaround += task.totaltime

print(f'\nAverage turnaround time for SJF is {average_turnaround/len(schedule):.2f}')