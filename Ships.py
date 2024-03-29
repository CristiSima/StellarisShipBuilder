import Weapons
import Modules
import Components
'''
Shield,Hull,Armor:
    Base=sum(Utility)
    Final=Base
    Final+=Base*(LVL+Auxilary)
'''
class Ship:
    def __init__(self,Class,MaxHull,Speed,Evasion,ComPoints,Cost):
        self.Class=Class
        self.BaseShield=0
        self.BaseArmor=0
        self.FinalHull=self.BaseHull=MaxHull
        self.FinalSpeed=self.BaseSpeed=Speed
        self.FinalEvasion=self.BaseEvasion=Evasion
        self.FinalCost=self.BaseCost=Cost

        self.FinalArmor=self.FinalShield=self.Power=0
        self.BaseShield=0
        self.FinalSpeed=self.BaseSpeed=Speed
        self.FinalEvasion=self.BaseEvasion=Evasion
        self.BonusTracking=0
        self.FinalArmor=self.FinalSheild=self.Power=0

        self.Reactor=Modules.Slot("CR",self)
        self.Sensors=Modules.Slot("CS",self)
        self.Hiperdrive=Modules.Slot("CH",self)
        self.Thrusters=Modules.Slot("CT",self)
        self.AI=Modules.Slot("CAI",self)
        self.Aura=None
        self.Name=""
        self.Modules=[]

    def Save(self):
        #Check add
        file=open("Data/Save/Ships/"+self.Class+"/"+"Ships.txt","r")
        n=0
        try:
            n=int(file.readline())
        except:
            n=0
        f=True
        for i in range(n):
            if(file.readline()[:-5]==self.Name):
                f=False
                break
        file.close()
        if(f):
            if(n==0):
                file=open("Data/Save/Ships/"+self.Class+"/"+"Ships.txt","w")
                file.write(str(1)+"\n")
                file.write(self.Name+".txt"+"\n")
                file.close()
            else:
                file=open("Data/Save/Ships/"+self.Class+"/"+"Ships.txt","r")
                file.readline()
                txt=file.read()
                file.close()
                file=open("Data/Save/Ships/"+self.Class+"/"+"Ships.txt","w")
                file.write(str(n+1)+"\n")
                file.write(txt)
                file.write(self.Name+".txt"+"\n")
            ## TODO:  ADD n++
            None
        del(f)
        ########
        File=open("Data/Save/Ships/"+self.Class+"/"+self.Name+".txt","w")
        File.write(self.Class+"\n")
        File.write(self.Name+"\n")
        File.write("\n")
        self.Reactor.Save(File)
        self.Hiperdrive.Save(File)
        self.Thrusters.Save(File)
        self.Sensors.Save(File)
        self.AI.Save(File)
        ##move to specific ship
        ##if(self.Aura):
        ##    self.Aura.Save(File)
        File.write("\n")
        return File
    def SetName(self,Name):
        self.Name=Name

    def Reset(self):
        None
        self.FinalHull=self.BaseHull
        self.FinalSpeed=self.BaseSpeed
        self.FinalEvasion=self.BaseEvasion

        self.FinalCost=self.BaseCost

        self.FinalArmor=self.Armor=0
        self.FinalShield=self.Shield=0
        self.Power=0
        self.BonusTracking=0

        #Overrive AND Call in Class
    OnBuild=None
    def Build(self):
        #Clear

        self.Reset()
        #Rebuild
        self.Reactor.Build()
        self.Hiperdrive.Build()
        self.Thrusters.Build()
        self.Sensors.Build()
        self.AI.Build()
        for M in self.Modules:
            M.Build()
        #checks if it can be builded
        # pree save
        None
        if(self.OnBuild):
            self.OnBuild[0](*self.OnBuild[1])

    def Print(self):
        if(self.Name!=""):
            print(self.Name)
        else:
            print("No Name")
        print()
        self.Reactor.Print()
        self.Hiperdrive.Print()
        self.Thrusters.Print()
        self.Sensors.Print()
        self.AI.Print()



    def Load(self,File):
        '''
        First Class_specific load that will call ship_general_load with self reference
        class_specific_load will generate internaly ship instance
        '''
        File.readline()
        self.Name=File.readline()[:-1]

        File.readline()

        self.Reactor.Equip(eval(File.readline()[:-1]))
        self.Hiperdrive.Equip(eval(File.readline()[:-1]))
        self.Thrusters.Equip(eval(File.readline()[:-1]))
        self.Sensors.Equip(eval(File.readline()[:-1]))
        self.AI.Equip(eval(File.readline()[:-1]))

        File.readline()
        None

class Corvete(Ship):
    def __init__(self):#self,Class,MaxHull,Speed,Evasion,ComPoints
        Ship.__init__(self,"Corvete",300,160,60,1,30)
        self.Core=Modules.Slot("MCC",self)
        self.Modules.append(self.Core)

    ##def Reset(self):
    ##    Ship.Reset(self)
    ##    self.Hull=300
    ##    self.Speed=160
    ##    self.Evasion=60

    def Save(self):
        File=Ship.Save(self)
        self.Core.Save(File)
        File.close()

    def Load(File_Name):
        File=open("Data/Save/Ships/Corvete/"+File_Name,"r")
        #print(File)
        S=Corvete()
        Ship.Load(S,File)
        S.Core.Load(File)
        return S
    def Print(self):
        Ship.Print(self)
        print()
        self.Core.Print()


class Destroyer(Ship):
    def __init__(self):#self,Class,MaxHull,Speed,Evasion,ComPoints
        Ship.__init__(self,"Destroyer",800,140,35,2,60)
        self.Bow=Modules.Slot("MDB",self)
        self.Stern=Modules.Slot("MDS",self)
        self.Modules.append(self.Bow)
        self.Modules.append(self.Stern)

    def Reset(self):
        Ship.Reset(self)
        self.Hull=800
        self.Speed=140
        self.Evasion=35

    def Save(self):
        File=Ship.Save(self)
        self.Bow.Save(File)
        self.Stern.Save(File)
        File.close()

    def Load(File_Name):
        File=open("Data/Save/Ships/Destroyer/"+File_Name,"r")
        #print(File)
        S=Destroyer()
        Ship.Load(S,File)
        S.Bow.Load(File)
        S.Stern.Load(File)
        return S
    def Print(self):
        Ship.Print(self)
        print()
        self.Bow.Print()
        self.Stern.Print()


class Cruiser(Ship):
    def __init__(self):#self,Class,MaxHull,Speed,Evasion,ComPoints
        Ship.__init__(self,"Cruiser",1800,120,10,4,120)
        self.Bow=Modules.Slot("MCB",self)
        self.Core=Modules.Slot("MCC",self)
        self.Stern=Modules.Slot("MCS",self)
        self.Modules.append(self.Bow)
        self.Modules.append(self.Core)
        self.Modules.append(self.Stern)

    def Reset(self):
        Ship.Reset(self)
        self.Hull=1800
        self.Speed=120
        self.Evasion=10

    def Save(self):
        File=Ship.Save(self)
        self.Bow.Save(File)
        self.Core.Save(File)
        self.Stern.Save(File)
        File.close()

    def Load(File_Name):
        File=open("Data/Save/Ships/Cruiser/"+File_Name,"r")
        #print(File)
        S=Cruiser()
        Ship.Load(S,File)
        S.Bow.Load(File)
        S.Core.Load(File)
        S.Stern.Load(File)
        return S
    def Print(self):
        Ship.Print(self)
        print()
        self.Bow.Print()
        self.Core.Print()
        self.Stern.Print()

class Battleship(Ship):
    def __init__(self):#self,Class,MaxHull,Speed,Evasion,ComPoints
        Ship.__init__(self,"Battleship",3000,100,5,8,240)
        self.Bow=Modules.Slot("MBB",self)
        self.Core=Modules.Slot("MBC",self)
        self.Stern=Modules.Slot("MBS",self)
        self.Modules.append(self.Bow)
        self.Modules.append(self.Core)
        self.Modules.append(self.Stern)

    def Reset(self):
        Ship.Reset(self)
        self.Hull=3000
        self.Speed=100
        self.Evasion=5

    def Save(self):
        File=Ship.Save(self)
        self.Bow.Save(File)
        self.Core.Save(File)
        self.Stern.Save(File)
        File.close()

    def Load(File_Name):
        File=open("Data/Save/Ships/Battleship/"+File_Name,"r")
        #print(File)
        S=Battleship()
        Ship.Load(S,File)
        S.Bow.Load(File)
        S.Core.Load(File)
        S.Stern.Load(File)
        return S
    def Print(self):
        Ship.Print(self)
        print()
        self.Bow.Print()
        self.Core.Print()
        self.Stern.Print()
