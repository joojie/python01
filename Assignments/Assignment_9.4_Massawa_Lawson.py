import re
fname = raw_input("Enter file:")
if fname is not None:
	fh = open('mbox-short.txt')

count = dict()

for line in fh:
	if line.startswith('From '):
		emails = line.split()
		email = emails[1] 
		if email not in count:
			count[email] = 1
	else:
		count[email] = count[email] + 1
		
print count
	
