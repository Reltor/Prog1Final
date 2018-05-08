import time
import random
import gameObjects
import EnemyCreator
import CharCreator
import items

itemList = items.createItems()
def combat(boss,player):
    print("")
    print("The big bad",boss.name," appears!")
    print("---------------------")
    print("player stats:")
    print("---------------------")
    player.getStats()
    time.sleep(1)
    print("")
    print("---------------------")
    print("enemy stats:")
    print("---------------------")
    boss.getStats()
    if boss.SPD > player.SPD:
        curTurn = "Enemy"
    elif player.SPD > boss.SPD:
        curTurn = "Player"
    else:
        if random.randint(1,2) == 1:
            curTurn = "Player"
        else:
            curTurn = "Enemy"
    fled = False
    while player.HP > 0 and boss.HP > 0 and not fled:
        if curTurn == "Player":
            print(">Physical    >Energy    >Flee    >Item")
            selection = ""
            while(selection not in ("Physical","Energy","Flee","Item")):
                selection = input("-->").title()
                if selection == "Physical":
                    print("you attack the",enemy.name,"with physical weapons")
                    time.sleep(1)
                    boss.takePDamage(player.PHY)
                    curTurn = "Enemy"
                elif selection == "Energy":
                    print("you use energy weapons on the",enemy.name)
                    time.sleep(1)
                    boss.takeEDamage(player.ENG)
                    curTurn = "Enemy"
                elif selection == "Item":
                    print("pick and item to use: ")
                    player,curTurn = items.inventory(player)
                elif selection == "Flee":
                    print("You can not run from a trainer battle.")
                elif selection == "Item":
                    pass
                    #list of usable items
                    #use "while selection not in" to make sure input is an item
                    #activate item buff
                    #remove item from inventory
        elif curTurn == "Enemy":
            atType = random.randint(1,100)
            if boss.PHY >= boss.ENG:
                if atType > 10:
                    print("The big bad",boss.name,"fires upon you with physical weapons!")
                    time.sleep(1)
                    player.takePDamage(boss.PHY)
                else:
                    print("The big bad",boss.name,"fires energy weapons! Those are hot stuff!")
                    time.sleep(1)
                    player.takeEDamage(boss.ENG)
            elif boss.PHY < boss.ENG:
                if atType > 10:
                    print("The big bad",boss.name,"uses energy weapons! Those are hot stuff!")
                    time.sleep(1)
                    player.takeEDamage(boss.ENG)
                else:
                    print("The",boss.name,"fires upon you with physical weapons!")
                    time.sleep(1)
                    player.takePDamage(boss.PHY)
            else:
                print("An Error Occured...")
            curTurn = "Player"
    if player.HP <= 0:
        print("-----------------")
        print("you faught valiently in the final battle but alass, the big bad",boss.name,"was too much for you. \n Better luck next time!")
        print("-----------------")
        playerRes = "L"
    elif fled == True:
        print("wait, how did you? um... this isn't suposed to be possible...")
        time.sleep(1)
        print("well, guess we are here now.")
        time.sleep(1)
        print("maybe you should close this window.")
        time.sleep(10)
        print("why are you still here?")
        time.sleep(2)
        print("are you looking for an easter egg? because there isn't one, this is a serious error, you were never meant to get here.")
        time.sleep(10)
        print("you aren't going to close this are you?")
        time.sleep(1)
        print("fine, i'll do it myself.")
        player.HP = 0
        playerRes = "R"
        pass
    else:
        player.encounter()
        ranDrop = random.randint(0,5)
        level = enemy.getLV()
        pickedItem = itemList[ranDrop][level]
        items.addItem(pickedItem)
        print("you got",pickedItem.name)
        playerRes = "W"
    return player, playerRes

def main():
    enemy = EnemyCreator.medEnemy(1)[0]
    player = CharCreator.main()
    combat(enemy,player)

