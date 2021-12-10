# 415953
# 2292863731
m=[x.rstrip()for x in open('a')]
p={'(':')','[':']','{':'}','<':'>'};s={')':(3,1),']':(57,2),'}':(1197,3),'>':(25137,4)}
z=0;x=[]
for row in m:
 v=''
 for a in row:
  if a in p:v+=a
  elif p[v[-1]]!=a:z+=s[a][0];break
  else:v=v[:-1]
 else:
  c=0
  for i in range(len(v))[::-1]:c*=5;c+=s[p[v[i]]][1]
  x+=[c]
x.sort()
print(z,x[len(x)//2])


#1043 738 547 439 427 429 428 339