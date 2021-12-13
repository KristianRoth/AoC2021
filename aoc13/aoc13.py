# 103
# 0  0 0    000  0  0 000   00  0000 000 
# 0  0 0    0  0 0  0 0  0 0  0 0    0  0
# 0000 0    000  0  0 000  0    000  0  0
# 0  0 0    0  0 0  0 0  0 0 00 0    000 
# 0  0 0    0  0 0  0 0  0 0  0 0    0 0 
# 0  0 0000 000   00  000   000 0    0  0

f=1;p=print;r=range;h=map
m,a=h(str.split,open('a').read().split('\n'*2))
m=[[*h(int,x.split(','))]for x in m]
a=[x.split('=')for x in a[2::3]]
for b in a:
 for d in m:g=b[0]=='y';e=2*(d[g]-int(b[1]));d[g]-=(0,e)[e>0]
 if f:p(len(set(h(str,m))));f=0
for y in r(6):
 for x in r(39):p(end=' 0'[[x,y]in m])
 p()

# 610 533 415 409 388 364 364 356 352 340 332 323 321 311 308

# b = a - 2*(a - e)
# b = a - 2*a + 2*e
# b = -a + 2*e