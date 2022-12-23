import customtkinter

from .gameMenu import GameMenu
from .gameMain import GameMain

class Handler():
    def __init__(self,root):
        self.root = root
        self.currentFrame = GameMenu(root,self)
        self.frames = [GameMain,GameMenu]

    def createFrame(self,frame):
        print("create")
        self.frames[frame](self.root,self)

    def destroyCurrentFrame(self):
        print("destroy")
        self.currentFrame.destroy()

    def changeFrame(self,frame):
        self.destroyCurrentFrame()
        self.createFrame(frame)