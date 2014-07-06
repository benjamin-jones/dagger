#!/usr/bin/python

import sys
import re
if __name__=="__main__":
	args = sys.argv
	if len(args) == 2:
		filename = args[1]
	else:
		print "Usage: ./dagger2.py filename"
		exit(-1)

	fp = open(filename)
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
	
	for symbol in symbols:
		print symbol + ":"
		for child in symbols[symbol]:
			print "\t" + child
