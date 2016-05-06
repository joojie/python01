userin = raw_input("enter a score between 0.0 and 1.0: ")
num = float(userin)

#thoughts on making a tuple and assigning grades based on position
#gradetup = i.items.sort - serious guess work here

# for ...,f,d,c,b,a in gradetup:
# 	grade = ...,f,d,c,b,a - here I get lost...
#print 'your grade is' grade 

if num > 1:
	print " error grade out of range"
elif num >= .9:
	print "your grade is A"
elif num >= .8:
	print "your grade is B"
elif num >= .7: 
	print 'your grade is C'
elif num >= .6:
	print 'your grade is D'

else:
	print 'your grade is F'