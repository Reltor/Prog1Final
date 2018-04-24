for c in range (NumOfEnemies):
    print("A wild",eList[c].name,"appears!")
    print("---------------------")
    print("hero stats:")
    print("---------------------")
    hero.showStats()
    print("---------------------")
    print("enemy stats:")
    print("---------------------")
    eList[c].getStats()
    if eList[c].SPD > hero.SPD:
        curTurn = "Enemy"
    elif hero.SPD > eList[c].SPD:
        curTurn = "Player"
    else:
        if random.randint(1,2) == 1:
            curTurn = "Player"
        else:
            curTurn = "Enemy"
    fled = False
    while hero.HP > 0 and eList[c].HP > 0 and not fled:
        if curTurn == "Player":
            print(">Physical    >Flee    >Energy    >Item")
            selection = ""
            while(selection not in ("Physical","Flee","Energy","Item")):
                selection = input("-->")
                if selection == "Physical":
                    print("you attack",eList[c].name)
                    eList[c].takePDamage(hero.PHY)
                elif selection == "Energy":
                    print("you use energy weapons on",eList[c].name)
                    eList[c].takeEDamage(hero.ENG)
                elif selection == "Flee":
                    roll = random.randint(1,100)
                    if hero.SPD > eList[c].SPD:
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
                        print("faild to flee")
                        time.sleep(1)
                elif selection == "Item":
                    pass
                    #list of usable items
                    #use "while selection not in" to make sure input is an item
                    #activate item buff
                    #remove item from inventory
                curTurn = "Enemy"
        elif curTurn == "Enemy":
            if eList[c].PHY >= eList[c].ENG:
                print("The",eList[c].name,"attacks!")
                hero.takePDamage(eList[c].PHY)
            elif eList[c].PHY < eList[c].ENG:
                print("The",eList[c].name,"uses energy weapons!")
                hero.takeEDamage(eList[c].ENG)
            else:
                print("An Error Occured...")
            curTurn = "Player"
    hero.encounter += 1
    if hero.HP <= 0:
        print("-----------------")
        print("you died")
        print("-----------------")
        break
