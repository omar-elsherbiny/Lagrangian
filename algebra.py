from fractions import Fraction
L=100
class Term:
    def __init__(self, degree, coefficient):
        self.d = degree
        self.c = coefficient
    def __mul__(self, other):
        if isinstance(other,int) or isinstance(other,float):
            return Term(self.d ,other*self.c)
        elif isinstance(other,Term):
            return Term(self.d+other.d, self.c*other.c)
        raise Exception(other)
    def __add__(self, other):
        if isinstance(other,int) or isinstance(other,float):
            if self.d==0:
                return Term(self.d, self.c+other)
            return None
        elif isinstance(other,Term):
            if self.d==other.d:
                return Term(self.d, self.c+other.c)
            else:
                return None
        raise Exception(other)
    def __repr__(self) -> str:
        if self.d==0: return str(Fraction(self.c).limit_denominator(L))
        C=Fraction(self.c).limit_denominator(L).as_integer_ratio()
        s=''
        if C[0]==1: s+=f"x^{self.d}"
        elif C[0]==-1: s+=f"-x^{self.d}"
        else: s+=f"{C[0]}x^{self.d}"
        if C[1]!=1: s+=f"/{C[1]}"
        return s
    __rmul__ = __mul__

class alg:
    def __init__(self, terms):
        self.terms=terms
    def _simplify(self):
        res=self.terms[:]
        for i,v in enumerate(res):
            for j in res[i+1:]:
                s = v+j
                if s!=None:
                    res.remove(v)
                    res.remove(j)
                    res.append(s)
                    break
        self.terms=[i for i in res if i.c != 0]
        return self
    def __mul__(self,other):
        if isinstance(other,int) or isinstance(other,float) or isinstance(other,Term):
            return alg([x*other for x in self.terms])._simplify()
        elif isinstance(other,alg):
            res=[]
            for term in self.terms:
                res.extend([x*term for x in other.terms])
            return alg(res)._simplify()
        raise Exception(other)
    def __add__(self,other):
        if isinstance(other,int) or isinstance(other,float) or isinstance(other,Term):
            return alg(self.terms+[other])._simplify()
        elif isinstance(other,alg):
            return alg(self.terms+other.terms)._simplify()
    def __repr__(self) -> str:
        self.terms.sort(key=lambda x:x.d,reverse=True)
        return str([repr(x) for x in self.terms])
    def formatted_poly(self):
        s=''
        self=self._simplify()
        self.terms.sort(key=lambda x:x.d,reverse=True)
        for t in self.terms: s+=repr(t)+' + '
        s=s[:-3].replace('+ -','- ')
        return s
    __rmul__ = __mul__

if __name__ == "__main__":
    a=alg([Term(1,1), Term(2,-0.5), Term(0,5)])
    b=alg([Term(1,3), Term(2,3), Term(0,5)])
    c=a+-1*b
    print('a: ',a.formatted_poly())
    print('b: ',b.formatted_poly())
    print('c: ',c.formatted_poly())