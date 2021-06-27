from constants import PERTURBANCE_RATE,INF
from math_operators import perturbe, probability, randInt, randomRange, randomize, sigmoid


class Connection():
	#in/out node, weight, enable bit, inovation # 
	def __init__(self,u,v,i,w):
		self.u = u
		self.v = v
		self.w = w
		self.e = 1 
		self.i = i
	
	def disableConnection(self):
		self.e = 0

	def mutateWeight(self):
		if probability(PERTURBANCE_RATE):
			self.w = perturbe(self.w)
		else:
			self.w = randomize()
	
class Genome():
	#add inputNodes, outputNodes, and One Bias Node
	def __init__(self,inputNodes,outputNodes):
		self.nodes = [[i,i+INF][i>=inputNodes+1] for i in range(0,inputNodes+outputNodes+1)]
		self.inputSize = inputNodes
		self.outputSize = outputNodes
		self.genes = []
		z = 0
		for i in range(inputNodes):
			for j in range(outputNodes):
				self.genes.append(Connection(i,j+inputNodes+1+INF,z,randomRange(-1.0,1.0)))
				z += 1
		self.connections = set()
		self.NodePlace = {}
		self.TotalNodes = inputNodes+outputNodes+1
	
	def connectionExist(self,u,v):
		if((u,v) in self.connections):
			return True
		return False

	def addConnection(self,u,v,inno,w):
		self.genes.append(Connection(u,v,inno,w))
		self.NodePlace[(u,v)] = len(self.genes)
	
	def splitConnection(self,u,v,d,inno):
		i = self.NodePlace[(u,v)]
		self.genes[i].disableConnection()
		self.addConnection(u,d,inno,1)
		self.connections.insert((u,d))
		self.addConnection(d,v,inno+1,1)
		self.connections.insert((d,v))
	
	def findNewConnection(self):
		while True:
			u = self.genes[randInt(0,self.TotalNodes-1)]
			v = self.genes[randInt(0,self.TotalNodes-1)]
			if(u>v):
				u,v = v,u
			if((u<=self.inputSize and v<=self.inputSize) or (u>=INF and v>=INF)):
				continue
			if(u!=v and not (u,v) in self.connections):
				return u,v

	def findSplit(self):
		n = len(self.genes)
		i = -1
		while True:
			i = randInt(0,n-1)
			if(self.genes[i].e==1):
				break
		return (self.genes[i].u,self.gens[i].v)
	
	def evaluate(self,input):
		nodeVal = input+[0]*(len(self.nodes)-self.inputSize)
		self.genes = sorted(self.genes, key = lambda genes: genes.v)
		sorted(self.nodes)
		nodeMapping = {}
		for i,g in enumerate(self.nodes):
			nodeMapping[g] = i 
		for i in range(0,len(self.genes)):
			genome = self.genes[i]
			print(genome.u,genome.v,genome.w)
			if(genome.e==1):
				u = nodeMapping[genome.u]
				v = nodeMapping[genome.v]
				nodeVal[v] += nodeVal[u]*genome.w
			if(i==len(self.genes)-1 or nodeMapping[self.genes[i+1].v]!=v):
				nodeVal[v] = sigmoid(nodeVal[v])
		return nodeVal[self.inputSize+1:]
