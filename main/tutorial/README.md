<!-- download markdown preview or look at this on github -->

# Pygame basics

more info at https://www.pygame.org/docs/
## table of contents
1. [making a window](#making-a-window)
2. [graphics](#graphics)
3. [making the player move](#making-the-player-move)
### making a window

ok so basically to make a window you use this:

```python
import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720)) #screen size (this is by pixels i think)
clock = pygame.time.Clock() #i dont even know what this means
running = True # opens the

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("purple")

    # GAME CODE HERE

    pygame.display.flip()

    clock.tick(60)

pygame.quit()

```

`screen.fill()` is the code you use for the background. you can use the colors red, purple, and yellow but theres probably more. when you're using this put your color inside of the parantheses and put quotation marks around it like this:

```python
screen.fill("red")
```

you can change the background in the window script if you want or you can copy and paste the code too

### graphics

ok so basically to draw a circle do this:

```python
pygame.draw.circle(screen, "red", player_pos, 40)
```

im not sure what `player_pos` means but i think its like the x or y axis (like the ones in scratch) that the player starts in

before running this tho you have to add this to your code:

```python
player_pos = pygame.Vextor2(screen.get_width() / 2, screen.get_height() / 2)
```

or else it will throw an error like this:
```powershell
NameError: name 'player_pos' is not defined
```
**in a tutorial**<br>
this basically means the computer doesnt know what you're talking about. this probably means you missed something in the tutorial and forgot to write the code <br><br>
<u> *(if u wanna go to the next part click [this](#making-the-player-move))*</u><br>

**not in a tutorial**<br>
you have to make a variable for the thingy

```python
print(idk)
```
so for example if you try to run this without any other code then it give you and error thats probably similar to this:

```powershell
NameError: name 'idk' is not defined
```
so just make the variable 

```python
idk = "balls"
```

and then the code will work if tyou use tthis example the result will be this:

```
balls
```
it will just say the word balls

### making the player move

ok so basically i dont know *__(will update later)__*
