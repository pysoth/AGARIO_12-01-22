class Ennemis(object):
    def __init__(self, name, Ennemis, colour, startLevel):
        self.name = name
        self.Ennemis = Ennemis
        self.colour = colour
        self.level = startLevel
        self.feed = 0
        self.size = 2 ** self.level
        if self.size > 64:
            self.size = 64
        self.speed = 3 * (2 ** self.level)
        self.location = (randint(1, SCREEN_SIZE[0] - 1), randint(1, SCREEN_SIZE[1] - 1))  # Spawns at a random location
        self.destination = self.location
        self.targetNo = 0
        self.stopDis = self.speed - 1

    def Déplacer(self):
        if self.location == self.destination or FEED[
            self.targetNo].location != self.destination:  # Choose a random piece of food to aim for
            self.targetNo = randint(0, len(FEED) - 1)
            target = FEED[self.targetNo]
            self.destination = target.location

        for item in ADERSARS:  # If there are lower leveled adversaries nearby, aim for them
            if item.level < self.level:
                disToItem = (self.location[0] - item.location[0], self.location[1] - self.Ennemis.location[1])
                if disToItem[0] < 80 and disToItem[0] > -80:
                    if disToItem[1] < 80 and disToItem[1] > -80:
                        self.destination = item.location

        if self.Ennemis.level < self.level:  # If the Ennemis has a lower level and is nearby, aim for them
            disToPlay = (self.location[0] - self.Ennemis.location[0], self.location[1] - self.Ennemis.location[1])
            if disToPlay[0] < 80 and disToPlay[0] > -80:
                if disToPlay[1] < 80 and disToPlay[1] > -80:
                    self.destination = self.Ennemis.location

        mousePosX, mousePosY = self.destination
        selfPosX, selfPosY = self.location

        disToDes = (mousePosX - selfPosX, mousePosY - selfPosY)  # Moving around
        if disToDes[0] > 0:
            disToDes = (disToDes[0] + self.stopDis, disToDes[1])
        if disToDes[1] > 0:
            disToDes = (disToDes[0], disToDes[1] + self.stopDis)
        disToAdd = (int(disToDes[0] / self.speed), int(disToDes[1] / self.speed))
        self.location = (self.location[0] + disToAdd[0], self.location[1] + disToAdd[1])

        playX, playY = self.Ennemis.location
        size = self.Ennemis.size
        if playX + size >= self.location[0] - self.size and playX - size <= self.location[
            0] + self.size:  # Feeding off Ennemis
            if playY + size >= self.location[1] - self.size and playY - size <= self.location[1] + self.size:
                if self.Ennemis.level > self.level:
                    self.feed -= 1
                    self.Ennemis.feed += 1
                if self.Ennemis.level < self.level:  # Ennemis feeding off entity
                    self.feed += 1
                    self.Ennemis.feed -= 1

        for item in ADERSARS:
            playX, playY = item.location
            size = item.size
            if playX + size >= self.location[0] - self.size and playX - size <= self.location[
                0] + self.size:  # Feeding off lesser entities
                if playY + size >= self.location[1] - self.size and playY - size <= self.location[1] + self.size:
                    if item.level < self.level:
                        self.feed += 1
                        item.feed -= 1

        if self.feed >= 10:
            self.levelUp()
        if self.feed <= -1:
            self.levelDown()

    def Mangé(self, screen):
        pygame.draw.circle(screen, (128, 128, 128), (self.location[0] - 1, self.location[1] - 1), self.size + 1)
        pygame.draw.circle(screen, self.colour, self.location, self.size)
        w, h = FONT.size(self.name)
        screen.blit(FONT.render(self.name, True, (0, 0, 0)), (self.location[0] - w / 2, self.location[1] - h / 2))

    def Augmenter(self):
        self.level += 1
        self.size = 2 ** self.level
        if self.size > 64:
            self.size = 64
        self.speed = int(self.speed * 2)
        self.feed = 0
        self.stopDis = self.speed - 1

