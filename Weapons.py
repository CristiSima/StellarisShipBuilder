'''
Range:int
Time : 1 day=10 Tick
Acuracy Tracking 0-100
'''

class Weapon:
    def __init__(self,Ship,Type,DmgType,Name,Range,Cooldown,Accuracy,Tracking,DmgMin,DmgMax,PowerCons):
        self.Ship=Ship
        self.Type=Type
        self.DmgType=DmgType
        self.Name=Name
        self.Range=range
        self.Cooldown=Cooldown
        self.Tracking=Tracking
        self.Accuracy=Accuracy
        self.DmgMin=DmgMin
        self.DmgMax=DmgMax
        self.PowerCons=PowerCons
        self.Target=None
        self.Wait4=0
<<<<<<< HEAD
    def Build(self):
        self.Ship.Power-=self.PowerCons 
=======
>>>>>>> refs/remotes/origin/master
    def Print(self):
        print(self.Name)
    def GetTarget(self,Targets):
        if(self.Target):
            if(self.Target.Alive):
                return

        for T in Targets:
            ## TODO:  Range check
            if(True):
                self.Target=T
                return

    def Attack(self):
        None

    def CheckAttack(self):
        if(self.Wait4==0):
            self.Attack()
            ## TODO: Attack
            self.Wait4-=1
        else:
            self.Wait4=self.Cooldown
class Empty(Weapon):
    def __init__(self,Ship):
        weapon.__init__(self,Ship,"","",0,0,0,0,0,0,0)
    def GetTarget(self,Targets):
        None
    def CheckAttack(self):
        None
class Energy(Weapon):
    def __init__(self,Ship,Type,Name,Range,Cooldown,Accuracy,Tracking,DmgMin,DmgMax,PowerCons):
        Weapon.__init__(self,Ship,Type,"Energy",Name,Range,Cooldown,Accuracy,Tracking,DmgMin,DmgMax,PowerCons)
#Kinetic

#Explosive
class Explosive(Weapon):
    ## TODO:  ADD Projectiles
    def __init__(self,Ship,Name,Range,Cooldown,Acuracy,Tracking,DmgMin,DmgMax,PowerCons,Evasion):
        Weapon.__init__(self,Ship,"WG","Explosive",Name,Range,Cooldown,Acuracy,Tracking,DmgMin,DmgMax,PowerCons)
        self.Evasion=Evasion

#Stike Craft

#point def
class PointDef(Weapon):
    def __init__(self,Ship,Name,Range,Cooldown,Acuracy,Tracking,DmgMin,DmgMax,PowerCons):
        Weapon.__init__(self,Ship,"WP","PointDef",Name,Range,Cooldown,Acuracy,Tracking,DmgMin,DmgMax,PowerCons)

#Titanic

class Laser(Energy):
    def __init__(self,Ship,Type,Name,Range,Tracking,DmgMin,DmgMax,PowerCons):
        Energy.__init__(self,Ship,Type,Name,Range,46,90,Tracking,DmgMin,DmgMax,PowerCons)
    def Attack(self):
        ## Shield:0.5
        ## Armor: 1.5
        ## Hull : 1
        None
class Missile(Explosive):
    def __init__(self,Ship,Name,DmgMin,DmgMax,PowerCons,Evasion):
        Explosive.__init__(self,Ship,Name,100,68,100,100,DmgMin,DmgMax,PowerCons,Evasion)
class Point_Def(PointDef):
    def __init__(self,Ship,Name,Range,Tracking,DmgMin,DmgMax,PowerCons):
        PointDef.__init__(self,Ship,Name,Range,5,75,Tracking,DmgMin,DmgMax,PowerCons)
    def Attack():
        ## Shield:1
        ## Armor: 0.25
        ## Hull : 1
        None
class Small:
    class Lasers:
        Name="Laser"
        Info=["Small Laser","Shield dmg * 1.5","Armor dmg *1.5"]
        class Laser_T1(Laser):
            Type="WS"
            Name="Blue Laser"
            Info=["Small Laser","Shield dmg * 1.5","Armor dmg *1.5","Dmg:6-16"]
            def __init__(self,Ship):
                Laser.__init__(self,Ship,"WS","Red Laser",40,50,6,16,5)
        Variants=[Laser_T1]
    Variants=[Lasers]
class Explosives:
    class Missiles:
        Name="Misiles"
        Info=["Ignore Shields","Hull dmg *1.25"]
        class Missile_T1(Missile):
            Type="WG"
            Name="Nuclear"
            Info=["Ignore Shields","Hull dmg *1.25","Dmg: 30-40"]
            def __init__(self,Ship):
                Missile.__init__(self,Ship,"Nuclear",30,40,10,0)
        Variants=[Missile_T1]
    Variants=[Missiles]
class Point:
    class Point_Defs:
        Name="Point Defense"
        Info=["armor dmg *0.25",]
        class Point_Def_T1(Point_Def):
            Name="Sentinel"
            Info=["armor dmg *0.25","Dmg: 1-4"]
            Type="WP"
            def __init__(self,Ship):
                Point_Def.__init__(self,Ship,"Sentinel",30,19,1,4,5)
        Variants=[Point_Def_T1]
    Variants=[Point_Defs]
