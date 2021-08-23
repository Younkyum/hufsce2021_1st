import random

def random_dice():
    rad = random.randrange(1,7)
    return rad

class City:
    def __init__(self, value):
        self.owner = "empty"
        self.value = 300
        self.num = value
    def own(self, player):
        if self.owner == 0:
            self.owner = player
            return self.owner
        else:
            return self.owner
    def value(self):
        return self.value

class player:
    def __init__(self):
        self.playernum = 0
        self.pro = 5000
        self.position = 0
    def buy(self, cityprice):
        self.pro = self.pro - cityprice
        return self.pro
    def passp(self, passprice):
        self.pro = self.pro - passprice
        return self.pro

Start = City(0)
Seoul = City(1)
Tokyo = City(2)
Sydney = City(3)
LA = City(4)
Cairo = City(5)
Phucket = City(6)
New_delhi = City(7)
Hanoi = City(8)
Paris = City(9)
citylist = [Start.num, Seoul.num, Tokyo.num, Sydney.num, LA.num, Cairo.num, Phucket.num, New_delhi.num, Hanoi.num, Paris.num]


player_1 = player()
player_1.playernum = 1
player_2 = player()
player_2.playernum = 2
