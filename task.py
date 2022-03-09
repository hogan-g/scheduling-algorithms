class Task(object):
    def __init__(self, name, priority, burst):
        self.name = name
        self.priority = priority
        self.burst = burst
        
        self.totaltime = 0
        self.timeleft = burst
        self.arrivaltime = None

        self.complete = False

    def __str__(self):
        return f'Task: {self.name}, Priority: {self.priority}, Burst: {self.burst}'
