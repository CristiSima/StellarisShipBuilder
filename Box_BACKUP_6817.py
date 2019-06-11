import pygame
import os
fonts=[
    "Orbitronio.ttf",
    "aerial.ttf",
    "AldotheApache.ttf",
]
pygame.init()
class TxtBox:
    #print(os.system("pwd"))
    def __init__(self,txt,poz,size,font_size,background,fontID=0):
        self.txt=txt
        self.Opoz=poz.copy()
        self.Osize=size.copy()
        self.poz=poz.copy()
        self.size=size.copy()
        self.font_size=font_size
        self.background=background
        self.font=pygame.font.Font("Data/Fonts/"+fonts[fontID],font_size)
        #print(self.poz,self.size)
        self.draw()
    def draw(self):
        self.poz=self.Opoz.copy()
        self.size=self.Osize.copy()
        self.TxtObj=self.font.render(self.txt,True,[0,0,0],[255,255,255])
        self.poz[0]+=(self.size[0]-self.font.size(self.txt)[0])//2
        self.poz[1]+=(self.size[1]-self.font.size(self.txt)[1])//2
        self.Rect=pygame.Rect(self.Opoz[0],self.Opoz[1],self.Osize[0],self.Osize[1])
        pygame.draw.rect(self.background,[255,255,255],self.Rect)
        self.background.blit(self.TxtObj,self.poz)
    def SetPoz(self,poz):
        self.poz=poz
    def size(self):
        return self.TxtObj
    def Add(self,c):
        self.txt+=c
        self.draw()
<<<<<<< HEAD
    def Change2(self,txt):
        self.txt=txt
        self.draw()
=======
>>>>>>> refs/remotes/origin/master
    def Pop(self):
        None
        self.txt=self.txt[:-1]
        self.draw()
    def Remove(self):
        pygame.draw.rect(self.background,[0,0,0],self.Rect)
class Line:
    def __init__(self,poz,txt,font,background):
        self.poz=poz
        self.txt=txt
        self.font=font
        self.background=background

        self.draw()
    def draw(self):
        self.TxtObj=self.font.render(self.txt,True,[0,0,0],[255,255,255])
        self.size=self.font.size(self.txt)
        self.Rect=pygame.Rect(self.poz[0],self.poz[1],self.size[0],self.size[1])
        pygame.draw.rect(self.background,[255,255,255],self.Rect)
        self.background.blit(self.TxtObj,self.poz)
        None
    def Remove(self):
        pygame.draw.rect(self.background,[0,0,0],self.Rect)


class InfoBox:
    def __init__(self,poz,size,txt,font_size,fontID,Screen):
        self.poz=poz
        self.size=size
        self.txt=txt
        self.font_size=font_size
        self.fontID=fontID
        self.Screen=Screen
        self.background=Screen.background
        self.font=pygame.font.Font("Data/Fonts/"+fonts[fontID],font_size)
        self.Rect=pygame.Rect(self.poz[0],self.poz[1],self.size[0],self.size[1])
        self.draw()
    def draw(self):
        self.lines=[]
        pygame.draw.rect(self.background,[255,255,255],self.Rect)
        for i in range(len(self.txt)):
            self.lines.append(Line((self.poz[0]+1,self.poz[1]+self.font.size("t")[1]*i),self.txt[i],self.font,self.Screen.background))
    def Remove(self):
        self.Clear()
        pygame.draw.rect(self.background,[0,0,0],self.Rect)

    def Clear(self):
        for l in self.lines:
            l.Remove()
        l=[]
    def Change2(self,txt):
        #print("C")
        if(self.txt==txt):
            return
        self.Clear()
        self.txt=txt
        self.draw()
        self.Screen.draw()


class TxtBox_AR(TxtBox):
        def __init__(self,txt,poz,size,font_size,background,fontID=0):
            self.txt=txt
<<<<<<< HEAD
            self.Opoz=poz.copy()
            self.Osize=size.copy()
=======
>>>>>>> refs/remotes/origin/master
            self.poz=poz.copy()
            self.poz[0]=poz[0]+size[0]
            #self.poz[1]=poz[1]+size[1]
            self.size=size.copy()
            self.font_size=font_size
            self.background=background
            self.font=pygame.font.Font("Data/Fonts/"+fonts[fontID],font_size)

            self.draw()
        def draw(self):
<<<<<<< HEAD
            self.poz=self.Opoz.copy()
            self.size=self.Osize.copy()
            self.poz[0]=self.poz[0]+self.size[0]
=======
>>>>>>> refs/remotes/origin/master
            self.TxtObj=self.font.render(self.txt,True,[0,0,0],[255,255,255])
            self.poz[0]-=self.font.size(self.txt)[0]
            self.size[0]=self.font.size(self.txt)[0]

            #self.poz[1]-=self.font.size(txt)[1]
            self.poz[1]+=(self.size[1]-self.font.size(self.txt)[1])//2
            self.size[1]=self.font.size(self.txt)[1]

            #print(self.poz,self.size)
            self.Rect=pygame.Rect(self.poz[0],self.poz[1],self.size[0],self.size[1])
            pygame.draw.rect(self.background,[255,255,255],self.Rect)
            self.background.blit(self.TxtObj,self.poz)

class TxtBox_AL(TxtBox):
        def __init__(self,txt,poz,size,font_size,background,fontID=0):
            self.txt=txt
<<<<<<< HEAD
            self.Opoz=poz.copy()
            self.Osize=size.copy()
            self.poz=poz.copy()
            self.size=size.copy()

            #self.poz[1]=poz[1]+size[1]
=======
            self.poz=poz.copy()
            #self.poz[1]=poz[1]+size[1]
            self.size=size.copy()
>>>>>>> refs/remotes/origin/master
            self.font_size=font_size
            self.background=background
            self.font=pygame.font.Font("Data/Fonts/"+fonts[fontID],font_size)

            self.draw()
        def draw(self):
<<<<<<< HEAD
            self.size=self.Osize.copy()
            self.poz=self.Opoz.copy()
=======
>>>>>>> refs/remotes/origin/master
            self.TxtObj=self.font.render(self.txt,True,[0,0,0],[255,255,255])
            #self.size[0]=self.font.size(txt)[0]

            #self.poz[1]-=self.font.size(txt)[1]
            self.poz[1]+=(self.size[1]-self.font.size(self.txt)[1])//2
            self.size[1]=self.font.size(self.txt)[1]
            self.poz[0]+=1
            #print(self.poz,self.size)
            self.Rect=pygame.Rect(self.poz[0]-1,self.poz[1],self.size[0],self.size[1])
            pygame.draw.rect(self.background,[255,255,255],self.Rect)
            self.background.blit(self.TxtObj,self.poz)

class Img:
    def __init__(self,poz,Screen,path=None):
        self.poz=poz
        self.path=path
        self.Screen=Screen
        self.img=None
        if(path):
            self.img=pygame.image.load(path)
            #self.img.set_colorkey([0,0,0])
            self.img.set_alpha(255)
            self.draw()

    def Change2(self,path=None):
        self.path=path
        if(path):
            self.img=pygame.image.load(path)
            #self.img.set_colorkey([0,0,0])
            self.img.set_alpha(255)
            self.draw()

    def draw(self):
        if(self.path):
            self.Screen.screen.blit(self.img,self.poz)
            pygame.display.flip()


class FCST:
    class TxtBox(TxtBox):
        def __init__(self,STATS,background):
            TxtBox.__init__(self,STATS.txt,STATS.poz,STATS.size,STATS.font_size,background,STATS.fontID)

    class TxtBox_AR(TxtBox_AR):
        def __init__(self,STATS,background):
            TxtBox_AR.__init__(self,STATS.txt,STATS.poz,STATS.size,STATS.font_size,background,STATS.fontID)

    class TxtBox_AL(TxtBox_AL):
        def __init__(self,STATS,background):
            TxtBox_AL.__init__(self,STATS.txt,STATS.poz,STATS.size,STATS.font_size,background,STATS.fontID)
    class InfoBox(InfoBox):
        def __init__(self,STATS,Screen):
            InfoBox.__init__(self,STATS.poz,STATS.size,STATS.txt,STATS.font_size,STATS.fontID,Screen)
