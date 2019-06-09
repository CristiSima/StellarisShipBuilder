import pygame
import Box


class Button:
    def __init__(self,Screen,poz,size):
        self.OnClick=[]
        self.OnHover=[]
        self.Screen=Screen
        self.poz=poz
        self.size=size
        self.FillRef()
    def Click(self):
        #print("Button at ",pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1])
        for f,p in self.OnClick:
            f(*p)
    def Hover(self):
        for f,p in self.OnHover:
            f(*p)
    def AddClick(self,f,p):
        self.OnClick.append((f,p))
    def AddHover(self,f,p):
        self.OnHover.append((f,p))
    def RemClick(self,i):
        self.OnClick.remove(i)

    def FillRef(self):
        for i in range(self.size[0]):
            for j in range(self.size[1]):
                self.Screen.M[self.poz[0]+i][self.poz[1]+j]=self
    def Remove(self):
        for i in range(self.size[0]):
            for j in range(self.size[1]):
                self.Screen.M[self.poz[0]+i][self.poz[1]+j]=self.Screen.EmptyBut

class Button_Empty:
    def Click(self):
        None
        #print("Empty at ",pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1])
    def Hover(self):
        None
class ButtonWtxt(Button):
    def __init__(self,Screen,poz,size,txt,font_size,fontID=0):
        Button.__init__(self,Screen,poz,size)
        self.txt=Box.TxtBox(txt,poz,size,font_size,Screen.background,fontID)
    def Remove(self):
        Button.Remove(self)
        self.txt.Remove()

class ButtonWphoto(Button):
    def __init__(self,poz,size,Screen,path=None):
        Button.__init__(self,Screen,poz,size)
        self.Img=Box.Img(poz,Screen,path)
        self.Img.draw()
    def draw(self):
        self.Img.draw()
    def Change2(self,path=None):
        self.Img.Change2(path)
class ButtonWsqr(Button):
    def __init__(self,poz,size,Screen,color=[255,255,255]):
        Button.__init__(self,Screen,poz,size)
        self.color=color
        self.draw()
    def draw(self):
        self.Rect=pygame.Rect(self.poz[0],self.poz[1],self.size[0],self.size[1])
        pygame.draw.rect(self.Screen.background,self.color,self.Rect)
    def Change2(self,color):
        self.color=color
        pygame.draw.rect(self.Screen.background,self.color,self.Rect)
        None
    def Remove(self):
        pygame.draw.rect(self.Screen.background,[0,0,0],self.Rect)
        Button.Remove(self)

class InBox(ButtonWtxt):
    def __init__(self,Screen,poz,size,font_size,fontID):
        ButtonWtxt.__init__(self,Screen,poz,size,"",font_size,fontID)
        self.AddClick(self.Focus,())
    def Focus(self):
        self.Screen.TxtBox=self
        self.OnClick=[]
        #print("Focus")
        None

    def Unfocus(self):
        #print("Unfocus")
        self.Screen.TxtBox=None
        self.AddClick(self.Focus,())
        None
class FCST:
    class ButtonWtxt(ButtonWtxt):
        def __init__(self,STATS,Screen):
            ButtonWtxt.__init__(self,Screen,STATS.poz,STATS.size,STATS.txt,STATS.font_size,STATS.fontID)
    class ButtonWphoto(ButtonWtxt):
        def __init__(self,STATS,Screen):
            ButtonWphoto.__init__(self,Screen,STATS.poz,STATS.size,STATS.txt,STATS.font_size,STATS.fontID,STATS.path)
    class ButtonWsqr(ButtonWsqr):
        def __init__(self,STATS,Screen):
            ButtonWsqr.__init__(self,STATS.poz,STATS.size,Screen)
    class InBox(InBox):
        def __init__(self,STATS,Screen):
            InBox.__init__(self,Screen,STATS.poz,STATS.size,STATS.font_size,STATS.fontID)
