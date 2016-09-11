#program to find word matching
                                 
t="hello world"
d="world shell"
e=""
for i in t:
	if " "!=i:
		e=e+i
	if " "==i:
		if e in d:
			print "found string %s"%e
	e=""
	
#program to find letter matching

t="hello world"
d="world shell"
 for i in t