# 1488669
# 1176514794
a=h=v=0
m=[(e,int(n))if'd'<e[0]else(e,-int(n))for e,n in[x.split()for x in open('a')]]
for x,y in m:
 if x[6:]:h+=y;v+=a*y
 else:a-=y
print(a*h,v*h)
