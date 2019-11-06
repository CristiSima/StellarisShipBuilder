import Constants as CST
import Buttons
import Box
import Ships
from Interface.ShipBuilder.Designer.Base import *
class Active(General):
    def __init__(self,Screen,stack,Ship=None):
        self.Class="Destroyer"
        if(Ship):
            self.Ship=Ships.Destroyer.Load(Ship+".txt")
        else:
            self.Ship=Ships.Destroyer()
        General.__init__(self,Screen,stack)
        self.Ship.OnBuild=(self.UpdateInfo,())
        self.Show()
    def Show(self):
        None
        General.Show(self)

        self.Bow=Module(self.Screen,CST.DesignerGeneral.of_L,self.Ship.Bow,self.Info)
        self.Stern=Module(self.Screen,CST.DesignerGeneral.of_R,self.Ship.Stern,self.Info)

        self.Screen.draw()
    def UpdateColor(self):
        self.Bow.UpdateColor()
        self.Stern.UpdateColor()
    def Clear(self):
        self.Ship.Print()

        General.Clear(self)
        self.Bow.Clear()
        self.Stern.Clear()
        None
