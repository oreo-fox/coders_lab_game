
WIDTH = 600
HEIGHT = 600

figur = Actor('bunny')
figur.x = 300
figur.y = 300

def draw():
    screen.clear()
    screen.fill((240, 211, 242))
    figur.draw()

def update():

    if keyboard[keys.RIGHT]:
        # Bewegt den Hasen nach rechts
        figur.x = figur.x + 3
    if keyboard[keys.LEFT]:
        # Bewegt den Hasen nach links
        figur.x = figur.x - 3
    if keyboard[keys.UP]:
        # Bewegt den Hasen nach oben
        figur.y = figur.y - 3
    if keyboard[keys.DOWN]:
        # Bewegt den Hasen nach unten
        figur.y = figur.y + 3

def on_mouse_down(pos):
    if figur.collidepoint(pos):
        figur.image = 'bunny_hurt'
        clock.schedule_unique(set_normal, 1.0)

def set_normal():
    figur.image = 'bunny'
