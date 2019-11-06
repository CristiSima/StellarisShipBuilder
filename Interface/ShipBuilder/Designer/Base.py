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
        if(Screen.Clean):
            if(command and Screen.Clean==command):
                Screen.Clean=(lambda a,b:(a[0](*a[1]),b[0](*b[1])),(Screen.Clean,(self.Remove,())))
            else:
                Screen.Clean[0](*Screen.Clean[1])
                Screen.Clean=(self.Remove,())
        else:
            Screen.Clean=(self.Remove,())

        self.Screen=Screen
        self.Slot=Slot
        self.Things=Things
        self.InfoPanel=InfoPanel

        self.l=l=[]
        #for T in Things.Variants:
        for i in range(len(Things.Variants)):
            l.append(Level_Selector(i,Screen,Slot,Things.Variants[i],InfoPanel))

            l[-1].But.AddClick(*Screen.Clean)
            if(command):
                l[-1].But.AddClick(*command)
                l[-1].But.AddClick(self.Remove,())
            else:
                l[-1].But.AddClick(self.Remove,())
        Screen.draw()
    def Remove(self):
        self.Screen.Clean=None
        for L in self.l:
            L.Remove()
        self.l=[]
        self.Screen.draw()

class Type_Selector:
    # txt=[["Laser","Plasmathrower"],["BLue Lasers","Red Lasers"],[],[]] =>>> MOve In Def
    # Things=[[Small.Lasers.Laser_T1,Small.Lasers.Laser_T2],[]]
    # Infos =>Move in Def
    def __init__(self,Screen,Slot,Things,InfoPanel):
        if(Screen.Clean):
            Screen.Clean[0](*Screen.Clean[1])
        Screen.Clean=(self.Remove,())

        self.poz=[10,200]
        self.size=[250,25]
        self.Screen=Screen
        self.Slot=Slot
        self.Things=Things
        self.InfoPanel=InfoPanel
        self.l=l=[]
        for i in range(len(Things.Variants)):
            print(Things.Variants[i].Name,self.poz)
            poz=[self.poz[0],self.poz[1]+27*(i)]
            l.append(Buttons.ButtonWtxt(Screen,poz,self.size,Things.Variants[i].Name,20,1))
            l[i].AddClick(Thing_Selector,(Screen,Slot,Things.Variants[i],InfoPanel,(self.Remove,())))
            #
            ##creat in Limbo
            #fix :lambda a,b:(a[0](*a[1]),b[0](*b[1]))
            #
            l[i].AddHover(InfoPanel.Change2,(Things.Variants[i].Info,))
            None
        Screen.draw()
    def Remove(self):
        self.Clean=None
        for i in self.l:

            i.Remove()

        self.Screen.draw()
class Colors:
    NoSlot=[50,50,50]
    Empty=[250,250,250]
    Filled=[150,150,150]
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
                if(self.Comp.Thing.Weapon1.Thing):
                    self.Weapon1.Change2(Colors.Filled)
                else:
                    self.Weapon1.Change2(Colors.Empty)
            else:
                self.Weapon1.Change2(Colors.NoSlot)

            if(self.Comp.Thing.Weapon2):
                if(self.Comp.Thing.Weapon2.Thing):
                    self.Weapon2.Change2(Colors.Filled)
                else:
                    self.Weapon2.Change2(Colors.Empty)
            else:
                self.Weapon2.Change2(Colors.NoSlot)

            if(self.Comp.Thing.Weapon3):
                if(self.Comp.Thing.Weapon3.Thing):
                    self.Weapon3.Change2(Colors.Filled)
                else:
                    self.Weapon3.Change2(Colors.Empty)
            else:
                self.Weapon3.Change2(Colors.NoSlot)

            if(self.Comp.Thing.Weapon4):
                if(self.Comp.Thing.Weapon4.Thing):
                    self.Weapon4.Change2(Colors.Filled)
                else:
                    self.Weapon4.Change2(Colors.Empty)
            else:
                self.Weapon4.Change2(Colors.NoSlot)

            if(self.Comp.Thing.Weapon5):
                if(self.Comp.Thing.Weapon5.Thing):
                    self.Weapon5.Change2(Colors.Filled)
                else:
                    self.Weapon5.Change2(Colors.Empty)
            else:
                self.Weapon5.Change2(Colors.NoSlot)

            if(self.Comp.Thing.Weapon6):
                if(self.Comp.Thing.Weapon6.Thing):
                    self.Weapon6.Change2(Colors.Filled)
                else:
                    self.Weapon6.Change2(Colors.Empty)
            else:
                self.Weapon6.Change2(Colors.NoSlot)


            if(self.Comp.Thing.Utility1):
                if(self.Comp.Thing.Utility1.Thing):
                    self.Utility1.Change2(Colors.Filled)
                else:
                    self.Utility1.Change2(Colors.Empty)
            else:
                self.Utility1.Change2(Colors.NoSlot)

            if(self.Comp.Thing.Utility2):
                if(self.Comp.Thing.Utility2.Thing):
                    self.Utility2.Change2(Colors.Filled)
                else:
                    self.Utility2.Change2(Colors.Empty)
            else:
                self.Utility2.Change2(Colors.NoSlot)

            if(self.Comp.Thing.Utility3):
                if(self.Comp.Thing.Utility3.Thing):
                    self.Utility3.Change2(Colors.Filled)
                else:
                    self.Utility3.Change2(Colors.Empty)
            else:
                self.Utility3.Change2(Colors.NoSlot)

            if(self.Comp.Thing.Utility4):
                if(self.Comp.Thing.Utility4.Thing):
                    self.Utility4.Change2(Colors.Filled)
                else:
                    self.Utility4.Change2(Colors.Empty)
            else:
                self.Utility4.Change2(Colors.NoSlot)

            if(self.Comp.Thing.Utility5):
                if(self.Comp.Thing.Utility5.Thing):
                    self.Utility5.Change2(Colors.Filled)
                else:
                    self.Utility5.Change2(Colors.Empty)
            else:
                self.Utility5.Change2(Colors.NoSlot)

            if(self.Comp.Thing.Utility6):
                if(self.Comp.Thing.Utility6.Thing):
                    self.Utility6.Change2(Colors.Filled)
                else:
                    self.Utility6.Change2(Colors.Empty)
            else:
                self.Utility6.Change2(Colors.NoSlot)

    def __init__(self,Screen,of,Comp,InfoPanel):
        self.Comp=Comp
        self.of=of
        self.Screen=Screen
        self.InfoPanel=InfoPanel
        self.Name=Buttons.ButtonWtxt(Screen,[0+of[0],0+of[1]],[200,30],"Select Core",20,1)

        T=None
        for i in eval("Ships.Modules."+Comp.Ship.Class+".Variants"):
            if(i.Type==Comp.Type):
                T=i

        self.Name.AddClick(Thing_Selector,(Screen,self.Comp,T,InfoPanel,(self.UpdateColor,())))
        self.Weapon1=Buttons.ButtonWsqr([of[0]+0,of[1]+40],[64,64],Screen,Colors.NoSlot)
        self.Weapon1.AddClick(self.CheckAdd,("Weapon1",))
        self.Weapon2=Buttons.ButtonWsqr([of[0]+68,of[1]+40],[64,64],Screen,Colors.NoSlot)
        self.Weapon2.AddClick(self.CheckAdd,("Weapon2",))
        self.Weapon3=Buttons.ButtonWsqr([of[0]+136,of[1]+40],[64,64],Screen,Colors.NoSlot)
        self.Weapon3.AddClick(self.CheckAdd,("Weapon3",))
        self.Weapon4=Buttons.ButtonWsqr([of[0]+0,of[1]+108],[64,64],Screen,Colors.NoSlot)
        self.Weapon4.AddClick(self.CheckAdd,("Weapon4",))
        self.Weapon5=Buttons.ButtonWsqr([of[0]+68,of[1]+108],[64,64],Screen,Colors.NoSlot)
        self.Weapon5.AddClick(self.CheckAdd,("Weapon5",))
        self.Weapon6=Buttons.ButtonWsqr([of[0]+136,of[1]+108],[64,64],Screen,Colors.NoSlot)
        self.Weapon6.AddClick(self.CheckAdd,("Weapon6",))


        self.Utility1=Buttons.ButtonWsqr([of[0]+0,of[1]+518],[64,64],Screen,Colors.NoSlot)
        self.Utility1.AddClick(self.CheckAdd,("Utility1",))
        self.Utility2=Buttons.ButtonWsqr([of[0]+68,of[1]+518],[64,64],Screen,Colors.NoSlot)
        self.Utility2.AddClick(self.CheckAdd,("Utility2",))
        self.Utility3=Buttons.ButtonWsqr([of[0]+136,of[1]+518],[64,64],Screen,Colors.NoSlot)
        self.Utility3.AddClick(self.CheckAdd,("Utility3",))
        self.Utility4=Buttons.ButtonWsqr([of[0]+0,of[1]+450],[64,64],Screen,Colors.NoSlot)
        self.Utility4.AddClick(self.CheckAdd,("Utility4",))
        self.Utility5=Buttons.ButtonWsqr([of[0]+68,of[1]+450],[64,64],Screen,Colors.NoSlot)
        self.Utility5.AddClick(self.CheckAdd,("Utility5",))
        self.Utility6=Buttons.ButtonWsqr([of[0]+136,of[1]+450],[64,64],Screen,Colors.NoSlot)
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
        self.Speed=[Box.FCST.TxtBox_AL(CST.DesignerGeneral.InfoBar.Speed.L,self.Screen.background),
              Box.FCST.TxtBox_AR(CST.DesignerGeneral.InfoBar.Speed.R,self.Screen.background)]
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

        self.SetBut()
        self.UpdateInfo()
    def UpdateColor(self):
        pass
    def SetBut(self):
        self.Reactor.AddClick(Thing_Selector,(self.Screen,self.Ship.Reactor,eval("Ships.Components.Reactors."+self.Class),self.Info))
        self.Hiperdrive.AddClick(Thing_Selector,(self.Screen,self.Ship.Hiperdrive,Ships.Components.Hiperdrives,self.Info))
        self.Thrusters.AddClick(Thing_Selector,(self.Screen,self.Ship.Thrusters,eval("Ships.Components.Thrusters."+self.Class),self.Info))
        self.Sensors.AddClick(Thing_Selector,(self.Screen,self.Ship.Sensors,Ships.Components.Sensors,self.Info))
        #self.AI.AddClick(Thing_Selector,(self.Screen,self.Ship.Reactor,eval("Ships.Components.AI."+self.Class),self.Info))
        None

    def UpdateInfo(self):
        self.Power[0].draw()
        self.Power[1].Change2(str(self.Ship.Power))
        self.Cost[0].draw()
        self.Cost[1].Change2(str(self.Ship.FinalCost))
        self.Hull[0].draw()
        self.Hull[1].Change2(str(self.Ship.FinalHull))
        self.Armor[0].draw()
        self.Armor[1].Change2(str(self.Ship.FinalArmor))
        self.Shield[0].draw()
        self.Shield[1].Change2(str(self.Ship.FinalShield))
        self.Speed[0].draw()
        self.Speed[1].Change2(str(int(self.Ship.FinalSpeed)))
        self.Evasion[0].draw()
        self.Evasion[1].Change2(str(self.Ship.FinalEvasion))
        try:
            self.UpdateColor()
        except:
            None
        self.Screen.draw()
    def Clear(self):
        None
        self.Ship.SetName(self.Name.txt.txt)

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

        self.Speed[0].Remove()
        self.Speed[1].Remove()

        self.Evasion[0].Remove()
        self.Evasion[1].Remove()

        self.Name.Remove()

        self.Reactor.Remove()
        self.Hiperdrive.Remove()
        self.Thrusters.Remove()
        self.Sensors.Remove()
        self.AI.Remove()


        self.Info.Remove()
