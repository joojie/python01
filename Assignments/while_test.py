while True:
	#it will try to get the user to enter an float (just to be safe with inputs)
    try:
        hours = float(input("Amount of hours: "))
    #if the user fails , it will trigger except
    except:
        print("Please enter number of hours")
    #it will print an error message and continue with the while
        continue

    else:
    #if no error then it will break out of the while
        break
while True:
    #it will try to get the user to enter an float (just to be safe with inputs)
    try:
        rate = float(input("Rate for each hour: "))
    #if the user fails , it will trigger except
    except:
        print("Please enter $/hr rate")
    #it will print an error message and continue with the while
        continue
        
    else:
    #if no error then it will break out of the while
        break
salary = hours * rate
print "your salary is $", salary