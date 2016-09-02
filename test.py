#!/usr/bin/python


for line in open("test.txt"):
    if "main" in line:
        print line.rstrip()

print "end open text.txt"

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


# define function
# document function

def add(a, b):
    '''my function name: add(a, b)
use test 
new test2 doc'''
    if True :
        print a + b
    else:
        print a - b
    print ''' test  add(a, b) '''


print add(2, 3)

# use .__doc__
print add.__doc__


print '''test help(add)'''

# use help function
help(add)
