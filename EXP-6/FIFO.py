from queue import Queue

def pageFaults(page, n, frames):
    print('Incoming page \t Pages')
    s=set()
    queue=Queue()
    page_faults=0

    for i in range(n):
        if len(s)<frames:
            if page[i] not in s:
                s.add(page[i])
                page_faults=page_faults+1
                queue.put(page[i])
        else:
            if page[i] not in s:
                value=queue.queue[0]
                queue.get()
                s.remove(value)
                s.add(page[i])
                queue.put(page[i])
                page_faults=page_faults+1

        print(page[i], end='\t\t\t\t\t')
        for q_item in queue.queue:
            print(q_item, end='\t')

        print()    
    return page_faults 

page=[7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1]
n=len(page)
frames= 3
page_faults=pageFaults(page, n, frames)
hits=n-page_faults
print("\nNo: of page faults:"+str(page_faults))
print("No: of hits:"+str(hits))
