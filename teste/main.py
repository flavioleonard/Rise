from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
from PPlay.keyboard import *

window = Window(width=1200, height=700)
window.set_title('Space Invaders')

nave = Sprite("nave.png")
nave.x = window.width / 2 - nave.width / 2
nave.y = window.height - 100


controle = window.get_keyboard()

velN = 300
velShoot = 500

tiro = Sprite("shoot.png")
show_shoot = False

tiro_copy = 0


while True:
    window.set_background_color((219, 210, 81))
    nave.draw()

    if (controle.key_pressed("left")):
        nave.x -= velN * window.delta_time()
    elif (controle.key_pressed("right")):
        nave.x += velN * window.delta_time()
    if (nave.x <= 0):
        nave.x = 0
    if (nave.x >= window.width - nave.width):
        nave.x = window.width - nave.width

    if controle.key_pressed("SPACE"):
        tiro.set_position(nave.x + nave.width / 2 - tiro.width / 2, nave.y)
        show_shoot = True
        tiro.draw()
        tiro_copy = tiro
    if show_shoot == True:
        tiro_copy.unhide()
        tiro.draw()
        tiro_copy.y -= velShoot * window.delta_time()
    tiro = tiro

    window.update()

