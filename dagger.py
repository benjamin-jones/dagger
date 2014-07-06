#!/usr/bin/python
from sys import argv, exit
from Elfparsing import Elf
import distorm3
import sys
import optparse
import re

def main():
	print "Welcome to DAGger"
	
	# Parse the command line arguments
	usage  = 'Usage: %prog [--b16 | --b32 | --b64] filename [offset]'
	parser = optparse.OptionParser(usage=usage)
	parser.add_option(  '--b16', help='80286 decoding',
                    action='store_const', dest='dt', const=distorm3.Decode16Bits  )
	parser.add_option(  '--b32', help='IA-32 decoding [default]',
                    action='store_const', dest='dt', const=distorm3.Decode32Bits  )
	parser.add_option(  '--b64', help='AMD64 decoding',
                    action='store_const', dest='dt', const=distorm3.Decode64Bits  )
	parser.set_defaults(dt=distorm3.Decode32Bits)
	options, args = parser.parse_args(sys.argv)

	if len(args) < 2:
    		parser.error('missing parameter: filename')

	filename = args[1]
	offset   = 0
	length   = None

	if len(args) == 3:
		try:
        		offset = int(args[2], 10)
    		except ValueError:
        		parser.error('invalid offset: %s' % args[2])
    		if offset < 0:
        		parser.error('invalid offset: %s' % args[2])
		elif len(args) > 3:
    			parser.error('too many parameters')


	binary = Elf(filename)

	if binary.isElf():
		print "Found ELF Binary: %s" %(argv[1])
		section_text = binary.extractRawSectionByName(".text")
		print "Size of section .text: %d bytes" %(len(section_text))
		
		data = "".join(map(chr,section_text))
		offset = binary.getSymbolAddrByName("_start")
		print "Entry point: " + str(offset)
		
		iterable = distorm3.DecodeGenerator(offset, data, options.dt)
		# Print each decoded instruction
		p = re.compile('0x[0-9a-f]+')
		for (offset, size, instruction, hexdump) in iterable:
			tokens = p.findall(instruction)
			try:
				if len(tokens) == 1:
					token = tokens[0]
					if len(token) > 6:
						addr = int(token,16)
						name = binary.getSymbolNameByAddr(addr)
						if name != None:
							instruction = instruction.replace(token,name)
			except ValueError:
				print ""
			if binary.getSymbolNameByAddr(offset) != None:
				offset = binary.getSymbolNameByAddr(offset)
				print("%s:" %(offset))
				print("\t%s" %(instruction))
			else:
				print("\t%s" %(instruction))

	else:
		print "Not an ELF Binary"
	exit(0)	
		

if __name__=="__main__":
	main()
