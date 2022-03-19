# Made by Gareth Hogan
# Student Num: 20379616
# I have read and acknowledge the DCU Academic Integrity and Plagiarism Policy.

import sys
from CPU import *

def add(list, task):
    list.append(task)
    return list

def printavg(avg, algorithm):
    print('-------------------------------------------------------------------')
    print(f'Average turnaround time for {algorithm} scheduling is {avg:.2f} MS')
    print('-------------------------------------------------------------------')

def runschedule(schedule, cputime):
    total_turnaround = 0

    for task in schedule:
        cputime = run(task, cputime)
        total_turnaround += task.totaltime

    return total_turnaround
