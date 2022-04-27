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

# Eine Liste für die Monster
monsters = []

# Hier geben wir die Anfangsposition des Hasen an
hase.x = 100
hase.y = 500

# ist der Hase oben angekommen?
jump_down = False

# Gesammelte Karotten und Anzahl Leben
score = 0
lifes = 3

# Die draw Funktion zeichnet etwas in das Fenster
# Mit screen.clear() stellen wir sicher, dass das fenster anfangs leer ist
def draw():
    screen.clear()

    # Fügt den Hintergrund hinzu
    screen.blit('background', (0, 0))

    # Fügt den Hasen hinzu
    hase.draw()

    # Zeichnet die Anzeige für die Karotten und Lebenspunkte
    screen.blit('carrot_count', (20,640))
    screen.blit('lifes', (150, 635))
    screen.draw.text(f"{score}", (80, 640), color='black', fontsize=60)
    screen.draw.text(f"{lifes}", (210, 640), color='black', fontsize=60)

    # Zeichnet Karroten und Monster
    for carrot in carrots:
        carrot.draw()
    for monster in monsters:
        monster.draw()

# Die update Funktion überprüft dauernd, ob etwas passiert
def update():

    if hase.y < 500:
        hase.image = "bunny1_jump"
    else:
        hase.image = "bunny1_stand"

    # Die Funktionen, welche die Monster/Karotten hinzufügen werden aufgerufen
    make_carrots()
    make_monsters()
    global score
    global lifes

    for carrot in carrots:
        if hase.colliderect(carrot):
            score += 1
            carrot.x = 750

    for monster in monsters:
        if hase.colliderect(monster):
            lifes -= 1
            monster.x = 750
            if lifes == 0:
                exit()

    # Wir nutzen if-statements um zu prüfen ob eine Taste gedrückt wird

    if keyboard[keys.RIGHT]:
        # Bewegt den Hasen nach rechts
        hase.x = hase.x + 3
    if keyboard[keys.LEFT]:
        # Bewegt den Hasen nach links
        hase.x = hase.x - 3

    if hase.y < 500:
        #  Lässt den Hasen zürück auf den Boden fallen, nachdem er gesprungen ist
        hase.y = hase.y + 2

    if keyboard[keys.SPACE]:

        global jump_down

        if jump_down and hase.y < 500:
            return

        elif jump_down and hase.y >= 500:
            jump_down = False

        elif hase.y >= 200 and not jump_down:
            hase.y = hase.y - 5

        elif hase.y < 200:
            jump_down = True

def on_key_up(key):
    if key == keys.SPACE:
        global jump_down
        jump_down = True

def make_carrots():
    # Mit dieser Funktion erstellen wir zufällig die Karotten

    if random.randint(0,100) < 1:
        y = random.randint(70, 350)
        carrots.append(Actor('carrot_fly', (0, y)))

    for carrot in carrots:
        carrot.x = carrot.x + 3
        if carrot.x >= 750:
            carrots.remove(carrot)

def make_monsters():
    # Mit dieser Funktion erstellen wir zufällig die Monster

    if random.randint(0, 300) < 1:
        y = random.randint(70, 350)
        monsters.append(Actor('monster1', (0, y)))

    for monster in monsters:
        monster.x = monster.x + 3
        if monster.x >= 750:
            monsters.remove(monster)

