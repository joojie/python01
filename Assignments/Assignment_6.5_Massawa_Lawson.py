text = "X-DSPAM-Confidence:    0.8475";
print text
print 
num = text[text.find('0'):]

num = float(num)
print "Floating point number ==", num
