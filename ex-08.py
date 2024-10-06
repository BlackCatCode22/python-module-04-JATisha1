han = open('mbox-short.txt')

for line in han:
    line = line.rstrip()
    print('Line:', line)
    if line == '' :
        print('Skip Blank')
    wds = line.split()
    print('Words:' ,wds)
    if wds [0] != 'From' :
        print ('Ignore')
        continue
    print(wds[2])  