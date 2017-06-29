import pygame
import socket
import random
import sys
from math import sin, cos

name = input('Wot ur name plz?\n')

pygame.init()
clock = pygame.time.Clock()

dwidth = 320
dheight = 200

display = pygame.display.set_mode((dwidth, dheight))

black = (0 ,0 ,0)
white = (255, 255, 255)
red = (255, 0, 100)
pink = (220, 0, 220)
green = (0, 255, 150)
blue = (0, 150, 255)


'''random start points of p1 and p2'''
rand = random.randint
p1 = {'x': rand(1,dwidth),
      'y': rand(1,dheight),
      'h': 0.0,
      's': 5,
      'l': 40}

p2 = {'x': rand(1,dwidth),
      'y': rand(1,dheight),
      'h': 0.0,
      's': 5,
      'l': 40}

'''set up network shit n that'''
host = '127.0.0.1'
port = random.randint(5001,6000)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))

server = ('127.0.0.1', 5000)

while True:

    '''NETWORK COMMUNICATIONZ HAPPEN HERE'''
    playerpos = (name, p1)
    playerpos = str(playerpos).encode()
    s.sendto(playerpos, server) #send your coords etc
    data, addr = s.recvfrom(1024)
    playerpos = eval(data.decode())
    if playerpos[0] != name:
        p2 = playerpos[1]

        

    display.fill(black)

    '''boundary box'''
    pygame.draw.rect(display, red, (0, 0, dwidth, dheight), 10)

    '''p1'''
    pygame.draw.rect(display, blue,
                     (p1['x']-10, p1['y'] -10, 20, 20), 0)
    pygame.draw.line(display, blue, (p1['x'], p1['y']),
                     (cos(p1['h'])*p1['l'] + p1['x'], sin(p1['h'])*p1['l'] + p1['y']), 10)

    '''p2'''
    pygame.draw.rect(display, red,
                     (p2['x']-10, p2['y'] -10, 20, 20), 0)
    pygame.draw.line(display, red, (p2['x'], p2['y']),
                     (cos(p2['h'])*p2['l'] + p2['x'], sin(p2['h'])*p2['l'] + p2['y']), 10)

    '''keyz'''
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        p1['x'] += cos(p1['h']) * p1['s']
        p1['y'] += sin(p1['h']) * p1['s']
        
    elif keys[pygame.K_DOWN]:
        p1['x'] -= cos(p1['h'])
        p1['y'] -= sin(p1['h'])
        
    if keys[pygame.K_LEFT]:
        p1['h'] -= 0.1

    elif keys[pygame.K_RIGHT]:
        p1['h'] += 0.1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
                quit()


    pygame.display.update()
    clock.tick(60)

s.close()
pygame.quit()
sys.exit()
