import gameObjects # the player object will be defined in gameObjects.py

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
