#Assignment 3.1

hrs = raw_input("Enter Hours:")
r = raw_input("Enter Rate:")
h = float(hrs)
rate = float(r)

if h > 40:
    pay = 40*rate +(h-40)*1.5*rate
    print pay
else:
    pay = h*rate
    print pay

 #Assignment 3.3

number=raw_input("Enter a number:")
n=float(number)

if (n <0.0) or (n >1.0):
    print "Error message"
elif n>=0.9:
    print "A"
elif n>=0.8:
    print "B"
elif n>=0.7:
    print "C"
elif n>=0.6:
    print "D"
else:
    print "F"
    