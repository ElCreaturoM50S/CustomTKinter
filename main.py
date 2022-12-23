import customtkinter
from src.components.gameHandler import Handler

class Root(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("400x500")

        self.title("snejk")
        self.gameMenuHandler = Handler(self)

root = Root()
root.mainloop()
