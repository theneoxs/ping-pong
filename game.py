# -- coding: utf-8 --
from __future__ import unicode_literals
import pygame
import re
from random import randint
from pygame.locals import *
from tkinter import *


class App(Frame):
    def __init__(self, master):
        super(App, self).__init__(master)
        self.grid()
        self.create()
        self.qwe = 0
        self.cont1 = 0
        self.cont2 = 0
        
        
    def create(self):
        self.inwidth = Label(self, text = "Введите ширину экрана:")
        self.inheight = Label(self, text = "Введите высоту экрана:")
        self.inwidth.grid(row = 0, column = 0, columnspan = 2, sticky = W)
        self.inheight.grid(row = 1, column = 0, columnspan = 2, sticky = W)
        self.ent1 = Entry(self)
        self.ent2 = Entry(self)
        self.ent1.grid(row = 0, column = 2, sticky = W)
        self.ent2.grid(row = 1, column = 2, sticky = W)
        self.ent1.insert(0, "0")
        self.ent2.insert(0, "0")
        self.but = Button(self, text = "Начать игру!", command = self.reveal)
        self.but.grid(row = 2, column = 0, sticky = W)
        self.but.bind('<Return>', self.change)
        
    def change(self, event):
        self.reveal()
        
    def reveal(self):
        self.cont1 = self.ent1.get()
        self.cont2 = self.ent2.get()
        global width
        width = 800
        if int(self.cont1) < 400:
            width = 400
        else:
            width = int(self.cont1)
        
        global height
        height = 400
        if int(self.cont2) < 200:
            height = 200
        else:
            height = int(self.cont2)  
            
        wind.destroy()
        
        

class Ball():
    def __init__(self, x, y):
        self.us = 0
        self.x = x
        self.y = y
        self.r = 6
        self.dx = width *5//800 - 3
        self.dy = 5
        self.color = (255, 255, 255)
    
    def move(self):
        self.x += self.dx
        self.y += self.dy
        pygame.draw.circle(screen,self.color,(self.x,self.y),self.r)
    
    def otskok_Y(self):
        self.dy = -self.dy
        if self.dy < 0:
            self.dy = -randint(1, 10)
        else:
            self.dy = randint(1, 10)
        if self.y > height + 20:
            self.y = height-self.r - 1
        if self.y < -20:
            self.y = self.r + 1
    def otskok_X(self):
        self.dx = -self.dx
        if self.us <= width * 4 // 800 + 1:
            self.us += 1
            if self.dx < 0:
                self.dx -= self.us
            else:
                self.dx += self.us
                
class Rock():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.x1 = 10
        self.y1 = height * 70 // 600
        self.colour = (255,255,255)
        self.dy = height * 15 // 600 + 5
    
    def move_UP(self):
        self.y -= self.dy
        if self.y < 0:
            self.y = 0
    
    def move_DOWN(self):
        self.y += self.dy
        if self.y > height-self.y1:
            self.y = height-self.y1       
    
    def scre(self):
        pygame.draw.rect(screen, self.colour, (self.x, self.y, self.x1, self.y1))
        
    
width = 800
height = 600

wind = Tk()
wind.title("Ping-pong: Базовые настройки")
wind.geometry("300x100")

app = App(wind)

app.mainloop()
        
pygame.init()

ball = Ball(width//2, height//2)
rock1 = Rock(20, 0)
rock1.y = height//2-rock1.y1//2
rock2 = Rock(width-20, 0)
rock2.y = height//2-rock2.y1//2
width1 = width
height1 = height
width = 800
height = 600

screen = pygame.display.set_mode((width, height))
screen2 = pygame.display.set_caption("Ping-Pong")
clock = pygame.time.Clock()
k = 0
l = 0
press = randint(1, 2)
ping = 0

ball.dx = 0
ball.dy = 0

jzsdft = pygame.font.SysFont('пикселипростоregular', 50)
font = pygame.font.SysFont('пикселипростоregular', 100)
font2 = pygame.font.SysFont('пикселипростоregular', 40)

#menu_song = '1.mp3'
#song = '2.mp3'
#pygame.mixer.music.load(menu_song)
#pygame.mixer.music.play()

pro = True
pro1 = True 
while pro:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pro1 = False
            pygame.quit()
            sys.exit()
    
    pressed_key = pygame.key.get_pressed()
    if pressed_key[K_SPACE]:
        pro = False
    
    text = font.render("Ping - Pong", True, (255, 255, 255))
    text2 = font2.render("Press Space to start", True, (255, 255, 255))
    
    screen.blit(text, [width * 80 // 300, height * 100 // 300])
    screen.blit(text2, [width * 150 // 450, height * 400 // 600])
            
    pygame.display.flip()
    clock.tick(30)    
    
#pygame.mixer.music.stop()

width = width1
height = height1
screen = pygame.display.set_mode((width, height))

#pygame.mixer.music.load(song)
#pygame.mixer.music.play()
  
while pro1:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pro1 = False
            
    pressed_key = pygame.key.get_pressed()
    if pressed_key[K_SPACE]:
        if press == 1:
            press = 0
            ping = 1
            ball.us = 0
            ball.dx = -10
            ball.dy = randint(-10, 10)
            
        if press == 2:
            press = 0
            ping = 1
            ball.us = 0
            ball.dx = 10
            ball.dy = randint(-10, 10)
    if pressed_key[K_w]:
        rock1.move_UP()
    if pressed_key[K_s]:
        rock1.move_DOWN()
    if pressed_key[K_UP]:
        rock2.move_UP()
    if pressed_key[K_DOWN]:
        rock2.move_DOWN()
    
    if ball.x - rock1.x1 - ball.r < rock1.x + 10 and ball.y > rock1.y  and ball.y < rock1.y + rock1.y1 and press == 0 or ball.x + ball.r > rock2.x - 10 and ball.y >rock2.y and ball.y < rock2.y + rock2.y1 and press == 0:
        ball.otskok_X()
        if ball.dy < 0:
            ball.dy = -randint(1, 10)
        else:
            ball.dy = randint(1, 10)        
    elif ball.x < ball.r + rock1.x + rock1.x1 - 9:
        press = 1
        ball.dx = 0
        ball.dy = 0
        ball.x = rock1.x + rock1.x1 + ball.r
        ball.y = rock1.y + 0.5*rock1.y1
        l += 1
    elif ball.x > width - ball.r - rock2.x1 + 3:
        press = 2
        ball.dx = 0
        ball.dy = 0
        ball.x = rock2.x - ball.r
        ball.y = rock2.y + 0.5*rock2.y1
        k += 1
        
    if ball.y < ball.r:
        ball.y = ball.r + 1
        ball.otskok_Y()
    elif ball.y > height - ball.r:
        ball.y = height -ball.r - 1
        ball.otskok_Y()        
        
    if press == 1:
        if ping == 1:
            ball.y = rock1.y + rock1.y1//2
    elif press == 2:
        if ping == 1:
            ball.y = rock2.y + rock2.y1//2   
        
    text = jzsdft.render(str(k), False, (255, 255, 255))
    text2 = jzsdft.render(str(l), False, (255, 255, 255))
    text3 = jzsdft.render(':', False, (255, 255, 255))
    
    ball.move()
    rock1.scre()
    rock2.scre()
    screen.blit(text3, [width/2, 10])
    if k < 10:
        screen.blit(text, [width/2-70, 10])
    elif k < 100:
        screen.blit(text, [width/2-90, 10])
    elif k < 1000:
        screen.blit(text, [width/2-110, 10])
    else:
        screen.blit(text, [width/2-110, 10])       
    if l < 10:
        screen.blit(text2, [width/2+50, 10])
    else:
        screen.blit(text2, [width/2+30, 10])
    
    pygame.display.flip()
    clock.tick(60)
    
      
#pygame.mixer.music.stop()
pygame.quit()
    
