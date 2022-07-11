def WaitingTime(process, n, burst, quantum):
    print('Process \t Burst Time \t\t Waiting Time')
    remainingBurst = [0]*n
    waitingTime = [0]*n

    for i in range(n):
        remainingBurst[i] = burst[i]
    t = 0

    while(1):
        done = True

        for i in range(n):
            if(remainingBurst[i] > 0):
                done = False

                if(remainingBurst[i] > quantum):
                    t = t+quantum
                    remainingBurst[i] = remainingBurst[i]-quantum

                else:
                    t = t+remainingBurst[i]
                    waitingTime[i] = t-waitingTime[i]
                    remainingBurst[i] = 0

            print(process[i], end='\t\t\t')
            print(burst[i], end='\t\t\t')
            print(waitingTime[i])

        if(done == True):
            break


process = [1, 2, 3]
n = 3
burst = [10, 5, 8]
quantum = 2
WaitingTime(process, n, burst, quantum)
