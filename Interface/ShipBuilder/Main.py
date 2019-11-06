import pygame
import Buttons
import Box
import Constants as CST
import Interface.ShipBuilder.Designer.Corvete as CorveteDesingner
import Interface.ShipBuilder.Designer.Destroyer as DestroyerDesingner
import Interface.ShipBuilder.Designer.Cruiser as CruiserDesingner
import Interface.ShipBuilder.Designer.Battleship as BattleshipDesingner

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
        but.append(Destroyer)

        self.Cruiser=Cruiser=Buttons.FCST.ButtonWtxt(CST.Ship_Builder.ClassSelector.SellectCruiser,self.Screen)
        but.append(Cruiser)

        self.Battleship=Battleship=Buttons.FCST.ButtonWtxt(CST.Ship_Builder.ClassSelector.SellectBattleship,self.Screen)
        but.append(Battleship)

        self.Titan=Titan=Buttons.FCST.ButtonWtxt(CST.Ship_Builder.ClassSelector.SellectTitan,self.Screen)
        #but.append(Titan)


        self.Screen.draw()

        for B in but:
            B.AddClick(self.Clear,())
        #Corvete.AddClick(CorveteI.Builder,(self.Screen,self.stack))
        Corvete.AddClick(Selector.Builder,(self.Screen,self.stack,CST.Ship_Builder.CorveteBuilder,CorveteDesingner,"Corvete"))
        Destroyer.AddClick(Selector.Builder,(self.Screen,self.stack,CST.Ship_Builder.DestroyerBuilder,DestroyerDesingner,"Destroyer"))
        Cruiser.AddClick(Selector.Builder,(self.Screen,self.stack,CST.Ship_Builder.CruiserBuilder,CruiserDesingner,"Cruiser"))
        Battleship.AddClick(Selector.Builder,(self.Screen,self.stack,CST.Ship_Builder.BattleshipBuilder,BattleshipDesingner,"Battleship"))

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

# TODO Change indent
class Selector:
    class Builder:
        def __init__(self,Screen,stack,ButPoz,NextInterface,FileName):
            self.Screen=Screen
            self.stack=stack
            self.ButPoz=ButPoz
            self.NextInterface=NextInterface
            self.FileName=FileName
            self.Show()
            stack.append(self)
        def Show(self):
            but=[]
            self.NewBut=New=Buttons.FCST.ButtonWtxt(self.ButPoz.NewButtton,self.Screen)
            but.append(New)


            self.LoadBut=Load=Buttons.FCST.ButtonWtxt(self.ButPoz.LoadButtton,self.Screen)

            but.append(Load)


            for B in but:
                B.AddClick(self.Clear,())
            New.AddClick(self.NextInterface.Active,(self.Screen,self.stack))
            Load.AddClick(Selector.Load,(self.Screen,self.stack,self.ButPoz,self.NextInterface,self.FileName))
            self.Screen.draw()
        def Clear(self):
            self.NewBut.Remove()
            self.LoadBut.Remove()
            self.Screen.draw()
    class Load:
        def __init__(self,Screen,stack,ButPoz,NextInterface,FileName):
            self.Screen=Screen
            self.stack=stack
            self.ButPoz=ButPoz
            self.NextInterface=NextInterface
            self.FileName=FileName
            self.Show()
        def Show(self):
            File=open("Data/Save/Ships/"+self.FileName+"/Ships.txt","r")
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
                self.buts[-1].AddClick(self.NextInterface.Active,(self.Screen,self.stack,names[i]))
            self.Screen.draw()
        def Clear(self):
            self.Title.Remove()
            for B in self.buts:
                B.Remove()
