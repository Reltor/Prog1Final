
#make it so if you haven't fought enough enemies, you are moved away from final boss.

#cheatCODE - PlayerName - Firefly (sets moves to max, all stats as high as possible, enemy counter high enough for final boss, displays coordinate of final boss)

#################################
######## Enemy and Player #######
#################################

class Entity(object):
    def __init__(self):
        pass
    #attributes from Entity Class----
            #attack
            #energy attack
            #armor
            #shields
            #name
            #speed
            #ascii art
            #location
    #methods
        #takePDamage() - taking normal attack damage
        #takeEDamage() - taking energy attack damage
        #showStats() - Summary of statistics relevant to the player
        #__str__() - Prints everything including background data - for debugging
        #save - use Pickle module.
    pass

class Enemy(Entity):
    def __init__(self):
        super().__init__()
        pass
        #attributes from Entity Class----
            #attack
            #energy attack
            #armor
            #shields
            #name
            #speed
            #ascii art
            #location
        #own attributes
            #dropChances
            #isBoss (y/n)
            #enemyClass (pick from a list)
        #methods from Entity
            #takeEDamage()
            #takePDamage()
            #save
        #overwritten Methods
            #__str__
            #showStats()
            
        
class Player(Entity):
    def __init__(self):
        super().__init(self)
            #attributes----
                #from Entity class
                    #attack (Corv - High, Destroyer - Medium, Cruiser - High, Battleship - High)
                    #energy attack (Corv - Medium, Destroyer - High, Cruiser - Mid, Battleship - Mid)
                    #armor (Corv - Super Low, Destroyer - Low, Cruiser - Mid, Battleship - Very High)
                    #shields (Corv - Medium, Destroyer - Medium, Cruiser - High, Battleship - High)
                    #name (Player Input)
                    #speed (Corv - Super High, Destroyer - High, Cruiser - Mid, Battleship Low)
                    #location
                #other
                    #inventory (Bottomless v1)
                    #ship class (Corvette, Destroyer, Cruiser, Battleship)
                    #movement range (1-4)
                    #num enemies defeated (used to see if you can fight the final boss yet)
                #methods from Entity
                    #takeEDamage()
                    #takePDamage()
                    #save
                #overwritten Methods
                    #__str__
                    #showStats()
            
            
#################################
######## Map Tiles ##############
#################################

class MapTile(object):
    def __init__(self,occupied = False,player = False,boss = False,asciiArt = "",location = (0,0)):
        ##### attributes #####
        #empty/occupied (is there an enemy or anomaly here)
        self.__occupied = occupied
        #player occupied (y/n)
        self.__playerOccupied = player
        #is the boss here (y/n)
        self.__bossOccupied = boss
        #location (x,y coordinate)
        self.__location = location
        #ascii art
        self.__asciiArt = asciiArt
    def __str__ (self):
        return "M"
    def getLoc(self):
        return self.__location
        
class AnomalyTile(MapTile):
    def __init__(self,occupied = True, player = False, boss = False,asciiArt = "", damage = 2, buff = "",location = (0,0)):
        super().__init__(occupied,player,boss,asciiArt,location)
            #attributes from MapTile
                #empty/occupied (occupied)
                #player occupied (y/n)
                #is the boss here (n)
                #location
                #ascii art
        #### seperate attributes ####
        #damage (how much damage it would do the the player landing on it)
        self.__damage = damage
        #debuff/buff (any buff or de-buff it would apply
        self.__buff = buff
    def __str__(self):
        return "A"
        
class BlackHoleTile(AnomalyTile):
    def __init__(self):
        super().__init__()
        #attributes from AnomalyTile
            #empty/occupied (occupied)
            #player occupied (y/n)
            #is the boss here (n)
            #location
            #ascii art
        #seperate attributes
            #killPlayer()
        #use setHP() method on Entity class to kill player
        pass
    def __str__(self):
        return "H"
    
class EnemyTile(MapTile):
    def __init__(self):
        super().__init__()
            #attributes from MapTile
                #empty/occupied (occupied)
                #player occupied (y/n)
                #is the boss here(n)
                #location
                #ascii art
            #seperate
                #enemy object
        pass
    def __str__(self):
        return "E"
    
class BossTile(MapTile):
    def __init__(self):
        super().__init__()
            #attributes from MapTile
                #empty/occupied (occupied)
                #player occupied (y/n)
                #is the boss here(y)
                #location
                #ascii art
            #seperate
                #boss dialogue
                    #ready to encounter dialogue
                    #not ready (go away) dialogue
        pass
    def __str__(self):
        return "B"

class PlayerTile(MapTile):
    def __init__(self):
        super().__init__()
        #attributes from MapTile
            #empty/occupied (occupied)
            #player occupied (y)
            #is the boss here(n)
            #location
            #ascii art
        pass
    def __str__(self):
        return "P"
        
class Board(object):
    def __init__(self,rowList):
        #takes a list of rows of map objects
        self.__board = rowList
    def getBoard(self):
        #returns the whole board
        return self.__board
    def printBasicBoard(self):
        #prints a basic graphic representation of the board
        rowSep = "----------------------------------"
        for row in self.__board:
            print(rowSep)
            for column in row:
                print(column, end=" |  ")
            print()
        print(rowSep)
    def setTile(self,xCoord,yCoord,newTile):
        #replaces a tile at the given coordinates with a new tile
        #useful if an enemy dies, or an anomaly is cleared
        #or literally any time the player changes position
        self.__board[yCoord-1][xCoord-1] = newTile


#################################
######## Misc Objects ###########
#################################            
    
class Buff(object):
    def __init__(self):
        #attributes
            #stat affected (atk, spd, armor, shield, energyatk, movement?)
            #quantity of buff/debuff (negative number for a debuff)
            #name of buff/debuff
        pass
        
class Item(object):
    def __init__(self):
            #attributes
                #name
                #flavor text
                #stat affected (atk, spd, armor, shield, eneryatk, none)
                #buff object
        pass


        
