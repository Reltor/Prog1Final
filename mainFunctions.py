import random
import gameObjects
import CharCreator
import EnemyCreator
import combat
import items
import pickle
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

def createBoard(rows,columns,player):
    #create a board of size x size dimensions via nested lists.
    rowList = []
    for row in range(rows):
        columnList = []
        for column in range(columns):
            columnList.append("")
        rowList.append(columnList)
    numEnemies = random.randint(2,4) #number range currently hardcoded, want to change
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
        enemyTile = createEnemyTile(coord)
        rowList[coord[1]-1][coord[0]-1] = enemyTile
        
    for coord in anomalyCoordList:
        anomalyTile = createAnomalyTile(coord)
        rowList[coord[1]-1][coord[0]-1] = anomalyTile
        
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
    playerTile = gameObjects.PlayerTile(player) #create the tile with the player
    playerCoord = generateCoordinates(masterCoordList[:],1,columns,rows)[0]
    masterCoordList.append(playerCoord)
    
    rowList[coord[1]-1][coord[0]-1] = playerTile #place it on the board
    
    #create empty tiles for all other points
    for row in rowList:
        for tile in row:
            if type(tile) is str:
                tileIndex = row.index(tile)
                row[tileIndex] = gameObjects.MapTile()
    gameBoard = gameObjects.Board(rowList)
    gameBoard.printBasicBoard()
    
    return gameBoard


def createEnemyTile(coord):
    EASY = 1
    MEDIUM = 2
    HARD = 3
    SUPERHARD = 4
    enemyClass = random.randint(1,4)
    if enemyClass == EASY:
        newEnemy = EnemyCreator.weakEnemy(1)[0]
    elif enemyClass == MEDIUM:
        newEnemy = EnemyCreator.medEnemy(1)[0]
    elif enemyClass == HARD:
        newEnemy = EnemyCreator.hardEnemy(1)[0]
    elif enemyClass == SUPERHARD:
        newEnemy = EnemyCreator.shEnemy(1)[0]
    #finish adding other enemy types
    enemyTile = gameObjects.EnemyTile(newEnemy, location = coord)
    return enemyTile

def createAnomalyTile(coord):
    #load anomaly definitions file
    #randomly select one and load its object (pickle)
    anomalyTile = gameObjects.AnomalyTile(location = coord)
    #return the object
    return anomalyTile



#################################
##### Gameplay Functions ########
#################################
    
def move(player,board):
    #ask the player for an x and y movement length
    validMove = False
    while not validMove:
        try:
            playerX = int(input("How far would you like to move left/right? (Negative numbers will be considered left)"))
            playerY = int(input("How far would you like to move up/down? (Negative numbers will be considered down"))
        except ValueError:
            print("Moves must be integer values")
        totalMoveLen = abs(playerX) + abs(playerY)
        if totalMoveLen > player.getMoveRange():
            print("That is too many spaces, please pick lower move values")
        elif totalMoveLen <= player.getMoveRange():
            newCoordX = player.getCoord[0] + playerX
            newCoordY = player.getCoord[1] + playerY
            if newCoordX => 1 and newCoordX <= board.getX() and newCoordY => 1 and newCoordY <= board.getY():
                newCoord = (newCoordX,newCoordY)
                validMove = True
            else:
                print("That move would take you off the board and is invalid")
    player.setLoc(newCoord)
    oldTile = board.getRawBoard()[player.getCoord[1]-1][player.getCoord[0]-1]
    newTile = board.getRawBoard()[newCoordY-1][newCoordX-1]
    oldTile.removePlayer()
    newTile.addPlayer()
    
    #if the movement lengths are less than or equal to the players max move
        #find the player
        #move the object by the specified x and y coordinates
        #set the tile the player used to be in to playeroccupied = no
        #set the new tile to player occupied = yes
    #return the board
    return player, board

#################################
############# Main ##############
#################################
    
def main():
    validResponse = False
    while not validResponse:
        loadSave = str(input("Would you like to load an existing save? [Y/N]? "))
        if loadSave == "Y" or loadSave == "N":
            validResponse = True
        else:
            print("That is not yes or no")
    if loadSave == "N":
        print("Beginning Game")
        player = CharCreator.main()
        board = createBoard(7,7,player)
    elif loadSave == "Y":
        board = loadGame()
        board.showBoard()
        player.gameSummary()

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

main()
