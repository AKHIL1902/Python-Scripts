x = 1000/3
y = 1000/5
print "Here is the multiple for 3 for 1000"
print range(x)
print "here is the multiple for 5  for 1000"
print range(y)

print "here Is the rest fo sequence"
def fib_first():
    a, b = 0, 1
    while  a < x:
        print b,
        a,b = b,a+b



def fib_second():
    a, b = 0, 1
    while b < y:
        print a,
        b, a = a, a+b

print fib_second()
print fib_first()


