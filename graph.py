import matplotlib.pyplot as plt

def plot(process_list):
    fig = plt.figure(figsize=(10,5))
    processIds = []
    waitingTime = []
    turnAround = []
    for i in process_list:
        processIds.append(i.pid)
        waitingTime.append(i.waiting)
        turnAround.append(i.tat)

    positions=[]
    position2=[]
    tick_pos=[]
    for i in range(len(process_list)):
        positions.append(i)
        position2.append(i+0.2)
        tick_pos.append(i+0.1)

    plt.bar(positions, waitingTime, width=0.2)
    plt.bar(position2, turnAround, width=0.2, color='g')
    plt.xticks(tick_pos, processIds)
    plt.show()
