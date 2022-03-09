from task import *

def run(task, cputime, timeslice=None):
    if timeslice is None:
        timeslice = task.burst
    if task.arrivaltime is None:
        task.arrivaltime = cputime
        task.totaltime = cputime

    cputime += timeslice

    if timeslice >= task.timeleft: #if process will be completed in this burst
        task.complete = True
        print(f'Running Task: {task.name}, {task.priority}, {task.burst} for {timeslice} units.')
        print(f'Process {task.name} loaded onto CPU first at time {task.arrivaltime} and ran for {task.burst} MS total, it had a turn-around time of {cputime}')
    else:
        task.timeleft -= timeslice
        print(f'Running Task: {task.name}, {task.priority}, {task.burst} for {timeslice} units. Task has {task.timeleft}MS remaining.')
    
    return cputime
