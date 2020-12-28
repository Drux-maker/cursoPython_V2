l = [1,2,3,-1,4]
s = ["H","o","l","a"]

def factorial(n):
    i = 1;
    while n > 1:
        i = n+i
        yield i
        n -=1

for e in factorial(5):
    print (e)

