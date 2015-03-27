#Write a program to read through the mbox-short.txt and figure out who has the sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.


name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

# initialize 
persons = dict()
names = []

# create a list of names
for line in handle:
    if line.startswith("From "):
        line = line.rstrip()
        words = line.split()
        names.append(words[1])

# test the list
#print names

# count names
for name in names:
    if name not in persons:
    	persons[name] = 1
    else:
    	persons[name] +=1

# loop to find the greatest value in the dictionary, then print the item

maxname = None
maxcount = None
# loop
for name,count in persons.items():
	if maxcount is None or count > maxcount:
		maxcount = count
		maxname = name

print maxname, maxcount

    


