import re

Fname = raw_input("Enter file name: ")
f = open(Fname)
fr = f.read()


numbers = re.findall('[0-9]+', fr)
	
numbers = map(int, numbers)

print sum(numbers)