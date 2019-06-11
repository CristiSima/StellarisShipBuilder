import pygame
import Constants
import sys
import math
import Buttons
import Weapons
import Modules
import Utilitys
import Components
import Ships
import Interface.Menu
import Box

def matrix(n,m,EB):
    M=[]
    T=[]
    for j in range(m):
        T.append(EB)
    for i in range(n):
        M.append(T.copy())
    return M

class Screen:
    def __init__(self,W,H):
        self.W=W
        self.H=H
        self.M=None
        self.TxtBox=None
        self.EmptyBut=Buttons.Button(self,(0,0),(0,0))
        self.M=matrix(W+1,H+1,self.EmptyBut)
        self.screen = pygame.display.set_mode((W,H))
        self.background=pygame.Surface((W,H))
        pygame.display.set_caption("Stellaris Space Combat Simulator")

    def draw(self):
        self.screen.blit(self.background,(0,0))
        pygame.display.flip()

    def Tick(self):
        self.M[pygame.mouse.get_pos()[0]][pygame.mouse.get_pos()[1]].Hover()
        for event in pygame.event.get():
            if(event.type==pygame.QUIT):
                sys.exit()
            if(event.type==pygame.KEYDOWN):
                #print(event.key)
                if(self.TxtBox):
                    None
                    if(event.key==27):
                        self.TxtBox.Unfocus()
                    if(event.key==8):#remove
                        self.TxtBox.txt.Pop()
                        self.draw()
                    if(event.key in range(ord("a"),ord("z")+1)):#add letters a->z
                        c=chr(event.key)
                        #print(pygame.key.get_pressed()[304])
                        #print(pygame.key.get_mods() and pygame.KMOD_CAPS)
                        #print("##############")
                        if( (pygame.key.get_pressed()[304]!=0) ):#^ ((pygame.key.get_mods() and pygame.KMOD_CAPS)!=0) ):#pygame.KMOD_SHIFT ???
                            print("ss")
                            c=chr(event.key-32)
                        self.TxtBox.txt.Add(c)
                        self.draw()
                    if(event.key in range(ord("0"),ord("9")+1)):#add letters a->z
                        c=chr(event.key)
                        self.TxtBox.txt.Add(c)
                        self.draw()

                else:
                    if(event.key==27):
                        sys.exit()
                    if(event.key==8):
                        if(len(self.stack)!=1):
                            #print(self.stack)
                            self.stack[-1].Clear()
                            self.stack.pop()
                            #print(self.stack)
                            self.stack[-1].Show()
                        else:
                            self.stack[-1].Clear()
                            sys.exit()
            if(event.type==pygame.MOUSEBUTTONUP):
                #print("Click")
                if(self.TxtBox):
                    if(self.M[pygame.mouse.get_pos()[0]][pygame.mouse.get_pos()[1]]!=self.TxtBox):
                        self.TxtBox.Unfocus()
                self.M[pygame.mouse.get_pos()[0]][pygame.mouse.get_pos()[1]].Click()


if(__name__=="__main__"):
    pygame.init()
    S=Screen(Constants.Window_With,Constants.Window_Height)
    S.draw()
    if(False):
        s=Ships.Corvete()
        s.Core.Equip(Modules.Corvete.Core.Interceptor)
        s.Core.Thing.Weapon1.Equip(Weapons.Small.Lasers.Laser_T1)
        s.Core.Thing.Utility1.Equip(Utilitys.Small.Shields.Shield_T1)
        s.SetName("Party")
        s.Save()
        l=Ships.Corvete.Load("Party.txt")
        l.SetName("P2")
        l.Save()
        B=Buttons.Button(S.M,(50,50),(50,50))
    S.stack=stack=[]
<<<<<<< HEAD

    #Main Menu
    #Interface.Menu.Active(S,stack)

    #Ship Design
    Interface.Menu.SB.Active(S,stack)

    #Corvete Design
=======
    Interface.Menu.Active(S,stack)

>>>>>>> refs/remotes/origin/master
    #Interface.Menu.SB.Corvete.Active(S,stack)


    #MainMenu.Show()
    #I=Box.Img((200,200),S,"/home/smu/Pictures/Screenshot.png")
    while True:
        #S.draw()
        S.Tick()
