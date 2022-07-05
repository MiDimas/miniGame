import pygame

pygame.init()
win = pygame.display.set_mode((500, 330))

pygame.display.set_caption('GameMiDi')

walkLeft = [pygame.image.load("sprite/left_walk0.png"), pygame.image.load("sprite/left_walk1.png"),
            pygame.image.load("sprite/left_walk2.png"), pygame.image.load("sprite/left_walk3.png"),
            pygame.image.load("sprite/left_walk4.png"), pygame.image.load("sprite/left_walk5.png"),
            pygame.image.load("sprite/left_walk6.png"), pygame.image.load("sprite/left_walk7.png")]

walkRight = [pygame.image.load("sprite/right_walk0.png"), pygame.image.load("sprite/right_walk1.png"),
             pygame.image.load("sprite/right_walk2.png"), pygame.image.load("sprite/right_walk3.png"),
             pygame.image.load("sprite/right_walk4.png"), pygame.image.load("sprite/right_walk5.png"),
             pygame.image.load("sprite/right_walk6.png"), pygame.image.load("sprite/right_walk7.png")]

playerStand = pygame.image.load("sprite/character_robot_idle.png")
bg = pygame.image.load("sprite/bg.png")
tile = pygame.image.load("sprite/tile_0000.png")

clock = pygame.time.Clock()

x = 50
y = 170

width = 90
height = 128

blockX = 250
blockY = 250
blockWidth = 10
blockHeight = 10

speed = 5
isJump = False
jumpCount = 10

left = False
right = False
aniCount = 0


def drawWin():
    global aniCount

    win.blit(bg, (0, 0))

    if aniCount + 1 >= 40:
        aniCount = 0

    if left:
        win.blit(walkLeft[aniCount // 5], (x, y))
        aniCount += 1
    elif right:
        win.blit(walkRight[aniCount // 5], (x, y))
        aniCount += 1
    else:
        win.blit(playerStand, (x, y))

    win.blit(tile, (blockX, blockY))
    pygame.display.update()


run = True
while run:
    clock.tick(40)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 5:
        if x > blockX + blockWidth or x <= blockX - width or isJump:
            x -= speed
            left = True
            right = False

    elif keys[pygame.K_RIGHT] and x < 400:
        if x < blockX - width or x >= blockX + blockWidth or isJump:
            x += speed
            left = False
            right = True
    else:
        left = False
        right = False
        aniCount = 0

    if not isJump:
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            if jumpCount > 0:
                y -= (jumpCount ** 2) / 2
            else:
                y += (jumpCount ** 2) / 2
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10
    drawWin()



pygame.quit()