fname = raw_input("\nEnter file name: ")
if fname is not None:
	fh=open('mbox-short.txt')
count = 0
lst = list()
for line in fh:
    words=line.split()
    if line.startswith('From '):
		count +=1
		for word in words:
			if words[1] not in lst:
				lst.append(word)
				#remove troublesome 'From' entries from list of emails
				for i in lst:
					if i == 'From':
						lst.remove('From')
    else:
		continue
print "\nThere were", count, "lines in the file with 'From ' as the first word\n"
print "\nThe", len(lst),'unique email adresses are:\n'
for a in lst:
	print a
print '\n'
		
