#fileExtensions
    #items - .item
    #save file - .scisav
    #enemyDef - .hostile
    #anomalyDef - .anomaly
    #artDef - .art

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
    #construct a gameObjects.Player() object from created stats. 
    #display the stats
    #return the player

########################
### EnemyCreator.py ####
########################

#this file creates enemies and returns them 
#function to make enemy
    #takes one arg ("low","medium","high","superhigh") that represents what level of enemy is being created
    #loads all the games items from file (pickle ftw)
    #if/elif structure for each possible enemy type
        #for each type, randomly generate each stat based on a set range of values
        #enemies droptables will be predefined
        #use the predefined list for the enemy to grab the right item objects
    #else
        #return null
    #construct an enemy class using all the info
    #return the enemy



########################
#### gameObjects.py ####
########################
#this file contains all the object definitions we will use throughout the game. 
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
            #takeEDamage()  
            #takePDamage()
        #overwritten Methods
            #__str__
            #showStats()
                #additionally displays drop tables, whether its the boss, and the enemy class
            
        
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
                    #num enemies defeated (used to see if you can fight the final boss yet)
                    #num anomalies explored                                                                     
                    #damage dealt
                    #damage taken
                #overwritten/new Methods
                    #pickupItem() - to take an item dropped
                    #useItem() - to use an item from inventory
                    #__str__
                    #showStats()
                    #takeEDamage()
                        #use Entity version
                        #add the damage to damage taken
                    #takePDamage()
                        #use Entity version
                        #add the damage to damage taken
            
    #################################
    ######## Map Tiles ##############
    #################################

#MapTile
        ##### attributes #####
        #empty/occupied (is there an enemy or anomaly here)
        #player occupied (y/n)
        #is the boss here (y/n)
        #location (x,y coordinate)
        #ascii art
        #player (a player object or null value)

        ##### methods #####
        #getter methods
        #setter methods
        #addPlayer
            #adds a player object to the tile
        #removePlayer
            #takes the player object
            #replaces it with null
            #returns the player objects

        
# a type of MapTile that contains an Anomaly, with its special effects and art
#AnomalyTile
            #attributes from MapTile
                #empty/occupied (occupied)
                #player occupied (y/n)
                #is the boss here (n)
                #location
                #ascii art
                #player
        #### seperate attributes ####
        #damage (how much damage it would do the the player landing on it)
        #debuff/buff (any buff or de-buff it would apply
        
# a special subtype of anomaly that kills the player when they land on it, very low chance to spawn        
#BlackHoleTile
        #attributes from AnomalyTile
            #empty/occupied (occupied)
            #player occupied (y/n)
            #is the boss here (n)
            #location
            #ascii art
            #player
        #seperate attributes
            #killPlayer()
            #get players energy mod and current health
                #calculate raw damage needed to kill them
                #apply needed damage
        

#an EnemyTile contains an enemy for the player to fight    
#EnemyTile
            #attributes from MapTile
                #empty/occupied (occupied)
                #player occupied (y/n)
                #is the boss here(n)
                #location
                #ascii art
                #player
            #seperate
                #enemy object
        

#a boss tile contains the final boss, there will never be more than one of these.     
#BossTile
            #attributes from MapTile
                #empty/occupied (occupied)
                #player occupied (y/n)
                #is the boss here(y)
                #location
                #ascii art
                #player
            #seperate
                #boss dialogue
                    #ready to encounter dialogue
                    #not ready (go away) dialogue
        

#a playertile is the tile where the player is, when a player is idle on a spot, whatever tile was there is replaced with this. When the player leaves this tile would be replaced with a generic maptile.
#PlayerTile
        #attributes from MapTile
            #empty/occupied (occupied)
            #player occupied (y)
            #is the boss here(n)
            #location
            #ascii art
        

#a Board is a list of lists of MapTile objects. It has methods to display itself, as well as replace tiles when their state changes. (player moves, enemy dies, etc)        
#Board
        #takes a list of rows of map objects
        #assigned as self.__board
    #getBoard(self):
        #return self.__board variable
    #getX
        #returns x length of board
    #getY
        #returns y length of board
    #printBasicBoard(self):
        #prints a basic graphic representation of the board
        #using seperators and other basic text representations
    #setTile(self,xCoord,yCoord,newTile):
        #replaces a tile at the given coordinates with a new tile
        #useful if an enemy dies, or an anomaly is cleared
        #or literally any time the player changes position
        #self.__board[yCoord-1][xCoord-1] = newTile


    #################################
    ######## Misc Objects ###########
    #################################            

#A buff object can be carried by an object, anomaly, etc. It can apply effects that either strengthen or weaken the player.    
#Buff
        #attributes
            #stat affected (atk, spd, armor, shield, energyatk, movement?)
            #quantity of buff/debuff (negative number for a debuff)
            #name of buff/debuff


#enemies can drop items, items can be anything from just a name with some flavor text, to an item that applies an actual buff effect.        
#Item
            #attributes
                #name
                #flavor text
                #stat affected (atk, spd, armor, shield, eneryatk, none)
                #buff object
            #methods
                #applyEffects() adds stat boosts to player
                #removeEffects() removes its buffs from the player
        
#class PermItem
    #an item that applies a permanent stat boost
    
#class TempItem
    #an item that applies a stat boost for X combat turns
    #x is defined by a time variable that is decremented every time the player ends a combat turn.

    #method: decreaseTimer(t) - reduces the amount of time left on the object by t
        #if timer is set low enough to hit 0 or lower, a running check of some kind will remove the effects on the player

#class OneUseItem
    #an item that applies a one combat turn stat boost (duration 1)


#class Anomaly
    #basically a pretty effect that applies debuffs
    #attributes
        #location
        #buff/debuffs
        #art
        #name
        #??????


########################
### mainFunctions.py ###
########################
    
#generateCoordinates
    #takes a number of coordinates, the currently existing coordinates and the x,y size of the board
    #create an empty list of new coordinates
    #generate a list X coordinates, checking to make sure they don't conflict with the ones that already exist
    #return the new list

#createBoard
    #takes the player as an argument, as well as x,y size of the board
    #takes an x,y size of the board
    #creates a list of Y rows
    #in each row creates a list of X columns
    #generates a random number of enemies, and their coordinates
    #decides what parts of those enemies are going to be what level based on player level.
        #for each enemy
            #use more random numbers to decide what level each enemy is
            #use the enemy creator to make the enemy based on that level
            #create an enemy tile with the enemy on it
        #places the enemy tiles into the list representing the board, at their coordinates
    #generate a random number of anomalies and coordinates
        #for each anomaly
            #randomly choose one from a file of definitions
            #create an anomalytile with that anomaly in it
        #place all the anomaly tiles at their coordinates
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
        #set the tile the player used to be in to be a generic MapTile if the tile was a PlayerTile
            #simply set playerOccupied = False if the tile is still occupied by something else
        #set the new tile to playerOccupied = Yes
        #set all tiles the player moved over to "scanned"
        #update players loc variable so it knows where it is
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
    #return board


#### MAIN FUNCTION FOR THE WHOLE GAME ####    
#main - handles the overarching game
    #load save (y/n)?
    #if no
        #create the player
        #create the board
    #if yes, load given save file.
        #check to make sure the file is a pickle file containing a legit save.
        #display the board
        #display character stats and other relevant info
    #check if the player has won, or is dead. if either is true move to the appropriate endGame function, else move on
    #check if the player is on an enemy/anomaly/boss tile. if they are occupied start encounter.
        #else ask the player, move, use item, save or quit. 
        #player moves or player was already on an occupied tile
            #check if the tile contains the final boss
                #if the tile does contain the boss check the players number of enemy defeats
                    #if the player has defeated enough enemies ask the player if they want to fight the boss
                        #if yes initiate a battle with the final boss - combat.py
                            #if you lose game over
                                #save the ending board
                                #sad pictures and death screens
                                #player is sad
                            #elif you win game won
                                #replace boss tile with playerTile
                                #{lots of celebration and statistics that inflate your ego}
                #else if player dont have enough encounters or dont want to fight, move the player away 1 tile - move()
                    #check where the player is
                    #if x coord <board size move the player one tile right
                    #elif y coord< board size move the player one tile down
                    #else move the player one tile left
            #if the tile doesnt contain the boss, check for an enemy or anomaly
                #if there is an enemy, fight it
                    #if the player wins, display {encouragment} {celebration} and replace their current tile with a PlayerTile
                    #elif the player loses, end the game {possibly lose a life}?
                    #elif the player runs, move them 1 tile randomly
                        #update the enemyTile with the enemies state after battle
                        
                #else if there is an anomaly, apply its effects to the player
                    #set anomaly tile to player occupied
                #else display "nothing happened"
            #change the state of all tiles the player moved across to "explored"
            #display the board at the end of the turn

    
        #use item
            #asks the player to choose an item from their inventory or cancel
            #if the player wants to use an item that is single use, warn them it will be wasted
                #if they still want to use it, use the item
                #else loop back to top

    
        #save
            #use a save function to save the board.
            #the board contains all objects and tiles and everything in play, so we should just need to save that one object.

    
        #quit
            #warns the player to save first
            #if they choose to save, run the save function
            #else terminate the program.

    #playerWins
        #celebration
        #list off enemies killed
        #damage done
        #damage taken
        #anomalies explored
        #???
        #THE END
    
    #playerLoses
        #tragic death message
        #list off enemies killed
        #damage done
        #damage taken
        #anomalies explored
        #celebrate the glorious life of what killed the player
        #THE END

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
                        #take the return value of the damage
                        #use method in Player class to add that damage to the players overall damage dealt
                    #elif flee, use speed to calculate a random chance to get away
                        #if the player flees successfully, end whole function, return "Fled" and Player and any remaining enemies
                        #elif the player doesn't flee successfuly, they forfeit their turn
                    #elif use item, have the player choose an item to use.
                        #list of usable items
                        #use "while selection not in" to make sure input is an item
                        #activate item buff
                        #remove item from inventory
                    #decrement timers for all items in players inventory that aren't permanent, except the just used one.
                    #if any items have reached 0, call their removeEffects() method and remove them from the player
                #if enemies turn
                    #check its energy and physical damage
                    #use chooseAttack() method to select an enemy attack to use
                    #use that attack
    #if the player won, end reason  = "WIN"
    #elif the player died, end reason = "DEAD"
    #elif the player ran, end reason = "RUN"
    #once all enemies are dead, the player is dead, or player runs.
        #return player, remaining enemies, reason combat ended
                

########################
##### encounter.py #####
########################
#anomalyEncounter
    #takes the player and anomaly as arguments
    #generates the flavor text for the anomaly
    #applies a buff or debuff effect to the player
    #iterates the player's anomaly counter
    #returns the player

########################
###### itemGen.py ######
########################
#just used by dev/enterprising player to add items to the games item lists outside the game

#createItem
    #used on the dev end to add an object to the game
    #takes stat affected, name of the object, how much it boosts the stat
    #constructs an Item object
    #appends it to gameItems.item
