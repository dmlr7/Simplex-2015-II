import sys

def lines(fp):
    print str(len(fp.readlines()))

def toint(arr): # convert a string array to int array
    if type(arr) is str :
        return map(int, arr.split())
    return map(int, arr)

def tofloat(arr): # convert a string array to int array
    if type(arr) is str :
        return map(float, arr.split())
    return map(float, arr)

def main():
    with open(sys.argv[1]) as f :
        lines = f.readlines()

    (m,n)   = toint(lines[0].split())
    bidx    = toint(lines[1].split()) #variables basicas
    sidx    = toint(lines[2].split()) #variables no basicas
    b       = tofloat(lines[3].split()) #valores solos
    A       = map(tofloat, lines[4:4+len(bidx)])
    obj     = tofloat(lines[4+len(bidx)]) 

    z = {}
    for i in range(len(sidx)) :
        z[sidx[i]] = obj[i+1]
    """
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
        print sidx[indxMatrizA]  
  
        #print "sale id"
        print bidx[indymatrizA]  
        #print "objetivo"
        number=obj[0] + aumento*z[sidx[indxMatrizA] ]
        print round(number,4)
    else: print "UNBOUNDED"
    """
    init(bidx,sidx,b,A,obj)

    # pivoting
    # print len(lines) , A, m, n, bidx, sidx, b, obj


def init(bidx,sidx,b,A,obj):
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
        pivote(bidx,sidx,b,Ap,obj,Z)
    else:
        opti()

def pivote(bidx,sidx,b,A,obj,z):
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
        print sidx[indxMatrizA]

        #print "sale id"
        print bidx[indymatrizA]
        #print "objetivo"
        number=obj[0] + aumento*z[sidx[indxMatrizA] ]
        print round(number,4)
    else: print "UNBOUNDED"

def opti():
    print("OPTIMI")

if __name__ == '__main__':
    main()
