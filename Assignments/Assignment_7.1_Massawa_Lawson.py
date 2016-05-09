fname = raw_input("Enter a filename: ")
if fname > None: fh = open('word.txt')
for line in fh:
	print str.upper(line.strip())