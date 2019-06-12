import pygame
import Buttons
import Box
import Constants as CST
import Interface.ShipBuilder.Designer.Corvete as Corvete
class Active:

    def __init__(self,Screen,stack):
        stack.append(self)
        self.Screen=Screen
        self.stack=stack
        self.Show()
    def Show(self):
        self.Title=Title=Box.FCST.TxtBox(CST.Ship_Builder.ClassSelector.SellectClass,self.Screen.background)

        self.but=but=[]
        self.Corvete=Corvete=Buttons.FCST.ButtonWtxt(CST.Ship_Builder.ClassSelector.SellectCorvete,self.Screen)
        but.append(Corvete)

        self.Destroyer=Destroyer=Buttons.FCST.ButtonWtxt(CST.Ship_Builder.ClassSelector.SellectDestroyer,self.Screen)
        #but.append(Destroyer)

        self.Cruiser=Cruiser=Buttons.FCST.ButtonWtxt(CST.Ship_Builder.ClassSelector.SellectCruiser,self.Screen)
        #but.append(Cruiser)

        self.Battleship=Battleship=Buttons.FCST.ButtonWtxt(CST.Ship_Builder.ClassSelector.SellectBattleship,self.Screen)
        #but.append(Battleship)

        self.Titan=Titan=Buttons.FCST.ButtonWtxt(CST.Ship_Builder.ClassSelector.SellectTitan,self.Screen)
        #but.append(Titan)


        self.Screen.draw()

        for B in but:
            B.AddClick(self.Clear,())
        Corvete.AddClick(CorveteBuilder,(self.Screen,self.stack))
        None

    def Clear(self):

            self.Title.Remove()
            self.Corvete.Remove()
            self.Destroyer.Remove()
            self.Cruiser.Remove()
            self.Battleship.Remove()
            self.Titan.Remove()
            self.Screen.draw()

#class ShipBuilder:
#    def __init__(self,Screen,stack):
#        self.Screen=Screen
#        self.stack=stack
#        stack.append(self)
#    def Show(self):
#        Load=Buttons.FCST.ButtonWtxt()
#        None
class CorveteBuilder:
    def __init__(self,Screen,stack):
        self.Screen=Screen
        self.stack=stack
        self.Show()
        stack.append(self)
    def Show(self):
        but=[]
        self.NewBut=New=Buttons.FCST.ButtonWtxt(CST.Ship_Builder.CorveteBuilder.NewButtton,self.Screen)
        but.append(New)


        self.LoadBut=Load=Buttons.FCST.ButtonWtxt(CST.Ship_Builder.CorveteBuilder.LoadButtton,self.Screen)

        but.append(Load)


        for B in but:
            B.AddClick(self.Clear,())
        New.AddClick(Corvete.Active,(self.Screen,self.stack))
        Load.AddClick(LoadCorvete,(self.Screen,self.stack))
        self.Screen.draw()
    def Clear(self):
        self.NewBut.Remove()
        self.LoadBut.Remove()
        self.Screen.draw()
class LoadCorvete:
    def __init__(self,Screen,stack):
        self.Screen=Screen
        self.stack=stack
        self.Show()
    def Show(self):
        File=open("Data/Save/Ships/Corvete/Ships.txt","r")
        n=int(File.readline())
        names=[]
        for i in range(n):
            names.append(File.readline()[:-5])
        File.close()
        self.Title=Box.TxtBox("Select Design",[350,50],[300,75],25,self.Screen.background,0)
        self.buts=[]
        for i in range(len(names)):
            self.buts.append(Buttons.ButtonWtxt(self.Screen,[350,130+42*i],[300,40],names[i],20,1))
            self.buts[-1].AddClick(self.Clear,())
            self.buts[-1].AddClick(Corvete.Active,(self.Screen,self.stack,names[i]))
        self.Screen.draw()
    def Clear(self):
        self.Title.Remove()
        for B in self.buts:
            B.Remove()
