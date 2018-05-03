import time
import random
import gameObjects
import EnemyCreatorV2
import CharCreator
import items

itemList = items.createItems()
def combat(enemy,player):
    print("")
    print("An",enemy.name," appears!")
    print("---------------------")
    print("player stats:")
    print("---------------------")
    player.showStats()
    time.sleep(1)
    print("")
    print("---------------------")
    print("enemy stats:")
    print("---------------------")
    enemy.getStats()
    if enemy.SPD > player.SPD:
        curTurn = "Enemy"
    elif player.SPD > enemy.SPD:
        curTurn = "Player"
    else:
        if random.randint(1,2) == 1:
            curTurn = "Player"
        else:
            curTurn = "Enemy"
    fled = False
    while player.HP > 0 and enemy.HP > 0 and not fled:
        if curTurn == "Player":
            print(">Physical    >Energy    >Flee    >Item")
            selection = ""
            while(selection not in ("Physical","Energy","Flee","Item")):
                selection = input("-->").title()
                if selection == "Physical":
                    print("you attack the",enemy.name,"with physical weapons")
                    time.sleep(1)
                    enemy.takePDamage(player.PHY)
                elif selection == "Energy":
                    print("you use energy weapons on the",enemy.name)
                    time.sleep(1)
                    enemy.takeEDamage(player.ENG)
                elif selection == "Item":
                    print("pick and item to use: ")
                    items.inventory()
                elif selection == "Flee":
                    if enemy.SPD != 1337:
                        roll = random.randint(1,100)
                        if player.SPD > enemy.SPD:
                            fleeChance = 90
                        else:
                            fleeChance = 50
                        if roll <= fleeChance:
                            print("-----------")
                            print("you Fled")
                            print("-----------")
                            fled = True
                            time.sleep(1)
                        else:
                            print("failed to flee")
                            time.sleep(1)
                    else:
                        print("failed to flee")
                        time.sleep(1)
                elif selection == "Item":
                    pass
                    #list of usable items
                    #use "while selection not in" to make sure input is an item
                    #activate item buff
                    #remove item from inventory
                curTurn = "Enemy"
        elif curTurn == "Enemy":
            atType = random.randint(1,100)
            if enemy.PHY >= enemy.ENG:
                if atType > 10:
                    print("The",enemy.name,"attacks with physical weapons!")
                    time.sleep(1)
                    player.takePDamage(enemy.PHY)
                else:
                    print("The",enemy.name,"uses energy weapons!")
                    time.sleep(1)
                    player.takeEDamage(enemy.ENG)
            elif enemy.PHY < enemy.ENG:
                if atType > 10:
                    print("The",enemy.name,"uses energy weapons!")
                    time.sleep(1)
                    player.takeEDamage(enemy.ENG)
                else:
                    print("The",enemy.name,"attacks with physical weapons!")
                    time.sleep(1)
                    player.takePDamage(enemy.PHY)
            else:
                print("An Error Occured...")
            curTurn = "Player"
    if player.HP <= 0:
        print("-----------------")
        print("you died")
        print("-----------------")
    elif fled == True:
        pass
    else:
        player.encounter += 1
        ranDrop = random.randint(0,5)
        pickedItem = itemList[ranDrop][enemy.LV]
        items.addItem(pickedItem)
        print("you got",pickedItem.name)

def main():
    enemy = EnemyCreatorV2.medEnemy(1)[0]
    player = CharCreator.main()
    combat(enemy,player)

main()
