# 373378
# 1682576647495

m=map(int,open('a').read().split(','));f=[0]*9
for i in m:f[i]+=1
for i in range(256):a,*f=f;f[6]+=a;f+=[a];i!=79 or print(sum(f))
print(sum(f))

# 173 146