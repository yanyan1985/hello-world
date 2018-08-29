#!/usr/bin/env python

from numpy import *
import operator
import fileinput
import math

#training dataset
def createDataSet(filename):
	for line in fileinput.input(files=(filename)) :
		a=fromstring(line,dtype=int, sep=' ')
		if(fileinput.isfirstline() == True):
			data = a
		else:
			data = vstack((data,a))
	return data

def calcEntropy(group):
	print "calcEntropy:" ,group
	label = group[:,-1]
	labelcounts = {}
	total = len(label)
	entrop = 0	

	for i in label:
		if i not in labelcounts:
			labelcounts[i] = 0
		labelcounts[i] += 1

	for j in labelcounts:
		p = float(labelcounts[j]) / total
		entrop -= ( p * (math.log(p,2)))

	return entrop

def chooseBestFeature(group):
	bestFeatureIndex = 0
	return bestFeatureIndex

def splitSet(index,group):
	maps={}
	return maps 

def buildTree(group): #[ [11 22 a] [12 22 b ] [11 21 c]]
	featIndex = -1
	label = [examples[-1] for examples in group] # [a a b ]
	branches={}
	if len(set(label))==0 :
		branches[-1] = group
		return featIndex, branches
	else:
		featIndex = chooseBestFeature(group) # featIndex = 1
		featValueSet = splitSet(featIndex,group) # featValueSet = {22:[[11 22 a] [12 22 b]], 21:[[11 21 c]]}

		for featValue in featValueSet: # 22:[[11 22 a] [12 22 b]]
			index,subTree = buildTree(featValueSet[featValue]) 
			if index == -1 :
				branches[featValue] = subTree  # branches[22]= subTree(map), branches[21]= subTree(map),

	#print featIndex,branches 
	return featIndex, branches


#main function
#build training dataset
tragroup = createDataSet('lenses.data.head')
calcEntropy(tragroup)
buildTree(tragroup)


