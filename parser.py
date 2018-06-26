import re
from collections import defaultdict
'''
	1.Match if in a line
	2.Match elif in a line
	3.Match else in a line
	4.Match tabs in a line
	5.Implement Graph data structure
	Alogorithm for graph Manipulation
		0.push global to stack
			1.addBlock
			2.addEdge to top of stack
			3.push block to stack
			4.if number of tabs decreases
				pop block from stack
			5.return to 1

'''


class Graph():

	def __init__(self):
		self._graph = defaultdict(set)
	def addEdge(self, startNode, endNode):
		self._graph[startNode].add(endNode)
		self._graph[endNode].add(startNode)
	def print(self):
		for k,v in self._graph.items():
			print(k)
			for item in v:
				print("\t\t",item)


class Parser():
	def __init__(self):
		self._blockCount = 0
		self._blockStack = ["Global"]
		self._graph = Graph()
		self._lines = None
		self._numberOfTabs = 0
		self._ifMatch = r"^(if)(\s+)(True|False|[a-zA-z0-9==]+)\s*:"
		self._elifMatch = r"^(elif)(\s+)(True|False|[A-Za-z0-9==]+)\s*:"
		self._elseMatch = r"^(else)\s*:"
		self._tabMatch = r"^(\t)+"
	def start(self):
		if self._lines is not None:
			for line in self._lines:
				numberOfTabs = self.matchTab(line)
				self._blockStack[len(self._blockStack)-1]
				if numberOfTabs < self._numberOfTabs:
					self._blockStack.pop()
					if len(self._blockStack) != 1 and numberOfTabs==0:
						self._blockStack.pop()
					self._numberOfTabs = numberOfTabs
				elif numberOfTabs > self._numberOfTabs:
					self._numberOfTabs = numberOfTabs
				foundConditionalBlock = self.checkConditionalBlock(line)
				self._blockStack[len(self._blockStack)-1]
				if foundConditionalBlock:
					self.addBlock(foundConditionalBlock)
			self._graph.print()
	def setLines(self, lines):
		self._lines = lines
	def checkConditionalBlock(self, line):
		line = line.strip()
		result = None
		if re.match(self._ifMatch, line):
			result = "If block-B"+str(self._blockCount)+"  "+re.match(self._ifMatch, line).group(3)
			self.incrementBlockCount()
		elif re.match(self._elifMatch, line):
			result = "Elif block-B"+str(self._blockCount)+"  "+re.match(self._elifMatch, line).group(3)
			self.incrementBlockCount()
		elif re.match(self._elseMatch, line):
			result = "Else block-B"+str(self._blockCount)
			self.incrementBlockCount()
		return result
	def incrementBlockCount(self):
		self._blockCount += 1
	def matchTab(self, line):
		matchObj = re.match(self._tabMatch, line)
		if(matchObj):
			return len(matchObj.group())
		return 0
	def addBlock(self, block):
		self._graph.addEdge(self._blockStack[len(self._blockStack)-1], block)
		self._blockStack.append(block)


def main(): 
	parser = Parser()
	with open("test.py") as file:
		lines = file.readlines()
	parser.setLines(lines)
	parser.start()
main()
