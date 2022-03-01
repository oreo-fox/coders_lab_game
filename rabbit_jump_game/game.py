import time
import random

# Der Titel des Spiels wird oben am Fenster angezeigt
TITLE = "Carrot Jump"

# Mit WIDTH und HEIGHT passt du die Fenstergrösse an
WIDTH = 700
HEIGHT = 700

# Hier erstellen wir unseren Hasen
hase = Actor('bunny1_stand')

# Eine Liste für die Karotten
carrots = []
CARROT_CHANCE = 1

# Hier geben wir die Anfangsposition des Hasen an
hase.x = 100
hase.y = 500

# ist der Hase oben angekommen?
jump_down = False


# Die draw Funktion zeichnet etwas in das Fenster
# Mit screen.clear() stellen wir sicher, dass das fenster anfangs leer ist
def draw():
    global carrots
    screen.clear()
    screen.blit('background', (0, 0))
    hase.draw()

    for carrot in carrots:
        carrot.draw()

# Die update Funktion überprüft dauernd, ob etwas passiert
def update():
    make_carrots()
    # Wir nutzen if-statements um zu prüfen ob eine Taste gedrückt wird
    if hase.y < 500:
        hase.y = hase.y + 2
    if keyboard[keys.RIGHT]:
        # Bewegt den Hasen nach rechts
        hase.x = hase.x + 3
    if keyboard[keys.LEFT]:
        # bewegt den Hasen nach links
        hase.x = hase.x - 3
    if keyboard[keys.SPACE]:

        global jump_down

        if jump_down and hase.y < 500:
            return

        elif jump_down and hase.y >= 500:
            jump_down = False

        elif hase.y >= 200 and not jump_down:
            hase.y = hase.y - 5
            jump_down = False

        elif hase.y < 200:
            jump_down = True


def make_carrots():
    global carrots

    if random.randint(0,100) < CARROT_CHANCE:
        y = random.randint(200, 400)
        carrots.append(Actor('carrot_fly', (0, y)))
    for carrot in carrots:
        carrot.x = carrot.x + 3
