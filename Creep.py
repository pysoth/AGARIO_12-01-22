class Creep(object):
    def __init__(self, Creep, value=1):
        self.value = value
        self.location = (randint(1, SCREEN_SIZE[0]-1), randint(1, SCREEN_SIZE[1]-1))    #Random spawn location
        self.Creep = Creep
        self.colour = COLOURS[randint(0, 5)]

    def Déplacer(self):
        playX, playY = self.Creep.location #Player feeding
        size = self.Creep.size
        if playX+size >= self.location[0]-self.value and playX-size <= self.location[0]+self.value:
            if playY+size >= self.location[1]-self.value and playY-size <= self.location[1]+self.value:
                self.value -=1
                self.Creep.feed += 1

        for adversary in ADERSARS:  #Other entities feeding
            if adversary.location[0]+adversary.size >= self.location[0]-self.value and adversary.location[0]-adversary.size <= self.location[0]+self.value:
                if adversary.location[1]+adversary.size >= self.location[1]-self.value and adversary.location[1]-adversary.size <= self.location[1]+self.value:
                    self.value -= 1
                    adversary.feed += 1

    def Mangé(self, screen):
        pygame.draw.circle(screen, (128, 128, 128), (self.location[0]-1, self.location[1]-1), self.value+1)
        pygame.draw.circle(screen, self.colour, self.location, self.value)