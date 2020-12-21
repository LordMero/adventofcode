from libs import read_file
from collections import Counter


group_list = read_file('input.txt')
#group_list = read_file('test.txt')

def parse_groups(group_list):
    
    groups, ans = [], []
    people = 0
    for k in range(len(group_list)):
        i = group_list[k]
        grp = {'people': 0, 'ans': 0, 'list': []}
        if len(i) == 0:
            grp['people'] = people
            grp['ans'] = len(set(ans))
            grp['list'] =  ans

            groups.append(grp)
            people = 0
            ans = []
            continue
        else:
            people += 1
            ans.extend([x for x in i])

        if k == len(group_list)-1:
            grp['people'] = people
            grp['ans'] = len(set(ans))
            grp['list'] =  ans
        
            groups.append(grp)
    return groups

groups = parse_groups(group_list)

print(groups)

s = 0
for g in groups:
    c = Counter(g['list'])
    print(c)
    for k,v in c.items():
        print(k, v)
        if v == g['people']:
            s += 1
print(s)
