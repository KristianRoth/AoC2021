# 3009600
# 6940518

r,y,t=int,len,print;k=j=g='';m=[x for x in open('a')]
def c(o,z,l,a=0):
 *b,=filter(lambda s:z==s[:y(z)],m)
 if y(b)<2:return b[0][o]
 for i in b:a+=r(i[o])
 return"01"[(a>=y(b)-a)^l]
for i in range(12):g+=c(i,k,1)
e=r(g,2);t((e^r('1'*12,2))*e)
exec("k+=c(y(k),k,1);j+=c(y(j),j,0);"*12)
t(r(k,2)*r(j,2))

# 481 475 465 464 458 455 451 402 378 347 343 340 336* 330 316 311 305 303