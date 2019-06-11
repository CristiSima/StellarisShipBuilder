class Component:
    def __init__(self,Type,Name,PowerCons,Ship):
        self.Type=Type
        self.Name=Name
        self.PowerCons=PowerCons
        self.Ship=Ship
    def Tick(self):
        None
    def Print(self):
        print(self.Name)
    def Effect1(self):
        None
    def Effect2(self):
        None
    def Build(self):
        self.Ship.Power-=self.PowerCons
        self.Effect1()

class Reactor(Component):
    Type="CR"
    def __init__(self,Name,PowerGen,Ship):
        Component.__init__(self,"CR",Name,-PowerGen,Ship)

class Reactors:
    class Corvete:
        class Reactor_T1(Reactor):
            Name="Fusion"
            Info=["Power +75"]
            def __init__(self,Ship):
                Reactor.__init__(self,"Fission Reactor",75,Ship)
        Variants=[Reactor_T1]

class Hiperdrive(Component):
    Type="CH"
    def __init__(self,Name,PowerCons,Ship):
        Component.__init__(self,"CD",Name,PowerCons,Ship)

class Hiperdrives:
    class Hiperdrive_T1(Hiperdrive):
        Name="Hiperdrive"
        Info=["FTL"]
        def __init__(self,Ship):
            Hiperdrive.__init__(self,"Hyper Drive I",10,Ship)
    Variants=[Hiperdrive_T1]
class Thruster(Component):
    Type="CT"
    def __init__(self,Name,PowerCons,Ship,SpeedMod,EvasionExtra):
        Component.__init__(self,"CT",Name,PowerCons,Ship)
        self.SpeedMod=SpeedMod
        self.EvasionExtra=EvasionExtra
    def Effect1(self):
<<<<<<< HEAD
        self.Ship.FinalSpeed+=self.Ship.Speed*self.SpeedMod
        self.Ship.FinalEvasion+=self.EvasionExtra
=======
        self.Ship.ExtraSpeed+=self.Ship.Speed*self.SpeedMod
        self.Ship.ExtraEvasion+=self.EvasionExtra
>>>>>>> refs/remotes/origin/master

class Thrusters:
    class Corvete:
        class Thruster_T1(Thruster):
            Name="Chemical"
            Info=["Power Drain: 10",]
            def __init__(self,Ship):
                Thruster.__init__(self,"Chemical Thrusters",10,Ship,0,0)
        Variants=[Thruster_T1]
class Sensor(Component):
    Type="CS"
    def __init__(self,Name,PowerCons,Ship,ExtraTracking):
        Component.__init__(self,"CS",Name,PowerCons,Ship)
        self.ExtraTracking=ExtraTracking
    def Effect1(self):
<<<<<<< HEAD
        #Global Modifier
        #self.Ship.FinalTracking+=self.ExtraTracking
        None
=======
        self.Ship.FinalTracking+=self.ExtraTracking
>>>>>>> refs/remotes/origin/master
class Sensors:
    class Sensor_T1(Sensor):
        Type="CS"
        Name="Radar"
        Info=["Old Teck"]
        def __init__(self,Ship):
            Sensor.__init__(self,"Radar System",5,Ship,0)
    Variants=[Sensor_T1]
