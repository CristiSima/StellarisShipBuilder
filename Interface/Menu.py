import pygame
import Box
import Buttons
import Constants as CST
import Interface.ShipBuilder.Main as SB

class Active:
    def __init__(self,Screen,stack):
        self.Screen=Screen
        self.stack=stack
        stack.append(self)
        self.Show()
    def Show(self):
        # V1
        #self.ShipBuilder_But=Buttons.Button(Screen.M,CST.ShipBuilder.poz,CST.ShipBuilder.size)
        #self.ShipBuilder_Txt=Box.TxtBox("Ship Builder",CST.ShipBuilder.poz,CST.ShipBuilder.size,CST.ShipBuilder.font_size,Screen.background)

        ## V2
        ##self.ShipBuilder=Buttons.ButtonWtxt(Screen.M,CST.ShipBuilder.poz,CST.ShipBuilder.size,CST.ShipBuilder.txt,CST.ShipBuilder.font_size,Screen.background)

        but=[]
        self.ShipBuilder=Buttons.FCST.ButtonWtxt(CST.ShipBuilder,self.Screen)
        but.append(self.ShipBuilder)

        self.FleetBuilder=Buttons.FCST.ButtonWtxt(CST.FleetBuilder,self.Screen)

        self.BattleSimulator=Buttons.FCST.ButtonWtxt(CST.BattleSimulator,self.Screen)


        self.Screen.draw()
        #but.append(self.FleetBuilder)
        #but.append(self.BattleSimulator)
        for B in but:
            B.AddClick(self.Clear,())
        self.ShipBuilder.AddClick(SB.Active,(self.Screen,self.stack))
    def Clear(self):
        self.ShipBuilder.Remove()
        self.FleetBuilder.Remove()
        self.BattleSimulator.Remove()
        self.Screen.draw()
