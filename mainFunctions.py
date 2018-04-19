import random
import gameObjects
#################################
######## Creator Functions ######
#################################
def generateCoordinates(coordList,numCoordinates,boardX,boardY):
    newCoords = []
    for point in range(numCoordinates):
        validCoord = False
        while not validCoord:
            xCoord = random.randint(1,boardX)
            yCoord = random.randint(1,boardX)
            coordPair = (xCoord,yCoord)
            if coordPair not in coordList:
                coordList.append(coordPair)
                newCoords.append(coordPair)
                validCoord = True
            else:
                validCoord = False
    return newCoords

def createBoard(rows,columns):
    #create a board of size x size dimensions via nested lists.
    rowList = []
    for row in range(rows):
        columnList = []
        for column in range(columns):
            columnList.append("")
        rowList.append(columnList)
    # masterCoordList tracks all used points, ensuring that anomalies, enemies and all other map tiles wont conflict or overwrite each other    
    #randomly choose a number of points based on some calculation
    numEnemies = random.randint(2,4)
    masterCoordList = []
    enemyCoordList = generateCoordinates(masterCoordList[:],numEnemies,columns,rows)
    for coord in enemyCoordList:
        masterCoordList.append(coord)
    numAnomalies = random.randint(2,4)
    anomalyCoordList = generateCoordinates(masterCoordList[:],numAnomalies,columns,rows)
    for coord in anomalyCoordList:
        masterCoordList.append(coord)
        
    #create enemy or anomaly tiles for those points
    for coord in enemyCoordList:
        enemyTile = gameObjects.EnemyTile()
        rowList[coord[1]-1][coord[0]-1] = enemyTile
        print(rowList[coord[1]-1][coord[0]-1])
    for coord in anomalyCoordList:
        anomalyTile = gameObjects.AnomalyTile()
        rowList[coord[1]-1][coord[0]-1] = anomalyTile
        print(rowList[coord[1]-1][coord[0]-1])
        
    #randomly place one "major/boss" enemy at another points
    bossCoord = generateCoordinates(masterCoordList[:],1,columns,rows)[0]
    masterCoordList.append(bossCoord)
    bossTile = gameObjects.BossTile()
    rowList[coord[1]-1][coord[0]-1] = bossTile
    print(rowList[coord[1]-1][coord[0]-1])
    
    #random chance for a black hole, insta-death at another point
    blackHoleChance = 10
    blackHoleInt = random.randint(0,blackHoleChance)
    if blackHoleInt == 1:
        blackHoleTile = gameObjects.BlackHoleTile()
        blackHoleCoord = generateCoordinates(masterCoordList[:],1,columns,rows)[0]
        rowList[coord[1]-1][coord[0]-1] = blackHoleTile
        print(rowList[coord[1]-1][coord[0]-1])
    #place the player
    playerTile = gameObjects.PlayerTile()
    playerCoord = generateCoordinates(masterCoordList[:],1,columns,rows)[0]
    masterCoordList.append(playerCoord)
    rowList[coord[1]-1][coord[0]-1] = playerTile
    #create empty tiles for all other points
    for row in rowList:
        for tile in row:
            if type(tile) is str:
                tileIndex = row.index(tile)
                row[tileIndex] = gameObjects.MapTile()
    gameBoard = gameObjects.Board(rowList)
    gameBoard.printBasicBoard()
    #return the board
    return gameBoard
        

def createPlayer(): #charCreator.py
    #get the players name
    #get their ship class (corvette, destroyer, cruiser, battleship)
    #load value ranges for that class
    #randomly generate (within specific values) stats based on class
    #load ascii art and speed for that class
    #create a player object with all the above info
    #return the object
    pass

def createEnemy():
    #load the enemy definitions file
    #randomly select one and load its object (use pickle to save the objects to file)
    #return the enemy
    pass

def createEnemyTile():
    #create an enemy
    #instantiate an EnemyTile object with that enemy
    #return the EnemyTile
    pass

def createAnomalyTile():
    #load anomaly definitions file
    #randomly select one and load its object (pickle)
    #return the object
    pass



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
    pass

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
                        #if you lose game over
                        #elif you win game won
                            #{lots of celebration and statistics that inflate your ego
            #else if any of the conditions above are not met, move the player away 1 tile
                #check where the player is
                #if x coord <board size move the player one tile right
                #elif y coord< board size move the player one tile down
                #else move the player one tile left
        #if the tile doesnt contain the boss, check for an enemy or anomaly
            #if there is an enemy, fight it
                #if the player wins, display {encouragment} {celebration} and replace the tile with an empty tile
                #elif the player loses, end the game {possibly lose a life}?
            #else if there is an anomaly, apply its effects to the player
            #else display "nothing happened"

createBoard(7,7)
