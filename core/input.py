import pygame

class Input(object):
    def __init__(self):
        #has the user quit the application?
        self.quit = False

        # lists to store key states down, up: discrete event;
        # lasts for one iteration pressed: continuos event, between down and up events
        self.keyDownList = []
        self.keyPressedList = []
        self.keyUpList = []
    
    def update(self):
        # reset discrete key states
        self.keyDownList = []
        self.keyUpList = []

        # iterate over all user input events (such as keyboard or mouse) that occurred since the last time events were checked
        for event in pygame.event.get():
        # quit event occurs by clicking button to close window
            if event.type == pygame.QUIT:
                self.quit = True

            # check for keydown and keyup events;
            # get name of key from event and append to or remove from corresponding lists

            if event.type == pygame.KEYDOWN:
                keyName = pygame.key.name(event.key)
                self.keyDownList.append(keyName)
                self.keyPressedList.append(keyName)
            if event.type == pygame.KEYUP:
                keyName = pygame.key.name(event.key)
                self.keyPressedList.remove(keyName)
                self.keyUpList.append(keyName)
    

    # functions to check key states
    def isKeyDown(self, keyCode):
        return keyCode in self.keyDownList
    def isKeyPressed(self, keyCode):
        return keyCode in self.keyPressedList
    def isKeyUp(self, keyCode):
        return keyCode in self.keyUpList







    
