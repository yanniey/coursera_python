def computepay(h,r):
    if h > 40:
        return (h-40)*r*1.5+40*r
    else:
    	return h*r

hrs = raw_input("Enter Hours:")
rate = raw_input("Enter Rate:")

p = computepay(float(hrs),float(rate))
print p