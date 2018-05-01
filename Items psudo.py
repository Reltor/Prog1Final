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
