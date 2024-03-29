import Constants as CST
import Buttons
import Box
import Ships
from Interface.ShipBuilder.Designer.Base import *
class Active(General):
    def __init__(self,Screen,stack,Ship=None):
        self.Class="Corvete"
        if(Ship):
            self.Ship=Ships.Corvete.Load(Ship+".txt")
        else:
            self.Ship=Ships.Corvete()
        General.__init__(self,Screen,stack)
        self.Ship.OnBuild=(self.UpdateInfo,())
        self.Show()
    def Show(self):
        None
        General.Show(self)
        self.Core=Module(self.Screen,CST.DesignerGeneral.of_M,self.Ship.Core,self.Info)

        self.Screen.draw()
    def UpdateColor(self):
        self.Core.UpdateColor()
    def Clear(self):
        self.Ship.Print()

        General.Clear(self)
        self.Core.Clear()
        None
