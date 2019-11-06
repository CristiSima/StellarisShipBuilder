class Utility:
    def __init__(self,Ship,Name,Type,PowerCons,Cost):
        self.Ship=Ship
        self.Name=Name
        self.Type=Type
        self.PowerCons=PowerCons
        self.Cost=Cost

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
        self.Effect2()
class Shield(Utility):
    def __init__(self,Ship,Name,Type,ExtraShield,PowerCons,Cost):
        Utility.__init__(self,Ship,Name,Type,PowerCons,Cost)
        self.ExtraShield=ExtraShield
    def Effect1(self):
        self.Ship.FinalShield+=self.ExtraShield
class Armor(Utility):
    def __init__(self,Ship,Name,Type,ExtraArmor,Cost):
        Utility.__init__(self,Ship,Name,Type,0,Cost)
        self.ExtraArmor=ExtraArmor
    def Effect1(self):
        self.Ship.FinalArmor+=self.ExtraArmor

class Small:
    class Shields:
        Name="Shield"
        Info=["Small Shield","Increase Shield Capacity"]
        class Shield_T1(Shield):
            Type="US"
            Name="Deflector"
            cost=5
            power_cons=15
            shield=50
            Info=["Deflector","Shield +"+str(shield),"Power Cons: "+str(power_cons),"Cost: "+str(cost)]
            def __init__(self,Ship):
                Shield.__init__(self,Ship,self.Name,"US",self.shield,self.power_cons,self.cost)
        class Shield_T2(Shield):
            Type="US"
            Name="Deflector2"
            cost=7
            power_cons=20
            shield=65
            Info=["Improved Deflector","Shield +"+str(shield),"Power Cons: "+str(power_cons),"Cost: "+str(cost)]
            def __init__(self,Ship):
                Shield.__init__(self,Ship,self.Name,"US",self.shield,self.power_cons,self.cost)


        class Shield_T3(Shield):
            Type="US"
            Name="Shields"
            cost=9
            power_cons=25
            shield=85
            Info=["Shield","Shield +"+str(shield),"Power Cons: "+str(power_cons),"Cost: "+str(cost)]
            def __init__(self,Ship):
                Shield.__init__(self,Ship,self.Name,"US",self.shield,self.power_cons,self.cost)


        class Shield_T4(Shield):
            Type="US"
            Name="Shields2"
            cost=9
            power_cons=35
            shield=110
            Info=["Advanced Shield","Shield +"+str(shield),"Power Cons: "+str(power_cons),"Cost: "+str(cost)]
            def __init__(self,Ship):
                Shield.__init__(self,Ship,self.Name,"US",self.shield,self.power_cons,self.cost)


        class Shield_T5(Shield):
            Type="US"
            Name="Shields3"
            cost=12
            power_cons=45
            shield=145
            Info=["Hyper Shield","Shield +"+str(shield),"Power Cons: "+str(power_cons),"Cost: "+str(cost)]
            def __init__(self,Ship):
                Shield.__init__(self,Ship,self.Name,"US",self.shield,self.power_cons,self.cost)

        Variants=[Shield_T1,Shield_T2,Shield_T3,Shield_T4,Shield_T5]
    class Armors:
        Name="Armor"
        Info=["Small Armor","Increase Armor Capacity"]
        class Armor_T1(Armor):
            Type="US"
            Name="Nanocomp"
            cost=10
            armor=50
            Info=["Nanocomposite","Armor +"+str(armor),"Cost: "+str(cost)]
            def __init__(self,Ship):
                Armor.__init__(self,Ship,self.Name,self.Type,self.armor,self.cost)


        class Armor_T2(Armor):
            Type="US"
            Name="Ceramo-metal"
            cost=13
            armor=65
            Info=["Ceramo-metal","Armor +"+str(armor),"Cost: "+str(cost)]
            def __init__(self,Ship):
                Armor.__init__(self,Ship,self.Name,self.Type,self.armor,self.cost)


        class Armor_T3(Armor):
            Type="US"
            Name="Plasteel"
            cost=17
            armor=85
            Info=["Plasteel","Armor +"+str(armor),"Cost: "+str(cost)]
            def __init__(self,Ship):
                Armor.__init__(self,Ship,self.Name,self.Type,self.armor,self.cost)


        class Armor_T4(Armor):
            Type="US"
            Name="Durasteel"
            cost=17
            armor=110
            Info=["Durasteel","Armor +"+str(armor),"Cost: "+str(cost)]
            def __init__(self,Ship):
                Armor.__init__(self,Ship,self.Name,self.Type,self.armor,self.cost)


        class Armor_T5(Armor):
            Type="US"
            Name="Neutronium"
            cost=22
            armor=145
            Info=["Neutronium","Armor +"+str(armor),"Cost: "+str(cost)]
            def __init__(self,Ship):
                Armor.__init__(self,Ship,self.Name,self.Type,self.armor,self.cost)
        Variants=[Armor_T1,Armor_T2,Armor_T3,Armor_T4,Armor_T5]
    Variants=[Shields,Armors]
class Medium:
    class Shields:
        Name="Shield"
        Info=["Madium Shield","Increase Shield Capacity"]
        class Shield_T1(Shield):
            Type="UM"
            Name="Deflector"
            cost=10
            power_cons=30
            shield=125
            Info=["Deflector","Shield +"+str(shield),"Power Cons: "+str(power_cons),"Cost: "+str(cost)]
            def __init__(self,Ship):
                Shield.__init__(self,Ship,self.Name,"UM",self.shield,self.power_cons,self.cost)


        class Shield_T2(Shield):
            Type="UM"
            Name="Deflector2"
            cost=13
            power_cons=30
            shield=160
            Info=["Improved Deflector","Shield +"+str(shield),"Power Cons: "+str(power_cons),"Cost: "+str(cost)]
            def __init__(self,Ship):
                Shield.__init__(self,Ship,self.Name,"UM",self.shield,self.power_cons,self.cost)


        class Shield_T3(Shield):
            Type="UM"
            Name="Shields"
            cost=17
            power_cons=50
            shield=215
            Info=["Shields","Shield +"+str(shield),"Power Cons: "+str(power_cons),"Cost: "+str(cost)]
            def __init__(self,Ship):
                Shield.__init__(self,Ship,self.Name,"UM",self.shield,self.power_cons,self.cost)


        class Shield_T4(Shield):
            Type="UM"
            Name="Shields2"
            cost=17
            power_cons=70
            shield=275
            Info=["Advanced Shields","Shield +"+str(shield),"Power Cons: "+str(power_cons),"Cost: "+str(cost)]
            def __init__(self,Ship):
                Shield.__init__(self,Ship,self.Name,"UM",self.shield,self.power_cons,self.cost)


        class Shield_T5(Shield):
            Type="UM"
            Name="Shields3"
            cost=22
            power_cons=90
            shield=360
            Info=["Hyper Shields","Shield +"+str(shield),"Power Cons: "+str(power_cons),"Cost: "+str(cost)]
            def __init__(self,Ship):
                Shield.__init__(self,Ship,self.Name,"UM",self.shield,self.power_cons,self.cost)
        Variants=[Shield_T1,Shield_T2,Shield_T3,Shield_T4,Shield_T5]
    Variants=[Shields]
class Large:
    class Shields:
        Name="Shield"
        Info=["Large Shield","Increase Shield Capacity"]
        class Shield_T1(Shield):
            Type="UL"
            Name="Deflector"
            cost=20
            power_cons=60
            shield=300
            Info=["Deflector","Shield +"+str(shield),"Power Cons: "+str(power_cons),"Cost: "+str(cost)]
            def __init__(self,Ship):
                Shield.__init__(self,Ship,self.Name,self.Type,self.shield,self.power_cons,self.cost)

        class Shield_T2(Shield):
            Type="UL"
            Name="Deflector"
            cost=26
            power_cons=80
            shield=390
            Info=["Improved Deflector","Shield +"+str(shield),"Power Cons: "+str(power_cons),"Cost: "+str(cost)]
            def __init__(self,Ship):
                Shield.__init__(self,Ship,self.Name,self.Type,self.shield,self.power_cons,self.cost)

        class Shield_T3(Shield):
            Type="UL"
            Name="Shield"
            cost=34
            power_cons=100
            shield=510
            Info=["Shield","Shield +"+str(shield),"Power Cons: "+str(power_cons),"Cost: "+str(cost)]
            def __init__(self,Ship):
                Shield.__init__(self,Ship,self.Name,self.Type,self.shield,self.power_cons,self.cost)

        class Shield_T4(Shield):
            Type="UL"
            Name="Shield2"
            cost=34
            power_cons=140
            shield=660
            Info=["Advanced Shield","Shield +"+str(shield),"Power Cons: "+str(power_cons),"Cost: "+str(cost)]
            def __init__(self,Ship):
                Shield.__init__(self,Ship,self.Name,self.Type,self.shield,self.power_cons,self.cost)

        class Shield_T5(Shield):
            Type="UL"
            Name="Shield3"
            cost=44
            power_cons=180
            shield=870
            Info=["Hyper Shield","Shield +"+str(shield),"Power Cons: "+str(power_cons),"Cost: "+str(cost)]
            def __init__(self,Ship):
                Shield.__init__(self,Ship,self.Name,self.Type,self.shield,self.power_cons,self.cost)
        Variants=[Shield_T1,Shield_T2,Shield_T3,Shield_T4,Shield_T5]
    Variants=[Shields]
class Auxilary:
    class ReactorBoost:
        Name="Reactor Boost"
        Info=["Reactor Boost","Power Gen"]
        class ReactorBoost_T1(Utility):
            Type="UA"
            Name="Reactor Boost"
            cost=5
            power_gen=20
            Info=["Reactor Boost","Power +"+str(power_gen),"Cost: "+str(cost)]
            def __init__(self,Ship):
                Utility.__init__(self,Ship,"Reactor Boost","UA",-self.power_gen,self.cost)
        Variants=[ReactorBoost_T1,]
    Variants=[ReactorBoost,]
