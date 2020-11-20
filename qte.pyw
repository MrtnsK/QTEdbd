import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
from pygame.locals import *
import random
import time
import sys

def wait():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and event.key == K_SPACE:
                return

def choose_mode():
    pygame.mixer.music.load("oui.wav")
    pygame.mixer.music.play()
    myfont = pygame.font.SysFont("Arial", 30)
    myfontsmall = pygame.font.SysFont("Arial", 10)
    fenetre.blit(myfontsmall.render("V0.1 by kemartin", 1, (0,0,255)), (1, 1))
    a = myfont.render("Press A to play with the basic configuration", 1, (255,255,255))
    b = myfont.render("Press B to play without audible signal", 1, (255,255,255))
    c = myfont.render("Press C to play with the doctor's madness (not available atm)", 1, (255,255,255))
    fenetre.blit(a, (100, 100))
    fenetre.blit(b, (100, 150))
    fenetre.blit(c, (100, 200))
    pygame.display.flip()
    loop = 1
    while loop:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_a:
                    return 1
                    print("fdp")
                if event.key == K_b:
                    return 2
                if event.key == K_c:
                    return 1 #mode 3 not done
                    # return 3

def qte_event(angle, fleche, fenetre, perso, position_perso, mode, rota): 
    pygame.mixer.music.load("bell.wav")
    t2w = random.randint(1, 10)
    # print("time before skill check : ", t2w, "s")
    time.sleep(t2w)
    if mode != 2:
        pygame.mixer.music.play()
    time.sleep(1)
    while angle >= -300 + rota:
        fenetre.fill((0,0,0))
        angle -= 0.3

        mx, my = pygame.mouse.get_pos()
        flechecpy = pygame.transform.rotate(fleche, angle)
        fenetre.blit(perso, (394 - int(perso.get_width()/2), 294 - int(perso.get_height()/2)))
        fenetre.blit(flechecpy, (394 - int(flechecpy.get_width()/2), 294 - int(flechecpy.get_height()/2)))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                loop = 0
            elif event.type == KEYDOWN:
                if event.key == K_SPACE:
                    if angle <= -7 + rota and angle >= -26 + rota:
                        fenetre.blit(myfont.render("Excellent", 1, (0,255,0)), (100, 50))
                        fenetre.blit(perso, (394 - int(perso.get_width()/2), 294 - int(perso.get_height()/2)))
                        fenetre.blit(flechecpy, (394 - int(flechecpy.get_width()/2), 294 - int(flechecpy.get_height()/2)))
                        pygame.display.update()
                        return
                    elif angle <= -26 + rota and angle >= -88 + rota:
                        fenetre.blit(myfont.render("Bon", 1, (255,255,255)), (100, 50))
                        fenetre.blit(perso, (394 - int(perso.get_width()/2), 294 - int(perso.get_height()/2)))
                        fenetre.blit(flechecpy, (394 - int(flechecpy.get_width()/2), 294 - int(flechecpy.get_height()/2)))
                        pygame.display.update()
                        return
                    else:
                        fenetre.blit(myfont.render("Raté", 1, (255,0,0)), (100, 50))
                        fenetre.blit(perso, (394 - int(perso.get_width()/2), 294 - int(perso.get_height()/2)))
                        fenetre.blit(flechecpy, (394 - int(flechecpy.get_width()/2), 294 - int(flechecpy.get_height()/2)))
                        pygame.display.update()
                        return


#Initialisation fenetre
pygame.init()
fenetre = pygame.display.set_mode((800, 600), DOUBLEBUF)
 
#Initialisation du mixer
pygame.mixer.init()
debug = False
#Affichage du fond
#fond = pygame.image.load("background.jpg").convert()
#fenetre.blit(fond, (0,0))


mode = choose_mode()
fenetre.fill((0,0,0))
# print("selected mode: ", mode)


#Affichage
perso = pygame.image.load("core2.png").convert_alpha()
position_perso = perso.get_rect()
perso = pygame.transform.scale(perso, (200, 200))
rota = random.randint(1, 90) * -1
perso = pygame.transform.rotate(perso, rota)

fleche = pygame.image.load("arrow4.png").convert_alpha()
fleche = pygame.transform.scale(fleche, (320, 86))

#Raffraichissement de la fenetre
pygame.display.flip()
 
#Initialisation du mixer et lancement de la musique
# pygame.mixer.music.load("bell.mp3")
# pygame.mixer.music.play()
loop = 1
angle = 60
myfont = pygame.font.SysFont("Arial", 30)
while loop:
    if debug:
        fenetre.fill((0,0,0))
        angle -= 0.3
        mx, my = pygame.mouse.get_pos()
        flechecpy = pygame.transform.rotate(fleche, angle)
        fenetre.blit(perso, (394 - int(perso.get_width()/2), 294 - int(perso.get_height()/2)))
        fenetre.blit(flechecpy, (394 - int(flechecpy.get_width()/2), 294 - int(flechecpy.get_height()/2)))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                loop = 0
            elif event.type == KEYDOWN:
                if event.key == K_d:
                    print(f'x : [{mx}] | y : [{my}]')
    else:
        fenetre.fill((0,0,0))
        qte_event(angle, fleche, fenetre, perso, position_perso, mode, rota)
        fenetre.blit(myfont.render("Press SPACE to restart", 1, (255,255,255)), (100, 100))
        pygame.display.update()
        wait()
        fenetre.fill((0,0,0))
        for event in pygame.event.get():
            if event.type == QUIT:
                loop = 0
            elif event.type == KEYDOWN:
                if event.key == K_d:
                    print(f'x : [{mx}] | y : [{my}]')
#Raffraichissement
    pygame.display.update()