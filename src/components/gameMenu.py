import customtkinter
from .gameFrame import GameFrame

class GameMenu(GameFrame):
    def __init__(self, root, handler):
        super().__init__(root,handler)

        self.button = customtkinter.CTkButton(master=self,text="Zagraj",command=self.zagraj)
        self.button.place(relx=0.5, rely=0.2, anchor=customtkinter.CENTER)
        
    def zagraj(self):
        self.handler.changeFrame(0)