from task import *

def run(task, cputime, timeslice=None):
    if timeslice is None:
        timeslice = task.burst
    if task.arrivaltime is None:
        task.arrivaltime = cputime
        task.totaltime = cputime

    task.totaltime += timeslice

    if timeslice >= task.timeleft: #if process will be completed in this burst
        print(f'Running Task: {task.name}, {task.priority}, {task.burst} for {timeslice} units.')
        print(f'Process {task.name} arrived at time {task.arrivaltime} and ran for {task.burst} MS. it had a turn-around time of {task.totaltime}')
    else:
        print(f'Running Task: {task.name}, {task.priority}, {task.burst} for {timeslice} units. Task has {task.timeleft}MS remaining.')
    
    cputime += timeslice
    return cputime
