import socket

mysock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('www.pythonlearn.com',80))
mysock.send('GET http://www.pythonlearn.com/code/intro-short.txt HTTP/1.0\n\n')

Etag = []
while True:
	data = mysock.recv(512)
	#for line in data:
	#	if line.startswith('Etag'):
	#		print line
	#		Etag.append(line)
	#	ConLen = line.startswith('Content-Length')
	#	CacCon = line.startswith('Cache-Control')
	#	ConTyp = line.startswith('Content-Type')
	if (len(data)<1):
		break
	print data, #"\n Assignment Data: \n"
#print Etag, "\n", ConLen, "\n", CacCon, "\n", ConTyp
	
mysock.close

'''ETag: "20f7401b-1d3-521e9853a392b"
 
Content-Length: 467
 
Cache-Control: max-age=604800, public
 
Content-Type: text/plain'''
