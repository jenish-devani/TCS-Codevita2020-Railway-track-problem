
from itertools import chain

x=int(input())

t=[]
for i in range(0,x):
    sn=input()
    sn=sn.split()
    t.append(sn)

ft=list(chain.from_iterable(t))

ar=[]
dp=[]

for i in range(0,len(ft)):
    ft[i]=int(ft[i])
    if i % 2 == 0:
        ar.append(ft[i])
    else:
        dp.append(ft[i])

odp=[]

for i in range(0,len(ar)):
    odp.append(ar[i]+dp[i])

oft=[]
oft=ar+odp
oft.sort()

ptl=[]
pt = 0

for i in oft:
    if i in ar:
        pt=pt+1
        ptl.append(pt)
    if i in odp:
        pt=pt-1
        ptl.append(pt)

print(max(ptl))

