

Window_With=1000
Window_Height=600

temp=None
### Interface
class ShipBuilder:
    size=[300,100]
    poz=[temp,100]## will change to be center
    font_size=30
    txt="Ship Builder"
    fontID=0
ShipBuilder.size[0], ShipBuilder.txt=400,"Ship Builder WIP"
ShipBuilder.poz[0]=(Window_With-ShipBuilder.size[0])//2

class FleetBuilder:
    size=[300,100]
    poz=[temp,250]## will change to be center
    font_size=30
    txt="Fleet Builder"
    fontID=0
FleetBuilder.txt="WIP NEXT"
FleetBuilder.poz[0]=(Window_With-FleetBuilder.size[0])//2

class BattleSimulator:
    size=[300,100]
    poz=[temp,400]## will change to be center
    font_size=30
    txt="Battle Simulator"
    fontID=0
BattleSimulator.size[0], BattleSimulator.txt=500,"WIP NEXT NEXT"
BattleSimulator.poz[0]=(Window_With-BattleSimulator.size[0])//2
###################################################
class Ship_Builder:
    class ClassSelector:
        class SellectClass:
            size=[300,50]
            poz=[temp,50]## will change to be center
            font_size=25
            txt="Sellect Ship Class"
            fontID=0

        class SellectCorvete:
            size=[300,50]
            poz=[temp,125]## will change to be center
            font_size=25
            txt="Corvete"
            fontID=0

        class SellectDestroyer:
            size=[300,50]
            poz=[temp,200]## will change to be center
            font_size=25
            txt="Destroyer"
            fontID=0

        class SellectCruiser:
            size=[300,50]
            poz=[temp,275]## will change to be center
            font_size=25
            txt="Cruiser"
            fontID=0

        class SellectBattleship:
            size=[300,50]
            poz=[temp,350]## will change to be center
            font_size=25
            txt="Battleship"
            fontID=0

        class SellectTitan:
            size=[300,50]
            poz=[temp,425]## will change to be center
            font_size=25
            txt="Titan"
            fontID=0
    class CorveteBuilder:
        class NewButtton:
            size=[500,100]
            poz=[temp,150]## will change to be center
            font_size=35
            txt="Design new Corvete"
            fontID=0
        class LoadButtton:
            size=[500,100]
            poz=[temp,350]## will change to be center
            font_size=35
            txt="Load Existing Corvete"
            fontID=0
        None

Ship_Builder.ClassSelector.SellectClass.poz[0]=(Window_With-Ship_Builder.ClassSelector.SellectClass.size[0])//2
Ship_Builder.ClassSelector.SellectCorvete.poz[0]=(Window_With-Ship_Builder.ClassSelector.SellectCorvete.size[0])//2
Ship_Builder.ClassSelector.SellectDestroyer.poz[0]=(Window_With-Ship_Builder.ClassSelector.SellectDestroyer.size[0])//2
Ship_Builder.ClassSelector.SellectCruiser.poz[0]=(Window_With-Ship_Builder.ClassSelector.SellectCruiser.size[0])//2
Ship_Builder.ClassSelector.SellectBattleship.poz[0]=(Window_With-Ship_Builder.ClassSelector.SellectBattleship.size[0])//2
Ship_Builder.ClassSelector.SellectTitan.poz[0]=(Window_With-Ship_Builder.ClassSelector.SellectTitan.size[0])//2
Ship_Builder.CorveteBuilder.NewButtton.poz[0]=(Window_With-Ship_Builder.CorveteBuilder.NewButtton.size[0])//2
Ship_Builder.CorveteBuilder.LoadButtton.poz[0]=(Window_With-Ship_Builder.CorveteBuilder.LoadButtton.size[0])//2
class DesignerGeneral:
    of_L=[50,10]
    of_M=[265,10]
    of_R=[480,10]
    class InfoBar:
        class InfoPanel:
            size=[190,190]
            poz=[800,10]
            font_size=15
            fontID=1
            txt=["Info Box",
                 "Hover over",
                 "a component",
                 "to see more"]
        class SaveBut:
            size=[193,75]
            poz=[800,500]## will change to be center
            font_size=30
            txt="Save"
            fontID=0
        class Cost:
            class L:#txt
                size=[193,40]
                poz=[800,250]
                font_size=20
                txt="Cost:"
                fontID=1
            class R:#Val
                size=[193,40]
                poz=[800,250]
                font_size=20
                txt="22"
                fontID=1
        class Power:
            class L:#txt
                size=[193,40]
                poz=[800,280]
                font_size=20
                txt="Power:"
                fontID=1
            class R:#Val
                size=[193,40]
                poz=[800,280]
                font_size=20
                txt="5"
                fontID=1
        class Hull:
            class L:#txt
                size=[193,40]
                poz=[800,310]
                font_size=20
                txt="Hull:"
                fontID=1
            class R:#Val
                size=[193,40]
                poz=[800,310]
                font_size=20
                txt="300"
                fontID=1
        class Armor:
            class L:#txt
                size=[193,40]
                poz=[800,340]
                font_size=20
                txt="Armor:"
                fontID=1
            class R:#Val
                size=[193,40]
                poz=[800,340]
                font_size=20
                txt="200"
                fontID=1
        class Shield:
            class L:#txt
                size=[193,40]
                poz=[800,370]
                font_size=20
                txt="Shield:"
                fontID=1
            class R:#Val
                size=[193,40]
                poz=[800,370]
                font_size=20
                txt="150"
                fontID=1
        class Evasion:
            class L:#txt
                size=[193,40]
                poz=[800,400]
                font_size=20
                txt="Evasion:"
                fontID=1
            class R:#Val
                size=[193,40]
                poz=[800,400]
                font_size=20
                txt="0.54"##vr %
                fontID=1
        class NameBox:
            size=[193,40]
            poz=[800,450]
            font_size=20
            txt=""##vr %
            fontID=1
    class Components:
        class Reactor:
            size=[64,64]
            poz=[715,120+68*0]
            path=None
        class Hiperdrive:
            size=[64,64]
            poz=[715,120+68*1]
            path=None
        class Thrusters:
            size=[64,64]
            poz=[715,120+68*2]
            path=None
        class Sensors:
            size=[64,64]
            poz=[715,120+68*3]
            path=None
        class AI:
            size=[64,64]
            poz=[715,120+68*4]
            path=None
        class Aura:
            size=[64,64]
            poz=[715,120+68*5]
            path=None

class DesignerCorvete:
    class Core:
        None
