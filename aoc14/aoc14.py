# 2740
# 2959788056211

w,e,*m=open('a').read().replace(' -> ','').split('\n')
o={x[:2]:[]for x in m};c={x:x in w for x in o}
for a,b,i in m:o[a+i]+=[a+b];o[i+b]+=[a+b]
def T(c,t):
 for i in [0]*t:c={k:sum([c[x]for x in o[k]])for k in c}
 r=[0]*99;r[ord(w[-1])]=1
 for x in c:r[ord(x[0])]+=c[x]
 print(max(r)-min(filter(int,r)))
T(c,10);T(c,40)

# 570 600 593 547 536 505 497 541 539 453 441 362 354 324 320 323 321 320
