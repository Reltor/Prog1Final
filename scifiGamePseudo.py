
########################
#### CharCreator.py ####
########################
#this file is responsible for creating and returning the player at the beginning of the game. 
#main function that generates a character
    #take user input, have then select a ship type from a displayed list
    #check to make sure they submitted a valid ship, loop until they do
    #ask the user to name their ship
    #if the user gives the name "Fire Fly" it will act as a "cheat code", setting up a ship for the user with extremely high stats
    #if the name isn't Fire Fly, stats will be generated based on the chosen ship class
    #use random.randint to select values for each needed stat from small ranges
    #encounters stat (to track the number of encounters a ship has been in) set to 0
    #construct a gameObjects.Player() object from those stats. 
    #display the stats
    #return the player

########################
### EnemyCreator.py ####
########################
#this file creates enemies and returns them 
#function to make weakEnemy
    #generate x enemies from a range of low stats
    #create an object for each
    #return a list of objects

#function to make medEnemy
    #generate x enemies from a range of medium stats
    #create an object for each
    #return a list of objects

#function to make hardEnemy
    #generate x enemies from a range of high stats
    #create an object for each
    #return a list of objects
#function to make super hard enemy
    #generate x enemies from a range of very high stats
    #create an object for each
    #return a list of objects


########################
#### gameObjects.py ####
########################
#this file contains all the objects we will use throughout the game. 
    #################################
    ######## Enemy and Player #######
    #################################

#class Entity is a superClass that provides the basics of both players and enemies
    #attributes----
            #attack
            #energy attack
            #armor
            #shields
            #name
            #speed
            #ascii art
            #location (x,y) 
    #methods
        #takePDamage() - taking normal attack damage - take physical damage, takes a damage amount as argument, modifies the value as appropriate and then effects the entity with it.
        #takeEDamage() - taking energy attack damage - take energy damage, takes a damage amount as argument, modifies the value as appropriate and then effects the entity with it.
        #showStats() - Summary of statistics relevant to the player
        #__str__() - Prints everything including background data - for debugging


#class Enemy is a subclass of entity
        #attributes from Entity Class----
            #attack
            #energy attack
            #armor
            #shields
            #name
            #speed
            #ascii art
            #location
        #own attributes - TODO
            #dropChances - enemies can drop items
            #isBoss (y/n) - flags whether this enemy is considered a final boss
            #enemyClass (pick from a list)
        #methods from Entity
            #takeEDamage() - 
            #takePDamage()
            #save
        #overwritten Methods
            #__str__
            #showStats() - No need to overwrite yet
            
        
#class Player is a subclass of entity
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
                    #inventory (Bottomless v1) - a list of the items the player has picked up
                    #ship class (Corvette, Destroyer, Cruiser, Battleship)
                    #movement range (1-4) - how many tiles can be moved per move max
                    #num enemies defeated (used to see if you can fight the final boss yet) - iterated every time an enemy is defeated. this is checked to
                                                                                             # see if you have progressed far enough to face the boss
                #methods from Entity
                    #takeEDamage()
                    #takePDamage()
                    #save
                #overwritten/new Methods
                    #pickupItem() - to take an item dropped
                    #useItem() - to use an item from inventory
                    #__str__
                    #showStats()
            
    #################################
    ######## Map Tiles ##############
    #################################

class MapTile(object):
    def __init__(self,occupied = False,player = False,boss = False,asciiArt = "",location = (0,0)):
        ##### attributes #####
        #empty/occupied (is there an enemy or anomaly here)
        #player occupied (y/n)
        #is the boss here (y/n)
        #location (x,y coordinate)
        #ascii art

        ##### methods #####
        #getter methods
        #setter methods

        
# a type of MapTile that contains an Anomaly, with its special effects and art
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
        #debuff/buff (any buff or de-buff it would apply
        
# a special subtype of anomaly that kills the player when they land on it, very low chance to spawn        
class BlackHoleTile(AnomalyTile):
    def __init__(self,occupied = True, player = False, boss = False,asciiArt = "", damage = 1000, buff = "",location = (0,0)):
        super().__init__(occupied,player,boss,asciiArt,damage,buff,location)
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

#an EnemyTile contains an enemy for the player to fight    
class EnemyTile(MapTile):
    def __init__(self,occupied = True,player = False,boss = False,asciiArt = "",location = (0,0)):
        super().__init__(occupied,player,boss,asciiArt,location)
            #attributes from MapTile
                #empty/occupied (occupied)
                #player occupied (y/n)
                #is the boss here(n)
                #location
                #ascii art
            #seperate
                #enemy object
        pass

#a boss tile contains the final boss, there will never be more than one of these.     
class BossTile(MapTile):
    def __init__(self,occupied = True,player = False,boss = True,asciiArt = "",location = (0,0)):
        super().__init__(occupied,player,boss,asciiArt,location)
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

#a playertile is the tile where the player is, when a player is idle on a spot, whatever tile was there is replaced with this. When the player leaves this tile would be replaced with a generic maptile.
class PlayerTile(MapTile):
    def __init__(self,occupied = True,player = True,boss = False,asciiArt = "",location = (0,0)):
        super().__init__(occupied,player,boss,asciiArt,location)
        #attributes from MapTile
            #empty/occupied (occupied)
            #player occupied (y)
            #is the boss here(n)
            #location
            #ascii art
        pass

#a Board is a list of lists of MapTile objects. It has methods to display itself, as well as replace tiles when their state changes. (player moves, enemy dies, etc)        
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

#A buff object can be carried by an object, anomaly, etc. It can apply effects that either strengthen or weaken the player.    
class Buff(object):
    def __init__(self):
        #attributes
            #stat affected (atk, spd, armor, shield, energyatk, movement?)
            #quantity of buff/debuff (negative number for a debuff)
            #name of buff/debuff
        pass

#enemies can drop items, items can be anything from just a name with some flavor text, to an item that applies an actual buff effect.        
class Item(object):
    def __init__(self):
            #attributes
                #name
                #flavor text
                #stat affected (atk, spd, armor, shield, eneryatk, none)
                #buff object
        pass
#class PermItem
    #an item that applies a permanent stat boost
    #applyEffects() adds stat boosts to player

#class TempItem
    #an item that applies a stat boost for X combat turns
    #x is defined by a time variable that is decremented every time the player ends a combat turn.

    #method: decreaseTimer(t) - reduces the amount of time left on the object by t
        #if timer is set low enough to hit 0 or lower, a running check of some kind will remove the effects on the player
    #applyEffects() adds stat boosts to player
#class OneUseItem
    #an item that applies a one combat turn stat boost (duration 1)
########################
### mainFunctions.py ###
########################
    
#generateCoordinates
    #takes a number of coordinates, the currently existing coordinates and the length of the board
    #create an empty list of new coordinates
    #generate a list X coordinates, checking to make sure they don't conflict with the ones that already exist
    #return the new list

#createBoard
    #takes the player as an argument, as well as x,y size of the board
    #takes an x,y size of the board
    #creates a list of Y rows
    #in each row creates a list of X columns
    #generates a random number of enemies, and their coordinates
        #places the enemies and their tiles into the list representing the board, at the coordinate
    #does the same as above for anomalies
    #generates one "boss" enemy, placing it at a new coordinate with a bosstile
    #random chance to spawn a blackhole with its coordinates and tile
    #places the player in an empty tile with a PlayerTile
    #all other spots are filled with generic map tiles
    #return the board
        
#createEnemyTile
    #creates an enemy using EnemyCreator.py
    #creates an EnemyTile
    #places the enemy in the tile and returns it

#createAnomalyTile
    #picks an anomaly from the list of defined anomalies
    #creates an AnomalyTile
    #places the anomaly on the tile and returns it

#move
    #takes a player object and the board
    #ask the player for an x and y movement length
    #if the movement lengths are less than or equal to the players max move
        #find the player based on the objects loc attribute
        #move the object by the specified x and y coordinates
        #set the tile the player used to be in to be a generic MapTile
        #set the new tile to playerOccupied = Yes
        #set all tiles the player moved over to "scanned"
    #return the board
#save
    #asks the user for a file name
    #appends {super secret extension} to the name
    #uses pickle to save the board to that file
    #ends the program

#load
    #ask the user for a file name
    #check to make sure the file exists, and has the right extension
    #if it does, load the file
    #else ask the user to confirm the filename
    #load the board from the file using pickle
    #le return le board


    
#main - handles the overarching game
    #load save (y/n)?
    #if no
        #create the player
        #create the board
    #if yes, load given save file.
        #check to make sure the file is a pickle file containing a legit 
    #ask the player, move, use item, save or quit. 
        #player moves
            #check if the tile contains the final boss
                #if the tile does contain the boss check the players number of enemy defeats
                    #if the player has defeated enough enemies ask the player if they want to fight the boss
                        #if yes initiate a battle with the final boss
                            #if you lose game over
                                #save the ending board
                                #sad pictures and death screens
                                #player is sad
                            #elif you win game won
                                #{lots of celebration and statistics that inflate your ego}
                #else if any of the conditions above are not met, move the player away 1 tile
                    #check where the player is
                    #if x coord <board size move the player one tile right
                    #elif y coord< board size move the player one tile down
                    #else move the player one tile left
            #if the tile doesnt contain the boss, check for an enemy or anomaly
                #if there is an enemy, fight it
                    #if the player wins, display {encouragment} {celebration} and replace the tile with an empty tile
                    #elif the player loses, end the game {possibly lose a life}?
                    #elif the player runs, move them 1 tile randomly 
                #else if there is an anomaly, apply its effects to the player
                #else display "nothing happened"
            #display the board at the end of the turn
        #use item
            #asks the player to choose an item from their inventory or cancel
            #if the player wants to use an item that is not a time based effect, warn them it will be wasted
                #if they still want to use it, use the item
                #else loop back to top
        #save
            #use a save function to save the board.
            #the board contains all objects and tiles and everything in play, so we should just need to save that one object.
        #quit
            #warns the player to save first
            #if they choose to save, run the save function
            #else terminate the program. 

########################
###### combat.py #######
########################

#combat
    #takes a player and a list of enemies
        #for each enemy
            #prints starting stats of enemy and player
            #checks speed attribute of boths
            #whoever has more speed goes first
            #while both are alive and neither has fled
                #if players turn
                    #ask the player to choose between using an item, physical attack, energy attack or running
                    #if physical or energy, use the corresponding function on the enemy (takeEDamage, takePDamage) with the players attack
                    #elif flee, use speed to calculate a random chance to get away
                        #if the player flees successfully, end whole function, return "Fled" and Player and any remaining enemies
                        #elif the player doesn't flee successfuly, they forfeit their turn
                    #elif use item, have the player choose an item to use.
                        #list of usable items
                        #use "while selection not in" to make sure input is an item
                        #activate item buff
                        #remove item from inventory
                #if enemies turn
                    #check its energy and physical damage
                    #use chooseAttack() method to select an enemy attack to use
                    #use that attack
    #if the player won, end reason  = "WIN"
    #elif the player died, end reason = "DEAD"
    #elif the player ran, end reason = "RUN"
    #once all enemies are dead, the player is dead, or player runs.
        #return player, remaining enemies, reason combat ended
                

