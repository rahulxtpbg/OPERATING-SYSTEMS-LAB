def PageFaults(page, n, frames):
    print('Incoming Page \t Pages')
    s = []
    page_faults = 0
    occurs = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    for i in range(n):
        if len(s) < frames:
            if page[i] not in s:
                s.append(page[i])
                page_faults = page_faults+1

        else:
            if page[i] not in s:
                for x in range(len(s)):
                    if s[x] not in page[i+1:]:
                        s[x] = page[i]
                        break
                    else:
                        occurs[x] = page[i+1:].index(s[x])
                else:
                    s[occurs.index(max(occurs))] = page[i]
            page_faults = page_faults+1

        print(page[i], end='\t\t\t\t\t')
        for i in range(len(s)):
            print(s[i], end='\t')

        print()
    return page_faults

page = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1]
n = len(page)
frames = 3
page_faults = PageFaults(page, n, frames)
hits = n-page_faults
print("\nNo: of page faults:"+str(page_faults))
print("No: of hits:"+str(hits))
