#10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below. Note that the autograder does not have support for the sorted() function.

name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

counts= []
freq = dict()
temp= []
# extract the hours and put the hours into a list
for line in handle:
    if line.startswith("From "):
        line = line.rstrip()
        words= line.split(":")
        hours = words[0][-2:]
        counts.append(hours)
        


# count the hours, put the hours and its frequency into a dictionary
for hour in counts:
    freq[hour] = freq.get(hour,0)+1

# put the dictionary into a list (so that we can use functions like sort() )

for hour, count in freq.items():
    temp.append((hour,count))

# sort the list by hour
temp.sort()

# print the list sorted by hour
for every_hour, frequency in temp:
    print every_hour, frequency
