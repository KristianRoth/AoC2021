# 51776
# 16830
r=set;t=range;c=0;g=lambda s,y:r(s).issubset(r(y))
a,*f=''.join([x for x in open('a')]).split('\n'*2)
d=[int(x)for x in a.split(',')]
*b,=map(lambda s:[*map(int,s.split())],f)
for i in t(len(d)):
 for v in b:
  for h in t(5):
   if g(v[h::5],d[:i])or g(v[h*5:-~h*5],d[:i]):a=(sum(v)-sum(*[r(d[:i])&r(v)]))*d[:i][-1];b.remove(v);c or print(a);c=1;break
print(a)

# 620 534 427 435 409 391 382 373 368 360