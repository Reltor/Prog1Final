
#make it so if you haven't fought enough enemies, you are moved away from final boss.

#cheatCODE - PlayerName - Firefly (sets moves to max, all stats as high as possible, enemy counter high enough for final boss, displays coordinate of final boss)

#################################
######## Enemy and Player #######
#################################

class Enemy(object):
    def __init__(self):
        #attributes----
            #attack
            #energy attack
            #armor
            #shields
            #name
            #speed
            #dropChances
            #ascii art
            #location
        
class Player(Enemy):
    def __init__(self):
        Enemy.__init__(self):
            #attributes----
                #from Enemy class
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

            
#################################
######## Map Tiles ##############
#################################

class MapTile(object):
    def __init__(self):
        #attributes
            #empty/occupied (is there an enemy or anomaly here)
            #player occupied (y/n)
            #is the boss here (y/n)
            #location (x,y coordinate)
            #ascii art
        
class Anomaly(MapTile):
    def __init__(self):
        MapTile.__init__(self):
            #attributes from MapTile
                #empty/occupied (occupied)
                #player occupied (y/n)
                #is the boss here (y/n)
                #location
                #ascii art
            #seperate attributes
                #damage (how much damage it would do the the player landing on it)
                #debuff/buff (any buff or de-buff it would apply)

class EnemyTile(MapTile):
    def __init__(self):
        MapTile.__init__(self):
            #attributes from MapTile
                #empty/occupied (occupied)
                #player occupied (y/n)
                #is the boss here(y/n)
                #location
                #ascii art
            #seperate
                #enemy object
            
#################################
######## Misc Objects ###########
#################################            
    
class Buff(object):
    def __init__(self):
        #attributes
            #stat affected (atk, spd, armor, shield, energyatk, movement?)
            #quantity of buff/debuff (negative number for a debuff)
            #name of buff/debuff
        
class Item(object):
    def __init__(self):
            #attributes
                #name
                #flavor text
                #stat affected (atk, spd, armor, shield, eneryatk, none)
                #buff object


#################################
######## Creator Functions ######
#################################
        
def createBoard(size):
    #create a board of size x size dimensions via nested lists.
    #randomly choose a number of points based on some calculation
    #create enemy or anomaly tiles for those points
    #randomly place one "major/boss" enemy at another points
    #random chance for a black hole, insta-death at another point
    #create empty tiles for all other points
    #return the board

def createPlayer():
    #get the players name
    #get their ship class (corvette, destroyer, cruiser, battleship)
    #load value ranges for that class
    #randomly generate (within specific values) stats based on class
    #load ascii art and speed for that class
    #create a player object with all the above info
    #return the object

def createEnemy():
    #load the enemy definitions file
    #randomly select one and load its object (use pickle to save the objects to file)
    #return the enemy

def createEnemyTile():
    #create an enemy
    #instantiate an EnemyTile object with that enemy
    #return the EnemyTile

def createAnomalyTile():
    #load anomaly definitions file
    #randomly select one and load its object (pickle)
    #return the object




#################################
##### Gameplay Functions ########
#################################
    
def move(player,board):
    #ask the player for an x and y movement length
    #if the movement lengths are less than or equal to the players max move
        #find the player
        #move the object by the specified x and y coordinates
        #set the tile the player used to be in to playeroccupied = no
        #set the new tile to player occupied = yes
    #return the board

#################################
############# Main ##############
#################################
    
def main():
    player = createPlayer()
    board = createBoard()
    #player moves
    #check if the tile contains the final boss
        #if the tile does contain the boss check the players number of enemy defeats
            #if the player has defeated enough enemies ask the player if they want to fight the boss
                #if yes initiate a battle with the final boss
        #else if any of the conditions above are not met, move the player away 1 tile
            #check where the player is
            #if x coord <board size move the player one tile right
            #elif y coord< board size move the player one tile down
            #else move the player one tile left
    #if the tile doesnt contain the boss, check for an enemy or anomaly
        #if there is an enemy, fight it
        #else if there is an anomaly, apply its effects to the player
        #else display "nothing happened"
