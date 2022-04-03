# Made by Gareth Hogan
# Student Num: 20379616
# I have read and acknowledge the DCU Academic Integrity and Plagiarism Policy.

from task import *

def run(task, cputime, timeslice=None): # this is the function to run a single task, used in runschedule, and plainly in RR
    if timeslice is None: # this option is to seperate RR from the others, if no time quantum is given, run the whole burst
        timeslice = task.burst
    if task.arrivaltime is None: # if the arrival time hasn't been set, set is as current time, i.e. if first time task arrives to CPU
        task.arrivaltime = cputime 
        task.totaltime = cputime


    if timeslice >= task.timeleft: #if process will be completed in this burst
        task.complete = True # sets boolean value saying task complete
        
        task.totaltime = (cputime + task.timeleft) # adds the last bit of time to the tasks totaltime

        cputime += task.timeleft # set the cputime for when this task is done

        print(f'Running Task: {task.name}, {task.priority}, {task.burst} for {task.timeleft} units.')
        print(f'Process {task.name} loaded onto CPU first at time {task.arrivaltime} and ran for {task.burst} MS total, it had a turn-around time of {cputime}')
        
    else: # if task will not be completed in this burst on CPU
        task.timeleft -= timeslice # calculate time left for task

        cputime += timeslice # increment the cputime by how long timeslice is

        print(f'Running Task: {task.name}, {task.priority}, {task.burst} for {timeslice} units. Task has {task.timeleft}MS remaining.')

    return cputime # returns new cputime after running this task
