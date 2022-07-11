def Allocation(rSeq, head):
    seek_count = 0
    distance = 0
    curr_track = 0
    left = rSeq[0:2]
    llen = len(left)
    right = rSeq[3:8]
    rlen = len(right)

    for i in range(rlen):
        curr_track = right[i]
        distance = abs(curr_track-head)
        seek_count = seek_count+distance
        head = curr_track

    for i in range(llen):
        curr_track = left[i]
        distance = abs(curr_track-head)
        seek_count = seek_count+distance
        head = curr_track

    left.reverse()
    print('The seek sequence in the right direction is:')
    for i in range(rlen):
        print(right[i])
    for i in range(llen):
        print(left[i])


rSeq = [176, 79, 34, 60, 92, 11, 41, 114]
n = len(rSeq)
head = 50
Allocation(rSeq, head)
