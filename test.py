#!/usr/bin/python

# use print
print 'test python!'

# use x and y
x = 2
y = 3
print x * 3


# import math lib
import math

print math.pi

z = math.pi
m = z * z

print z
print str(z)

print len(str(z))


# use for and range
for i in range(0, 10):
    print i


# use break
print 'break test'

for i in range(10):
    if i <= 5:
        print i;
    else:
        print 'break'
        break


a = int(raw_input("input a:"))
b = int(raw_input("input b:"))


print a + b
print a * b
print a % b
print a / b
print a % b

