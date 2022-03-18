import sys
from files import *
from functions import *
from task import *
from errorhandler import *
from CPU import *

cputime = 0
tasklist = [] # list with no real ordering just with all tasks
total_turnaround = 0

schedulefile = checkforfile()

readandadd(schedulefile, tasklist) #reads file and adds all task to list

# Create Schedule depending on algorithm
# list where tasks will be ordered in the way they need to be, for Priority it is sorted by task.priority, reverse so highest is first
schedule = sorted(tasklist, key=lambda x: x.priority, reverse=True) 

total_turnaround = runschedule(schedule, cputime)

avg = total_turnaround/len(schedule)
printavg(avg, "Priority")
