import time
import random

class Player (object):
    def __init__(self,name,HP,PHY,ARM,SPD,ENG,SHD,encounter):
        self.name = name
        self.HP = HP
        self.PHY = PHY
        self.ARM = ARM
        self.SPD = SPD
        self.ENG = ENG
        self.SHD = SHD
        self.encounter = encounter
    def takePDamage(self,ePHY):
        daENGe = ePHY - self.ARM / 2
        if daENGe < 1:
            daENGe = 1
        self.HP = self.HP - daENGe
        print("current HP = ",self.HP)
    def takeEDamage(self,eENG):
        damage = eENG - self.SHD / 2
        if damage < 1:
            damage = 1
        self.HP = self.HP - damage
        print("current HP = ",self.HP)
    def showStats(self):
        print("Name = ",self.name)
        print("HP = ",self.HP)
        print("PHY = ",self.PHY)
        print("ARM = ",self.ARM)
        print("SPD = ",self.SPD)
        print("ENG = ",self.ENG)
        print("SHD = ",self.SHD)
        print("Number of encounters = ",self.encounter)
    def save(self):
        delimit = "~"
        File = open("GameLib.txt","w")
        File.write(self.name+delimit+str(self.HP)+delimit+str(self.PHY)+delimit+str(self.ARM)+delimit+str(self.SPD)+delimit+str(self.ENG)+delimit+str(self.SHD)+delimit+str(self.encounter))
        File.close



def main():
    Pclass = input("Please select a ship: >corvette >destroyer >cruiser >battle ship ")
    while(Pclass not in ("corvette","destroyer","cruiser","battle ship")):
        Pclass = input("-->")
    ShipName = input("Please name your ship: ")
    if ShipName == "Fire Fly":
        HP = 500
        PHY = 500
        ARM = 500
        SPD = 500
        ENG = 500
        SHD = 500
        encounter = 10
        hero = Player(ShipName,HP,PHY,ARM,SPD,ENG,SHD,encounter)
        hero.save()
    else:
        if Pclass == "corvette":
            HP = random.randint(10,15)
            PHY = random.randint(15,20)
            ARM = random.randint(5,10)
            SPD = random.randint(15,20)
            ENG = random.randint(10,15)
            SHD = random.randint(15,20)
            encounter = 0
            hero = Player(ShipName,HP,PHY,ARM,SPD,ENG,SHD,encounter)
        elif Pclass == "destroyer":
            HP = random.randint(15,20)
            PHY = random.randint(10,20)
            ARM = random.randint(10,15)
            SPD = random.randint(10,15)
            ENG = random.randint(10,20)
            SHD = random.randint(10,15)
            encounter = 0
            hero = Player(ShipName,HP,PHY,ARM,SPD,ENG,SHD,encounter)
        elif Pclass == "cruiser":
            HP = random.randint(20,25)
            PHY = random.randint(15,20)
            ARM = random.randint(15,20)
            SPD = random.randint(5,10)
            ENG = random.randint(15,20)
            SHD = random.randint(5,10)
            encounter = 0
            hero = Player(ShipNameHP,PHY,ARM,SPD,ENG,SHD,encounter)
        elif Pclass == "battle ship":
            HP = random.randint(25,30)
            PHY = random.randint(17,20)
            ARM = random.randint(15,20)
            SPD = random.randint(0,3)
            ENG = random.randint(15,20)
            SHD = random.randint(1,5)
            encounter = 0
            hero = Player(ShipName,HP,PHY,ARM,SPD,ENG,SHD,encounter)
    hero.showStats()
    hero.save()
    return hero
