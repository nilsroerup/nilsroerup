import random

def add(a,b):
    return a if b == 0 else add(a^b, (a&b) << 1)

def multiply(a,b):    
    runningSum = 0
    while a:
        if a&1:
            runningSum = add(runningSum, b)
        a = a>>1
        b = b<<1
    return runningSum

 
# unittests
def testAdd():
    for i in range(20):
        a = random.randint(0,999)
        b = random.randint(0,999)
        assert(add(a,b) == a+b)
        # print("%i+%i=%i == %i" % (a,b,add(a,b), a+b))

def testMultiply():
    for i in range(20):
        a = random.randint(0,999)
        b = random.randint(0,999)
        assert(multiply(a,b) == a*b)
        # print("%i*%i=%i == %i" % (a,b,multiply(a,b), a*b) )

def tests():
    testAdd()
    testMultiply()



tests()
