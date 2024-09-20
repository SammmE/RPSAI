import random

def aiTurn():
    aiNum = random.randint(0, 2)
    if aiNum == 0:
        aiChoice = 'R'
    elif aiNum == 1:
        aiChoice = 'P'
    else:
        aiChoice = 'S'
    return aiChoice

def userTurn():
    print('Play your turn (R = Rock, P = Paper, S = Scissors)')
    userChoice = input().upper()
    if userChoice in ['R', 'P', 'S']:
        return userChoice
    else:
        print('Invalid Option')
        return userTurn()

def gamelogic(aiChoice, userChoice):
    if aiChoice == userChoice:
        gamestate = 'Draw'
    elif aiChoice == 'S' and userChoice == 'P':
        gamestate = 'AI Wins'
    elif aiChoice == 'P' and userChoice == 'R':
        gamestate = 'AI Wins'
    elif aiChoice == 'R' and userChoice == 'S':
        gamestate = 'AI Wins'
    elif aiChoice == 'S' and userChoice == 'R':
        gamestate = 'User Wins'
    elif aiChoice == 'P' and userChoice == 'S':
        gamestate = 'User Wins'
    elif aiChoice == 'R' and userChoice == 'P':
        gamestate = 'User Wins'
    return gamestate

while True:
    aiChoice = aiTurn()
    userChoice = userTurn()
    print(f'AI chose: {aiChoice}, You chose: {userChoice}')
    print(gamelogic(aiChoice, userChoice))
