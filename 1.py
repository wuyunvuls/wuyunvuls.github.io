import sys
import os
from bs4 import BeautifulSoup
reload(sys)
sys.setdefaultencoding('utf8')
htmlLoc = "bugs/"
htmlName = os.listdir(htmlLoc)
print(htmlName)
indexhtml = open("index.html","w")
setCharset = '<head><meta http-equiv="Content-Type" content="text/html; charset=utf-8" /> </head>'
indexhtml.write(setCharset)
for order,i in enumerate(htmlName):
	if i[0] == 'w':
		i = "bugs/"+i
		soup = BeautifulSoup(open(i),"html.parser")
		url ='<input type="checkbox" name="" value="" /><a href="'+i+'">'+str(order+1)+". "+soup.title.string+'</a>'
		indexhtml.write(url)
		indexhtml.write("</br>")
print "done!"