# Ping-Pong
# By Alexander Belyakov, alexander.belyakov@gmail.com

import pygame, random, sys
from pygame.locals import *

FPS = 30
WINDOWWIDTH = 640
WINDOWHEIGHT = 480
PADDLEWIDTH = 10
PADDLEHEIGHT = 60
BALLSIZE = 10
MISSILESIZE = 10
NETHEIGHT = WINDOWHEIGHT
NETWIDTH = 10

PADDLESPEED = 5
MISSILESPEED = 10
VICTORYGOALS = 9

BLACK  = (0,   0,   0  )
WHITE  = (255, 255, 255)
ORANGE = (255, 153, 0  )

BACKGROUNDCOLOR = BLACK
LEFTPLAYERCOLOR = WHITE
RIGHTPLAYERCOLOR = WHITE
BALLCOLOR = WHITE
NETCOLOR = WHITE
TEXTCOLOR = WHITE
MISSILECOLOR = ORANGE

def terminate():
    pygame.quit()
    sys.exit()

def waitForKeyPress():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYUP:
                if event.key == K_ESCAPE:
                    terminate()
                if event.key == K_RETURN:
                    return

def showTitleScreen():
    showText = True
    while True:
        DISPLAYSURF.fill(BACKGROUNDCOLOR)
        x0 = WINDOWWIDTH / 2 - 115 # "PING PONG" is 230 pixels wide
        y0 = WINDOWHEIGHT / 2 - 100 # "PING PONG" is 150 pixels high + "PRESS ANY KEY TO START"
        drawLetter("P", DISPLAYSURF, TEXTCOLOR, x0 + 20, y0)
        drawLetter("I", DISPLAYSURF, TEXTCOLOR, x0 + 80, y0)
        drawLetter("N", DISPLAYSURF, TEXTCOLOR, x0 + 100, y0)
        drawLetter("G", DISPLAYSURF, TEXTCOLOR, x0 + 160, y0)
        drawLetter("P", DISPLAYSURF, TEXTCOLOR, x0, y0 + 80)
        drawLetter("O", DISPLAYSURF, TEXTCOLOR, x0 + 60, y0 + 80)
        drawLetter("N", DISPLAYSURF, TEXTCOLOR, x0 + 120, y0 + 80)
        drawLetter("G", DISPLAYSURF, TEXTCOLOR, x0 + 180, y0 + 80)
        if showText == True:
            drawText("PRESS ENTER TO START", font, TEXTCOLOR, DISPLAYSURF, x0 + 15, y0 + 180)
        showText = not showText
        drawText("Alexander Belyakov, 2014", smallFont, TEXTCOLOR, DISPLAYSURF, x0 + 40, WINDOWHEIGHT - 20)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYUP:
                if event.key == K_ESCAPE:
                    terminate()
                if event.key == K_RETURN:
                    return
        FPSCLOCK.tick(2)

def drawLetter(letter, surface, color, x, y):
    if letter == "P":
        pygame.draw.rect(surface, color, (x, y, 10, 70))
        pygame.draw.rect(surface, color, (x + 10, y, 40, 10))
        pygame.draw.rect(surface, color, (x + 40, y + 10, 10, 30))
        pygame.draw.rect(surface, color, (x + 10, y + 30, 30, 10))
    elif letter == "I" or letter == "1":
        pygame.draw.rect(surface, color, (x, y, 10, 70))
    elif letter == "N":
        pygame.draw.rect(surface, color, (x, y, 10, 70))
        pygame.draw.polygon(surface, color, ((x + 10, y), (x + 10, y + 20), (x + 40, y + 69), (x + 40, y + 49)))
        pygame.draw.rect(surface, color, (x + 40, y, 10, 70))
    elif letter == "G":
        pygame.draw.rect(surface, color, (x, y, 10, 70))
        pygame.draw.rect(surface, color, (x + 10, y, 40, 10))
        pygame.draw.rect(surface, color, (x + 10, y + 60, 40, 10))
        pygame.draw.rect(surface, color, (x + 40, y + 30, 10, 30))
        pygame.draw.rect(surface, color, (x + 20, y + 30, 20, 10))
    elif letter == "O" or letter == "0":
        pygame.draw.rect(surface, color, (x, y, 10, 70))
        pygame.draw.rect(surface, color, (x + 10, y, 40, 10))
        pygame.draw.rect(surface, color, (x + 40, y + 10, 10, 60))
        pygame.draw.rect(surface, color, (x + 10, y + 60, 30, 10))
    elif letter == "2":
        pygame.draw.rect(surface, color, (x, y, 50, 10))
        pygame.draw.rect(surface, color, (x + 40, y + 10, 10, 20))
        pygame.draw.rect(surface, color, (x, y + 30, 50, 10))
        pygame.draw.rect(surface, color, (x, y + 40, 10, 20))
        pygame.draw.rect(surface, color, (x, y + 60, 50, 10))
    elif letter == "3":
        pygame.draw.rect(surface, color, (x, y, 50, 10))
        pygame.draw.rect(surface, color, (x + 40, y + 10, 10, 60))
        pygame.draw.rect(surface, color, (x + 10, y + 30, 40, 10))
        pygame.draw.rect(surface, color, (x, y + 60, 50, 10))
    elif letter == "4":
        pygame.draw.rect(surface, color, (x, y, 10, 40))
        pygame.draw.rect(surface, color, (x + 40, y, 10, 70))
        pygame.draw.rect(surface, color, (x + 10, y + 30, 30, 10))
    elif letter == "S" or letter == "5":
        pygame.draw.rect(surface, color, (x, y, 50, 10))
        pygame.draw.rect(surface, color, (x, y + 10, 10, 20))
        pygame.draw.rect(surface, color, (x, y + 30, 50, 10))
        pygame.draw.rect(surface, color, (x + 40, y + 40, 10, 20))
        pygame.draw.rect(surface, color, (x, y + 60, 50, 10))
    elif letter == "6":
        pygame.draw.rect(surface, color, (x, y, 50, 10))
        pygame.draw.rect(surface, color, (x, y + 10, 10, 60))
        pygame.draw.rect(surface, color, (x + 10, y + 30, 40, 10))
        pygame.draw.rect(surface, color, (x + 40, y + 40, 10, 30))
        pygame.draw.rect(surface, color, (x + 10, y + 60, 40, 10))
    elif letter == "7":
        pygame.draw.rect(surface, color, (x, y, 50, 10))
        pygame.draw.rect(surface, color, (x + 40, y + 10, 10, 60))
        pygame.draw.rect(surface, color, (x + 20, y + 30, 30, 10))
    elif letter == "8":
        pygame.draw.rect(surface, color, (x, y, 50, 10))
        pygame.draw.rect(surface, color, (x, y + 10, 10, 60))
        pygame.draw.rect(surface, color, (x + 10, y + 30, 30, 10))
        pygame.draw.rect(surface, color, (x + 40, y + 10, 10, 60))
        pygame.draw.rect(surface, color, (x + 10, y + 60, 40, 10))
    elif letter == "9":
        pygame.draw.rect(surface, color, (x, y, 50, 10))
        pygame.draw.rect(surface, color, (x, y + 10, 10, 30))
        pygame.draw.rect(surface, color, (x + 10, y + 30, 30, 10))
        pygame.draw.rect(surface, color, (x + 40, y + 10, 10, 60))
        pygame.draw.rect(surface, color, (x, y + 60, 50, 10))
    elif letter == "A":
        pygame.draw.rect(surface, color, (x, y, 50, 10))
        pygame.draw.rect(surface, color, (x, y + 10, 10, 60))
        pygame.draw.rect(surface, color, (x + 10, y + 30, 30, 10))
        pygame.draw.rect(surface, color, (x + 40, y + 10, 10, 60))
    elif letter == "M":
        pygame.draw.rect(surface, color, (x, y, 50, 10))
        pygame.draw.rect(surface, color, (x, y + 10, 10, 60))
        pygame.draw.rect(surface, color, (x + 20, y + 10, 10, 60))
        pygame.draw.rect(surface, color, (x + 40, y + 10, 10, 60))
    elif letter == "E":
        pygame.draw.rect(surface, color, (x, y, 50, 10))
        pygame.draw.rect(surface, color, (x, y + 10, 10, 60))
        pygame.draw.rect(surface, color, (x + 10, y + 30, 30, 10))
        pygame.draw.rect(surface, color, (x, y + 60, 50, 10))
    elif letter == "V":
        pygame.draw.rect(surface, color, (x, y, 10, 70))
        pygame.draw.polygon(surface, color, ((x + 10, y + 50), (x + 10, y + 69), (x + 50, y), (x + 40, y)))
    elif letter == "R":
        pygame.draw.rect(surface, color, (x, y, 10, 70))
        pygame.draw.rect(surface, color, (x + 10, y, 40, 10))
        pygame.draw.rect(surface, color, (x + 40, y + 10, 10, 30))
        pygame.draw.rect(surface, color, (x + 10, y + 30, 30, 10))
        pygame.draw.polygon(surface, color, ((x + 30, y + 40), (x + 40, y + 70), (x + 50, y + 70), (x + 40, y + 40)))
    return

def drawText(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def moveBall():
    ball["rect"] = pygame.Rect (ball["rect"].left + ball["vel"][0] * ballSpeed, ball["rect"].top + ball["vel"][1] * ballSpeed, BALLSIZE, BALLSIZE)

def hasBallHitWall():
    if ball["rect"].top < 0:
        ball["rect"].top = 0
        ball["vel"][1] = -(ball["vel"][1])
    if ball["rect"].bottom > WINDOWHEIGHT:
        ball["rect"].bottom = WINDOWHEIGHT
        ball["vel"][1] = -(ball["vel"][1])

def showGameScreen(leftScore, rightScore):
    DISPLAYSURF.fill(BACKGROUNDCOLOR)
    pygame.draw.rect(DISPLAYSURF, NETCOLOR, (WINDOWWIDTH / 2 - NETWIDTH / 2, 0, NETWIDTH, NETHEIGHT)) # Net
    if leftScore == 1:
        drawLetter(str(leftScore), DISPLAYSURF, LEFTPLAYERCOLOR, WINDOWWIDTH / 2 - NETWIDTH / 2 - 30, 20) # Left Score
    else:
        drawLetter(str(leftScore), DISPLAYSURF, LEFTPLAYERCOLOR, WINDOWWIDTH / 2 - NETWIDTH / 2 - 70, 20) # Left Score
    drawLetter(str(rightScore), DISPLAYSURF, RIGHTPLAYERCOLOR, WINDOWWIDTH / 2 + NETWIDTH / 2 + 20, 20) # Right Score
    pygame.draw.rect(DISPLAYSURF, BALLCOLOR, (ball["rect"].left, ball["rect"].top, BALLSIZE, BALLSIZE)) # Ball
    pygame.draw.rect(DISPLAYSURF, LEFTPLAYERCOLOR, (leftPlayerPaddle.left, leftPlayerPaddle.top, PADDLEWIDTH, PADDLEHEIGHT)) # Left Paddle
    pygame.draw.rect(DISPLAYSURF, RIGHTPLAYERCOLOR, (rightPlayerPaddle.left, rightPlayerPaddle.top, PADDLEWIDTH, PADDLEHEIGHT)) # Right Paddle
    # drawText(str(leftPlayerMissile), smallFont, TEXTCOLOR, DISPLAYSURF, 20, 20)
    pygame.display.update()

def getPlayerInput():
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
            terminate()
        if event.type == KEYDOWN:
            if event.key == ord("w"):
                paddleMoves["leftUp"] = True
                paddleMoves["leftDown"] = False
            if event.key == ord("s"):
                paddleMoves["leftDown"] = True
                paddleMoves["leftUp"] = False
            if event.key == K_UP:
                paddleMoves["rightUp"] = True
                paddleMoves["rightDown"] = False
            if event.key == K_DOWN:
                paddleMoves["rightDown"] = True
                paddleMoves["rightUp"] = False
        if event.type == KEYUP:
            if event.key == ord("w"):
                paddleMoves["leftUp"] = False
            if event.key == ord("s"):
                paddleMoves["leftDown"] = False
            if event.key == K_UP:
                paddleMoves["rightUp"] = False
            if event.key == K_DOWN:
                paddleMoves["rightDown"] = False
            if event.key == ord("m"):
                if musicOn[0]:
                    musicOn[0] = False
                    pygame.mixer.music.pause()
                elif not musicOn[0]:
                    musicOn[0] = True
                    pygame.mixer.music.unpause()

def isMusicSwitched(musicOn):
    for event in pygame.event.get():
        if event.type == KEYUP:
            if event.key == ord("m"):
                if musicOn:
                    musicOn = False
                    pygame.mixer.music.pause()
                elif not musicOn:
                    musicOn = True
                    pygame.mixer.music.unpause()
    return musicOn

def hasPaddleHitWall(paddle):
    if paddle.top < 0: paddle.top = 0
    if paddle.bottom > WINDOWHEIGHT: paddle.bottom = WINDOWHEIGHT

def hasBallHitPaddle(paddle):
    if ball["rect"].colliderect(paddle):
        ball["vel"][0] = -(ball["vel"][0])
        hitSound.play()
        if paddle.left == 0:
            ball["rect"].left = PADDLEWIDTH + 1
        if paddle.right == WINDOWWIDTH:
            ball["rect"].right = WINDOWWIDTH - PADDLEWIDTH - 1

def movePaddles():
    if paddleMoves["leftUp"] == True: leftPlayerPaddle.top -= PADDLESPEED
    if paddleMoves["leftDown"] == True: leftPlayerPaddle.top += PADDLESPEED
    if paddleMoves["rightUp"] == True: rightPlayerPaddle.top -= PADDLESPEED
    if paddleMoves["rightDown"] == True: rightPlayerPaddle.top += PADDLESPEED

def hasPlayerScored():
    if ball["rect"].left < 0: return "right"
    elif ball["rect"].right > WINDOWWIDTH: return "left"
    else: return ""

def showResults(leftScore, rightScore):
    x0 = WINDOWWIDTH / 2 - 115 # "GAME OVER" is 230 pixels wide
    y0 = WINDOWHEIGHT / 2 - 75 # "GAME OVER" is 150 pixels high
    pygame.draw.rect(DISPLAYSURF, BACKGROUNDCOLOR, (x0 - 20, y0 - 20, 270, 190))
    drawLetter("G", DISPLAYSURF, TEXTCOLOR, x0, y0)
    drawLetter("A", DISPLAYSURF, TEXTCOLOR, x0 + 60, y0)
    drawLetter("M", DISPLAYSURF, TEXTCOLOR, x0 + 120, y0)
    drawLetter("E", DISPLAYSURF, TEXTCOLOR, x0 + 180, y0)
    drawLetter("O", DISPLAYSURF, TEXTCOLOR, x0, y0 + 80)
    drawLetter("V", DISPLAYSURF, TEXTCOLOR, x0 + 60, y0 + 80)
    drawLetter("E", DISPLAYSURF, TEXTCOLOR, x0 + 120, y0 + 80)
    drawLetter("R", DISPLAYSURF, TEXTCOLOR, x0 + 180, y0 + 80)
    pygame.display.update()

# Game Starts Here

pygame.mixer.pre_init(frequency=22050, size=-16, channels=1, buffer=512)
pygame.mixer.init(frequency=22050, size=-16, channels=1, buffer=512)
pygame.init()

FPSCLOCK = pygame.time.Clock()

DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption("Ping-Pong")

pygame.mouse.set_visible(False)

font = pygame.font.SysFont(None, 24)
smallFont = pygame.font.SysFont(None, 18)

hitSound = pygame.mixer.Sound("hit.wav")
hitSound.set_volume(0.4)
missSound = pygame.mixer.Sound("miss.wav")
missSound.set_volume(0.2)
gameOverSound = pygame.mixer.Sound("gameover2.wav")
pygame.mixer.music.load("ping-pong-music.wav")
pygame.mixer.music.set_volume(0.5)

# Loop for entire program

while True:
    
    leftScore = 0
    rightScore = 0
    leftPlayerPaddle = pygame.Rect(0, ((WINDOWHEIGHT / 2) - (PADDLEHEIGHT / 2)), PADDLEWIDTH, PADDLEHEIGHT)
    rightPlayerPaddle = pygame.Rect((WINDOWWIDTH - PADDLEWIDTH), ((WINDOWHEIGHT / 2) - (PADDLEHEIGHT / 2)), PADDLEWIDTH, PADDLEHEIGHT)
    paddleMoves = {"leftUp":False, "leftDown":False, "rightUp":False, "rightDown":False}
    
    gameOverSound.play()
    showTitleScreen()
    
    musicOn = [True]
    pygame.mixer.music.play(-1, 0.0)

    # Loop for one game

    while True:

        if leftScore == VICTORYGOALS or rightScore == VICTORYGOALS:
            showGameScreen(leftScore, rightScore)
            FPSCLOCK.tick(2)
            break

        timeCounter = 0
        ballSpeed = 4

        ball = {"rect":pygame.Rect(((WINDOWWIDTH / 2) - (BALLSIZE / 2)), ((WINDOWHEIGHT / 2) - (BALLSIZE / 2)), BALLSIZE, BALLSIZE), "vel":[]}
        ball["vel"] = [random.choice([-1, 1]), random.choice([-1, 1])]

        # Loop for one score

        while True:

            getPlayerInput()                        # Check for button presses
            movePaddles()                           # Move paddles
            hasPaddleHitWall(leftPlayerPaddle)      # If paddle hits wall, don't move further
            hasPaddleHitWall(rightPlayerPaddle)     # If paddle hits wall, don't move further
            moveBall()                              # Move ball
            hasBallHitWall()                        # If ball hits wall, change vertical velocity to opposite
            hasBallHitPaddle(leftPlayerPaddle)      # If ball hits paddle, change horizontal velocity to opposite
            hasBallHitPaddle(rightPlayerPaddle)     # If ball hits paddle, change horizontal velocity to opposite
            showGameScreen(leftScore, rightScore)   # Draw paddles, ball, net and scores
            
            if hasPlayerScored() == "left":
                leftScore += 1
                missSound.play()
                break
            if hasPlayerScored() == "right":
                rightScore += 1
                missSound.play()
                break

            # Ball gradually speeds up

            if ballSpeed < 10:
                timeCounter += 1
            if timeCounter == FPS * 2 and ballSpeed == 4:
                timeCounter = 0
                ballSpeed = 5
            if timeCounter == FPS * 4 and ballSpeed == 5:
                timeCounter = 0
                ballSpeed = 6
            if timeCounter == FPS * 6 and ballSpeed == 6:
                timeCounter = 0
                ballSpeed = 7
            if timeCounter == FPS * 8 and ballSpeed == 7:
                timeCounter = 0
                ballSpeed = 8
            if timeCounter == FPS * 10 and ballSpeed == 8:
                timeCounter = 0
                ballSpeed = 9
            if timeCounter == FPS * 12 and ballSpeed == 9:
                timeCounter = 0
                ballSpeed = 10
            
            FPSCLOCK.tick(FPS)

    showResults(leftScore, rightScore)
    pygame.mixer.music.stop()
    gameOverSound.play()
    waitForKeyPress()
