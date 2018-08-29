#!/usr/bin/env python
from numpy import *

def loadDataSet():
	postingList=[
			[' my', 'dog', 'has', 'flea', 'problems', 'help', 'please'], 
			['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
			['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
			['stop', 'posting', 'stupid', 'worthless', 'garbage'],
			['mr', 'licks', 'ate', 'my', 'steak', 'how',' to',  'stop', 'him'],
			['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']
			]
	classVec = [0, 0, 0, 1, 0, 1] 
	return postingList, classVec

def createVocabList( dataSet):
	vocabSet = set([]) 
	for document in dataSet:
		vocabSet = vocabSet | set( document) 
	return list( vocabSet) 
	
def setOfWords2Vec( vocabList, inputSet):
	returnVec = [0]* len( vocabList) 
	for word in inputSet:
		if word in vocabList: 
			returnVec[ vocabList.index( word)] = 1 
		else: 
			print "the word: %s is not in my Vocabulary!" % word 
	return returnVec


def trainNB0( trainMatrix, trainCategory):
	numTrainDocs = len( trainMatrix) 
	numWords = len( trainMatrix[ 0])
	pAbusive = sum( trainCategory)/ float( numTrainDocs)
	p0Num = ones( numWords); #[ 1 1 1 ...1]
	p1Num = ones( numWords) 
	p0Denom = 2.0;
	p1Denom = 2.0 
	for i in range( numTrainDocs):
		if trainCategory[ i] == 1:
			p1Num += trainMatrix[ i] 
			p1Denom += sum( trainMatrix[ i]) 
		else: 
			p0Num += trainMatrix[ i] 
			p0Denom += sum( trainMatrix[ i]) 
	p1Vect = log(p1Num/ p1Denom) #p(wi|c1) = freq(wi)/freq(all words in c1)
	p0Vect = log(p0Num/ p0Denom) #p(wi|c0) = freq(wi)/freq(all words in c0)
	return p0Vect, p1Vect, pAbusive # ln(p(wi|c0)), ln(p(wi|c1)), p(c1)

def classifyNB( vec2Classify, p0Vec, p1Vec, pClass1):
	p1 = sum( vec2Classify * p1Vec) + log( pClass1) 
	p0 = sum( vec2Classify * p0Vec) + log( 1.0 - pClass1) 
	if p1 > p0: 
		return 1 
	else:
		return 0



def testNB():
	listOPosts, listClasses = loadDataSet()
	myVocabList = createVocabList(listOPosts) # all words

	trainMat=[] # all doc matrix in vector
	for postinDoc in listOPosts: 
		trainMat. append( setOfWords2Vec( myVocabList, postinDoc))

	p0V, p1V, pAb =  trainNB0( trainMat, listClasses)
	testEntry = ['garbage', 'stupid', 'dalmation']

	thisDoc = array( setOfWords2Vec( myVocabList, testEntry))
	print thisDoc
	print testEntry,' classified as: ',classifyNB( thisDoc, p0V, p1V, pAb)

testNB()


