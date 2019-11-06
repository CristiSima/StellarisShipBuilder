class Component:
    def __init__(self,Type,Name,PowerCons,Cost,Ship):
        self.Type=Type
        self.Name=Name
        self.PowerCons=PowerCons
        self.Cost=Cost
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
        self.Ship.FinalCost+=self.Cost
        self.Effect1()

class Reactor(Component):
    Type="CR"
    def __init__(self,Name,PowerGen,Cost,Ship):
        Component.__init__(self,"CR",Name,-PowerGen,Cost,Ship)

class Reactors:
    class Corvete:
        class Reactor_T1(Reactor):
            Name="Fission"
            power_gen=75
            cost=10
            Info=[Name,"Power +"+str(power_gen),"Cost: "+str(cost)]
            def __init__(self,Ship):
                Reactor.__init__(self,"Fission Reactor",self.power_gen,self.cost,Ship)
        class Reactor_T2(Reactor):
            Name="Fusion"
            power_gen=100
            cost=13
            Info=[Name,"Power +"+str(power_gen),"Cost: "+str(cost)]
            def __init__(self,Ship):
                Reactor.__init__(self,"Fission Reactor",self.power_gen,self.cost,Ship)
        class Reactor_T3(Reactor):
            Name="Cold Fussion"
            power_gen=130
            cost=17
            Info=[Name,"Power +"+str(power_gen),"Cost: "+str(cost)]
            def __init__(self,Ship):
                Reactor.__init__(self,"Fission Reactor",self.power_gen,self.cost,Ship)
        class Reactor_T4(Reactor):
            Name="Antimatter"
            power_gen=170
            cost=22
            Info=[Name,"Power +"+str(power_gen),"Cost: "+str(cost)]
            def __init__(self,Ship):
                Reactor.__init__(self,"Fission Reactor",self.power_gen,self.cost,Ship)
        class Reactor_T5(Reactor):
            Name="0-Point"
            power_gen=220
            cost=28
            Info=[Name,"Power +"+str(power_gen),"Cost: "+str(cost)]
            def __init__(self,Ship):
                Reactor.__init__(self,"Fission Reactor",self.power_gen,self.cost,Ship)
        class Reactor_T6(Reactor):
            Name="Dark Matter"
            power_gen=285
            cost=37
            Info=[Name,"Power +"+str(power_gen),"Cost: "+str(cost)]
            def __init__(self,Ship):
                Reactor.__init__(self,"Fission Reactor",self.power_gen,self.cost,Ship)
        Variants=[Reactor_T1,Reactor_T2,Reactor_T3,Reactor_T4,Reactor_T5,Reactor_T6]
    class Destroyer:
        class Reactor_T1(Reactor):
            Name="Fission"
            power_gen=140
            cost=20
            Info=[Name,"Power +"+str(power_gen),"Cost: "+str(cost)]
            def __init__(self,Ship):
                Reactor.__init__(self,"Fission Reactor",self.power_gen,self.cost,Ship)
        class Reactor_T2(Reactor):
            Name="Fusion"
            power_gen=180
            cost=26
            Info=[Name,"Power +"+str(power_gen),"Cost: "+str(cost)]
            def __init__(self,Ship):
                Reactor.__init__(self,"Fission Reactor",self.power_gen,self.cost,Ship)
        class Reactor_T3(Reactor):
            Name="Cold Fussion"
            power_gen=240
            cost=34
            Info=[Name,"Power +"+str(power_gen),"Cost: "+str(cost)]
            def __init__(self,Ship):
                Reactor.__init__(self,"Fission Reactor",self.power_gen,self.cost,Ship)
        class Reactor_T4(Reactor):
            Name="Antimatter"
            power_gen=320
            cost=44
            Info=[Name,"Power +"+str(power_gen),"Cost: "+str(cost)]
            def __init__(self,Ship):
                Reactor.__init__(self,"Fission Reactor",self.power_gen,self.cost,Ship)
        class Reactor_T5(Reactor):
            Name="0-Point"
            power_gen=430
            cost=56
            Info=[Name,"Power +"+str(power_gen),"Cost: "+str(cost)]
            def __init__(self,Ship):
                Reactor.__init__(self,"Fission Reactor",self.power_gen,self.cost,Ship)
        class Reactor_T6(Reactor):
            Name="Dark Matter"
            power_gen=550
            cost=74
            Info=[Name,"Power +"+str(power_gen),"Cost: "+str(cost)]
            def __init__(self,Ship):
                Reactor.__init__(self,"Fission Reactor",self.power_gen,self.cost,Ship)
        Variants=[Reactor_T1,Reactor_T2,Reactor_T3,Reactor_T4,Reactor_T5,Reactor_T6]
    class Cruiser:
        class Reactor_T1(Reactor):
            Name="Fission"
            power_gen=280
            cost=40
            Info=[Name,"Power +"+str(power_gen),"Cost: "+str(cost)]
            def __init__(self,Ship):
                Reactor.__init__(self,"Fission Reactor",self.power_gen,self.cost,Ship)
        class Reactor_T2(Reactor):
            Name="Fusion"
            power_gen=360
            cost=52
            Info=[Name,"Power +"+str(power_gen),"Cost: "+str(cost)]
            def __init__(self,Ship):
                Reactor.__init__(self,"Fission Reactor",self.power_gen,self.cost,Ship)
        class Reactor_T3(Reactor):
            Name="Cold Fussion"
            power_gen=480
            cost=68
            Info=[Name,"Power +"+str(power_gen),"Cost: "+str(cost)]
            def __init__(self,Ship):
                Reactor.__init__(self,"Fission Reactor",self.power_gen,self.cost,Ship)
        class Reactor_T4(Reactor):
            Name="Antimatter"
            power_gen=620
            cost=88
            Info=[Name,"Power +"+str(power_gen),"Cost: "+str(cost)]
            def __init__(self,Ship):
                Reactor.__init__(self,"Fission Reactor",self.power_gen,self.cost,Ship)
        class Reactor_T5(Reactor):
            Name="0-Point"
            power_gen=800
            cost=112
            Info=[Name,"Power +"+str(power_gen),"Cost: "+str(cost)]
            def __init__(self,Ship):
                Reactor.__init__(self,"Fission Reactor",self.power_gen,self.cost,Ship)
        class Reactor_T6(Reactor):
            Name="Dark Matter"
            power_gen=1030
            cost=148
            Info=[Name,"Power +"+str(power_gen),"Cost: "+str(cost)]
            def __init__(self,Ship):
                Reactor.__init__(self,"Fission Reactor",self.power_gen,self.cost,Ship)
        Variants=[Reactor_T1,Reactor_T2,Reactor_T3,Reactor_T4,Reactor_T5,Reactor_T6]
    class Battleship:
        class Reactor_T1(Reactor):
            Name="Fission"
            power_gen=550
            cost=80
            Info=[Name,"Power +"+str(power_gen),"Cost: "+str(cost)]
            def __init__(self,Ship):
                Reactor.__init__(self,"Fission Reactor",self.power_gen,self.cost,Ship)
        class Reactor_T2(Reactor):
            Name="Fusion"
            power_gen=720
            cost=104
            Info=[Name,"Power +"+str(power_gen),"Cost: "+str(cost)]
            def __init__(self,Ship):
                Reactor.__init__(self,"Fission Reactor",self.power_gen,self.cost,Ship)
        class Reactor_T3(Reactor):
            Name="Cold Fussion"
            power_gen=950
            cost=136
            Info=[Name,"Power +"+str(power_gen),"Cost: "+str(cost)]
            def __init__(self,Ship):
                Reactor.__init__(self,"Fission Reactor",self.power_gen,self.cost,Ship)
        class Reactor_T4(Reactor):
            Name="Antimatter"
            power_gen=1250
            cost=176
            Info=[Name,"Power +"+str(power_gen),"Cost: "+str(cost)]
            def __init__(self,Ship):
                Reactor.__init__(self,"Fission Reactor",self.power_gen,self.cost,Ship)
        class Reactor_T5(Reactor):
            Name="0-Point"
            power_gen=1550
            cost=224
            Info=[Name,"Power +"+str(power_gen),"Cost: "+str(cost)]
            def __init__(self,Ship):
                Reactor.__init__(self,"Fission Reactor",self.power_gen,self.cost,Ship)
        class Reactor_T6(Reactor):
            Name="Dark Matter"
            power_gen=2000
            cost=296
            Info=[Name,"Power +"+str(power_gen),"Cost: "+str(cost)]
            def __init__(self,Ship):
                Reactor.__init__(self,"Fission Reactor",self.power_gen,self.cost,Ship)
        Variants=[Reactor_T1,Reactor_T2,Reactor_T3,Reactor_T4,Reactor_T5,Reactor_T6]
    class Titan:
        class Reactor_T1(Reactor):
            Name="Fission"
            power_gen=1100
            cost=160
            Info=[Name,"Power +"+str(power_gen),"Cost: "+str(cost)]
            def __init__(self,Ship):
                Reactor.__init__(self,"Fission Reactor",self.power_gen,self.cost,Ship)
        class Reactor_T2(Reactor):
            Name="Fusion"
            power_gen=1450
            cost=208
            Info=[Name,"Power +"+str(power_gen),"Cost: "+str(cost)]
            def __init__(self,Ship):
                Reactor.__init__(self,"Fission Reactor",self.power_gen,self.cost,Ship)
        class Reactor_T3(Reactor):
            Name="Cold Fussion"
            power_gen=1900
            cost=272
            Info=[Name,"Power +"+str(power_gen),"Cost: "+str(cost)]
            def __init__(self,Ship):
                Reactor.__init__(self,"Fission Reactor",self.power_gen,self.cost,Ship)
        class Reactor_T4(Reactor):
            Name="Antimatter"
            power_gen=2500
            cost=352
            Info=[Name,"Power +"+str(power_gen),"Cost: "+str(cost)]
            def __init__(self,Ship):
                Reactor.__init__(self,"Fission Reactor",self.power_gen,self.cost,Ship)
        class Reactor_T5(Reactor):
            Name="0-Point"
            power_gen=3200
            cost=448
            Info=[Name,"Power +"+str(power_gen),"Cost: "+str(cost)]
            def __init__(self,Ship):
                Reactor.__init__(self,"Fission Reactor",self.power_gen,self.cost,Ship)
        class Reactor_T6(Reactor):
            Name="Dark Matter"
            power_gen=4200
            cost=592
            Info=[Name,"Power +"+str(power_gen),"Cost: "+str(cost)]
            def __init__(self,Ship):
                Reactor.__init__(self,"Fission Reactor",self.power_gen,self.cost,Ship)
        Variants=[Reactor_T1,Reactor_T2,Reactor_T3,Reactor_T4,Reactor_T5,Reactor_T6]
    class Platform:
        class Reactor_T1(Reactor):
            Name="Fission"
            power_gen=200
            cost=20
            Info=[Name,"Power +"+str(power_gen),"Cost: "+str(cost)]
            def __init__(self,Ship):
                Reactor.__init__(self,"Fission Reactor",self.power_gen,self.cost,Ship)
        class Reactor_T2(Reactor):
            Name="Fusion"
            power_gen=260
            cost=26
            Info=[Name,"Power +"+str(power_gen),"Cost: "+str(cost)]
            def __init__(self,Ship):
                Reactor.__init__(self,"Fission Reactor",self.power_gen,self.cost,Ship)
        class Reactor_T3(Reactor):
            Name="Cold Fussion"
            power_gen=340
            cost=34
            Info=[Name,"Power +"+str(power_gen),"Cost: "+str(cost)]
            def __init__(self,Ship):
                Reactor.__init__(self,"Fission Reactor",self.power_gen,self.cost,Ship)
        class Reactor_T4(Reactor):
            Name="Antimatter"
            power_gen=440
            cost=44
            Info=[Name,"Power +"+str(power_gen),"Cost: "+str(cost)]
            def __init__(self,Ship):
                Reactor.__init__(self,"Fission Reactor",self.power_gen,self.cost,Ship)
        class Reactor_T5(Reactor):
            Name="0-Point"
            power_gen=575
            cost=44
            Info=[Name,"Power +"+str(power_gen),"Cost: "+str(cost)]
            def __init__(self,Ship):
                Reactor.__init__(self,"Fission Reactor",self.power_gen,self.cost,Ship)
        class Reactor_T6(Reactor):
            Name="Dark Matter"
            power_gen=750
            cost=74
            Info=[Name,"Power +"+str(power_gen),"Cost: "+str(cost)]
            def __init__(self,Ship):
                Reactor.__init__(self,"Fission Reactor",self.power_gen,self.cost,Ship)
        Variants=[Reactor_T1,Reactor_T2,Reactor_T3,Reactor_T4,Reactor_T5,Reactor_T6]
class Hiperdrive(Component):
    Type="CH"
    # NO jump charge time modifier implemented
    def __init__(self,Name,PowerCons,Cost,Ship):
        Component.__init__(self,"CD",Name,PowerCons,Cost,Ship)
class Hiperdrives:
    class Hiperdrive_T1(Hiperdrive):
        Name="Hiper drive I"
        power_cons=10
        cost=5
        Info=[Name,"FTL"]
        def __init__(self,Ship):
            Hiperdrive.__init__(self,self.Name,self.power_cons,self.cost,Ship)
    class Hiperdrive_T2(Hiperdrive):
        Name="Hiper drive 2"
        power_cons=15
        cost=10
        Info=[Name,"FTL","Jump time:-0.25"]
        def __init__(self,Ship):
            Hiperdrive.__init__(self,self.Name,self.power_cons,self.cost,Ship)
    class Hiperdrive_T3(Hiperdrive):
        Name="Hiper drive 3"
        power_cons=12
        cost=15
        Info=[Name,"FTL","Jump time:-0.50"]
        def __init__(self,Ship):
            Hiperdrive.__init__(self,self.Name,self.power_cons,self.cost,Ship)
    class JumpDrive(Hiperdrive):
        Name="Jump Drive"
        power_cons=30
        cost=20
        Info=[Name,"FTL","Jump time:-0.70"]
        def __init__(self,Ship):
            Hiperdrive.__init__(self,self.Name,self.power_cons,self.cost,Ship)
    class PsiDrive(Hiperdrive):
        Name="PsiDrive"
        power_cons=30
        cost=20
        Info=[Name,"FTL","Jump time:-0.80"]
        def __init__(self,Ship):
            Hiperdrive.__init__(self,self.Name,self.power_cons,self.cost,Ship)
    Variants=[Hiperdrive_T1,Hiperdrive_T2,Hiperdrive_T3,JumpDrive,PsiDrive]

class Thruster(Component):
    Type="CT"
    def __init__(self,Name,PowerCons,Cost,Ship,SpeedMod,EvasionExtra):
        Component.__init__(self,"CT",Name,PowerCons,Cost,Ship)
        self.SpeedMod=SpeedMod
        self.EvasionExtra=EvasionExtra
    def Effect1(self):
        self.Ship.FinalSpeed+=self.Ship.BaseSpeed*self.SpeedMod
        self.Ship.FinalEvasion+=self.EvasionExtra
class Thrusters:
    class Corvete:
        class Thruster_T1(Thruster):
            Name="Chemical"
            power_cons=10
            cost=3
            Info=[Name,"Power Drain: "+str(power_cons),"Cost: "+str(cost),]
            def __init__(self,Ship):
                Thruster.__init__(self,"Chemical Thrusters",self.power_cons,self.cost,Ship,0,0)
        class Thruster_T2(Thruster):
            Name="Ion"
            power_cons=15
            cost=6
            speed_mod=0.25
            extra_evasion=5
            Info=[Name,"Power Drain: "+str(power_cons),"Speed: +"+str(speed_mod),"Evasion: +"+str(extra_evasion),"Cost: "+str(cost),]
            def __init__(self,Ship):
                Thruster.__init__(self,"Ion Thrusters",self.power_cons,self.cost,Ship,self.speed_mod,self.extra_evasion)
        class Thruster_T3(Thruster):
            Name="Plasma"
            power_cons=20
            cost=9
            speed_mod=0.50
            extra_evasion=10
            Info=[Name,"Power Drain: "+str(power_cons),"Speed: +"+str(speed_mod),"Evasion: +"+str(extra_evasion),"Cost: "+str(cost),]
            def __init__(self,Ship):
                Thruster.__init__(self,"Plasma Thrusters",self.power_cons,self.cost,Ship,self.speed_mod,self.extra_evasion)
        class Thruster_T4(Thruster):
            Name="Impulse"
            power_cons=25
            cost=12
            speed_mod=0.75
            extra_evasion=15
            Info=[Name,"Power Drain: "+str(power_cons),"Speed: +"+str(speed_mod),"Evasion: +"+str(extra_evasion),"Cost: "+str(cost),]
            def __init__(self,Ship):
                Thruster.__init__(self,"Impulse Thrusters",self.power_cons,self.cost,Ship,self.speed_mod,self.extra_evasion)
        class Thruster_T5(Thruster):
            Name="Dark Matter"
            power_cons=30
            cost=12
            speed_mod=1.25
            extra_evasion=20
            Info=[Name,"Power Drain: "+str(power_cons),"Speed: +"+str(speed_mod),"Evasion: +"+str(extra_evasion),"Cost: "+str(cost),]
            def __init__(self,Ship):
                Thruster.__init__(self,"Dark Matter Thrusters",self.power_cons,self.cost,Ship,self.speed_mod,self.extra_evasion)
        Variants=[Thruster_T1,Thruster_T2,Thruster_T3,Thruster_T4,Thruster_T5]
    class Destroyer:
        class Thruster_T1(Thruster):
            Name="Chemical"
            power_cons=20
            cost=6
            Info=[Name,"Power Drain: "+str(power_cons),"Cost: "+str(cost),]
            def __init__(self,Ship):
                Thruster.__init__(self,"Chemical Thrusters",self.power_cons,self.cost,Ship,0,0)
        class Thruster_T2(Thruster):
            Name="Ion"
            power_cons=30
            cost=12
            speed_mod=0.25
            extra_evasion=5
            Info=[Name,"Power Drain: "+str(power_cons),"Speed: +"+str(speed_mod),"Evasion: +"+str(extra_evasion),"Cost: "+str(cost),]
            def __init__(self,Ship):
                Thruster.__init__(self,"Ion Thrusters",self.power_cons,self.cost,Ship,self.speed_mod,self.extra_evasion)
        class Thruster_T3(Thruster):
            Name="Plasma"
            power_cons=40
            cost=18
            speed_mod=0.50
            extra_evasion=10
            Info=[Name,"Power Drain: "+str(power_cons),"Speed: +"+str(speed_mod),"Evasion: +"+str(extra_evasion),"Cost: "+str(cost),]
            def __init__(self,Ship):
                Thruster.__init__(self,"Plasma Thrusters",self.power_cons,self.cost,Ship,self.speed_mod,self.extra_evasion)
        class Thruster_T4(Thruster):
            Name="Impulse"
            power_cons=50
            cost=24
            speed_mod=0.75
            extra_evasion=15
            Info=[Name,"Power Drain: "+str(power_cons),"Speed: +"+str(speed_mod),"Evasion: +"+str(extra_evasion),"Cost: "+str(cost),]
            def __init__(self,Ship):
                Thruster.__init__(self,"Impulse Thrusters",self.power_cons,self.cost,Ship,self.speed_mod,self.extra_evasion)
        class Thruster_T5(Thruster):
            Name="Dark Matter"
            power_cons=60
            cost=24
            speed_mod=1.25
            extra_evasion=20
            Info=[Name,"Power Drain: "+str(power_cons),"Speed: +"+str(speed_mod),"Evasion: +"+str(extra_evasion),"Cost: "+str(cost),]
            def __init__(self,Ship):
                Thruster.__init__(self,"Dark Matter Thrusters",self.power_cons,self.cost,Ship,self.speed_mod,self.extra_evasion)
        Variants=[Thruster_T1,Thruster_T2,Thruster_T3,Thruster_T4,Thruster_T5]
    class Cruiser:
        class Thruster_T1(Thruster):
            Name="Chemical"
            power_cons=40
            cost=12
            Info=[Name,"Power Drain: "+str(power_cons),"Cost: "+str(cost),]
            def __init__(self,Ship):
                Thruster.__init__(self,"Chemical Thrusters",self.power_cons,self.cost,Ship,0,0)
        class Thruster_T2(Thruster):
            Name="Ion"
            power_cons=60
            cost=24
            speed_mod=0.25
            extra_evasion=5
            Info=[Name,"Power Drain: "+str(power_cons),"Speed: +"+str(speed_mod),"Evasion: +"+str(extra_evasion),"Cost: "+str(cost),]
            def __init__(self,Ship):
                Thruster.__init__(self,"Ion Thrusters",self.power_cons,self.cost,Ship,self.speed_mod,self.extra_evasion)
        class Thruster_T3(Thruster):
            Name="Plasma"
            power_cons=80
            cost=36
            speed_mod=0.50
            extra_evasion=10
            Info=[Name,"Power Drain: "+str(power_cons),"Speed: +"+str(speed_mod),"Evasion: +"+str(extra_evasion),"Cost: "+str(cost),]
            def __init__(self,Ship):
                Thruster.__init__(self,"Plasma Thrusters",self.power_cons,self.cost,Ship,self.speed_mod,self.extra_evasion)
        class Thruster_T4(Thruster):
            Name="Impulse"
            power_cons=100
            cost=48
            speed_mod=0.75
            extra_evasion=15
            Info=[Name,"Power Drain: "+str(power_cons),"Speed: +"+str(speed_mod),"Evasion: +"+str(extra_evasion),"Cost: "+str(cost),]
            def __init__(self,Ship):
                Thruster.__init__(self,"Impulse Thrusters",self.power_cons,self.cost,Ship,self.speed_mod,self.extra_evasion)
        class Thruster_T5(Thruster):
            Name="Dark Matter"
            power_cons=120
            cost=48
            speed_mod=1.25
            extra_evasion=20
            Info=[Name,"Power Drain: "+str(power_cons),"Speed: +"+str(speed_mod),"Evasion: +"+str(extra_evasion),"Cost: "+str(cost),]
            def __init__(self,Ship):
                Thruster.__init__(self,"Dark Matter Thrusters",self.power_cons,self.cost,Ship,self.speed_mod,self.extra_evasion)
        Variants=[Thruster_T1,Thruster_T2,Thruster_T3,Thruster_T4,Thruster_T5]
    class Battleship:
        class Thruster_T1(Thruster):
            Name="Chemical"
            power_cons=80
            cost=24
            Info=[Name,"Power Drain: "+str(power_cons),"Cost: "+str(cost),]
            def __init__(self,Ship):
                Thruster.__init__(self,"Chemical Thrusters",self.power_cons,self.cost,Ship,0,0)
        class Thruster_T2(Thruster):
            Name="Ion"
            power_cons=120
            cost=48
            speed_mod=0.25
            extra_evasion=5
            Info=[Name,"Power Drain: "+str(power_cons),"Speed: +"+str(speed_mod),"Evasion: +"+str(extra_evasion),"Cost: "+str(cost),]
            def __init__(self,Ship):
                Thruster.__init__(self,"Ion Thrusters",self.power_cons,self.cost,Ship,self.speed_mod,self.extra_evasion)
        class Thruster_T3(Thruster):
            Name="Plasma"
            power_cons=160
            cost=72
            speed_mod=0.50
            extra_evasion=10
            Info=[Name,"Power Drain: "+str(power_cons),"Speed: +"+str(speed_mod),"Evasion: +"+str(extra_evasion),"Cost: "+str(cost),]
            def __init__(self,Ship):
                Thruster.__init__(self,"Plasma Thrusters",self.power_cons,self.cost,Ship,self.speed_mod,self.extra_evasion)
        class Thruster_T4(Thruster):
            Name="Impulse"
            power_cons=200
            cost=96
            speed_mod=0.75
            extra_evasion=15
            Info=[Name,"Power Drain: "+str(power_cons),"Speed: +"+str(speed_mod),"Evasion: +"+str(extra_evasion),"Cost: "+str(cost),]
            def __init__(self,Ship):
                Thruster.__init__(self,"Impulse Thrusters",self.power_cons,self.cost,Ship,self.speed_mod,self.extra_evasion)
        class Thruster_T5(Thruster):
            Name="Dark Matter"
            power_cons=240
            cost=96
            speed_mod=1.25
            extra_evasion=20
            Info=[Name,"Power Drain: "+str(power_cons),"Speed: +"+str(speed_mod),"Evasion: +"+str(extra_evasion),"Cost: "+str(cost),]
            def __init__(self,Ship):
                Thruster.__init__(self,"Dark Matter Thrusters",self.power_cons,self.cost,Ship,self.speed_mod,self.extra_evasion)
        Variants=[Thruster_T1,Thruster_T2,Thruster_T3,Thruster_T4,Thruster_T5]
    class Titan:
        class Thruster_T1(Thruster):
            Name="Chemical"
            power_cons=160
            cost=48
            Info=[Name,"Power Drain: "+str(power_cons),"Cost: "+str(cost),]
            def __init__(self,Ship):
                Thruster.__init__(self,"Chemical Thrusters",self.power_cons,self.cost,Ship,0,0)
        class Thruster_T2(Thruster):
            Name="Ion"
            power_cons=240
            cost=96
            speed_mod=0.25
            extra_evasion=5
            Info=[Name,"Power Drain: "+str(power_cons),"Speed: +"+str(speed_mod),"Evasion: +"+str(extra_evasion),"Cost: "+str(cost),]
            def __init__(self,Ship):
                Thruster.__init__(self,"Ion Thrusters",self.power_cons,self.cost,Ship,self.speed_mod,self.extra_evasion)
        class Thruster_T3(Thruster):
            Name="Plasma"
            power_cons=320
            cost=144
            speed_mod=0.50
            extra_evasion=10
            Info=[Name,"Power Drain: "+str(power_cons),"Speed: +"+str(speed_mod),"Evasion: +"+str(extra_evasion),"Cost: "+str(cost),]
            def __init__(self,Ship):
                Thruster.__init__(self,"Plasma Thrusters",self.power_cons,self.cost,Ship,self.speed_mod,self.extra_evasion)
        class Thruster_T4(Thruster):
            Name="Impulse"
            power_cons=400
            cost=192
            speed_mod=0.75
            extra_evasion=15
            Info=[Name,"Power Drain: "+str(power_cons),"Speed: +"+str(speed_mod),"Evasion: +"+str(extra_evasion),"Cost: "+str(cost),]
            def __init__(self,Ship):
                Thruster.__init__(self,"Impulse Thrusters",self.power_cons,self.cost,Ship,self.speed_mod,self.extra_evasion)
        class Thruster_T5(Thruster):
            Name="Dark Matter"
            power_cons=480
            cost=192
            speed_mod=1.25
            extra_evasion=20
            Info=[Name,"Power Drain: "+str(power_cons),"Speed: +"+str(speed_mod),"Evasion: +"+str(extra_evasion),"Cost: "+str(cost),]
            def __init__(self,Ship):
                Thruster.__init__(self,"Dark Matter Thrusters",self.power_cons,self.cost,Ship,self.speed_mod,self.extra_evasion)
        Variants=[Thruster_T1,Thruster_T2,Thruster_T3,Thruster_T4,Thruster_T5]

class Sensor(Component):
    Type="CS"
    def __init__(self,Name,PowerCons,Cost,Ship,ExtraTracking):
        Component.__init__(self,"CS",Name,PowerCons,Cost,Ship)
        self.ExtraTracking=ExtraTracking
    def Effect1(self):
        self.Ship.BonusTracking+=self.ExtraTracking
class Sensors:
    class Sensor_T1(Sensor):
        Type="CS"
        Name="Radar"
        cost=2
        power_cons=5
        tracking=0
        Info=[Name,"Cost: "+str(cost),"Power Cost: "+str(power_cons),"tracking: +"+str(tracking)]
        def __init__(self,Ship):
            Sensor.__init__(self,"Radar System",self.power_cons,self.cost,Ship,self.tracking)
    class Sensor_T2(Sensor):
        Type="CS"
        Name="Gravitic"
        cost=3
        power_cons=10
        tracking=5
        Info=[Name,"Cost: "+str(cost),"Power Cost: "+str(power_cons),"tracking: +"+str(tracking)]
        def __init__(self,Ship):
            Sensor.__init__(self,"Gravitic Sensors",self.power_cons,self.cost,Ship,self.tracking)
    class Sensor_T3(Sensor):
        Type="CS"
        Name="Subspace"
        cost=6
        power_cons=15
        tracking=10
        Info=[Name,"Cost: "+str(cost),"Power Cost: "+str(power_cons),"tracking: +"+str(tracking)]
        def __init__(self,Ship):
            Sensor.__init__(self,"Subspace Sensor",self.power_cons,self.cost,Ship,self.tracking)
    class Sensor_T4(Sensor):
        Type="CS"
        Name="Tachyons"
        cost=4
        power_cons=20
        tracking=15
        Info=[Name,"Cost: "+str(cost),"Power Cost: "+str(power_cons),"tracking: +"+str(tracking)]
        def __init__(self,Ship):
            Sensor.__init__(self,"Tachyon Sensors",self.power_cons,self.cost,Ship,self.tracking)

    Variants=[Sensor_T1,Sensor_T2,Sensor_T3,Sensor_T4]

## TODO:  add Aura
## TODO:  add AI
