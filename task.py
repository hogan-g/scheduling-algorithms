# Made by Gareth Hogan
# Student Num: 20379616
# I have read and acknowledge the DCU Academic Integrity and Plagiarism Policy.

class Task(object): # class to store a task
    def __init__(self, name, priority, burst):
        self.name = name
        self.priority = priority
        self.burst = burst
        
        self.totaltime = 0 # total time for task to complete
        self.timeleft = burst # timeleft is initially burst
        self.arrivaltime = None # don't know what time it arrives yet

        self.complete = False # default it task is not complete

    def __str__(self):
        return f'Task: {self.name}, Priority: {self.priority}, Burst: {self.burst}'
