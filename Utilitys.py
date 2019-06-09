class Utility:
    def __init__(self,Ship,Name,Type,PowerCons):
        self.Ship=Ship
        self.Name=Name
        self.Type=Type
        self.PowerCons=PowerCons

    def Tick(self):
        None
    def Print(self):
        print(self.Name)
    def Effect1(self):
        None
    def Effect2(self):
        None
class Shield(Utility):
    def __init__(self,Ship,Name,Type,ExtraShield,PowerCons):
        Utility.__init__(self,Ship,Name,Type,PowerCons)
        self.ExtraShield=ExtraShield
    def Effect1(self):
        self.Ship.FinalShield+=self.ExtraShield

class Small:
    class Shields:
        Name="Shield"
        Info=["Small Shield","Increase Shield Capacity"]
        class Shield_T1(Shield):
            Type="US"
            Name="Shield"
            Info=["Small Shield","Shield +50","Power Cons: 15"]
            def __init__(self,Ship):
                Shield.__init__(self,Ship,"Deflector","US",50,15)
        Variants=[Shield_T1]
    Variants=[Shields]
class Auxilary:
    class ReactorBuster:
        Name="Reactor Buster"
        Info=["Reactor Buster","Generates Power"]
        class ReactorBuster_T1(Utility):
            Type="UA"
            Name="Reactor Buster"
            Info=["Reactor Buster","Powe +20"]
            def __init__(self,Ship):
                Utility.__init__(self,Ship,"Reactor Buster","UA",-20)
        Variants=[ReactorBuster_T1,]
    Variants=[ReactorBuster,]
