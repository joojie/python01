smallest = None
largest = None

while True:
    num = raw_input('Enter two or more different numbers: ')
    if num == 'done': 
        break
	print num

    try:
        num = float(num)
    except:
        print 'Invalid input'
        continue                            

    if smallest == None or num < smallest:
        smallest = num

    if largest == None or num > largest:
        largest = num

print 'Maximum:', largest
print 'Minimum:', smallest
