han = open('mbox-short.txt')

for line in han:
    line = line.rstrip()
    print('Line:', line)
    wds = line.split()
    print('Words:' ,wds)
    #guardian in a compound statement
    if len(wds) > 3 or wds[0] != 'From':
        continue
    if wds [0] != 'From' :
       # print ('Ignore')
        continue
    print(wds[2])  