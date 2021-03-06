def find_row(bp):
    u = 128
    d = 0
     
    for i in range(7):
       r = (u-d)//2
       if bp[i] == 'F':
          u = d +r
       else:
          d = u - r
       print(bp[i], d, u)
    return d

def find_col(bp):
    u = 8
    d = 0
    bp = bp[-3:]
    for i in range(3):
       r = (u-d)//2
       if bp[i] == 'L':
          u = d +r
       else:
          d = u - r
       print(bp[i], d, u)
    return d

with open('input.txt') as f: 
    bps = f.read().splitlines()

    ids = []
    for bp in bps:
        row = find_row(bp)
        col = find_col(bp)
        ids.append(row*8 +  col)
    
    sorted_ids = sorted(ids, reverse=True)

    test = []
    for i in range(len(ids)-1):
        test.append(sorted_ids[i]-sorted_ids[i+1])
    inx = test.index(2)

    print(sorted_ids[inx-2:inx+2])
