import customtkinter

class GameMenu():
    def __init__(self,root):
        self.rootFrame = customtkinter.CTkFrame(
            master=root,
            width=300,
            height=300
            corner_radius=10)
        self.rootFrame.pack(padx=20, pady=20, sticky="nsew")