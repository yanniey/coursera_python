# Use words.txt as the file name
fname = raw_input("Enter file name: ")

try:
	fhand = open(fname)
except:
	print "File cannot be opened:", fname
	exit()

for text in fhand:
    text = text.rstrip()
    print text.upper()
    