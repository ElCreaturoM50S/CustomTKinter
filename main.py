import customtkinter

class Root(customtkinter.CKt):
    def __init__(self):
        super().__init__()

        self.geometry("300x300")
        self.title("snejk")

        self.gameMenu = None
        self.gameMain = None

root = Root()
root.mainloop()
