import os, fnmatch, sys, shutil

def find_files(directory, pattern):
	for root, dirs, files in os.walk(directory):
		for basename in files:
			if fnmatch.fnmatch(basename, pattern):
				filename = os.path.join(root, basename)
				yield filename

def move(source, destination):
	print "moving " + source + " to " + destination
	shutil.copy(source, destination)

source = "/Users/kaipa/Downloads/complete"
pattern = "?erson.?f.?nterest*avi"
pattern1 = "?erson.?f.?nterest*mp4"
destination="/Volumes/port2/Series/Person of Interest/Season 1"

def move_files(pattern, source, destination):
	for file in find_files(source, pattern):
		move(file, destination)

move_files(pattern, source, destination)
move_files(pattern1, source, destination)
# move_files("*Korra*mkv", source, "/Volumes/port2/Series/Korra")
