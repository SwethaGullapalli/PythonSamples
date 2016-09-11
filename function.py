# definition of functions for os module

import os
import shutil
def path_exists(path_pass):
	if os.path.exists(path_pass):
		print "Folder already exists"
	else:
		os.mkdir(path_pass)
def file_move(sourcefilepath, destinationfolderpath):
		shutil.move(sourcefilepath, destinationfolderpath)
	