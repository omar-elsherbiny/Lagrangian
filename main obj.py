from algebra import *
    
n = int(input("n: "))
pnts=[]
res=alg([])

for i in range(n):
    p = input(f"point {i}: ").split(' ')
    pnts.append((float(p[0]),float(p[1])))
pnts.sort(key=lambda x:x[0])

for i in range(n):
    k=pnts[i][1]
    prod=alg([1])
    for j in range(n):
        if j==i: continue
        k/=pnts[i][0]-pnts[j][0]
        prod*=alg([Term(1,1),Term(0,-pnts[j][0])])
    if k!=0:
        res+=prod*k

print(n,[(float(x[0]),float(x[1])) for x in pnts])
print(res.formatted_poly())