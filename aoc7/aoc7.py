# 342730
# 92335207

*m,=map(int,open('a').read().split(','));l=range(999)
for x in[sum(map(lambda s:abs(s-c),m))for c in l],[sum(map(lambda s:abs(s-c)*(1+abs(s-c))//2,m))for c in l]:print(min(x))

# 302 192 180 175