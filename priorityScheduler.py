from graph import *
from middlePage import *
class Process:
    def __init__(self,pid,priority,burst_time,arrival_time):
        self.pid=pid
        self.priority=priority
        self.burst_time=burst_time
        self.arrival_time=arrival_time
        self.waiting=0
        self.tat=0

    def isProcessComplete(self):
        return self.burst_time==0

    def __str__(self):
        template = "Id = {}, priority = {}, waiting time = {}, turnaround time = {}"
        return template.format(self.pid, self.priority, self.waiting, self.tat)

# def allProcessCompleted(process_list):
#     for p in process_list:
#         if not p.isProcessComplete():
#             return False

def run_simulation(process_list):
    # time is the local reference to time
    seq_list=[]
    time = 0
    finished = 0
    while finished!=len(process_list):
        active_process=[]
        for p in process_list:
            if p.arrival_time <= time and (not p.isProcessComplete()):
                active_process.append(p)
        active_process.sort(key=lambda x: x.priority)
        if active_process[0].burst_time > 0:
            active_process[0].burst_time -= 1
            # print(active_process[0].pid, end=' ')
            seq_list.append(active_process[0].pid)
            if active_process[0].burst_time == 0:
                finished += 1
                active_process[0].tat = time+1
                print(active_process[0])

        for i in range(1, len(active_process)):
            active_process[i].waiting += 1

        time += 1
    return seq_list

def run(n=0,pid=[],priority=[],burst_time=[],arrival_time=[]):
    process_list = []
    # pid = list(map(int,input("id = ").split(',')))
    # priority = list(map(int, input("priority = ").split(',')))
    # burst_time = list(map(int, input("burst time = ").split(',')))
    # arrival_time = list(map(int, input("arrival time = ").split(',')))

    for i in range(0, n):
        process_list.append(Process(pid[i], priority[i], burst_time[i], arrival_time[i]))
    seq_list = run_simulation(process_list)
    draw(seq_list,process_list)

