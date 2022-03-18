import sys
from files import *
from functions import *
from task import *
from errorhandler import *
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

while schedule:
    cputime = run(schedule[0], cputime, time_quantum)

    if schedule[0].complete: # if task is done remove from schedule
        total_turnaround += schedule[0].totaltime
        removed_task = schedule.pop(0)

    else: # task has finished time quantum move to back of queue
        removed_task = schedule.pop(0)
        schedule.append(removed_task)

avg = total_turnaround/num_of_tasks
printavg(avg, "Priority")