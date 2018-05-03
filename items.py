#create item objects that will benefit the player so they are ready for the final boss
#give the items methods that would allow them to modify the players stats
    #pass the player as a parameter to the item method
    #have the method check what stat the item changes
    #modify the stat
    #return the player object to the game
#to use an item, the user inputs what catagory they want to select from
#the program prints the names of all the available item from the selected catagory
#the item is then applied

##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
##Items for final project:
##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
##
##plasma shield: permanent 2 point boost to shields
##deflector shield: permanent 3 point boost to shileds
##kojima field: permanent 5 point boost to shields
##spiral shield: permanent 10 point boost to shields
##
##reinforced armor: permanent 2 point boost to armor
##titanium plating: permanent 3 point boost to armor
##adamantium lining: permanent 5 point boost to armor
##star metal coating: permanent 10 point boost to armor
##
##enhanced FTL drive: permanent 2 point boost to speed
##K-F drive: permanent 3 point boost to speed
##warp drive: permanent 5 point boost to speed
##quantum drive: permanent 10 point boost to speed
##
##enhanced lasers: permanent 2 point boost to energy
##PPC: permanent 3 point boost to energy
##turbo cannon: permanent 5 point boost to energy
##partical lance: permanent 10 point boost to energy
##
##high velocity rounds: permanent 2 point boost to physical
##rail guns: permanent 3 point boost to physical
##anti matter rounds: permament 5 point boost to physical
##FTL rounds: permanent 10 point boost to physical
##
##reinforced hull: permanent 2 point boost to HP
##endo-steel: permanent 3 point boost to HP
##impact absorbers: permanent 5 point boost to HP
##the power of friendship: permanent 10 point boost to HP

#--------------------
#Item drops
#--------------------

#each time an enemy is defeated, they will drop a random item from the items list
#the rarity of the item dropped will depend on the dificaulty of the enemy that dropped it
#using the item "map" the enemy dificaulty picks the row (rarity) of the item dropped, and a random number generator picks the column (type) of item dropped
#the item selected for the drop is then passed to the player's inventory




#The following is needed in the main program in order to generate and use items.


#these 2 lines should go before any items are referenced
import random
import pickle
'''
import items
itemList = items.createItems()


def useItem(player):
    print("0)HP  1)PHY  2)ARM  3)SPD  4)ENG  5)SHD")
    catagory = int(input("please select the number of the buff catagory you want: "))
    i = 0
    for x in itemList[catagory]:
        print(i,")",x.name)
        i += 1
    number = int(input("please select the number of the item you want to use: "))
    itemList[catagory][number].boostStat(player)
    player.showStats()
    return player
'''


class Perm(object):
    def __init__(self,name,boost,stat):
        self.name = name
        self.boost = boost
        self.stat = stat
    def boostStat(self,Player):
        if self.stat == "HP":
            Player.HP += self.boost
            return Player
        elif self.stat == "PHY":
            Player.PHY += self.boost
            return Player
        elif self.stat == "ARM":
            Player.ARM += self.boost
            return Player
        elif self.stat == "SPD":
            Player.SPD += self.boost
            return Player
        elif self.stat == "ENG":
            Player.ENG += self.boost
            return Player
        elif self.stat == "SHD":
            Player.SHD += self.boost
            return Player

        
'''
class Temp(Perm):
    def __init__(self,name,boost,stat,time):
        super().__init__(name,boost,stat)
        self.time = time
'''


def createItems():
    iList = []
    commonList = []
    unCommonList = []
    rareList = []
    superRareList = []
    hpList = []
    phyList = []
    armList = []
    spdList = []
    engList = []
    shdList = []
    #creats HP items list
    reinforced = Perm("reinforced hull",2,"HP")
    hpList.append(reinforced)
    endo = Perm("endo-steel",3,"HP")
    hpList.append(endo)
    impact = Perm("impact absorbers",5,"HP")
    hpList.append(impact)
    friendship = Perm("the power of friendship",10,"HP")
    hpList.append(friendship)
    #creats PHY items list
    hvr = Perm("high velocity rounds",2,"PHY")
    phyList.append(hvr)
    rail = Perm("rail guns",3,"PHY")
    phyList.append(rail)
    amr = Perm("anti matter rounds",5,"PHY")
    phyList.append(amr)
    ftlr = Perm("FTL rounds",10,"PHY")
    phyList.append(ftlr)
    #creats ARM items list
    reArmor = Perm("reinforced armor",2,"ARM")
    armList.append(reArmor)
    titanium = Perm("titanium plating",3,"ARM")
    armList.append(titanium)
    adamantium = Perm("adamantium lining",5,"ARM")
    armList.append(adamantium)
    star = Perm("star metal coating",10,"ARM")
    armList.append(star)
    #create SPD items list
    ftld = Perm("enhanced FTL drive",2,"SPD")
    spdList.append(ftld)
    kf = Perm("K-F drive",3,"SPD")
    spdList.append(kf)
    warp = Perm("warp drive",5,"SPD")
    spdList.append(warp)
    quantum = Perm("quantum drive",10,"SPD")
    spdList.append(quantum)
    #create ENG items list
    eLasers = Perm("enhanced lasers",2,"ENG")
    engList.append(eLasers)
    PPC = Perm("PPC",3,"ENG")
    engList.append(PPC)
    turbo = Perm("turbo cannon",5,"ENG")
    engList.append(turbo)
    partical = Perm("partical lance",10,"ENG")
    engList.append(partical)
    #creats SHD items list
    plasma = Perm("plasma shield",2,"SHD")
    shdList.append(plasma)
    deflect = Perm("deflector shield",3,"SHD")
    shdList.append(deflect)
    kojima = Perm("kojima field",5,"SHD")
    shdList.append(kojima)
    spiral = Perm("spiral shield",10,"SHD")
    shdList.append(spiral)
    #append all lists into an overall item list
    iList.append(hpList)
    iList.append(phyList)
    iList.append(armList)
    iList.append(spdList)
    iList.append(engList)
    iList.append(shdList)
    return iList

#--------------------
#Random item drops
#--------------------


#each time an enemy is defeated, they will drop a random item from the items list
#the rarity of the item dropped will depend on the dificaulty of the enemy that dropped it
#using the item "map" the enemy dificaulty picks the row (rarity) of the item dropped, and a random number generator picks the column (type) of item dropped
#the item selected for the drop is then passed to the player's inventory
def inventory():
    inventory = []
    pickle_in = open("inventory.inv","rb")
    try:
        inventory = pickle.load(pickle_in)
    except EOFError:
        inventory = []
    inventory = pickle.load(pickle_in)
    pickle_in.close()
    for x in inventory:
        print(x.name)

def addItem(drop):
    inventory = []
    pickle_in = open("inventory.inv","rb")
    try:
        inventory = pickle.load(pickle_in)
    except EOFError:
        inventory = []
    pickle_in.close()
    inventory.append(drop)
    pickle_out = open("inventory.inv","wb")
    pickle.dump(inventory,pickle_out)
    pickle_out.close




def test():
    itemList = createItems()
    ranDrop = random.randint(0,5)
    pickedItem = itemList[ranDrop][0]
    print(pickedItem.name)
        
