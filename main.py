import customtkinter
import random

class Root(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.resizable(0,0)
        self.title("snejk")
        
        self.score = 0
        self.direction = "right"
        self.isGameOn = False

        self.gameWidth = 700
        self.gameHeight = 900
        self.speed = 120
        self.spaceSize = 50
        self.bodyParts = 2
        self.direction = "right"
        self.foodColor = "#ffff00"
        self.snakeColor = "#ff0000"
        self.backgroundColor = "#808080"
        self.gameoverBackgroundColor = "#000000"
        self.textBoxSpace = 350
        self.lockChangeDirection = False

        self.geometry(str(self.gameWidth)+'x'+str(self.gameHeight))

        self.canvas = customtkinter.CTkCanvas(
            master=self,
            bg=self.backgroundColor,
            height=self.gameHeight-self.textBoxSpace,
            width=self.gameWidth
        )

        self.label = customtkinter.CTkLabel(
            master=self,
            text="Scores:{}".format(self.score),
            font=('consolas', 40)
        )

        self.button = customtkinter.CTkButton(
            master=self,
            command=self.newGame,
            width=500,
            height=100,
            text="START",
            font=('consolas', 40)
        )

        self.colorchanger = customtkinter.CTkOptionMenu(
            master=self,
            values=["Czerwony","Zielony","Niebieski"],
            command=self.changeSnake
        )

        self.slider = customtkinter.CTkSlider(
            master=self,
            from_=240,
            to=30,
            command=self.changeSpeed
        )

        self.speedLabel = customtkinter.CTkLabel(
            master=self,
            text="Prędkość snejka",
            font=('consolas', 40)
        )

        self.label.pack()
        self.canvas.pack()
        self.button.pack(pady=10)
        self.colorchanger.pack(pady=10)
        self.speedLabel.pack(pady=10)
        self.slider.pack()

    def changeSnake(self,color):
        if color == "Czerwony":
            self.snakeColor = "#ff0000"
        elif color == "Zielony":
            self.snakeColor = "#00ff00"
        elif color == "Niebieski":
            self.snakeColor = "#0000ff"

    def changeSpeed(self,speed):
        print(self.speed)
        self.speed=int(speed)

    def nextTurn(self,snake,food):


        x,y = snake.coordinates[0]
        if self.direction == 'up':
            y -= self.spaceSize
        elif self.direction == 'down':
            y += self.spaceSize
        elif self.direction == 'left':
            x -= self.spaceSize
        elif self.direction == 'right':
            x += self.spaceSize

        snake.coordinates.insert(0, (x,y))
        square = self.canvas.create_rectangle(
                x,
                y,
                x + self.spaceSize,
                y + self.spaceSize,
                fill=self.snakeColor)
        snake.squares.insert(0,square)

        if x == food.coordinates[0] and y == food.coordinates[1]:
            self.score += 1
            
            self.label.configure(text="Scores:{}".format(self.score))
            self.canvas.delete("food")
            food = Food()
        else:
            del snake.coordinates[-1]
            self.canvas.delete(snake.squares[-1])
            del snake.squares[-1]

        if self.checkCollisions(snake):
            self.gameOver()
        else:
            self.after(self.speed, self.nextTurn, snake, food)
        self.lockChangeDirection == False
        
    def changeDirection(self,newDirection):
        if self.isGameOn == False or self.lockChangeDirection == True: 
            return

        self.lockChangeDirection == True
        if newDirection == 'left':
            if self.direction != 'right':
                self.direction = newDirection

        if newDirection == 'right':
            if self.direction != 'left':
                self.direction = newDirection
        
        if newDirection == 'up':
            if self.direction != 'down':
                self.direction = newDirection
        
        if newDirection == 'down':
            if self.direction != 'up':
                self.direction = newDirection

    def checkCollisions(self,snake):
        x,y = snake.coordinates[0]
        if x<0 or x>=self.gameWidth:
            return True

        elif y<0 or y>=self.gameHeight-self.textBoxSpace:
            return True

        for bodyParts in snake.coordinates[1:]:
            if x == bodyParts[0] and y == bodyParts[1]:
                return True

        return False

    def gameOver(self):
        self.isGameOn = False
        self.canvas.delete(customtkinter.ALL)
        self.canvas.create_text(self.canvas.winfo_width()/2,
        self.canvas.winfo_height()/2,
        font=('consolas', 70),
        text='KONIEC',
        fill='red',
        tag='gameover')

    def newGame(self):
        if self.isGameOn==True:
            return

        self.canvas.delete(customtkinter.ALL)
        self.score = 0
        self.label.configure(text="Scores:{}".format(self.score))
        self.direction = "right"
        snake=Snake()
        food=Food()
        self.isGameOn = True
        self.nextTurn(snake, food)

root = Root()

class Snake:
    def __init__(self):
        self.bodySize = root.bodyParts
        self.coordinates = []
        self.squares = []

        for i in range(0, root.bodyParts):
            self.coordinates.append([0,0])

        for x,y in self.coordinates:
            square = root.canvas.create_rectangle(
                x,
                y,
                x + root.spaceSize,
                y + root.spaceSize,
                fill=root.snakeColor, tag="snake")
            self.squares.append(square)

class Food:
    def __init__(self):
        x = random.randint(0,int((root.gameWidth/root.spaceSize)-1))*root.spaceSize
        y = (random.randint(0,int(((root.gameHeight-root.textBoxSpace*1.5)/root.spaceSize)-1))*root.spaceSize)

        self.coordinates = [x,y]
        root.canvas.create_oval(
            x,
            y,
            x+root.spaceSize,
            y+root.spaceSize,
            fill=root.foodColor,
            tag='food'
        )
        print(self.coordinates)

windowWidth = root.winfo_width()
windowHeight = root.winfo_height()
screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()

x = int((screenWidth/2) - (windowWidth/2))
y = int((screenHeight/2) - (windowHeight/2))

root.bind('<Left>', lambda evnet: root.changeDirection('left'))
root.bind('<Right>', lambda event: root.changeDirection('right'))
root.bind('<Up>', lambda event: root.changeDirection('up'))
root.bind('<Down>', lambda event: root.changeDirection('down'))

root.mainloop()
