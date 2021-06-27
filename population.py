from genomes import *

class Population():
	def __init__(self,populationSize,inputNodes,OutputNodes):
		self.globalInovation = 0
		self.population = [Genome(inputNodes,OutputNodes) for i in range(populationSize)]
		self.innovations = {}
	
	

P = Population(10,4,1)

a = [1,2,3]
b = [7]
c = b+a
print(c)