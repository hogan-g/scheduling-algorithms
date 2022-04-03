# Made by Gareth Hogan
# Student Num: 20379616
# I have read and acknowledge the DCU Academic Integrity and Plagiarism Policy.

import sys
from CPU import *

def add(list, task): # adds task to given list
    list.append(task)
    return list # return updated list

def printavg(avg, algorithm): # fancy formatting for printing average
    print('-------------------------------------------------------------------')
    print(f'Average turnaround time for {algorithm} scheduling is {avg:.2f} MS')
    print('-------------------------------------------------------------------')

def runschedule(schedule, cputime): # runschedule runs the whole list of task objects, used for FCFS, SJF and Priority
    total_turnaround = 0

    for task in schedule: # for every task
        cputime = run(task, cputime) # run and then return cputime when finished
        total_turnaround += task.totaltime # add tasks total time to turnaround

    return total_turnaround
