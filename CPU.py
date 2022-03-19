# Made by Gareth Hogan
# Student Num: 20379616
# I have read and acknowledge the DCU Academic Integrity and Plagiarism Policy.

from task import *

def run(task, cputime, timeslice=None):
    if timeslice is None:
        timeslice = task.burst
    if task.arrivaltime is None:
        task.arrivaltime = cputime
        task.totaltime = cputime


    if timeslice >= task.timeleft: #if process will be completed in this burst
        task.complete = True
        
        task.totaltime = (cputime + task.timeleft)

        cputime += task.timeleft

        print(f'Running Task: {task.name}, {task.priority}, {task.burst} for {task.timeleft} units.')
        print(f'Process {task.name} loaded onto CPU first at time {task.arrivaltime} and ran for {task.burst} MS total, it had a turn-around time of {cputime}')
        
    else:
        task.timeleft -= timeslice

        cputime += timeslice

        print(f'Running Task: {task.name}, {task.priority}, {task.burst} for {timeslice} units. Task has {task.timeleft}MS remaining.')

    return cputime
