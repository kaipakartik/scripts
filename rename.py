import os, fnmatch, sys, shutil, re, string
def get_new_name(filename):
	return filename.replace("interest", "Interest")

def find_dir(directory):
	for dirpath, dirs, files in os.walk(directory):
		for filename in files:
			oldname = os.path.join(dirpath, filename)
			newname = os.path.join(dirpath, get_new_name(filename))
			move(oldname, newname)

def move(source, destination):
	print "moving " + source + " to " + destination
	shutil.move(source, destination)

source = "/Volumes/port2/Series/Person of Interest/Season 1"

find_dir(source)
