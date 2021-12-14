

class anglerFish:
    def __init__(self, reproTime=8):
        self.reproTimer = reproTime

    def isTimeToRepro(self):
        if self.reproTimer < 0:
            self.reproTimer = 6
            return True
        else:
            return False

    def getTimer(self):
        return self.reproTimer

    def reduceTimer(self):
        self.reproTimer -= 1