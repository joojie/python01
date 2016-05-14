init = raw_input('Enter Filename: ')
if init is not None:
	fhand=open('mbox-short.txt')
count=0
spamAVG=0
for line in fhand:
    words=line.split()
    if line.startswith('X-DSPAM-Confidence:'):
		count +=1
		spamAVG=spamAVG+float(words[1])
    else:
        continue
if count is 0: print "'X-DSPAM-Confidence:    0.8475 occurence':" ,count
else:
	spamAVG=spamAVG/count
	print "Count=",count,"Avg X-DSPAM-Confidence:" ,spamAVG
