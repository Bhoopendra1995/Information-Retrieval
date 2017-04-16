from collections import defaultdict
query= input()
d = defaultdict(int)
for query in query.split():
    d[query] += 1
newDict = {}
with open('ans1.txt', 'r') as f:
    for line in f:
        splitLine = line.split()
        newDict[string(splitLine[0])] = ",".join(splitLine[1:])
for item in query.split():
	if item in newDic:
		print(item)


		
