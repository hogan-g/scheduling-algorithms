import sys
from files import *
from lists import *
from task import *
from errorhandler import *
from CPU import *

time_quantum = 10
cputime = 0
tasklist = [] # list with no real ordering just with all tasks
average_turnaround = 0

schedulefile = checkforfile()

readandadd(schedulefile, tasklist) #reads file and adds all task to list
num_of_tasks = len(tasklist)

# list where tasks will be ordered in the way they need to be, for RR it starts as the same list, order changes in scheduler
schedule = tasklist

while schedule:
    cputime = run(schedule[0], cputime, time_quantum)
    average_turnaround += schedule[0].totaltime

    if schedule[0].complete: # if task is done remove from schedule
        removed_task = schedule.pop(0)
    else: # task has finished time quantum move to back of queue
        removed_task = schedule.pop(0)
        schedule.append(removed_task)


print(f'\nAverage turnaround time for Priority is {average_turnaround/num_of_tasks:.2f} MS')