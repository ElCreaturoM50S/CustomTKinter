import customtkinter
from .gameFrame import GameFrame

class GameMain(GameFrame):
    def __init__(self, root, handler):
        super().__init__(root,handler)
        self.configure(fg_color="blue")

        #stats frame holder
        statsHolder = customtkinter.CTkFrame(
            master=self,
            height=100,
            width=400
        )
        statsHolder.grid(row=0,column=0)

        #create grid
        gridHolder = customtkinter.CTkFrame(
            master=self,
            height=100,
            width=400,
            fg_color="white"
        )
        gridHolder.grid(row=1,column=0)

        colors = ["green","dark green"]
        size = 40
        for x in range(10):
            for y in range(10):
                frame = customtkinter.CTkFrame(
                    master=gridHolder,
                    fg_color=colors[(y+x)%2],
                    height=size,width=size,
                    corner_radius=0
                    )
                frame.grid(row=x,column=y)