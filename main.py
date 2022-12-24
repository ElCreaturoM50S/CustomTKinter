import customtkinter
import random

class Root(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        
        self.resizable(0,0)
        self.title("snejk")
        
        self.score = 0
        self.direction = "right"

        self.gameWidth = 700
        self.gameHeight = 700
        self.speed = 180
        self.spaceSize = 50
        self.bodyParts = 2
        self.direction = "right"
        self.foodColor = "#ffff00"
        self.snakeColor = "#ff0000"
        self.backgroundColor = "#808080"

        self.geometry(str(self.gameWidth)+'x'+str(self.gameHeight))

        self.label = customtkinter.CTkLabel(
            self,
            text="Scores:{}".format(self.score),
            font=('consolas', 40)
        )

        self.canvas = customtkinter.CTkCanvas(
            self,
            bg=self.backgroundColor,
            height=self.gameHeight,
            width=self.gameWidth
        )
        self.canvas.pack()

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

            #label
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

    def changeDirection(self,newDirection):
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

        elif y<0 or y>=self.gameHeight:
            return True

        for bodyParts in snake.coordinates[1:]:
            if x == bodyParts[0] and y == bodyParts[1]:
                return True

        return False

    def gameOver(self):
        self.canvas.delete(customtkinter.ALL)
        self.canvas.create_text(self.canvas.winfo_width()/2,
        self.canvas.winfo_height()/2,
        font=('consolas', 70),
        text='KONIEC',
        fill='red',
        tag='gameover')

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
        print((root.gameWidth/root.spaceSize)-1)
        x = random.randint(0,(root.gameWidth/root.spaceSize)-1)*root.spaceSize
        y = random.randint(0,(root.gameHeight/root.spaceSize)-1)*root.spaceSize

        self.coordinates = [x,y]
        root.canvas.create_oval(
            x,
            y,
            x+root.spaceSize,
            y+root.spaceSize,
            fill=root.foodColor,
            tag='food'
        )


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

snake=Snake()
food=Food()

root.nextTurn(snake, food)

root.mainloop()
