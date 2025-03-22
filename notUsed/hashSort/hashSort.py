import re
nStr = ''
cnt = 0
get = 0
e = 0
f = open('BigMonster.txt')
lines = f.readlines()
f.close()
for i in range(len(lines)):
    nList = re.split(r'\W+', lines[i])
    print(re.findall('the', lines[i]))
for i in range(len(nList)):
    for c in range(len(nList[i])):
        for d in range(len(nList[i][c])):
            if cnt == 3:
                cnt = 0
                nStr = ''
                break
            nStr += nList[i][c][d]
            if nStr == 'the':
                get += 1
                print(get)
            cnt += 1
print(lines[0])