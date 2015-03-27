# Use the file name mbox-short.txt as the file name
confidence = 0
count = 0
sum_confidence = 0
average = 0
fname = raw_input("Enter file name: ")
fh = open(fname)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : 
        continue
    else:
        count +=1
        confidence= float(filter(str.isdigit, line))/10000
        sum_confidence +=confidence
        average = sum_confidence / count
           

print "Average spam confidence:", average
    