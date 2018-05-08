import gameObjects, time
from os import system
def main(anomaly,player):
    system("cls")
    anomaly.showFlavorText()
    anomaly.applyEffect(player)
    time.sleep(2)
    system("cls")
    player.getStats()
    player.encounter()
    return player
