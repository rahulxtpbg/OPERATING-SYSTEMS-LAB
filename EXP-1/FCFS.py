def WaitingTime(process, n, burst):
    print('Process \t Burst Time \t\t Turnaround Time \t\t Waiting Time')
    turnAroundTime = [0]*n
    waitingTime = [0]*n

    for i in range(n):
        t = burst[i]
        turnAroundTime[i] = turnAroundTime[i-1]+t
        waitingTime[i] = turnAroundTime[i]-t

    for i in range(n):
        print(process[i], end='\t\t\t')
        print(burst[i], end='\t\t\t')
        print(turnAroundTime[i], end='\t\t\t')
        print(waitingTime[i])

process = [1, 2, 3]
n = 3
burst = [10, 5, 8]
WaitingTime(process, n, burst)
