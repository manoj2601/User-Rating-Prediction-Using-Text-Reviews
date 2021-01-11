import json
import sys
import numpy as np
import re
import math
from collections import Counter
import random

# def printDict(theta):
# 	for item in theta:
# 		if(theta[item] != [0,0,0,0,0]):
# 			print(f"{item} : {theta[item]}")

f = open(sys.argv[1],)

line = f.readline()
phi = [0,0,0,0,0]
while line:
	a = json.loads(line)
	phi[int(a['stars'])-1] +=1	
	line = f.readline()

class1 = max(phi[0], max(phi[1], max(phi[2], max(phi[3], phi[4]))))
clas = 0
if(class1==phi[1]):
	clas = 1
elif(class1==phi[2]):
	clas = 2
elif(class1==phi[3]):
	clas = 3
elif(class1 == phi[4]):
	clas = 4

f.close()

f = open(sys.argv[2],)

test = []
line = f.readline()
while line:
	test.append(json.loads(line))
	line = f.readline()
f.close()
correct1 = 0
wrong1 = 0
correct2 = 0
wrong2 = 0
print("total tests : ", len(test))

for line in test:
	if(random.choice([1,2,3,4,5]) == int(line['stars'])):
		correct1+=1
	else:
		wrong1+=1
	if(int(line['stars']) == clas+1):
		correct2+=1
	else:
		wrong2+=1

print("Randomly Prediction")
print("correct Prediction: ", correct1)
print("incorrect Prediction: ", wrong1)

print("Majority Prediction")
print("correct Prediction: ", correct2)
print("incorrect Prediction: ", wrong2)
