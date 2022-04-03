import sys
from files import *
from functions import *
from task import *
from errorhandler import *
# Made by Gareth Hogan
# Student Num: 20379616
# I have read and acknowledge the DCU Academic Integrity and Plagiarism Policy.

from CPU import *

time_quantum = 10
cputime = 0
tasklist = [] # list with no real ordering just with all tasks
total_turnaround = 0

schedulefile = checkforfile()

readandadd(schedulefile, tasklist) #reads file and adds all task to list
num_of_tasks = len(tasklist)

# Create Schedule depending on algorithm
# list where tasks will be ordered in the way they need to be, for RR it starts as the same list, order changes while running
schedule = tasklist

while schedule: # while the schedule list is not empty, i.e. while tasks haven't finished yet
    cputime = run(schedule[0], cputime, time_quantum) # run task at front of list for time quantum, returns updated cpu time

    if schedule[0].complete: # if task is done remove from schedule
        total_turnaround += schedule[0].totaltime # add the total time for this finished task to total turnaround for scheduler
        removed_task = schedule.pop(0) # remove task object from list

    else: # task has finished time quantum move to back of queue
        removed_task = schedule.pop(0) # remove from list
        schedule.append(removed_task) # place at back of list

avg = total_turnaround/num_of_tasks
printavg(avg, "Round Robin ") # send to print avg function with label Round Robin