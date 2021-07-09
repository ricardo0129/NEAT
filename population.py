from math_operators import binarySearch
from genomes import *

class Population():
	def __init__(self,populationSize,inputNodes,OutputNodes):
		self.globalInnovation = 0
		self.population = [Genome(inputNodes,OutputNodes) for i in range(populationSize)]
		self.populationSize = populationSize
		#storing tupple (u,v,i) 
		#if i == 0 then split gene 
		#else its a connections gene
		self.innovations = {}
		self.nodeCounter = inputNodes+OutputNodes+1
		for i in range(populationSize):
			for j in range(3):
				self.addMutation(self.population[i])

	def crossover(self,genomeA,fitnessA,genomeB,fitnessB):
		A = self.population[genomeA].genes
		B = self.population[genomeB].genes
		if fitnessA<fitnessB:
			A,B = B,A
		A = sorted(A, key = lambda genes: genes.i)
		for g in A:
			print(str(g)+" ",end='')
		print("")
		B = sorted(B, key = lambda genes: genes.i)
		for g in B:
			print(str(g)+" ",end='')
		print("")
		C = []
		for i in range(0,len(A)):
			j = binarySearch(B,A[i].i)
			if j==-1:
				C.append(A[i])
			else:

			


	
	def splitMutation(self,genome):
		u,v = genome.findSplit()
		i,d = self.getInnovation(u,v,1)
		genome.splitConnection(u,v,d,i,i+1)
	
	def addMutation(self,genome):
		u,v = genome.findNewConnection()
		i,_ = self.getInnovation(u,v,0)
		genome.addConnection(u,v,i,randomRange(-1.0,1.0))

	
	def mutate(self,genome):
		if probability(0.5):
			#add connections
			self.splitMutation(genome)
		else:
			#split connection
			self.addMutation(genome)
	
	def getInnovation(self,inNode,outNode,geneType):
		if (inNode,outNode,geneType) in self.innovations:
			return self.innovations[(inNode,outNode,geneType)]
		elif geneType==0:
			self.innovations[(inNode,outNode,geneType)] = (self.globalInnovation,self.nodeCounter)
			self.nodeCounter+=1
			self.globalInnovation+=2
		elif geneType==1:
			self.innovation[(inNode,outNode,geneType)]= (self.globalInnovation,-1)
			self.globalInnovation+=1
		return self.innovations[(inNode,outNode,geneType)]

		




P = Population(10,4,1)
P.crossover(0,0,1,1)