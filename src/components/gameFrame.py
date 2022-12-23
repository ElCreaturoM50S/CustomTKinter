import customtkinter

class GameFrame(customtkinter.CTkFrame):
    def __init__(self, root, handler):
        super().__init__(
            master=root,
            width=400,
            height=500
            )
        self.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)
        self.handler = handler