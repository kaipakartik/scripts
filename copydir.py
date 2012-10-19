import os, fnmatch, sys, shutil

def find_dir(directory, pattern):
	for root, dirs, files in os.walk(directory):
		for basename in dirs:
			if fnmatch.fnmatch(basename, pattern):
				yield basename, root + "/" + basename

def move(source, destination):
	print "moving " + source + "to " + destination
	shutil.move(source, destination)
	
def copy(basename, source, destination):
	print "Copying " + source + "to " + destination
	shutil.copytree(source, destination + "/" + basename)

source = "/Users/kaipa/Downloads"
patterns = ["*Unwritten*", "*Great Comics*", "*Habibi*", "*Locke & Key*", "Most Important Comics", "*Batman- The Black Mirror*", "*Graphic Nove*", "*RASL*"]
destination="/Volumes/port2/Comics"

for pattern in patterns:
	for basename,dirname in find_dir(source, pattern):
		copy(basename, dirname, destination)