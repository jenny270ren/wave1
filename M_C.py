c = int(input())
t = c//200
c=c%200
l = c//100
c=c%100
q = c//25
c=c%25
d = c//10
c=c%10
n = c//5
c=c%5
p = c
print (t, "toonies", l, "loonies", q, "quarters", d,"dimes", n,"nickels",p, "pennies")