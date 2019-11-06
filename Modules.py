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
            if(self.Type[1]=="M"):
                return Weapons.Medium
            if(self.Type[1]=="L"):
                return Weapons.Large
            if(self.Type[1]=="P"):
                return Weapons.Point
            if(self.Type[1]=="G"):
                return Weapons.Explosives
        if(self.Type[0]=="U"):
            if(self.Type[1]=="S"):
                return Utilitys.Small
            if(self.Type[1]=="M"):
                return Utilitys.Medium
            if(self.Type[1]=="L"):
                return Utilitys.Large
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

'''
Type="TYPE"
Name="Artillery"
Info=["Weapons: ","Utilitys: "]
def __init__(self,Ship):
    Module.__init__(self,"TYPE","Artillery",Ship)
    self.Weapon=Slot("W",Ship)

    self.Utility=Slot("U",Ship)
'''
class Corvete:
    class Core:
        Type="MCC"
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
    Variants=[Core]
class Destroyer:
    class Bow:
        Type="MDB"
        class Artillery(Module):
            Type="MDB"
            Name="Artillery"
            Info=["Weapons: 1L","Utilitys: 6S"]
            def __init__(self,Ship):
                Module.__init__(self,"MDB","Artillery",Ship)
                self.Weapon1=Slot("WL",Ship)

                self.Utility1=Slot("US",Ship)
                self.Utility2=Slot("US",Ship)
                self.Utility3=Slot("US",Ship)
                self.Utility4=Slot("US",Ship)
                self.Utility5=Slot("US",Ship)
                self.Utility6=Slot("US",Ship)
        class Gunship(Module):
            Type="MDB"
            Name="Gunship"
            Info=["Weapons: 2S 1M","Utilitys: 6S"]
            def __init__(self,Ship):
                Module.__init__(self,"MDB","Gunship",Ship)
                self.Weapon1=Slot("WM",Ship)
                self.Weapon2=Slot("WS",Ship)
                self.Weapon3=Slot("WS",Ship)

                self.Utility1=Slot("US",Ship)
                self.Utility2=Slot("US",Ship)
                self.Utility3=Slot("US",Ship)
                self.Utility4=Slot("US",Ship)
                self.Utility5=Slot("US",Ship)
                self.Utility6=Slot("US",Ship)
        class PicketShip(Module):
            Type="MDB"
            Name="Picket Ship"
            Info=["Weapons: 2S 1P","Utilitys: 6S"]
            def __init__(self,Ship):
                Module.__init__(self,"MDB","Picket Ship",Ship)
                self.Weapon1=Slot("WP",Ship)
                self.Weapon2=Slot("WS",Ship)
                self.Weapon3=Slot("WS",Ship)

                self.Utility1=Slot("US",Ship)
                self.Utility2=Slot("US",Ship)
                self.Utility3=Slot("US",Ship)
                self.Utility4=Slot("US",Ship)
                self.Utility5=Slot("US",Ship)
                self.Utility6=Slot("US",Ship)

        Variants=[Artillery,Gunship,PicketShip]
    class Stern:
        Type="MDS"
        class Gunship(Module):
            Type="MDS"
            Name="Gunship"
            Info=["Weapons: 1M","Utilitys: 1A"]
            def __init__(self,Ship):
                Module.__init__(self,"MDS","Gunship",Ship)
                self.Weapon1=Slot("WM",Ship)

                self.Utility1=Slot("UA",Ship)
        class Interceptor(Module):
            Type="MDS"
            Name="Interceptor"
            Info=["Weapons: 2S","Utilitys: 1A"]
            def __init__(self,Ship):
                Module.__init__(self,"MDS","Interceptor",Ship)
                self.Weapon1=Slot("WS",Ship)
                self.Weapon2=Slot("WS",Ship)

                self.Utility1=Slot("UA",Ship)
        class PicketShip(Module):
            Type="MDS"
            Name="Picket Ship"
            Info=["Weapons: 2P","Utilitys: 1A"]
            def __init__(self,Ship):
                Module.__init__(self,"MDS","Picket Ship",Ship)
                self.Weapon1=Slot("WP",Ship)
                self.Weapon2=Slot("WP",Ship)

                self.Utility1=Slot("UA",Ship)

        Variants=[Gunship,Interceptor,PicketShip]
    Variants=[Bow,Stern]

class Cruiser:
    class Bow:
        Type="MCB"
        class Artillery(Module):
            Type="MCB"
            Name="Artillery"
            Info=["Weapons: 1L ","Utilitys: 4M"]
            def __init__(self,Ship):
                Module.__init__(self,"MCB","Artillery",Ship)
                self.Weapon1=Slot("WL",Ship)

                self.Utility1=Slot("UM",Ship)
                self.Utility2=Slot("UM",Ship)
                self.Utility3=Slot("UM",Ship)
                self.Utility4=Slot("UM",Ship)

        class Broadside(Module):
            Type="MCB"
            Name="Broadside"
            Info=["Weapons: 2M ","Utilitys: 4M"]
            def __init__(self,Ship):
                Module.__init__(self,"MCB","Broadside",Ship)
                self.Weapon1=Slot("WM",Ship)
                self.Weapon2=Slot("WM",Ship)

                self.Utility1=Slot("UM",Ship)
                self.Utility2=Slot("UM",Ship)
                self.Utility3=Slot("UM",Ship)
                self.Utility4=Slot("UM",Ship)

        class Torpedo(Module):
            Type="MCB"
            Name="Torpedo"
            Info=["Weapons: 2S 1G ","Utilitys: 4M"]
            def __init__(self,Ship):
                Module.__init__(self,"MCB","Torpedo",Ship)
                self.Weapon1=Slot("WS",Ship)
                self.Weapon2=Slot("WS",Ship)
                self.Weapon3=Slot("WG",Ship)

                self.Utility1=Slot("UM",Ship)
                self.Utility2=Slot("UM",Ship)
                self.Utility3=Slot("UM",Ship)
                self.Utility4=Slot("UM",Ship)

        Variants=[Artillery,Broadside,Torpedo]
    class Core:
        Type="MCC"
        class Artillery(Module):
            Type="MCC"
            Name="Artillery"
            Info=["Weapons: 1L 1M","Utilitys: 4M"]
            def __init__(self,Ship):
                Module.__init__(self,"MCC","Artillery",Ship)
                self.Weapon1=Slot("WL",Ship)
                self.Weapon2=Slot("WM",Ship)

                self.Utility1=Slot("UM",Ship)
                self.Utility2=Slot("UM",Ship)
                self.Utility3=Slot("UM",Ship)
                self.Utility4=Slot("UM",Ship)

        class Broadside(Module):
            Type="MCC"
            Name="Broadside"
            Info=["Weapons: 3M","Utilitys: 4M"]
            def __init__(self,Ship):
                Module.__init__(self,"MCC","Broadside",Ship)
                self.Weapon1=Slot("WM",Ship)
                self.Weapon2=Slot("WM",Ship)
                self.Weapon3=Slot("WM",Ship)

                self.Utility1=Slot("UM",Ship)
                self.Utility2=Slot("UM",Ship)
                self.Utility3=Slot("UM",Ship)
                self.Utility4=Slot("UM",Ship)

        class Hangar(Module):
            Type="MCC"
            Name="Hangar"
            Info=["Weapons: 2P 1H","Utilitys: 4M"]
            def __init__(self,Ship):
                Module.__init__(self,"MCC","Hangar",Ship)
                self.Weapon1=Slot("WP",Ship)
                self.Weapon2=Slot("WP",Ship)
                self.Weapon3=Slot("WH",Ship)

                self.Utility1=Slot("UM",Ship)
                self.Utility2=Slot("UM",Ship)
                self.Utility3=Slot("UM",Ship)
                self.Utility4=Slot("UM",Ship)

        class Torpedo(Module):
            Type="MCC"
            Name="Torpedo"
            Info=["Weapons: 2S 2G","Utilitys: 4M"]
            def __init__(self,Ship):
                Module.__init__(self,"MCC","Torpedo",Ship)
                self.Weapon1=Slot("WS",Ship)
                self.Weapon2=Slot("WS",Ship)
                self.Weapon3=Slot("WG",Ship)
                self.Weapon4=Slot("WG",Ship)

                self.Utility1=Slot("UM",Ship)
                self.Utility2=Slot("UM",Ship)
                self.Utility3=Slot("UM",Ship)
                self.Utility4=Slot("UM",Ship)

        Variants=[Artillery,Broadside,Hangar,Torpedo]
    class Stern:
        Type="MCS"
        class Broadside(Module):
            Type="MCS"
            Name="Broadside"
            Info=["Weapons: 1M","Utilitys: 2A"]
            def __init__(self,Ship):
                Module.__init__(self,"MCC","Broadside",Ship)
                self.Weapon1=Slot("WM",Ship)

                self.Utility1=Slot("UA",Ship)
                self.Utility2=Slot("UA",Ship)

        class Gunship(Module):
            Type="MCC"
            Name="Gunship"
            Info=["Weapons: 2S","Utilitys: 2A"]
            def __init__(self,Ship):
                Module.__init__(self,"MCC","Gunship",Ship)
                self.Weapon1=Slot("WS",Ship)
                self.Weapon2=Slot("WS",Ship)

                self.Utility1=Slot("UA",Ship)
                self.Utility2=Slot("UA",Ship)


        Variants=[Broadside,Gunship]
    Variants=[Bow,Core,Stern]

class Battleship:
    class Bow:
        Type="MBB"
        class Artillery(Module):
            Type="MBB"
            Name="Artillery"
            Info=["Weapons: 2L","Utilitys: 3L"]
            def __init__(self,Ship):
                Module.__init__(self,"MBB","Artillery",Ship)
                self.Weapon1=Slot("WL",Ship)
                self.Weapon2=Slot("WL",Ship)

                self.Utility1=Slot("UL",Ship)
                self.Utility2=Slot("UL",Ship)
                self.Utility3=Slot("UL",Ship)

        class Broadside(Module):
            Type="MBB"
            Name="Broadside"
            Info=["Weapons: 2S 1M 1L","Utilitys: 2A"]
            def __init__(self,Ship):
                Module.__init__(self,self.Type,self.Name,Ship)
                self.Weapon1=Slot("WS",Ship)
                self.Weapon2=Slot("WS",Ship)
                self.Weapon3=Slot("WM",Ship)
                self.Weapon4=Slot("WL",Ship)

                self.Utility1=Slot("UL",Ship)
                self.Utility2=Slot("UL",Ship)
                self.Utility3=Slot("UL",Ship)

        class Hangar(Module):
            Type="MBB"
            Name="Hangar"
            Info=["Weapons: 1M 2P 1H","Utilitys: 3L"]
            def __init__(self,Ship):
                Module.__init__(self,self.Type,self.Name,Ship)
                self.Weapon1=Slot("WM",Ship)
                self.Weapon2=Slot("WP",Ship)
                self.Weapon3=Slot("WP",Ship)
                self.Weapon4=Slot("WH",Ship)

                self.Utility1=Slot("UL",Ship)
                self.Utility2=Slot("UL",Ship)
                self.Utility3=Slot("UL",Ship)

        class SpinalMount(Module):
            Type="MBB"
            Name="Spinal Mount"
            Info=["Weapons: 1X","Utilitys: 3L"]
            def __init__(self,Ship):
                Module.__init__(self,self.Type,self.Name,Ship)
                self.Weapon1=Slot("WX",Ship)

                self.Utility1=Slot("UL",Ship)
                self.Utility2=Slot("UL",Ship)
                self.Utility3=Slot("UL",Ship)

        Variants=[Artillery,Broadside,Hangar,SpinalMount]
    class Core:
        Type="MBC"
        class Artillery(Module):
            Type="MBC"
            Name="Artillery"
            Info=["Weapons: 3L","Utilitys: 3L"]
            def __init__(self,Ship):
                Module.__init__(self,self.Type,self.Name,Ship)
                self.Weapon1=Slot("WL",Ship)
                self.Weapon2=Slot("WL",Ship)
                self.Weapon3=Slot("WL",Ship)

                self.Utility1=Slot("UL",Ship)
                self.Utility2=Slot("UL",Ship)
                self.Utility3=Slot("UL",Ship)

        class Broadside(Module):
            Type="MBC"
            Name="Broadside"
            Info=["Weapons: 2M 2L","Utilitys: 3L"]
            def __init__(self,Ship):
                Module.__init__(self,self.Type,self.Name,Ship)
                self.Weapon1=Slot("WM",Ship)
                self.Weapon2=Slot("WM",Ship)
                self.Weapon3=Slot("WL",Ship)
                self.Weapon4=Slot("WL",Ship)

                self.Utility1=Slot("UL",Ship)
                self.Utility2=Slot("UL",Ship)
                self.Utility3=Slot("UL",Ship)

        class Carrier(Module):
            Type="MBC"
            Name="Carrier"
            Info=["Weapons: 2S 2P 2H","Utilitys: 3L"]
            def __init__(self,Ship):
                Module.__init__(self,self.Type,self.Name,Ship)
                self.Weapon1=Slot("WS",Ship)
                self.Weapon2=Slot("WS",Ship)
                self.Weapon3=Slot("WP",Ship)
                self.Weapon4=Slot("WP",Ship)
                self.Weapon5=Slot("WH",Ship)
                self.Weapon6=Slot("WH",Ship)

                self.Utility1=Slot("UL",Ship)
                self.Utility2=Slot("UL",Ship)
                self.Utility3=Slot("UL",Ship)

        class Hangar(Module):
            Type="MBC"
            Name="Hangar"
            Info=["Weapons: 4M 1H","Utilitys: 3L"]
            def __init__(self,Ship):
                Module.__init__(self,self.Type,self.Name,Ship)
                self.Weapon1=Slot("WM",Ship)
                self.Weapon2=Slot("WM",Ship)
                self.Weapon3=Slot("WM",Ship)
                self.Weapon4=Slot("WM",Ship)
                self.Weapon5=Slot("WH",Ship)

                self.Utility1=Slot("UL",Ship)
                self.Utility2=Slot("UL",Ship)
                self.Utility3=Slot("UL",Ship)

        Variants=[Artillery,Broadside,Carrier,Hangar]
    class Stern:
        Type="MBS"
        class Artillery(Module):
            Type="MBS"
            Name="Artillery"
            Info=["Weapons: 1L","Utilitys: 2A"]
            def __init__(self,Ship):
                Module.__init__(self,self.Type,self.Name,Ship)
                self.Weapon1=Slot("WL",Ship)

                self.Utility1=Slot("UA",Ship)
                self.Utility2=Slot("UA",Ship)

        class Broadside(Module):
            Type="MBS"
            Name="Broadside"
            Info=["Weapons: 2M","Utilitys: 2A"]
            def __init__(self,Ship):
                Module.__init__(self,self.Type,self.Name,Ship)
                self.Weapon1=Slot("WM",Ship)
                self.Weapon2=Slot("WM",Ship)

                self.Utility1=Slot("UA",Ship)
                self.Utility2=Slot("UA",Ship)

        Variants=[Artillery,Broadside]
    Variants=[Bow,Core,Stern]
if(__loader__!="Modules"):
    import Modules
    import Utilitys
    import Weapons
    import Components
