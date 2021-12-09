e,s=enumerate,sum
m=[int(x)for x in open('a')]
print(s([1 for i,z in e(m)if z>m[i-1]]),s([1 for i,z in e(m)if s(m[i:i+3])<s(m[i+1:i+4])]))
