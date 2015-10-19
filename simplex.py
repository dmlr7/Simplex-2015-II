import sys
from operator import add
from operator import sub
class Simplex:
  def __init__(self,argv):
    """
    with open(argv[0]) as f:
        self.out = f.read().splitlines()
        for i in self.out[:3]:
            print type(i)
            #i=map(float,i)
            """
    with open(argv[1]) as f:
        lines = f.readlines()
        #print(lines)

    (m,n)   = self.toint(lines[0])
    bidx    = self.toint(lines[1].split()) #variables basicas
    sidx    = self.toint(lines[2].split()) #variables no basicas
    b       = self.tofloat(lines[3].split()) #valores solos
    A       = map(self.tofloat, lines[4:4+len(bidx)])
    obj     = self.tofloat(lines[4+len(bidx)]) 

    z = {}
    for i in range(len(sidx)):
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

  def printIter(self,bidx,sidx,b,A,obj):
    for i in range(len(bidx)):
        print("x"+str(bidx[i])+"|"+str(b[i])+"\t|"+str(A[i])+"|")
    print("Z |"+str(obj[0])+"\t|"+str(obj[1:])+" |")
    s = ""
    for i in range(len(sidx)):
       s = s+" | x"+str(sidx[i])+" "
    print("       "+s+"|\n")

  def init(self,bidx,sidx,b,A,obj,z):
    #print(bidx,sidx,b,A,obj)
    self.printIter(bidx,sidx,b,A,obj)
    if min(b) < 0:
        Ap = []
        objN =[]
        for i in range(0, len(bidx)):
            Ap.append(A[i]+[1])
        for i in range(0,len(sidx)+1):
            objN.append(0)

        Z = {}
        Z[0] = -1
        #print "Z:",Z
        #print Ap
        b.append(0)

        sidx.append(0)
        objN.append(-1)
        self.printIter(bidx,sidx,b,Ap,objN)
        bidx,sidx,b,Ap,objN,Z = self.pivoteinit(bidx,sidx,b,Ap,objN,Z)
        i = 0
        while True:
            #if(b[len(b)-1] == 0 and objN[sidx.index(0)+1] == -1):
             #break
            res = self.pivote(bidx,sidx,b,Ap,objN,Z )
            #print(res,i)
            #print(b[len(b)-1] == 0,objN[sidx.index(0)+1] == -1)
            if res == "UNBOUNDED":
                #print "No se puede inicializar"
                break

            if(0 in sidx):
                if(objN[0] == 0 and objN[sidx.index(0)+1] == -1):
                    break

            bidx = res[0]
            sidx = res[1]
            b = res[2]
            Ap = res[3]
            objN = res[4]
            Z = res[5]
            i = i +1



        if(objN[0] == 0 and objN[sidx.index(0)+1] == -1):
            print("Dicionario factible")
        else:
            print("Diccionario no factible")

        """
        bidx,sidx,b,Ap,objN,Z = self.pivoteinit(bidx,sidx,b,Ap,objN,Z)
        bidx,sidx,b,Ap,objN,Z =self.pivote(bidx,sidx,b,Ap,objN,Z )
        bidx,sidx,b,Ap,objN,Z =self.pivote(bidx,sidx,b,Ap,objN,Z )
        self.pivote(bidx,sidx,b,Ap,objN,Z )

        print(b[len(b)-1] == 0 and objN[sidx.index(0)+1] == -1)
        #self.pivote(bidx,sidx,b,Ap,objN,Z )
        """




    else:
        self.opti(bidx,sidx,b,A,obj,z)

  def rempla(self,list1,list2,val):
      for i in range(len(list1)):
          #print(str(list1[i])+" + "+str(val)+" * "+str(list2[i]))
          list1[i] = list1[i] + val*list2[i]
          #print("= "+str(list1[i]))
      #print("nLista",list1)
      return list1

  def pivoteinit(self,bidx,sidx,b,A,obj,z):
    indVarEntra = sidx[len(sidx)-1]
    indxMatrizA = len(sidx)-1
    ix = {}
    indVarSale = 100
    indymatrizA=-1;
    for j in range(len(bidx)) :
        ix[bidx[j]] = A[j][indxMatrizA]
        if(A[j][indxMatrizA] > 0 and b[j]/(A[j][indxMatrizA]) <= indVarSale):
            if(b[j]/-(A[j][indxMatrizA]) == indVarSale and bidx[j]<bidx[indymatrizA]):
                indymatrizA=j
            else:
                indVarSale=b[j]/(A[j][indxMatrizA])
                indymatrizA=j
    if(indymatrizA >= 0):
        aumento = float(b[indymatrizA]/-A[indymatrizA][indxMatrizA])
        #print(obj)
        #print(obj[0],aumento,z[sidx[indxMatrizA]],aumento*z[sidx[indxMatrizA]])
        print "x"+str(sidx[indxMatrizA])+" and x"+str(bidx[indymatrizA])+"leaves"
        #print "entra id"
        #print sidx[indxMatrizA]

        #print "sale id"
        #print bidx[indymatrizA]
        #print "objetivo"
        number = obj[0] + aumento*z[sidx[indxMatrizA]]
        #print(number)
        res = [sidx[indxMatrizA],bidx[indymatrizA],round(number,4)]
    else: return "UNBOUNDED"

    bidx,sidx,b,A,obj,z = self.remplaPiv(bidx,sidx,b,A,obj,z,res)
    #print(bidx,sidx,b,A,obj,z)
    return bidx,sidx,b,A,obj,z

  def remplaPiv(self,bidx,sidx,b,Ap,objN,Z,res):
        #print(bidx,sidx,b,A,obj,z)
        indSidx = sidx.index(res[0])
        indBidx = bidx.index(res[1])
        xC = Ap[indBidx][indSidx]
        objN[0] = res[2]
        #print(b)
        #print("var",xC,"bids",bidx,"ind",indBidx,"res1",res[1])
        if xC > 0:
            cam = [n/-xC for n in Ap[bidx.index(res[1])]]

            cam[len(sidx)-1] = cam[len(sidx)-1]*-1
            sidx[indSidx] = res[1]
            bidx[indBidx] = res[0]

            for i in range(len(bidx)+1):
                if i == indBidx:
                    Ap[i] = cam
                else:
                    if i == len(bidx):
                        val = objN[len(sidx)]

                        b[i] = b[i] + val*b[indBidx]
                        #print(b[i])
                        objN[1:] = self.rempla(objN[1:len(sidx)],cam[:len(sidx)-1],val) +[val]
                    else:
                        b[i] = b[i] - Ap[i][indSidx]*b[indBidx]
                        #print(b[i])
                        Ap[i] = self.rempla(Ap[i][:len(sidx)-1],cam[:len(sidx)-1],Ap[i][indSidx])+[cam[len(sidx)-1]]

            Z = {}
            for i in range(len(sidx)):
                Z[sidx[i]] = objN[i+1]
            #print(b)
            b[indBidx] = -b[indBidx]
            #print(b)
            self.printIter(bidx,sidx,b,Ap,objN)
            #print(bidx,sidx,b,Ap,objN,Z)
            return (bidx,sidx,b,Ap,objN,Z)
        else:
            #print(bidx,indBidx)
            #print("ec a des",Ap[indBidx])

            tempA = Ap[indBidx][indSidx]
            temmpZ = objN[1]
            #print("tempA",tempA)
            Ap[indBidx][indSidx] = -1
            cam = [n/-xC for n in Ap[bidx.index(res[1])]]
            #print(cam)
            #print("ec des",cam,"b",b)
            #print("x",sidx[indSidx],"b",b)
            sidx[indSidx] = res[1]
            bidx[indBidx] = res[0]

            #print("sid",sidx,"bix",bidx)
            #if(indBidx==0):
                #b[indBidx] = -b[indBidx]/tempA
                #print("ENTRE")
            #print("baccaaa",b)
            if (tempA != 1.0 and tempA!= -1.0):
                #print("ENTREEEEEE")
                if(tempA>0):
                    b[indBidx] = b[indBidx]/tempA
                else:
                    b[indBidx] = -b[indBidx]/tempA
            #print("index",Ap[indBidx][indSidx],"b",b[indBidx],b)
            #print(objN)
            #print("bacca",b)
            #b[indBidx] = b[indBidx]/tempA
            #b[indBidx] = -b[indBidx]

            #print("nue",b[indBidx])
            for i in range(len(bidx)+1):
                if i == indBidx:
                    Ap[i] = cam
                    #b[i] = b[i]/Ap[indBidx][indSidx]

                else:
                    if i == len(bidx):
                        #print("Normal",objN)
                        val = objN[indSidx+1]
                        valx = objN[1]

                        #print("val",val)
                        #print(b)
                        #print("resc",res[2],"valor",b[i]+val*b[indBidx])
                        b[i] = b[i] + val*b[indBidx]
                        temp = -objN[indSidx+1]
                        #print("temo",temp,"ind",indSidx,"x",sidx[indSidx])
                        objN[1] = 0
                        #print(val)
                        #print(objN[1:])
                        #print("sum",cam[:len(sidx)])
                        #print("norm",objN[1:])
                        objN[1:] = self.rempla(objN[1:],cam[:len(sidx)],val)

                        #print("aCambio",objN[1:],"in",indSidx)

                        objN[indSidx+1]= val*cam[indSidx]
                        objN[1] = cam[indSidx]



                        #print("cambio",objN[1:])
                        #print("Cambio",objN)"""
                    else:
                        val = Ap[i][indSidx]
                        #print("valNoZ",val)
                        #print(b[i])
                        #print(val)
                        #print(b[indBidx])
                        b[i] = b[i] + val*b[indBidx]
                        #print("b["+str(i)+"]="+str(b[i]))
                        #print(Ap[i],cam)
                        Ap[i][indSidx] = 0
                        Ap[i] = self.rempla(Ap[i],cam,val)
                        #print("res",Ap[i])
                        #print(cam)
            #print("bnue",b)
            if(0 in bidx):
                objN[1] = -Ap[bidx.index(0)][0]

            if(0 in sidx):
                if(objN[0] == 0 and sidx.index(0)+1 != 1):
                    objN[1] = 0
                else:
                    if(objN[0] == 0 and sidx.index(0)+1 == 1):
                        objN[1] = -1
            self.printIter(bidx,sidx,b,Ap,objN)
            Z = {}
            for i in range(len(sidx)):
                Z[sidx[i]] = objN[i+1]


            return (bidx,sidx,b,Ap,objN,Z)
        #return bidx,sidx,Ap,objN,Z


  def pivote(self,bidx,sidx,b,A,obj,z):
    indxMatrizA = -1
    indVarEntra=100
    for i in range(len(sidx)):
        if (obj[i+1] > 0 and sidx[i] <= indVarEntra ):
            indVarEntra=sidx[i]
            indxMatrizA=i

    ix = {}
    indVarSale = 100
    indymatrizA= -1;

    for j in range(len(bidx)):
        ix[bidx[j]] = A[j][indxMatrizA]
        if(-A[j][indxMatrizA] != 0):
            val = float((int(100*b[j])/-(A[j][indxMatrizA]))/100)
        #print("val",val, indymatrizA,"x"+str(bidx[indymatrizA]))
        #print("val2",b[j]/-A[j][indxMatrizA])
        #print("x"+str(bidx[j]),A[j][indxMatrizA])
        #print("COMM",val <= indVarSale, A[j][indxMatrizA] < 0)
        if(A[j][indxMatrizA] < 0 and val <= indVarSale):

            #print("INDEX COM1",j,val == indVarSale)
            #print("INDEX COM2",bidx[j] < bidx[indymatrizA])
            #print("VALUE nue bidx",bidx[j])
            #print("VALUE temv",bidx[indymatrizA])
            if(val == indVarSale and bidx[j] < bidx[indymatrizA]):
                indymatrizA = j
            elif(val < indVarSale):
                indVarSale = val
                indymatrizA = j
    #print(indymatrizA)
    #print(bidx,indymatrizA)
    if(indymatrizA >= 0 and indxMatrizA >=0):
        aumento = float(b[indymatrizA]/-A[indymatrizA][indxMatrizA])

        print "x"+str(sidx[indxMatrizA])+" and x"+str(bidx[indymatrizA])+"leaves"
        #print sidx[indxMatrizA]

        #print "sale id"
        #print bidx[indymatrizA]
        #print "objetivo"
        number = obj[0] + aumento*z[sidx[indxMatrizA]]
        res = [sidx[indxMatrizA],bidx[indymatrizA],round(number,4)]
    else:
        return "UNBOUNDED"
    bidx,sidx,b,A,obj,z = self.remplaPiv(bidx,sidx,b,A,obj,z,res)
    return bidx,sidx,b,A,obj,z

  def opti(self, bidx, sidx, b, A, obj, z):
    s = self.pivote(bidx,sidx,b,A,obj,z)
    print s[0]
    print s[1]
    print s[2]