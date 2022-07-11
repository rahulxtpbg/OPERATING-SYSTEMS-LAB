def Allocation(rSeq, head):
    seek_count = 0
    distance = 0
    curr_track = 0

    for i in range(n):
        curr_track = rSeq[i]
        distance = abs(curr_track-head)
        seek_count = seek_count+distance
        head = curr_track

    print('The seek sequence is:')
    for i in range(n):
        print(rSeq[i])


rSeq = [176, 79, 34, 60, 92, 11, 41, 114]
n = len(rSeq)
head = 50
Allocation(rSeq, head)
