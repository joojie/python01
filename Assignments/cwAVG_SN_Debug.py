def centered_average(nums):
	largest = None
	smallest = None
	for number in nums:
		
		if number > largest:
			largest = float(number)
	for number in nums:
		if smallest is None:
			smallest = float(number)
		elif number < smallest:
			smallest = float(number)
			
	pos_lrg = nums.index(largest)
	pos_sml = nums.index(smallest)
    
	nums.pop(pos_lrg)
	nums.pop(pos_sml)
	avg = sum(nums)/len(nums)

#What's messing me up now is when I run it. I get an Error saying "Pop index out of range" which don't make sense

	return avg

nums = list(range(1,2001))
print " the list of numbers 1-2000:" ,nums
print "the sum of numbers of 1-2000 with 1 and 2000 removed is:" ,sum(nums[1:-1])
print "the centerweighted average of numbers 1-2000 is:" ,centered_average(nums)