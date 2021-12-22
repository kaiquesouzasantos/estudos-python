from tkinter import * 
import random 
import time

WIDTH = 800
HEIGHT = 600

janela = Tk()
canvas = Canvas(janela, width=WIDTH, height=HEIGHT)
janela.title('Animation')
canvas.pack()

class Ball:
    def __init__(self, color, size):
        self.shape = canvas.create_oval(10, 10, size, size, fill=color)
        self.xspeed = random.randrange(-10,10)
        self.yspeed = random.randrange(-10,10)

    def move(self):
        canvas.move(self.shape, self.xspeed, self.yspeed)
        pos = canvas.coords(self.shape)
        if pos[3] >= HEIGHT or pos[1] <= 0:
            self.yspeed = -self.yspeed
        if pos[2] >= WIDTH or pos[0] <= 0:
            self.xspeed = -self.xspeed

colors = ['red', 'green', 'blue', 'orange', 'yellow', 'cyan', 'magenta']
balls = []

for i in range(100):
    balls.append(Ball(random.choice(colors),random.randrange(50, 100)))

while True:
    for ball in balls:
        ball.move()
    janela.update()
    time.sleep(0.01)

janela.mainloop()