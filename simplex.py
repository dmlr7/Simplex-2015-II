import sys
class Simplex:
  def __init__(self,argv):

    with open(argv[2]) as f:
        self.out = f.read().splitlines()
        for i in self.out[:3]:
            print type(i)
            #i=map(float,i)
    with open(argv[1]) as f:
        lines = f.readlines()
        print(lines)

    (m,n)   = self.toint(lines[0])
    bidx    = self.toint(lines[1].split()) #variables basicas
    sidx    = self.toint(lines[2].split()) #variables no basicas
    b       = self.tofloat(lines[3].split()) #valores solos
    A       = map(self.tofloat, lines[4:4+len(bidx)])
    obj     = self.tofloat(lines[4+len(bidx)]) 

    z = {}
    for i in range(len(sidx)) :
        z[sidx[i]] = obj[i+1]


    self.init(bidx,sidx,b,A,obj,z)

    # pivoting
    # print len(lines) , A, m, n, bidx, sidx, b, obj

  def lines(self,fp):
    print str(len(fp.readlines()))

  def toint(self,arr): # convert a string array to int array
    if type(arr) is str :
        return map(int, arr.split())
    return map(int, arr)

  def tofloat(self,arr): # convert a string array to int array
    if type(arr) is str :
        return map(float, arr.split())
    return map(float, arr)

  

  def init(self,bidx,sidx,b,A,obj,z):
    print(bidx,sidx,b,A,obj)
    if min(b) < 0:
        Ap = []
        for i in range(0, len(bidx)):
            Ap.append(A[i]+[1])
        Z = {}
        Z[0] = -1
        print "Z:",Z
        print Ap
        sidx.append(0)
        self.pivote(bidx,sidx,b,Ap,obj,Z)
    else:
        self.opti(bidx,sidx,b,A,obj,z)

  def pivote(self,bidx,sidx,b,A,obj,z):
    indxMatrizA = -1
    indVarEntra=100
    for i in range(len(sidx)):
        if (z[sidx[i]] > 0 and sidx[i] <= indVarEntra ):
            indVarEntra=sidx[i]
            indxMatrizA=i

    ix = {}
    indVarSale = 100
    indymatrizA=-1;
    for j in range(len(bidx)) :
        ix[bidx[j]] = A[j][indxMatrizA]
        if(A[j][indxMatrizA]<0 and b[j]/-(A[j][indxMatrizA]) <= indVarSale):
            if(b[j]/-(A[j][indxMatrizA]) == indVarSale and bidx[j]<bidx[indymatrizA]):
                indymatrizA=j
            else:
                indVarSale=b[j]/-(A[j][indxMatrizA])
                indymatrizA=j
    if(indymatrizA >= 0):
        aumento=float(b[indymatrizA]/-A[indymatrizA][indxMatrizA])

        #print "entra id"
        #print sidx[indxMatrizA]

        #print "sale id"
        #print bidx[indymatrizA]
        #print "objetivo"
        number=obj[0] + aumento*z[sidx[indxMatrizA] ]
        return [sidx[indxMatrizA],bidx[indxMatrizA],round(number,4)]
    else: return "UNBOUNDED"

  def opti(self,bidx,sidx,b,A,obj,z):
    s=self.pivote(bidx,sidx,b,A,obj,z)
    print s[0]
    print s[1]
    print s[2]