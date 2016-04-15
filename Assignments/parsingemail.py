data = 'From stephen.marquard@uct.ac.za Sat'
#       0123456789012345678901234567890

#find the first @
atpost = data.find("@")
print atpost
#should print out 21

#find the space after the email
sppos = data.find(" ",atpost)
#should print out 31

#set host to by slicing , also do +1 to avoid "@" 
host = data[atpost+1 : sppos]
print host
#should print out @uct.ac.za
