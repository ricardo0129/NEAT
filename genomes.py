from constants import PERTURBANCE_RATE
from math_operators import perturbe, probability, randInt, randomize


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
	def __init__(self,inputNodes,OutPutNodes):
		self.nodes = [i for i in range(inputNodes+OutPutNodes+1)]
		self.genes = []
		self.connections = set()
		self.NodePlace = {}
		self.TotalNodes = inputNodes+OutPutNodes+1
	
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
		self.addConnection(d,v,inno+1,1)
	
	def findNewConnection(self):
		while True:
			u = randInt(0,self.TotalNodes-1)
			v = randInt(0,self.TotalNodes-1)
			if(u!=v and not (u,v) in self.connections):
				return u,v

	def findSplit(self):
		n = len(self.genes)
		i = randInt(0,n-1)
		return (self.genes[i].u,self.gens[i].v)




class Population():
	def __init__(self,populationSize,inputNodes,OutputNodes):
		self.globalInovation = 0
		self.population = [Genome(inputNodes,OutputNodes) for i in range(populationSize)]
		self.innovations = {}

P = Population(10,4,1)

		
