#import os
#os.makedirs(r"C:\Users\Swetha\Desktop\test\1\2\3\4")
#os.remove(r"C:\Users\Swetha\Desktop\test\hello")
#os.rename(r"C:\Users\Swetha\Desktop\test\hello",r"C:\Users\Swetha\Desktop\test\world")
#os.system("mspaint")
#os.listdir(r"C:\Users\Swetha\Desktop\test")


# program to put same extension files into the folder created for that extension on the desktop

import os
import function
function.path_exists(r"C:\Users\Swetha\Desktop\module")
#get the list of files on the desktop
get_items=os.listdir(r"C:\Users\Swetha\Desktop")
print get_items
files_list=[]
for filename in get_items:
	DotIndex=filename.find('.')
	print DotIndex
	sourcefilepath=r"C:\Users\Swetha\Desktop"+"\\"+filename
	if filename[0]!='.' and DotIndex>0 and os.path.isfile(sourcefilepath):
		files_list.append(filename)
for filename in files_list:
	DotIndex=filename.index('.')
	extension=filename[DotIndex+1::]
	sourcefilepath=r"C:\Users\Swetha\Desktop"+"\\"+filename
	folderPath = r"C:\Users\Swetha\Desktop\module" + "\\" + extension
	print folderPath
	function.path_exists(folderPath)
	function.file_move(sourcefilepath,folderPath)
		
	
	
 