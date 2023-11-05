from fractions import Fraction
n = int(input("n: "))
pnts=[]
res=''

for i in range(n):
    p = input(f"point {i}: ").split(' ')
    pnts.append((float(p[0]),float(p[1])))
pnts.sort(key=lambda x:x[0])

for i in range(n):
    k=pnts[i][1]
    prod=''
    for j in range(n):
        if j==i: continue
        k/=pnts[i][0]-pnts[j][0]
        if pnts[j][0]==0: prod+='x'
        else: prod+=f"(x-{pnts[j][0]})"
    if k!=0:
        c=Fraction(k).limit_denominator(9999).as_integer_ratio()
        if c[0]==1:
            res+=prod
        elif c[0]==-1:
            res+='-'+prod
        else:
            res+=str(c[0])+prod
        if c[1]!=1:
            res+='/'+str(c[1])
        res+='+'
res=res[:-1].replace('+-','-')
print(n,[(float(x[0]),float(x[1])) for x in pnts])
print(res)