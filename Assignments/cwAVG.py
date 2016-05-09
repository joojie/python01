def cwAVG(nums):
	snums = sorted(nums)
	cwNums = snums[1:-1]
	cwAVG = sum(cwNums)/ len(cwNums)
	return cwAVG

nums = list(range(1,1001))
print cwAVG(nums)
