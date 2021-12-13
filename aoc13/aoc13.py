# 810
# 0     0   0         0 0 0     0     0   0 0 0       0 0     0 0 0 0   0 0 0  
# 0     0   0         0     0   0     0   0     0   0     0   0         0     0
# 0 0 0 0   0         0 0 0     0     0   0 0 0     0         0 0 0     0     0
# 0     0   0         0     0   0     0   0     0   0   0 0   0         0 0 0  
# 0     0   0         0     0   0     0   0     0   0     0   0         0   0  
# 0     0   0 0 0 0   0 0 0       0 0     0 0 0       0 0 0   0         0     0

o,a=map(str.split,open('a').read().split('\n'*2))
m=[[*eval(x)]for x in o]
for c in a[2::3]:
 for d in m:b,n=c.split('=');g=b=='y';d[g]-=max(0,2*(d[g]-int(n)))
 if o:o=print(len({*map(str,m)}))
for y in range(6):print(*[' 0'[[x,y]in m]for x in range(39)])

# 610 533 415 409 388 364 364 356 352 340 332 323 321 311 308 306 302 291 290 286 274 272 270 266 265 257 255