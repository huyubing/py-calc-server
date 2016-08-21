#!/usr/bin/python

print '''Test
my
home 
hz'''

print 'age',42

# as
import math as math_my

print math_my.sin(30)

print math_my.pi

x, y , z = 1, 2, 'xxx'



# test
s = {'name': "damin", "age": 34}
key, value = s.popitem()
print key
print value


# use if else elif

name = raw_input("input your name:")

if name == "huyubing":
    print "your name is :", name
else:
    print "your name is ---- ", name


# use while

x = 1
while x < 10:
    print x
    x += 1



print "hello, %s!" % name

# use for loop

words = ['this', 'is', 'an']
for w in words:
    print w

numbers = [1, 2, 3, 6 , 9]
for num in numbers:
    print num

# for key value
d = {"name": "damin", "age": 34}
for key in d:
    print key, " ----", d[key]

for key, value in d.items():
    print key, "====:", value

    
