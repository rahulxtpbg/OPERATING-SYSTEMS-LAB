def WaitingTime(process, n, burst):
    aJob = []
    turnAroundTime = [0]*n
    waitingTime = [0]*n
    print('Process \t Burst Time \t\t  Turnaround Time \t Waiting Time')

    for i in range(n):
        t = min(burst)
        turnAroundTime[i] = turnAroundTime[i-1]+t
        waitingTime[i] = turnAroundTime[i]-t
        aJob.append(t)
        burst.remove(t)

    for i in range(n):
        print(process[i], end='\t\t\t')
        print(aJob[i], end='\t\t\t')
        print(turnAroundTime[i], end='\t\t\t')
        print(waitingTime[i])

process = [1, 2, 3]
n = 3
burst = [10, 5, 8]
burstDuplicate = [10, 5, 8]
WaitingTime(process, n, burst)
