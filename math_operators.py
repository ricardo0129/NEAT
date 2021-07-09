import random
import math

random.seed(None)

#simulate probability of x∈[0,1]; return true if event with probability x occurs
def probability(x):
	return random.random()<=x 

#slightly mutate val x by some delta; return x∈[0,1]
def perturbe(x):
	x = random.gauss(x,0.05)
	return max(min(x,1.0),0.0)

def randomize():
	return random.random() 

def randomRange(a,b):
	return a+(b-a)*random.random()

def randInt(a,b):
	return random.randint(a,b)

def sigmoid(x):
	return 1.0/(1+math.exp(-4.9*x))

def binarySearch(A,x):
	L = 0, R = len(A)
	while L<=R:
		M = int((L+R)/2)
		if A[M].i==x:
			return M
		elif A[M].i<x:
			L = M+1
		else:
			R = M-1
	return -1