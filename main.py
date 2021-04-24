import pygame
import math
from pygame import mixer
from time import sleep
from random import randint
try:
        pygame.init()
        screen = pygame.display.set_mode((950, 550))
        pygame.display.set_caption("Stick man")
        background = pygame.image.load("grass and rocks better version.png")
        stickman = pygame.image.load("stickman.png")
        sky = pygame.image.load("sky.png")
        font = pygame.font.Font('BebasNeue-Regular.ttf', 28)
        gameoverfont = pygame.font.Font('BebasNeue-Regular.ttf', 70)
        playagain = pygame.font.Font('BebasNeue-Regular.ttf', 17)
        madeby = pygame.font.Font('BebasNeue-Regular.ttf', 12)
        c = 0

        playerx = 150
        playery = 375
        playerx_change = 0
        playery_change = 0
        jump = "ready"

        standing = True
        nottouching = True
        alive = True

        nubmer_of_pionts = 0

        mixer.music.load("backgroundmusic.mp3")
        mixer.music.play(-1)
        collisionSound = mixer.Sound("KnifeStab.mp3")

        # saw
        saw = pygame.image.load("saw-blade.png")
        sawx_change = []
        sawimage = []
        sawx = []
        randomxforsaw = [900, 1200, 1600, 2000, 2500, 2700, 3000, 3300, 3600, 4000, 4500]
        speedofsaw = [7.8,6.5,5, 3, 1]
        print("ok so there are some bugs..\n*sometimes the score will not increase\n espicly if the blade is moving fast\n after inputing number of blades i have gievn a 2 second deplay to help swtiching to the game \n5 is the recomended number of blades\nspeed of every blade is different everytime u try again ")
        #take 3
        numberofsaws = 4
        sleep(2)
        orginalsawx=[]

        for i in range(numberofsaws):
            sawimage.append(pygame.image.load("saw-blade.png"))
            sawx.append(randomxforsaw[randint(0, 10)])
            sawx_change.append(speedofsaw[randint(0, 3)])
        for i in range(numberofsaws):
            orginalsawx.append(sawx[i])

        def player(x, y):
            screen.blit(stickman, (x, y))


        # displays saw movenmet
        def sawMove(x, y):
            screen.blit(saw, (x, y))


        # saw movent and teleportation
        def saw_movement(i):
            global sawx_change
            global nottouching
            global sawx
            global saw_x_orginal
            global nubmer_of_pionts

            if nottouching:
                    sawx[i] -= sawx_change[i]
                    if sawx[i] > 0:
                        sawMove(sawx[i], 425)


                    if sawx[i]<=0:
                        sawx[i] = orginalsawx[i]
                        nubmer_of_pionts += 1



        # uses sawx
        def score_display():
            global nubmer_of_pionts
            global nottouching
            if nottouching:
                score = font.render("Score:" + str(nubmer_of_pionts), True, (255, 255, 255))
                screen.blit(score, (10, 225))


        # saw collision needs x and y of saw
        def collision(i):
            global nottouching
            global sawx

            distance = math.sqrt(math.pow((sawx[i] + 32) - playerx, 2) + math.pow(457 - playery, 2))
            if distance < 85 and playerx > sawx[i] + 32:
                nottouching = False

            elif distance < 100 and playerx < sawx[i] + 32:
                nottouching = False


        def gameover(points):
            global alive
            if not nottouching:
                score = font.render("Score:" + str(points), True, (255, 255, 255))
                screen.blit(score, (445, 300))
                gameoverdisplay = gameoverfont.render("GAME OVER", True, (255, 255, 255))
                screen.blit(gameoverdisplay, (365, 200))
                playagaindisplay = playagain.render("Restart to play again", True, (255, 255, 255))
                screen.blit(playagaindisplay, (415, 275))
                alive = False


        def death():
            global c
            if not nottouching and c < 1:
                screen.fill((255, 0, 0))
                collisionSound.play()
                pygame.display.update()
                sleep(0.02)
                screen.fill((191, 0, 0))
                pygame.display.update()
                sleep(0.03)
                screen.fill((255, 0, 0))
                pygame.display.update()
                sleep(0.02)
                c = 1


        running = True
        while running:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        playerx_change = -2
                    if event.key == pygame.K_RIGHT:
                        playerx_change = 2
                    if event.key == pygame.K_UP:
                        if jump == "ready":
                            playery_change = -4
                            jump = "jumping"

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        playerx_change = 0
                    if event.key == pygame.K_DOWN:
                        standing = True

            if alive:
                playerx += playerx_change
                playery += playery_change

            screen.fill((255, 255, 255))
            screen.blit(sky, (0, 0))

            # requies loop
            for i in range(numberofsaws):
               saw_movement(i)
               collision(i)

            # no need for for loop
            score_display()

            screen.blit(background, (0, 450))

            # not need for change
            death()

            gameover(nubmer_of_pionts)

            if playerx < 0:
                playerx = 0
            if playerx > 920:
                playerx = 920
            if playery < 375 - 100:
                playery_change = +3.6
            if playery > 375:
                jump = "ready"
                playery = 375
            if standing:
                player(playerx, playery)
            madebyme = madeby.render("Made by - Madhav", True, (255, 255, 255))
            screen.blit(madebyme, (878, 537))

            pygame.display.update()
except:
    print("u did not input a integer. close and try again")
    input("press enter to close")
