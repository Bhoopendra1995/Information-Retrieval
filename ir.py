#!/usr/bin/python
import glob
from porter2stemmer import Porter2Stemmer
import pickle
from collections import defaultdict
global flag 
import string
import math
flag=0
invertextIndex={}
#fo= open("wordcount.text","wb")
#files= ['hindi-document-00001.txt','hindi-document-00002.txt','hindi-document-00003.txt']
files = list (glob.glob('files/*'))
length= len(files)
for doc in files :
	# print (doc)
	f = open(doc,"r").read()
	doc_id=doc
	c = f.find('<TITLE>') + len('<TITLE>')
	c1 = f.find('</TITLE>')
	con1 = f[c:c1]
	c = f.find('<TEXT>') + len('<TEXT>')
	c1 = f.find('</TEXT>')
	con2 = f[c:c1]
	con = con1 + con2
	exclude = set(string.punctuation)
	s = ''.join(ch for ch in con if ch not in exclude)
	text= s.split(" ")
	# print(text)
	stoplistTakenOut= []
	stopWorld= open('stop.txt',"r").read().split("\n")
	for j in text:
		if j not in stopWorld:
			stoplistTakenOut.append(j)
	#print(stoplistTakenOut)
	stemmer = Porter2Stemmer()
	stemDone = []
	for j in stoplistTakenOut:
		stemDone.append(stemmer.stem(j))
	#print(stemDone)
	l = set(stemDone)
	wordUnique = list(l)
	for i in range(len(wordUnique)):
		c=stemDone.count(str(wordUnique[i]))
		if flag != 0:
			if wordUnique[i] in invertextIndex.keys():
				invertextIndex[str(wordUnique[i])][doc_id] = c

			else:	
				invertextIndex[str(wordUnique[i])] = {}
				invertextIndex[str(wordUnique[i])][doc_id] = c

		else:
			invertextIndex[str(wordUnique[i])] = {}
			invertextIndex[str(wordUnique[i])][doc_id] = c
			flag = 1
qw={}			
file = open('ans1.txt', 'w')
for i in invertextIndex.keys():
	file.write(str(i) + '\t\t\t\t')
	file.write(str(invertextIndex.get(i)) + '\n')
file.close()
query= input("enter a query")
# d = defaultdict(int)
# for query in query.split():
#     d[query] += 1
quer = query.split()
for item in quer:
	if item in invertextIndex.keys():
		print(len(invertextIndex[item]))
		# print(length/(len(invertextIndex[item])))
		qw[query] = quer.count(item)*math.log((length/(len(invertextIndex[item]))))
print(qw)

dw = {}
for item in quer:
	for dc in invertextIndex[item].keys():
		dw[dc] = invertextIndex[item][dc] * math.log(length/(len(invertextIndex[item])))
print(dw)

