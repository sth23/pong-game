"""
Final Project: Pong Game
Author: Sean
Credit: Tutorials
Assignment: Create an old-school Pong Game
"""

from ggame import App, RectangleAsset, CircleAsset, Sprite, LineStyle, Color
import math
import random

# Colors & lines
red = Color(0xff0000, 1.0)
orange = Color(0xffa500, 1.0)
yellow = Color(0xffff00, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
purple = Color(0x800080, 1.0)
black = Color(0x000000, 1.0)
white = Color(0xffffff, 1.0)
gray = Color(0x888888, 0.5)
noline = LineStyle(0, black)
whiteline = LineStyle(1, white)

class Wall(Sprite):
    def __init__(self, asset, position):
        super().__init__(asset, position)
        
class Ball(Sprite):
    circ = CircleAsset(5, noline, black)
    def __init__(self, position):
        super().__init__(Ball.circ, position)
        self.fxcenter = self.fycenter = 0.5
        self.speed = 2
        self.vx = self.speed
        self.vy = 0
        
    def wallBounce(self):
        self.vy = -self.vy
        
    def paddleBounce(self):
        self.vx = -self.vx
        
    def step(self):
        self.x += self.vx
        self.y += self.vy
        
class Paddle(Sprite):
    rect = RectangleAsset(20, 100, noline, black)
    def __init__(self, position):
        super().__init__(Paddle.rect, position)
        self.speed = 5
        self.vy = 0
        self.fxcenter = self.fycenter = 0.5
        
        PongGame.listenKeyEvent("keydown", "up arrow", self.goUpOn)
        PongGame.listenKeyEvent("keyup", "up arrow", self.goUpOff)
        PongGame.listenKeyEvent("keydown", "down arrow", self.goDownOn)
        PongGame.listenKeyEvent("keyup", "down arrow", self.goDownOff)
        
    def goUpOn(self, event):
        self.vy = -self.speed
        
    def goUpOff(self, event):
        self.vy = 0
        
    def goDownOn(self, event):
        self.vy = self.speed
        
    def goDownOff(self, event):
        self.vy = 0
        
    def step(self):
        self.y += self.vy
        
class PongGame(App):
    def __init__(self):
        super().__init__()
        
        # Create top & bottom wall
        self.wallthickness = 10
        self.rect = RectangleAsset(self.width, self.wallthickness, noline, black)
        self.topwall = Wall(self.rect, (0, 0))
        self.bottomwall = Wall(self.rect, (0, self.height - self.wallthickness))
        
        # Create Paddles
        self.player1 = Paddle((self.width - 40, self.height / 2))
        self.player2 = Paddle((40, self.height / 2))
        
        self.ball = Ball((self.width / 2, self.height / 2))
        
    def step(self):
        self.player1.step()
        self.player2.step()
        self.ball.step()
        
myapp = PongGame()
myapp.run()