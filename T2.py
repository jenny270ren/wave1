s = int(input())
d=s//86400
s=s%86400
h=s//3600
if h<10:
    h= "0"+str(h)
s=s%3600
m=s//60
if m<10:
    m= "0"+str(m)
s=s%60
if s<10:
    s= 0+str(s)
print(d,":",h,":",m,":",s)
