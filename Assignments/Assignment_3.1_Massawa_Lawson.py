#input data from user for hours and rate
hrs = raw_input("Enter Hours: ")
h = float(hrs)
rate = raw_input ("Enter rate per hour: ")
r = float(rate)

#calculate regular pay rate or overtime pay rate
if h <=40:
	pay = (h * r)
else:
	pay = (40*r)+((h-40)*(r*1.5))

#print pay
print "your pay is: " ,pay