fruit = 'banana'

word = raw_input('Write a fruit:')

if word < fruit:
	print 'word is less than' + fruit
elif word > fruit:
	print 'word is greater than:' + fruit
else:
	print 'the word is fruit'