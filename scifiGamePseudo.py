#fileExtensions
    #items - .item
    #save file - .scisav
    #enemyDef - .hostile
    #anomalyDef - .anomaly
    #artDef - .art


########################
### mainFunctions.py ###
########################
    
#generateCoordinates
    #takes a number of coordinates, the currently existing coordinates and the x,y size of the board
    #create an empty list of new coordinates
    #generate a list X coordinates, checking to make sure they don't conflict with the ones that already exist
        #if they don't conflict add them to the list of new coordinates
        #once there are the required number of new coordinates, return them
    #return the new list

#createBoard
    #takes the player as an argument, as well as x,y size of the board
    #creates a list of Y rows
    #in each row creates a list of X columns
    #generates a random number of enemies
        #for each enemy generates its coordinates using generateCoordinates()
        #random numbers 1-4 represent enemy level (EASY,MEDIUM,HARD,SUPERHARD), for each coordinate a random number is chosen
        #for each enemy
            #generate a random number to decide the enemy level
            #use the enemy creator to make the enemy based on that level
            #create an enemy tile with the enemy in it 
        #place the enemy tiles into the list representing the board, at their designated coordinates
    #generate a random number of anomalies and coordinates
        #for each anomaly
            #randomly choose one from a file of definitions
            #create an anomalytile with that anomaly in it
        #place all the anomaly tiles at their coordinates
    #generates one "boss" enemy, placing it at a new coordinate with a bosstile
    #random chance to spawn a blackhole with its coordinates and tile
    #all other spots are filled with generic map tiles
    #pick a random one of these map tiles
        #generate player coordinates and set the appropriate tile to playerOccupied
    #return the board
        
#createEnemyTile
    #creates an enemy using EnemyCreator.py
    #instantiates an EnemyTile object using that enemy
    #places the enemy in the tile and returns the tile

#createAnomalyTile
    #picks an anomaly from the list of defined anomalies
    #creates an AnomalyTile
    #places the anomaly on the tile and returns it

#move
    #takes a player object, board and ord of key press
    #if ORD is UP
        #check to make sure board exists at that coord
            #if not leave everything alone
            #print "due to subspace anomaly you are unable to explore this region of space"
        #subtract 1 from Y coord
    #elif ord is DOWN
        #check to make sure board exists at that coord
            #if not leave everything alone
            #print "due to subspace anomaly you are unable to explore this region of space"
        #add 1 to Y coord
    #elif ord is LEFT
        #check to make sure board exists at that coord
            #if not leave everything alone
            #print "due to subspace anomaly you are unable to explore this region of space"
        #subtract 1 from X coord
    #elif ord is RIGHT
        #check to make sure board exists at that coord
            #if not leave everything alone
            #print "due to subspace anomaly you are unable to explore this region of space"
        #add 1 to X coord


    #set old tile to playerOccupied = False
    #if tile is empty and and enemyTile, change to wreckage tile - if time
    #elif tile is anomaly tile, do nothing else
    #elif tile is empty, do nothing else
    #change player coord
    #redraw board
    #return board, player
    
 
#moveAway
    #used to run from boss or fight
    #takes player object and board
    #finds the player
    #randomly generates a direction to move
    #tries to move the player that direction
    #redraws
    #if that tile is occupied, continues to move the player until it finds an empty tile.
    #change player coord
    #redraw board
    #return board, player
    
#save
    #takes a player and a board as args
    #asks the user for a file name
    #appends {super secret extension} to the name
    #uses pickle to save the board to that file
    #uses pickle to save the player to that file
    #ends the program

#load
    #ask the user for a file name
        #check to make sure the file exists, and has the right extension
        #if it does, load the file
        #load the board from the file using pickle
        #load the player from the file using pickle
    #else ask the user to confirm the filename

    #return board, player


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
        #player presses key move -> [UP/DOWN/LEFT/RIGHT ARROWS] OR Q [Quit] OR S [Save] OR I [Inventory]
            #player moves
                #MOVE()
                #player moves to an occupied tile
                    #encounter = True
                    #check if the tile contains the final boss
                        #if the tile does contain the boss check the players number of enemy defeats
                            #if the player has defeated enough enemies ask the player if they want to fight the boss
                                #if yes initiate a battle with the final boss - combat.py
                                    #if you lose game over   -playerLoses()
                                    #elif you win game won   -playerWins()
                        #else if player doesnt have enough encounters or dont want to fight, move the player away
                            #move the player one tile based on RNG and position (Up,down,left,right)
                            #loop random moves until a valid move is found. 
                            #while not valid move
                                #moveAway()
                                
                    #if the tile doesnt contain the boss, check for an enemy or anomaly
                        #if there is an enemy, fight it
                            #if the player wins, display {encouragment} {celebration} and replace their current tile with a PlayerTile
                            #elif the player loses, end the game {possibly lose a life}?
                            #elif the player runs, move them 1 tile randomly
                                #update the enemyTile with the enemies state after battle
                                
                        #else if there is an anomaly, player encounters the anomaly
                            #set anomaly tile to player occupied
                #player moves to unoccupied tile
            #redraw board
            
        
            #use item
                #asks the player to choose an item from their inventory or cancel
                #if the player wants to use an item that is single use, warn them it will be wasted
                    #if they still want to use it, use the item
                    #else loop back to top
        
            #save
                #use a save function to save the board.
                #the board contains all objects and tiles and everything in play, so we should just need to save that one object.

        
            #quit
                #warns the player to save first [Q] to quit, [S] to save
                    #if they choose to save, run the save function
                    #else terminate the program.

#playerWins
    #replace boss tile with playerTile
    #redraw board
    #{lots of celebration and statistics that inflate your ego}
    #celebration
    #list off enemies killed
    #damage done
    #damage taken
    #anomalies explored
    #???
    #THE END

#playerLoses
    #save the ending board
    #sad pictures and death screens
    #player is sad
    #tragic death message
    #list off enemies killed
    #damage done
    #damage taken
    #anomalies explored
    #celebrate the glorious life of what killed the player
    #THE END

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
            #hp
    #methods
        #takePDamage() - taking normal attack damage - take physical damage, takes a damage amount as argument, modifies the value as appropriate and then effects the entity with it.
        #takeEDamage() - taking energy attack damage - take energy damage, takes a damage amount as argument, modifies the value as appropriate and then effects the entity with it.
        #showStats() - Summary of statistics relevant to the player
        #takeDMG
        #changeXStat (setters for all the statz)
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
            #hp
        #own attributes - TODO
            #dropChances - enemies can drop items
            #isBoss (y/n) - flags whether this enemy is considered a final boss
            #enemyClass (pick from a list)
        #methods from Entity
            #takeEDamage()  
            #takePDamage()
            #changeXStat()
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
                    #hp
                #other
                    #inventory (Bottomless v1) - a list of the items the player has picked up
                    #ship class (Corvette, Destroyer, Cruiser, Battleship)
                    #num enemies defeated (used to see if you can fight the final boss yet)
                    #num anomalies explored                                                                     
                    #damage dealt
                    #damage taken
                #overwritten/new Methods
                    #pickupItem() - to take an item dropped
                    #usePowerup() - to use an item from inventory
                        #take an item from inventory
                        #find its effect
                        #apply the effect to the player
                    #useCombatItem()
                        #heals
                        #torpedos
                        #etc
                        #apply effects to enemy
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

        ##### methods #####
        #getter methods
        #setter methods
        #addPlayer
            #adds a player object to the tile
        #removePlayer
            #takes the player object
            #replaces it with null
            #returns the player objects
        #__str__(self):
            #if the tile doesn't have a player, display tile art/char representation
            #elif the tile is playerOccupied, display "P"
            #return display value

        
# a type of MapTile that contains an Anomaly, with its special effects and art
#AnomalyTile
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
#BlackHoleTile
        #attributes from AnomalyTile
            #empty/occupied (occupied)
            #player occupied (y/n)
            #is the boss here (n)
            #location
            #ascii art
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
            #seperate
                #boss dialogue
                    #ready to encounter dialogue
                    #not ready (go away) dialogue
        

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
        #self.__board[yCoord][xCoord] = newTile
    #addPlayer(coord)
        #sets the tile at coord to playerOccupied
    #removePlayer(coord)
        #sets the tile at coord to not playerOccupied
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
                    #elif use item and player has items to use, have the player choose an item to use.
                        #list of useable combat items
                        #choice with plaintext
                        #use item
                        #if item does damage, add to players overall damage
                #if enemies turn
                    #check its energy and physical damage
                    #use chooseAttack() method to select an enemy attack to use
                    #use that attack
            #drop an item for the player
                #item pickup 
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
    #redraw with below vvvvv
    #generates the flavor text for the anomaly
    #applies a buff or debuff effect to the player
    #iterates the player's anomaly counter
    #returns the player

########################
###### itemGen.py ######
########################
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

##### combat items #####

##insert remove shields item here
##insert remove armor item here
##insert reduce speed item here
##insert damage item here
##insert useless item here - FIREWORKSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS


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

