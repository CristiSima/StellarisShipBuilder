import Constants as CST
import Buttons
import Box
import Ships
class Level_Selector:
    def __init__(self,place,Screen,Slot,Thing,InfoPanel):
        None
        self.poz=poz=[250,200]
        self.size=size=[250,25]
        poz[1]+=(size[1]+2)*place
        self.Screen=Screen
        self.Slot=Slot
        self.Thing=Thing
        self.poz=poz
        self.size=size
        self.txt=txt=Thing.Name
        self.Info=Info=Thing.Info
        self.InfoPanel=InfoPanel
        self.But=Buttons.ButtonWtxt(Screen,poz,size,txt,20,1)
        self.But.AddClick(Slot.Equip,(Thing,))
        self.But.AddHover(InfoPanel.Change2,(Info,))
        self.Screen.draw()
    def Remove(self):
        self.Screen.draw()
        self.But.Remove()

class Thing_Selector:
    def __init__(self,Screen,Slot,Things,InfoPanel,command=None):
        self.Screen=Screen
        self.Slot=Slot
        self.Things=Things
        self.InfoPanel=InfoPanel

        self.l=l=[]
        #for T in Things.Variants:
        for i in range(len(Things.Variants)):
            l.append(Level_Selector(i,Screen,Slot,Things.Variants[i],InfoPanel))
        for i in l:
            if(command):
                i.But.AddClick(*command)
            i.But.AddClick(self.Remove,())
        Screen.draw()
    def Remove(self):
        for L in self.l:
            L.Remove()
        self.l=[]
        self.Screen.draw()

class Type_Selector:
    # txt=[["Laser","Plasmathrower"],["BLue Lasers","Red Lasers"],[],[]] =>>> MOve In Def
    # Things=[[Small.Lasers.Laser_T1,Small.Lasers.Laser_T2],[]]
    # Infos =>Move in Def
    def __init__(self,Screen,Slot,Things,InfoPanel):
        self.poz=[10,200]
        self.size=[250,25]
        self.Screen=Screen
        self.Slot=Slot
        self.Things=Things
        self.InfoPanel=InfoPanel
        self.l=l=[]
        for i in range(len(Things.Variants)):
            l.append(Buttons.ButtonWtxt(Screen,self.poz,self.size,Things.Variants[i].Name,20,1))
            l[i].AddClick(Thing_Selector,(Screen,Slot,Things.Variants[i],InfoPanel,(self.Remove,())))
            l[i].AddHover(InfoPanel.Change2,(Things.Variants[i].Info,))
            None
        Screen.draw()
    def Remove(self):
        for i in self.l:
                i.Remove()

        None
class Module:
    def CheckAdd(self,Dest):
        if(self.Comp.Thing):
            target=eval("self.Comp.Thing."+Dest)
            if(target):
                Type_Selector(self.Screen,target,target.Target(),self.InfoPanel)
        else:
            None
    def UpdateColor(self):
        if(self.Comp.Thing):
            if(self.Comp.Thing.Weapon1):
                self.Weapon1.Change2([255,255,255])
            else:
                self.Weapon1.Change2([100,100,100])

            if(self.Comp.Thing.Weapon2):
                self.Weapon2.Change2([255,255,255])
            else:
                self.Weapon2.Change2([100,100,100])

            if(self.Comp.Thing.Weapon3):
                self.Weapon3.Change2([255,255,255])
            else:
                self.Weapon3.Change2([100,100,100])

            if(self.Comp.Thing.Weapon4):
                self.Weapon4.Change2([255,255,255])
            else:
                self.Weapon4.Change2([100,100,100])

            if(self.Comp.Thing.Weapon5):
                self.Weapon5.Change2([255,255,255])
            else:
                self.Weapon5.Change2([100,100,100])

            if(self.Comp.Thing.Weapon6):
                self.Weapon6.Change2([255,255,255])
            else:
                self.Weapon6.Change2([100,100,100])


            if(self.Comp.Thing.Utility1):
                self.Utility1.Change2([255,255,255])
            else:
                self.Utility1.Change2([100,100,100])

            if(self.Comp.Thing.Utility2):
                self.Utility2.Change2([255,255,255])
            else:
                self.Utility2.Change2([100,100,100])

            if(self.Comp.Thing.Utility3):
                self.Utility3.Change2([255,255,255])
            else:
                self.Utility3.Change2([100,100,100])

            if(self.Comp.Thing.Utility4):
                self.Utility4.Change2([255,255,255])
            else:
                self.Utility4.Change2([100,100,100])

            if(self.Comp.Thing.Utility5):
                self.Utility5.Change2([255,255,255])
            else:
                self.Utility5.Change2([100,100,100])

            if(self.Comp.Thing.Utility6):
                self.Utility6.Change2([255,255,255])
            else:
                self.Utility6.Change2([100,100,100])

    def __init__(self,Screen,of,Comp,InfoPanel):
        self.Comp=Comp
        self.of=of
        self.Screen=Screen
        self.InfoPanel=InfoPanel
        self.Name=Buttons.ButtonWtxt(Screen,[0+of[0],0+of[1]],[200,30],"Select Core",20,1)
        self.Name.AddClick(Thing_Selector,(Screen,self.Comp,Ships.Modules.Corvete.Core,InfoPanel,(self.UpdateColor,())))
        self.Weapon1=Buttons.ButtonWsqr([of[0]+0,of[1]+40],[64,64],Screen,[100,100,100])
        self.Weapon1.AddClick(self.CheckAdd,("Weapon1",))
        self.Weapon2=Buttons.ButtonWsqr([of[0]+68,of[1]+40],[64,64],Screen,[100,100,100])
        self.Weapon2.AddClick(self.CheckAdd,("Weapon2",))
        self.Weapon3=Buttons.ButtonWsqr([of[0]+136,of[1]+40],[64,64],Screen,[100,100,100])
        self.Weapon3.AddClick(self.CheckAdd,("Weapon3",))
        self.Weapon4=Buttons.ButtonWsqr([of[0]+0,of[1]+108],[64,64],Screen,[100,100,100])
        self.Weapon4.AddClick(self.CheckAdd,("Weapon4",))
        self.Weapon5=Buttons.ButtonWsqr([of[0]+68,of[1]+108],[64,64],Screen,[100,100,100])
        self.Weapon5.AddClick(self.CheckAdd,("Weapon5",))
        self.Weapon6=Buttons.ButtonWsqr([of[0]+136,of[1]+108],[64,64],Screen,[100,100,100])
        self.Weapon6.AddClick(self.CheckAdd,("Weapon6",))


        self.Utility1=Buttons.ButtonWsqr([of[0]+0,of[1]+518],[64,64],Screen,[100,100,100])
        self.Utility1.AddClick(self.CheckAdd,("Utility1",))
        self.Utility2=Buttons.ButtonWsqr([of[0]+68,of[1]+518],[64,64],Screen,[100,100,100])
        self.Utility2.AddClick(self.CheckAdd,("Utility2",))
        self.Utility3=Buttons.ButtonWsqr([of[0]+136,of[1]+518],[64,64],Screen,[100,100,100])
        self.Utility3.AddClick(self.CheckAdd,("Utility3",))
        self.Utility4=Buttons.ButtonWsqr([of[0]+0,of[1]+450],[64,64],Screen,[100,100,100])
        self.Utility4.AddClick(self.CheckAdd,("Utility4",))
        self.Utility5=Buttons.ButtonWsqr([of[0]+68,of[1]+450],[64,64],Screen,[100,100,100])
        self.Utility5.AddClick(self.CheckAdd,("Utility5",))
        self.Utility6=Buttons.ButtonWsqr([of[0]+136,of[1]+450],[64,64],Screen,[100,100,100])
        self.Utility6.AddClick(self.CheckAdd,("Utility6",))

        self.UpdateColor()
        Screen.draw()
    def Clear(self):
        self.Name.Remove()

        self.Weapon1.Remove()
        self.Weapon2.Remove()
        self.Weapon3.Remove()
        self.Weapon4.Remove()
        self.Weapon5.Remove()
        self.Weapon6.Remove()

        self.Utility1.Remove()
        self.Utility2.Remove()
        self.Utility3.Remove()
        self.Utility4.Remove()
        self.Utility5.Remove()
        self.Utility6.Remove()
class General:
    def __init__(self,Screen,stack):
        self.Screen=Screen
        self.stack=stack
        stack.append(self)
    def SetName(self):
        self.Ship.SetName(self.Name.txt.txt)
    def Show(self):
        self.Info=Box.FCST.InfoBox(CST.DesignerGeneral.InfoBar.InfoPanel,self.Screen)

        self.Save=Buttons.FCST.ButtonWtxt(CST.DesignerGeneral.InfoBar.SaveBut,self.Screen)
        self.Save.AddClick(self.SetName,())
        self.Save.AddClick(self.Ship.Save,())

        self.Cost=[Box.FCST.TxtBox_AL(CST.DesignerGeneral.InfoBar.Cost.L,self.Screen.background),
              Box.FCST.TxtBox_AR(CST.DesignerGeneral.InfoBar.Cost.R,self.Screen.background)]
        self.Power=[Box.FCST.TxtBox_AL(CST.DesignerGeneral.InfoBar.Power.L,self.Screen.background),
              Box.FCST.TxtBox_AR(CST.DesignerGeneral.InfoBar.Power.R,self.Screen.background)]
        self.Hull=[Box.FCST.TxtBox_AL(CST.DesignerGeneral.InfoBar.Hull.L,self.Screen.background),
              Box.FCST.TxtBox_AR(CST.DesignerGeneral.InfoBar.Hull.R,self.Screen.background)]
        self.Armor=[Box.FCST.TxtBox_AL(CST.DesignerGeneral.InfoBar.Armor.L,self.Screen.background),
              Box.FCST.TxtBox_AR(CST.DesignerGeneral.InfoBar.Armor.R,self.Screen.background)]
        self.Shield=[Box.FCST.TxtBox_AL(CST.DesignerGeneral.InfoBar.Shield.L,self.Screen.background),
              Box.FCST.TxtBox_AR(CST.DesignerGeneral.InfoBar.Shield.R,self.Screen.background)]
        self.Evasion=[Box.FCST.TxtBox_AL(CST.DesignerGeneral.InfoBar.Evasion.L,self.Screen.background),
              Box.FCST.TxtBox_AR(CST.DesignerGeneral.InfoBar.Evasion.R,self.Screen.background)]

        self.Name=Buttons.FCST.InBox(CST.DesignerGeneral.InfoBar.NameBox,self.Screen)
        self.Name.txt.Change2(self.Ship.Name)



        self.Reactor=Buttons.FCST.ButtonWsqr(CST.DesignerGeneral.Components.Reactor,self.Screen)
        self.Hiperdrive=Buttons.FCST.ButtonWsqr(CST.DesignerGeneral.Components.Hiperdrive,self.Screen)
        self.Thrusters=Buttons.FCST.ButtonWsqr(CST.DesignerGeneral.Components.Thrusters,self.Screen)
        self.Sensors=Buttons.FCST.ButtonWsqr(CST.DesignerGeneral.Components.Sensors,self.Screen)
        self.AI=Buttons.FCST.ButtonWsqr(CST.DesignerGeneral.Components.AI,self.Screen)

        ## # TODO:  MOVE TO Titan CLASS
        ## self.Aura=Buttons.FCST.ButtonWsqr(CST.DesignerGeneral.Components.Aura,self.Screen)

    def UpdateInfo(self):
        self.Power[0].draw()
        self.Power[1].Change2(str(self.Ship.Power))
        self.Hull[0].draw()
        self.Hull[1].Change2(str(self.Ship.FinalHull))
        self.Armor[0].draw()
        self.Armor[1].Change2(str(self.Ship.FinalArmor))
        self.Shield[0].draw()
        self.Shield[1].Change2(str(self.Ship.FinalShield))
        self.Evasion[0].draw()
        self.Evasion[1].Change2(str(self.Ship.FinalEvasion))
        self.Screen.draw()
    def Clear(self):
        None
        self.Save.Remove()

        self.Cost[0].Remove()
        self.Cost[1].Remove()

        self.Power[0].Remove()
        self.Power[1].Remove()

        self.Hull[0].Remove()
        self.Hull[1].Remove()

        self.Armor[0].Remove()
        self.Armor[1].Remove()

        self.Shield[0].Remove()
        self.Shield[1].Remove()

        self.Evasion[0].Remove()
        self.Evasion[1].Remove()

        self.Name.Remove()

        self.Reactor.Remove()
        self.Hiperdrive.Remove()
        self.Thrusters.Remove()
        self.Sensors.Remove()
        self.AI.Remove()
class Active(General):
    def __init__(self,Screen,stack,Ship=None):
        if(Ship):
            self.Ship=Ships.Corvete.Load(Ship+".txt")

        else:
            self.Ship=Ships.Corvete()
        General.__init__(self,Screen,stack)
        self.Ship.OnBuild=(self.UpdateInfo,())
        self.Show()
    def SetBut(self):
        self.Reactor.AddClick(Thing_Selector,(self.Screen,self.Ship.Reactor,Ships.Components.Reactors.Corvete,self.Info))

        self.Hiperdrive.AddClick(Thing_Selector,(self.Screen,self.Ship.Hiperdrive,Ships.Components.Hiperdrives,self.Info))

        self.Thrusters.AddClick(Thing_Selector,(self.Screen,self.Ship.Thrusters,Ships.Components.Thrusters.Corvete,self.Info))
        self.Sensors.AddClick(Thing_Selector,(self.Screen,self.Ship.Sensors,Ships.Components.Sensors,self.Info))
        #self.AI.AddClick(Thing_Selector,(self.Screen,self.Ship.Reactor,Ships.Components.AI.Corvete,self.Info))
        None
    def Show(self):
        None
        General.Show(self)

        self.SetBut()
        #self.Core=Module(self.Screen,CST.DesignerGeneral.of_M,Ships.Modules.Slot("MCC",self.Ship))
        self.Core=Module(self.Screen,CST.DesignerGeneral.of_M,self.Ship.Core,self.Info)
        #self.g=Level_Selectore([100,100],[100,50],"Blue Lasers",self.Screen,self.Core.Comp,Ships.Modules.Corvete.Core.Interceptor,self.Info,["Large Weapon","Domg *1.5"])
        #self.Selectore=Thing_Selector(self.Screen,self.Core.Comp,Ships.Modules.Corvete.Core,self.Info)
        #self.Core=Module(self.Screen,CST.DesignerGeneral.of_L,self.Ship.Core)
        #self.Core=Module(self.Screen,CST.DesignerGeneral.of_R,self.Ship.Core)
        #self.Core.Comp.Equip(Ships.Modules.Corvete.Core.Interceptor)
        #Type_Selector(self.Screen,self.Core.Comp.Thing.Weapon1,Ships.Weapons.Small,self.Info)

        #self.Selectore.Remove()
        self.UpdateInfo()
        self.Screen.draw()
    def Clear(self):
        self.Ship.SetName(self.Name.txt.txt)
        self.Ship.Print()


        #print(self.Ship.Power)

        General.Clear(self)
        self.Core.Clear()
        self.Info.Remove()
        None
