#input data from user for hours and rate
def computepay(h,r):
	if h <=40:
		p = (h * r)
	else:
		p = (40*r)+((h-40)*(r*1.5))
	return p
hrs = raw_input("Enter Hours: ")
h = float(hrs)
rate = raw_input("Enter rate per hour: ")
r = float(rate)

p=computepay(h,r)
print "your pay is: ",p