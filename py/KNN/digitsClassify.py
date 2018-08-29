#!/usr/bin/env python

from numpy import *
import operator
import fileinput

#training dataset
def createDataSet(filename):
	for line in fileinput.input(files=(filename)) :
		a=fromstring(line,dtype=int, sep=',',count=65)
		if(fileinput.isfirstline() == True):
			data = a
		else:
			data = vstack((data,a))
	group = data[:,0:64]
	label = data[:,64]
	return group,label

def classify0(inX, dataSet, labels,k):
	dataSetSize = dataSet.shape[0]
	diffMax = tile(inX, (dataSetSize,1)) - dataSet
	sqDiffMax = diffMax**2
	sqDistances = sqDiffMax.sum(axis=1)
	distances = sqDistances**0.5
	sortedDistIndicies = distances.argsort()

	classCount = {}
	for i in range (k):
		voteILabel = labels[sortedDistIndicies[i]]
		classCount[ voteILabel ] = classCount.get(voteILabel,0) +1

	sortedClassCount = sorted(classCount.iteritems(), key = operator.itemgetter(1), reverse=True)
	return sortedClassCount[0][0]

#main function
#build training dataset
tragroup,tralabel = createDataSet('optdigits.tra')

#build testing dataset
tesgroup,teslabel= createDataSet('optdigits.tes')

#for each testing data, k=3
pos=0
neg=0
for i in range(len(tesgroup)):
	if classify0(tesgroup[i],tragroup,tralabel,5) == teslabel[i]:
		pos = pos + 1
	else:
		neg = neg + 1

#Accuracy on the testing set with k-nn
print pos,neg,float(pos)/(pos+neg)
