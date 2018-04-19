import time
import random

class Enemy (object):
    def __init__(self,HP,PHY,ARM,SPD,ENG,SHD):
        self.HP = HP
        self.PHY = PHY
        self.ARM = ARM
        self.SPD = SPD
        self.ENG = ENG
        self.SHD = SHD
    def takePDamage(self,ePHY):
        damage = ePHY - self.ARM / 2
        if damage < 1:
            damage = 1
        self.HP = self.HP - damage
        print("enemy health = ",self.HP)
    def takeEDamage(self,eENG):
        damage = eENG - self.SHD / 2
        if damage < 1:
            damage = 1
        self.HP = self.HP - damage
        print("enemy health = ",self.HP)
    def getStats(self):
        print("Name = ",self.name)
        print("HP = ",self.HP)
        print("PHY = ",self.PHY)
        print("ARM = ",self.ARM)
        print("SPD = ",self.SPD)
        print("ENG = ",self.ENG)
        print("SHD = ",self.SHD)
    def getName(self):
        print(self.name)

def weakEnemy(NumOfEnemies):
    WList = []
    for a in range (NumOfEnemies):
        HP = random.randint(8,13)
        PHY = random.randint(13,18)
        ARM = random.randint(3,8)
        SPD = random.randint(13,18)
        ENG = random.randint(8,13)
        SHD = random.randint(13,18)
        TempEnemy = Enemy(HP,PHY,ARM,SPD,ENG,SHD)
        WList.append(TempEnemy)
    return WList

def medEnemy(NumOfEnemies):
    MList = []
    for b in range (NumOfEnemies):
        HP = random.randint(13,18)
        PHY = random.randint(8,18)
        ARM = random.randint(8,13)
        SPD = random.randint(8,13)
        ENG = random.randint(8,18)
        SHD = random.randint(8,13)
        TempEnemy = Enemy(HP,PHY,ARM,SPD,ENG,SHD)
        MList.append(TempEnemy)
    return MList

def hardEnemy(NumOfEnemies):
    HList = []
    for c in range (NumOfEnemies):
        HP = random.randint(18,23)
        PHY = random.randint(13,18)
        ARM = random.randint(13,18)
        SPD = random.randint(3,8)
        ENG = random.randint(13,18)
        SHD = random.randint(3,8)
        TempEnemy = Enemy(HP,PHY,ARM,SPD,ENG,SHD)
        HList.append(TempEnemy)
    return HList

def shEnemy(NumOfEnemies):
    SHList = []
    for d in range (NumOfEnemies):
        HP = random.randint(23,28)
        PHY = random.randint(15,18)
        ARM = random.randint(13,18)
        SPD = random.randint(1,1)
        ENG = random.randint(13,18)
        SHD = random.randint(1,3)
        TempEnemy = Enemy(HP,PHY,ARM,SPD,ENG,SHD)
        SHList.append(TempEnemy)
    return SHList

