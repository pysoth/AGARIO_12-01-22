import pygame
from random import randint
from pygame.locals import *
import time



def main(name, colour):
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)
    pygame.display.set_caption("Py-gario")

    clock = pygame.time.Clock()

    Avatar = Avatar(name, colour)  # Creates the player

    populate(Avatar)  # Creates food

    for item in ['Joueur1', 'Joueur2', 'Joueur3']:  # Creates adversaries
        adversar = Ennemis(item, player, COLOURS[randint(0, len(COLOURS) - 1)], randint(1, 3))
        ADERSARS.append(adversar)



    while Avatar.level > 0:  # Mainloop
        clock.tick()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
        if len(ADERSARS) == 0:

            break

        screen.fill((255, 255, 255))

        populate(Avatar)

        Avatar.update()
        for item in ADERSARS:  # Updates the enemies
            item.update()
            if item.level <= 0:
                ADERSARS.remove(item)
            else:
                item.render(screen)
        for item in FEED:  # Updates the food
            item.update()
            if item.value <= 0:
                FEED.remove(item)
            else:
                item.render(screen)
        Avatar.render(screen)

        scoreBoard(screen, Avatar)  # Dispalays scores

        pygame.display.update()

    endFont = pygame.font.Font(None, 36)
    w, h = endFont.size(text)
    screen.blit(endFont.render(text, True, (0, 0, 0)), ((SCREEN_SIZE[0] / 2) - w / 2, (SCREEN_SIZE[1] / 2) - h / 2))
    pygame.display.update()
    time.sleep(2)

    pygame.quit()


def scoreBoard(screen, Avatar): #Displays scores
    y = 0
    scores = []
    for item in ADERSARS:
        scores.append((item.feed+item.level*10, item.name))
    scores.append((Avatar.feed+Avatar.level*10, Avatar.name))
    scores.sort()
    scores.reverse()
    for score in scores:
        w, h = FONT.size("%s : %i" % (score[1], score[0]))
        y += 2+h/2
        screen.blit(FONT.render("%s : %i" % (score[1], score[0]), True, (0, 0, 0)), (SCREEN_SIZE[0]-w, y))


def populate(Avatar):   #Ensures that 10 feed is always on screen
    while len(FEED) < 10:
        food = Feed(Avatar, randint(1, 3))
        FEED.append(food)



if __name__ == "__main__":
    from Tkinter import *
    from tkColorChooser import askcolor


    def askColour():
        triple = None
        while triple == None:
            triple, hexstr = askcolor()
        return triple


    name = ''
    while name == '':
        name = raw_input("Name: ")
    colour = askColour()
    main(name, colour)
    quit