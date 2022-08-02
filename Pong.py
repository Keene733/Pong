from tkinter import *
import time

points1 = 0
points2 = 0

app = Tk()
app.title("Pong")
app.resizable(0, 0)

canvas = Canvas(width=500, height=400)
canvas.config(bg="gray")
canvas.pack()
app.update()

canvas.create_line(250, 0, 250, 500, fill="white")

class LeftPaddle:
    def __init__(self, frame, color):

        self.frame = frame
        self.lads= canvas.create_rectangle(0, 200, 30, 250, fill=color)
        self.y = 0
        self.canvas_height = self.frame.winfo_height()
        self.canvas_width = self.frame.winfo_width()
        self.frame.bind_all("a", self.left)
        self.frame.bind_all("d", self.right)
        self.player_moves = self.frame.create_text(125, 75, text="press d to move right\na to move left")

    def draw(self):
        self.frame.move(self.lads, 0, self.y)
        pos = self.frame.coords(self.lads)
        #pos [1] and pos [3] is used to compare the y values of the left paddle
        if pos[1] <= 0:
            self.y = 0
        if pos[3] >= 400:
            self.y = 0

    def left(self, event):
        self.y = -5

    def right(self, event):
        self.y = 5


class RightPaddle:
    def __init__(self, frame, color):
        self.frame = frame
        self.rads = canvas.create_rectangle(470, 200, 500, 250, fill=color)
        self.canvas_height = self.frame.winfo_height()
        self.canvas_width = self.frame.winfo_width()
        self.y = 0
        self.frame.bind_all("<Left>", self.left)
        self.frame.bind_all("<Right>", self.right)
        self.player_moves = self.frame.create_text(375, 75, text="use arrow keys to move")

    def draw(self):
        self.frame.move(self.rads, 0, self.y)
        pos = self.frame.coords(self.rads)
        # pos [1] and pos [3] is used to compare the y values of the right paddle
        if pos[1] <= 0:
            self.y = 0
        if pos[3] >= 400:
            self.y = 0

    def left(self, event):
        self.y = 5

    def right(self, event):
        self.y = -5


class PingPongBall:
    def __init__(self, frame, color, paddle_red, paddle_blue):
        self.frame = frame
        self.paddle_red = paddle_red
        self.paddle_blue = paddle_blue
        self.ball = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.frame.move(self.ball, 230, 200)
        begin_at = [-3, -2, -1, 0, 1, 2, 3]

        self.x = begin_at[0]
        self.y = -begin_at[1]
        self.frame_height = self.frame.winfo_height()
        self.canvas_width = self.frame.winfo_width()

    def score(self, score_left,score_right):
        global points1
        global points2

        if score_left:
            a = self.frame.create_text(125, 40, text=points1, font=("Times", 20), fill="Red")
            canvas.itemconfig(a, fill="gray")
            points1 += 1
            a = self.frame.create_text(125, 40, text=points1, font=("Times", 20), fill="Red")

        if score_right:
            a = self.frame.create_text(375, 40, text=points2, font=("Times", 20), fill="Blue")
            canvas.itemconfig(a, fill="gray")
            points2 += 1
            a = self.frame.create_text(375, 40, text=points2, font=("Times", 20), fill="Blue")

    def draw(self):
        self.frame.move(self.ball, self.x, self.y)
        pos = self.frame.coords(self.ball)
        # pos [1] and [3] compare y, pos [0] and [2] compare x
        if pos[1] <= 0:
            self.y = 3
        if pos[3] >= self.frame_height:
            self.y = -3
        if pos[0] <= 0:
            self.x = 3
            self.score(score_left=True,score_right=False)
        if pos[2] >= self.canvas_width:
            self.x = -3
            self.score(score_right=True,score_left=False)
        if self.hit_red(pos):
            self.x = 3
        if self.hit_blue(pos):
            self.x = -3

    def hit_red(self, pos):
        paddle_pos = self.frame.coords(self.paddle_red.lads)
        if pos[1] >= paddle_pos[1] :
            if pos[1] <= paddle_pos[3]:
                if pos[0] >= paddle_pos[0] and pos[2] <= paddle_pos[2]:
                    return True
            return False

    def hit_blue(self, pos):
        paddle_pos = self.frame.coords(self.paddle_blue.rads)
        if pos[1] >= paddle_pos[1] :
            if pos[1] <= paddle_pos[3]:
                if pos[2] >= paddle_pos[0] :
                    if pos[2] <= paddle_pos[2]:
                        return True
            return False

left_paddle = LeftPaddle(canvas, "Red")
right_paddle = RightPaddle(canvas, "Blue")
ball =PingPongBall(canvas, "Yellow", left_paddle, right_paddle)

while TRUE:
    ball.draw()
    left_paddle.draw()
    right_paddle.draw()
    app.update()
    time.sleep(0.01)
app.mainloop()


