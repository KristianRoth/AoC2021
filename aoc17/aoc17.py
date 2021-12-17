# 4278
# 1994
import re
m=c=0;S=300;Q,W,E,R=[int(x)for x in re.findall(r'[-\d]+',open('a').read())]
for i in range(S*S):
 x,y=i%S,i//S-S/2;e=o=g=0;n=-S
 while o>E:g=max(g,o);e+=x;o+=y;x-=x>0;y-=1;n=(n,g)[Q<=e<=W<S>E<=o<=R]
 c+=n!=-S;m=max(m,n)
print(m,c)

# 503 438 330 285 281 273 270 246 245 242 240