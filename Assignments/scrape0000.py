#scrapes a site, finds jpg files, appends html code, and writes the HTML code to a txt file for each file.
import urllib
from BeautifulSoup	import *
from urllib import *

nums = range(2,46)

for num in nums:
	url = 'http://www.todaysbuzz.com/todays-buzz/all-the-best-looks-from-the-2016-met-gala/'+str(num)+"/"
	openurl = urllib.urlopen(url).read()

	soup = BeautifulSoup(openurl)

	tags = soup('img')


	with open("src.txt", "a+") as file:
		for tag in tags:
			if tag.get('src',None).find('uploads/2016') != -1:
				tag = "<img src='"+tag.get('src')+"'/>"
				print num, tag
				file.write(tag)