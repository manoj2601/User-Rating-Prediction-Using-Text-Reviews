import json
import sys
import numpy as np
import re
import math
import utils
from collections import Counter
from sklearn.metrics import confusion_matrix
import seaborn as sn
import pandas as pd
import matplotlib.pyplot as plt

def printDict(theta):
	for item in theta:
		if(theta[item] != [0,0,0,0,0]):
			print(f"{item} : {theta[item]}")

f = open(sys.argv[1],)

train = []
line = f.readline()
while line:
	train.append(json.loads(line))
	line = f.readline()
f.close()

phi = [0.0, 0.0, 0.0, 0.0, 0.0]
total = len(train)
for i in range(0,len(train)):
	line = train[i]
	# str1 = utils.getStemmedDocuments(line['text'], False)
	# a = 'text'
	# line.update(a = str1)
	# train[i] = line
	phi[int(line['stars'])-1]+=1.0

for i in range(0,5):
	phi[i] = phi[i]/total

training_dictionary = set([])
print("Feature is : Bigrams with stemming")

totalWordPerClass = [0,0,0,0,0]
for i in range(0, len(train)):
	words = re.split("[.(), \-!?:\n\\*']+", train[i]['text'])
	stri = ""
	for word in words:
		stri += word+" "
	nwords = utils.getStemmedDocuments(stri, True)
	words = nwords
	nwords = []
	j=0
	while(j<len(words)):
		if(j != len(words)-1):
			nwords.append(words[j]+words[j+1])
		else:
			nwords.append(words[j])
		j+=1
	words = nwords
	train[i]['text'] = words
	i = int(train[i]['stars'])-1
	for word in words:
		totalWordPerClass[i]+=1
		training_dictionary.add(word)

print("Parameters for naive bayes:")
print("Phi : ", phi)
print("size of the training_dictionary: ", len(training_dictionary))
print("calculating theta")

theta = {}

for word in training_dictionary:
	val = [0.0, 0.0, 0.0, 0.0, 0.0]
	theta[word] = val

for line in train:
	words = line['text']
	fd = Counter(words).most_common()
	index = int(line['stars']-1)
	for (a,b) in fd:
		arr = theta[a]
		arr[index]+=b
		theta.update(a = arr)

for item in theta:
	arr = theta[item]
	for i in range(0, 5):
		arr[i] = (arr[i]+1)/(totalWordPerClass[i]+len(training_dictionary))
	theta.update(item=arr)

print("All Parameters calculated")
print("Testing on test data with stemming and stopwords removing")

f = open(sys.argv[2],)

test = []
line = f.readline()
while line:
	test.append(json.loads(line))
	line = f.readline()
f.close()
correct = 0
wrong = 0
ypredict = []
yactual = []
cmatrix = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]] 
for line in test:
	text = line['text']
	words = re.split("[.(), \-!?:\n\\*']+", text)
	stri = ""
	for word in words:
		stri += word+" "
	words = utils.getStemmedDocuments(stri, True)
	j=0
	nwords = []
	while(j<len(words)):
		if(j != len(words)-1):
			nwords.append(words[j]+words[j+1])
		else:
			nwords.append(words[j])
		j+=1
	words = nwords
	k = 0
	c = 0
	max1 = math.log(phi[k])
	for string in words:
		if(string in theta):
			max1 += math.log(theta[string][k])
		else:
			max1 += math.log(1/(totalWordPerClass[k]+len(training_dictionary)))
	
	for k in range(1,5):
		ret = math.log(phi[k])
		for string in words:
			if(string in theta):
				ret += math.log(theta[string][k])
			else:
				ret += math.log(1/(totalWordPerClass[k]+len(training_dictionary)))
		if(ret > max1):
			max1 = ret
			c = k
	ypredict.append(c+1)
	yactual.append(int(line['stars']))
	cmatrix[c][int(line['stars'])-1]+=1
	if(c+1==int(line['stars'])):
		correct+=1
	else:
		wrong+=1

print("Testing Completed")
print("correct predictions: ", correct)
print("incorrect predictions: ", wrong)
print("Confusion Matrix:")
print(cmatrix)
confatrix = confusion_matrix(yactual,ypredict)
plt.imshow(confatrix)
plt.title("Confusion Matrix")
plt.colorbar()
plt.set_cmap("Greens")
plt.ylabel("True labels")
plt.xlabel("Predicted label")
plt.savefig('q1e2ConMatrix.png')