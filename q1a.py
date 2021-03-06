import json
import sys
import numpy as np
import re
import math
from collections import Counter

# def printDict(theta):
# 	for item in theta:
# 		if(theta[item] != [0,0,0,0,0]):
# 			print(f"{item} : {theta[item]}")

f = open(sys.argv[1],)

train = []
line = f.readline()
while line:
	train.append(json.loads(line))
	line = f.readline()
f.close()

phi = [0.0, 0.0, 0.0, 0.0, 0.0]
total = len(train)
for line in train:
	phi[int(line['stars'])-1]+=1.0

for i in range(0,5):
	phi[i] = phi[i]/total

training_dictionary = set([])

totalWordPerClass = [0,0,0,0,0]
for line in train:
	words = re.split("[.(), \-!?:\n\\*']+", line['text'])
	i = int(line['stars'])-1
	for word in words:
		totalWordPerClass[i]+=1
		training_dictionary.add(word)

# print(len(training_dictionary))
# print(np.sum(totalWordPerClass))
print("Parameters for naive bayes:")
print("Phi : ", phi)
print("size of the training_dictionary: ", len(training_dictionary))
print("calculating theta")
theta = {}

for word in training_dictionary:
	val = [0.0, 0.0, 0.0, 0.0, 0.0]
	theta[word] = val

for line in train:
	text = line['text']
	fd = Counter(re.split("[.(), \-!?:\n\\*']+", text)).most_common()
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
print("Testing on test data")
f = open(sys.argv[2],)

test = []
line = f.readline()
while line:
	test.append(json.loads(line))
	line = f.readline()
f.close()
correct = 0
wrong = 0
print("total tests : ", len(test))
for i in range(0, len(test)):
	line = test[i]
	text = line['text']
	words = re.split("[.(), \-!?:\n\\*']+", text)
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
	if(c+1==int(line['stars'])):
		correct+=1
	else:
		wrong+=1

print("Testing Completed")
print("correct predictions: ", correct)
print("incorrect predictions: ", wrong)