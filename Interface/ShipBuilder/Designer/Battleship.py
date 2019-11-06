import Constants as CST
import Buttons
import Box
import Ships
from Interface.ShipBuilder.Designer.Base import *
class Active(General):
    def __init__(self,Screen,stack,Ship=None):
        self.Class="Battleship"
        if(Ship):
            self.Ship=Ships.Battleship.Load(Ship+".txt")
        else:
            self.Ship=Ships.Battleship()
        General.__init__(self,Screen,stack)
        self.Ship.OnBuild=(self.UpdateInfo,())
        self.Show()
    def Show(self):
        None
        General.Show(self)

        self.Bow=Module(self.Screen,CST.DesignerGeneral.of_L,self.Ship.Bow,self.Info)
        self.Core=Module(self.Screen,CST.DesignerGeneral.of_M,self.Ship.Core,self.Info)
        self.Stern=Module(self.Screen,CST.DesignerGeneral.of_R,self.Ship.Stern,self.Info)

        self.Screen.draw()
    def UpdateColor(self):
        self.Bow.UpdateColor()
        self.Core.UpdateColor()
        self.Stern.UpdateColor()
    def Clear(self):
        self.Ship.Print()

        General.Clear(self)
        self.Bow.Clear()
        self.Core.Clear()
        self.Stern.Clear()
        None
