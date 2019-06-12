class Module:
    def __init__(self,Type,Name,Ship):
        self.Name=Name
        self.Type=Type
        self.Ship=Ship
        self.Weapon1=self.Weapon2=self.Weapon3=self.Weapon4=self.Weapon5=self.Weapon6=None
        self.Utility1=self.Utility2=self.Utility3=self.Utility4=self.Utility5=self.Utility6=None
    def Save(self,File):
        #File.write(str(type(self))[8:-2]+"\n")

        if(self.Weapon1):
            self.Weapon1.Save(File)
        if(self.Weapon2):
            self.Weapon2.Save(File)
        if(self.Weapon3):
            self.Weapon3.Save(File)
        if(self.Weapon4):
            self.Weapon4.Save(File)
        if(self.Weapon5):
            self.Weapon5.Save(File)
        if(self.Weapon6):
            self.Weapon6.Save(File)
        File.write("\n")
        if(self.Utility1):
            self.Utility1.Save(File)
        if(self.Utility2):
            self.Utility2.Save(File)
        if(self.Utility3):
            self.Utility3.Save(File)
        if(self.Utility4):
            self.Utility4.Save(File)
        if(self.Utility5):
            self.Utility5.Save(File)
        if(self.Utility6):
            self.Utility6.Save(File)
        File.write("\n")

    def Load(self,File):

        if(self.Weapon1):
            self.Weapon1.Load(File)
        if(self.Weapon2):
            self.Weapon2.Load(File)
        if(self.Weapon3):
            self.Weapon3.Load(File)
        if(self.Weapon4):
            self.Weapon4.Load(File)
        if(self.Weapon5):
            self.Weapon5.Load(File)
        if(self.Weapon6):
            self.Weapon6.Load(File)

        File.readline()
        if(self.Utility1):
            self.Utility1.Load(File)
        if(self.Utility2):
            self.Utility2.Load(File)
        if(self.Utility3):
            self.Utility3.Load(File)
        if(self.Utility4):
            self.Utility4.Load(File)
        if(self.Utility5):
            self.Utility5.Load(File)
        if(self.Utility6):
            self.Utility6.Load(File)
    def Print(self):
        print(self.Name)
        print()
        if(self.Weapon1):
            self.Weapon1.Print()
        if(self.Weapon2):
            self.Weapon2.Print()
        if(self.Weapon3):
            self.Weapon3.Print()
        if(self.Weapon4):
            self.Weapon4.Print()
        if(self.Weapon5):
            self.Weapon5.Print()
        if(self.Weapon6):
            self.Weapon6.Print()
        print()
        if(self.Utility1):
            self.Utility1.Print()
        if(self.Utility2):
            self.Utility2.Print()
        if(self.Utility3):
            self.Utility3.Print()
        if(self.Utility4):
            self.Utility4.Print()
        if(self.Utility5):
            self.Utility5.Print()
        if(self.Utility6):
            self.Utility6.Print()
        print()
        print()


    def Build(self):
        if(self.Weapon1):
            self.Weapon1.Build()
        if(self.Weapon2):
            self.Weapon2.Build()
        if(self.Weapon3):
            self.Weapon3.Build()
        if(self.Weapon4):
            self.Weapon4.Build()
        if(self.Weapon5):
            self.Weapon5.Build()
        if(self.Weapon6):
            self.Weapon6.Build()

        if(self.Utility1):
            self.Utility1.Build()
        if(self.Utility2):
            self.Utility2.Build()
        if(self.Utility3):
            self.Utility3.Build()
        if(self.Utility4):
            self.Utility4.Build()
        if(self.Utility5):
            self.Utility5.Build()
        if(self.Utility6):
            self.Utility6.Build()



class Slot:
    def __init__(self,Type,Ship):
        self.Type=Type
        self.Ship=Ship
        ### AB
        ### A=[W(Weapon),U(Utility),M(Module)]
        ### B: Specific subtype
        ###
        ###
        self.Thing=None
    def Equip(self,Thing):
        if(Thing):
            if(Thing=="None"):
                return
            if(self.Type==Thing.Type):
                self.Thing=Thing(self.Ship)
                self.Ship.Build()

    def Target(self):
        if(self.Type[0]=="W"):
            if(self.Type[1]=="S"):
                return Weapons.Small
            if(self.Type[1]=="P"):
                return Weapons.Point
            if(self.Type[1]=="G"):
                return Weapons.Explosives
        if(self.Type[0]=="U"):
            if(self.Type[1]=="S"):
                return Utilitys.Small
            if(self.Type[1]=="A"):
                return Utilitys.Auxilary
        print("ERRRROR")
        print("ERRRROR")
        print("ERRRROR")
        print("ERRRROR")
        print("ERRRROR")

    def Save(self,File):
        '''
        if(self.Type[0]=='M'):
            self.Thing.Save(File)
        else:
            if(self.Thing):
                File.write(str(type(self.Thing))[8:-2]+"\n")
            else:
                File.write("None"+"\n")
        '''
        if(self.Thing):
            File.write(str(type(self.Thing))[8:-2]+"\n")
            if(self.Type[0]=='M'):
                self.Thing.Save(File)
        else:
            File.write("None"+'\n')
    def Print(self):
        if(self.Thing):
            self.Thing.Print()
        else:
            print("None")
    def Load(self,File):
        None
        '''

        '''
        self.Equip(eval(File.readline()[:-1]))
        if(self.Thing   and  self.Type[0]=="M"):
            self.Thing.Load(File)
    def Build(self):
        if(self.Thing):
            self.Thing.Build()
class Corvete:
    class Core:
        class Interceptor(Module):
            Type="MCC"
            Name="Interceptor"
            Info=["Weapons: 3S","Utility: 3S 1A"]
            def __init__(self,Ship):
                Module.__init__(self,"MCC","Interceptor",Ship)
                self.Weapon1=Slot("WS",Ship)
                self.Weapon2=Slot("WS",Ship)
                self.Weapon3=Slot("WS",Ship)

                self.Utility1=Slot("US",Ship)
                self.Utility2=Slot("US",Ship)
                self.Utility3=Slot("US",Ship)
                self.Utility4=Slot("UA",Ship)

        class MissileBoat(Module):
            Type="MCC"
            Name="Missile Boat"
            Info=["Weapons: 1S 1G","Utility: 3S 1A"]
            def __init__(self,Ship):
                Module.__init__(self,"MCC","Missile Boat",Ship)
                self.Weapon1=Slot("WS",Ship)
                self.Weapon2=Slot("WG",Ship)

                self.Utility1=Slot("US",Ship)
                self.Utility2=Slot("US",Ship)
                self.Utility3=Slot("US",Ship)
                self.Utility4=Slot("UA",Ship)

        class PicketShip(Module):
            Type="MCC"
            Name="Picket Ship"
            Info=["Weapons: 2S 1P","Utility: 3S 1A"]
            def __init__(self,Ship):
                Module.__init__(self,"MCC","Picket Ship",Ship)
                self.Weapon1=Slot("WS",Ship)
                self.Weapon2=Slot("WS",Ship)
                self.Weapon3=Slot("WP",Ship)

                self.Utility1=Slot("US",Ship)
                self.Utility2=Slot("US",Ship)
                self.Utility3=Slot("US",Ship)
                self.Utility4=Slot("UA",Ship)

        Variants=[Interceptor,MissileBoat,PicketShip]
if(__loader__!="Modules"):
    import Modules
    import Utilitys
    import Weapons
    import Components
