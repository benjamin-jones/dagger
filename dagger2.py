#!/usr/bin/python
# Dagger 2, DAGs from objdump disassembly files
import sys
import re

def getSymbols(filename):
	try:	
		fp = open(filename)
	except IOError:
		print "Could not open " + filename
		exit(-1)

	p = re.compile('\<[\-\._0-9a-zA-Z@]+\>:')
	p2 = re.compile('\<[\-\._0-9a-zA-Z@]+\>[^ :]')
	symbols = {}
	current_function = ""
	for line in fp:
		m = p.findall(line)
		if len(m) == 1:
			current_function = m[0].strip(":").strip("<").strip(">")
			symbols[current_function] = []
		m2 = p2.findall(line)
		if len(m2) == 1:
			current_symbol = m2[0].strip().strip("<").strip(">")
			if current_function != "":
				symbols[current_function].append(current_symbol)
	return symbols
def buildVectors(symbols):
	matrix = [0]*len(symbols)*len(symbols)
	functions = []
	vectors = {}
	for function in symbols:
		functions.append( function  )
	for i in range(len(functions)):
		for j in range(len(functions)):
			members = symbols[functions[i]]
			for member in members:
				if member == functions[j]:
					matrix[i*len(symbols)+j] += 1
	index = 0
	for function in functions:
		vector = matrix[index*len(functions):index*len(functions)+len(functions)-1]
		vectors[function] = vector
		index += 1

	return vectors
	
def main():
	args = sys.argv
	if len(args) == 2:
		filename = args[1]
	else:
		print "Usage: ./dagger2.py filename"
		exit(-1)

	symbols = getSymbols(filename)
	vectors = buildVectors(symbols)
	
		
if __name__=="__main__":
	main()	

	
		
