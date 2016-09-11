# program to find values on nse

import urllib2
from bs4 import BeautifulSoup

urlpath="http://www.tallgrasssoft.com/"
get_data=urllib2.urlopen(urlpath)
#html_page=
obj_parse=BeautifulSoup(get_data,'html.parser')
#get_value=obj_parse.find('a',attrs={'target':'_top'})
#get_value=obj_parse.find('i',attrs={'class':'fa fa-phone'})
#print get_value.parent.text
get_value=obj_parse.find_all('a')
print get_value.parents
#for i in get_value:
#	print i.contents
	