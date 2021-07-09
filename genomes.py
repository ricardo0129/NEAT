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
	
	def __str__(self):
		return "("+str(self.u)+"->"+str(self.v)+",w:"+str(self.w)+",e:"+str(self.e)+",i:"+str(self.i)+")"
	
	
class Genome():
	#add inputNodes, outputNodes, and One Bias Node
	def __init__(self,inputNodes,outputNodes):
		self.nodes = [[i,i+INF][i>=inputNodes+1] for i in range(0,inputNodes+outputNodes+1)]
		self.inputSize = inputNodes
		self.outputSize = outputNodes
		self.NodePlace = {}
		self.genes = []
		self.connections = set()
	
	def connectionExist(self,u,v):
		if (u,v) in self.connections:
			return True
		return False

	def addConnection(self,u,v,inno,w):
		self.NodePlace[(u,v)] = len(self.genes)
		self.genes.append(Connection(u,v,inno,w))
		self.connections.add((u,v))
	
	def splitConnection(self,u,v,d,inno1,inno2):
		i = self.NodePlace[(u,v)]
		self.genes[i].disableConnection()
		self.addConnection(u,d,inno1,1.0)
		self.addConnection(d,v,inno2,randomRange(-1.0,1.0))
		self.nodes.append(d)
	
	def findNewConnection(self):
		while True:
			u = self.nodes[randInt(0,len(self.nodes)-1)]
			v = self.nodes[randInt(0,len(self.nodes)-1)]
			if u>v:
				u,v = v,u
			if (u<=self.inputSize and v<=self.inputSize) or (u>=INF and v>=INF):
				continue
			if u!=v and not (u,v) in self.connections:
				return u,v

	def findSplit(self):
		n = len(self.genes)
		i = -1
		while True:
			i = randInt(0,n-1)
			if self.genes[i].e==1:
				break
		return (self.genes[i].u,self.genes[i].v)
	
	def evaluate(self,input):
		nodeVal = input+[0]*(len(self.nodes)-self.inputSize)
		self.genes = sorted(self.genes, key = lambda genes: genes.v)
		sorted(self.nodes)
		nodeMapping = {}
		for i,g in enumerate(self.nodes):
			nodeMapping[g] = i 
		for i in range(0,len(self.genes)):
			genome = self.genes[i]
			if genome.e==1:
				u = nodeMapping[genome.u]
				v = nodeMapping[genome.v]
				nodeVal[v] += nodeVal[u]*genome.w
				if (i==len(self.genes)-1) or (nodeMapping[self.genes[i+1].v]!=v):
					nodeVal[v] = sigmoid(nodeVal[v])
		return nodeVal[(len(self.nodes)-self.outputSize):]

t = Genome(4,2)
r = [0.2,0.4,0.7,0.22]
r = t.evaluate(r)
print(r)