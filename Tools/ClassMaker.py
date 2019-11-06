class Make:
    def One(a,b,c,d,e,f,g,h,n=1):
            print('''
            class {0}_T{8}({0}):
                Type="{4}"
                Name="{1}"
                cost={5}
                power_cons={6}
                {2}={7}
                Info=["{3}","{0} +"+str({2}),"Power Cons: "+str(power_cons),"Cost: "+str(cost)]
                def __init__(self,Ship):
                    {0}.__init__(self,Ship,self.Name,self.Type,self.{2},self.power_cons,self.cost)
            '''.format(a,b,c,d,e,f,g,h,n))
    def Set(A,B,C,a,b,c,d,e):#a,c,e   1 3 5
        Make.One(A,a[0],B,a[1],C,a[2],a[3],a[4],n=1)
        Make.One(A,b[0],B,b[1],C,b[2],b[3],b[4],n=2)
        Make.One(A,c[0],B,c[1],C,c[2],c[3],c[4],n=3)
        Make.One(A,d[0],B,d[1],C,d[2],d[3],d[4],n=4)
        Make.One(A,e[0],B,e[1],C,e[2],e[3],e[4],n=5)

#Make.One("Shield","Deflector","shield","Deflector","UL",6,7,8)
#Make.Set("Shield","shield","UL",("Deflector","Deflector",20,60,300),("Deflector","Improved Deflector",26,80,390),("Shield","Shield",34,100,510),("Shield2","Advanced Shield",34,140,660),("Shield3","Hyper Shield",44,180,870))
Make.Set("Armor","armor","US",("Nanocomp","Nanocomposite",10,0,50),("Ceramo-metal","Ceramo-metal",13,0,65),("Plasteel","Plasteel",17,0,85),("Durasteel","Durasteel",17,0,110),("Neutronium","Neutronium",22,0,145))
