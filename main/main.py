import pygame
# ok paste this in your terminal:
#
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0  # dt = delta time but idk what it means

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
while running:
    for event in pygame.event.get():
        # pygame.QUIT = when the user clicks x
        if event.type == pygame.QUIT:
            running = False

    # this is the color of the screen to run it click on the play button on the top
    screen.fill("purple")

    # GAME CODE HERE
    pygame.draw.circle(screen, "red", player_pos, 40)  # draws a yellow circle

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:  # the last part with the w is like the keys u use to move
        player.pos.y -= 300 * dt  # the y is like move 300 by the y axis since it has a minus next to the equal sign its basically saying move by y -300 every time u press w

    if keys[pygame.K_s]:
        # since this has a plus this means move by y +300 (or 300) every time you press S
        player_pos.y += 300  # ! doesnt work for some reason

        # TODO: fix the thingy

    pygame.display.flip()

    clock.tick(60) / 1000

pygame.quit()
