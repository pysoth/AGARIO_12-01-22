class Avatar(object):
    def __init__(self, name, colour):
        self.name = name
        self.colour = colour
        self.level = 1
        self.feed = 0
        self.size = 2
        self.speed = 6
        self.location = (SCREEN_SIZE[0]/2, SCREEN_SIZE[1]/2)
        self.destination = self.location
        self.stopDis = 5    #Stopping distance

    def Déplacer(self):
        mousePosX, mousePosY = pygame.mouse.get_pos()   #Finds most recent mouse position on window
        self.destination = (mousePosX, mousePosY)       #Sets destination
        selfPosX, selfPosY = self.location

        disToDes = (mousePosX-selfPosX, mousePosY-selfPosY) #Works out the distance to the mouse
        if disToDes[0] > 0:
            disToDes = (disToDes[0]+self.stopDis, disToDes[1])  #If the distance is less than 0, add the stopping distance
        if disToDes[1] > 0:
            disToDes = (disToDes[0], disToDes[1]+self.stopDis)
        disToAdd = (int(disToDes[0]/self.speed),int(disToDes[1]/self.speed))    #Add distance/speed to current location to get a new location
        self.location = (self.location[0]+disToAdd[0], self.location[1]+disToAdd[1])

        if self.feed >= 10: #Leveling Up
            self.levelUp()

        if self.feed <= -1: #Leveling Down
            self.levelDown()

    def Mangé(self, screen):
        pygame.draw.circle(screen, (128, 128, 128), (self.location[0]-1, self.location[1]-1), self.size+1)  #Draw shadow
        pygame.draw.circle(screen, self.colour, self.location, self.size)   #Draw circle
        w, h = FONT.size(self.name)
        my_font = FONT.render(self.name, True, (0, 0, 0))
        screen.blit(my_font, (self.location[0]-w/2, self.location[1]-h/2))  #Render the name

    def Augmenter(self):
        self.level += 1
        self.size = 2**self.level
        if self.size > 64:
            self.size = 64
        self.speed = int(self.speed*2)  #* slows down the entity (increases amount of sections distance divided by)
        if self.speed > 192:
            self.speed = 192
        self.feed = 0
        self.stopDis = self.speed-1

