#File Handling
file_name=r"D:\python\SureshGit\class_py\log.txt"
a=open(file_name,'r')
c=a.readlines()
print c
"""a.write("my first file\n")
a.write("This file contains ")
a.write("three lines")
"""
"""new_filename=r"C:\Users\Swetha\Desktop\pythonfile"
b=open(new_filename,'w')
for i in c:
	result=i.split(" ")
	print result[0],result[-1]
	b.write(result[0]+" "+result[-1])
	"""
	
