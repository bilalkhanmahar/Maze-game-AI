import turtle
import random
import time

from levels import level_1, level_2
from sprites import sprite_images

# Screen setup
wn = turtle.Screen()
wn.bgcolor('#1c2f2f')
wn.title('Maze Game')
wn.setup(width=700, height=700)
wn.tracer(0)

grid_block_size = 24

# Register shapes
for sprite in sprite_images:
    wn.register_shape(sprite)

wn.register_shape("restart.gif")
wn.register_shape("exit.gif")
wn.register_shape("nextlevel.gif")  # <-- Register Next Level Button

# Game variables
walls = []
treasures = []
enemies = []
pen_walls = []
difficulty = 1
game_running = True
current_level = 1
message_turtle = None  # Used to clear previous message

# Pen
class Pen(turtle.Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.color('#362020')
        self.shape("jungle.gif")
        self.penup()
        self.speed(0)
        self.goto(x, y)
        self.stamp()
        self.hideturtle()

# Player
class Player(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.speed(0)
        self.name = 'Player'
        self.shape("player-right.gif")
        self.gold = 0

    def move(self, dx, dy):
        new_x = self.xcor() + dx
        new_y = self.ycor() + dy
        if (new_x, new_y) not in walls:
            self.setposition(new_x, new_y)
            if dx > 0:
                self.shape("player-right.gif")
            elif dx < 0:
                self.shape("player-left.gif")

    def move_up(self): self.move(0, 24)
    def move_down(self): self.move(0, -24)
    def move_left(self): self.move(-24, 0)
    def move_right(self): self.move(24, 0)
    def hide(self): hide_sprite(self)

# Treasure
class Treasure(turtle.Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.penup()
        self.speed(0)
        self.shape('gold.gif')
        self.name = 'Treasure'
        self.gold = 100
        self.goto(x, y)

    def hide(self): hide_sprite(self)

# Enemy
class Enemy(turtle.Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.penup()
        self.speed(0)
        self.name = 'Enemy'
        self.shape('enemy-right.gif')
        self.setposition(x, y)
        self.direction = set_direction()

    def change_direction(self):
        if not game_running:
            return

        dx, dy = 0, 0
        if self.direction == 'up': dy = 24
        elif self.direction == 'down': dy = -24
        elif self.direction == 'left': dx = -24; self.shape('enemy-left.gif')
        elif self.direction == 'right': dx = 24; self.shape('enemy-right.gif')

        if self.distance(player) < (difficulty * 100):
            if player.xcor() < self.xcor(): self.direction = 'left'
            elif player.xcor() > self.xcor(): self.direction = 'right'
            elif player.ycor() < self.ycor(): self.direction = 'down'
            elif player.ycor() > self.ycor(): self.direction = 'up'

        next_x = self.xcor() + dx
        next_y = self.ycor() + dy

        if (next_x, next_y) not in walls:
            self.setposition(next_x, next_y)
        else:
            self.direction = set_direction()

        wn.ontimer(self.change_direction, random.randint(200, 400))

    def hide(self): hide_sprite(self)

# Utility Functions
def hide_sprite(sprite):
    sprite.setposition(2000, 2000)
    sprite.hideturtle()

def set_direction():
    return random.choice(['up', 'down', 'left', 'right'])

def check_collision(sprite1, sprite2):
    global game_running
    if sprite1.distance(sprite2) < grid_block_size:
        if sprite2.name == 'Treasure':
            sprite1.gold += sprite2.gold
            sprite2.hide()
            treasures.remove(sprite2)
            if len(treasures) == 0:
                game_win()
        elif sprite2.name == 'Enemy':
            player.hide()
            game_over()

def display_message(message, color):
    global message_turtle
    if message_turtle:
        message_turtle.clear()
        message_turtle.hideturtle()
    message_turtle = turtle.Turtle()
    message_turtle.hideturtle()
    message_turtle.color(color)
    message_turtle.penup()
    message_turtle.goto(0, 0)
    message_turtle.write(message, align="center", font=("Arial", 24, "bold"))

# Restart & Exit Functions
def restart_game(x=None, y=None):
    global game_running, treasures, enemies, message_turtle, current_level

    if message_turtle:
        message_turtle.clear()
        message_turtle.hideturtle()

    restart_button.hideturtle()
    exit_button.hideturtle()
    next_level_button.hideturtle()

    for enemy in enemies:
        enemy.hide()
    for treasure in treasures:
        treasure.hide()
    for wall_pen in pen_walls:
        wall_pen.clear()
        wall_pen.hideturtle()

    enemies.clear()
    treasures.clear()
    walls.clear()
    pen_walls.clear()

    player.gold = 0
    player.showturtle()

    # Reset to Level 1
    current_level = 1
    setup_maze(level_1)

    for enemy in enemies:
        wn.ontimer(enemy.change_direction, 250)

    game_running = True

def exit_game(x=None, y=None):
    wn.bye()

def game_over():
    global game_running
    game_running = False
    display_message(f"Game Over! Score: {player.gold}", "red")

    restart_button.goto(0, -60)
    restart_button.showturtle()
    restart_button.onclick(restart_game)

    exit_button.goto(0, -120)
    exit_button.showturtle()
    exit_button.onclick(exit_game)

def game_win():
    global current_level, game_running, message_turtle

    if message_turtle:
        message_turtle.clear()
        message_turtle.hideturtle()

    game_running = False

    if current_level == 1:
        display_message("Level 1 Complete!", "green")
        next_level_button.goto(0, -60)
        next_level_button.showturtle()
        next_level_button.onclick(start_next_level)
    else:
        display_message(f"You Win! Final Score: {player.gold}", "green")

        # Show restart and exit buttons after completing level 2
        restart_button.goto(0, -60)
        restart_button.showturtle()
        restart_button.onclick(restart_game)

        exit_button.goto(0, -120)
        exit_button.showturtle()
        exit_button.onclick(exit_game)

def start_next_level(x=None, y=None):
    global current_level, game_running

    if message_turtle:
        message_turtle.clear()
        message_turtle.hideturtle()

    next_level_button.hideturtle()

    clear_level()
    current_level = 2
    setup_maze(level_2)

    for enemy in enemies:
        wn.ontimer(enemy.change_direction, 250)

    game_running = True

def clear_level():
    for t in treasures:
        t.hide()
    for e in enemies:
        e.hide()
    for wall_pen in pen_walls:
        wall_pen.clear()
        wall_pen.hideturtle()

    treasures.clear()
    enemies.clear()
    walls.clear()
    pen_walls.clear()

# Maze setup
def setup_maze(level):
    max_enemies = 2 if current_level == 1 else 4
    enemy_count = 0

    for y in range(len(level)):
        for x in range(len(level[y])):
            char = level[y][x]
            screen_x = -288 + (x * 24)
            screen_y = 288 - (y * 24)

            if char == 'X':
                pen = Pen(screen_x, screen_y)
                pen_walls.append(pen)
                walls.append((screen_x, screen_y))
            elif char == 'P':
                player.setposition(screen_x, screen_y)
            elif char == 'T':
                treasures.append(Treasure(screen_x, screen_y))
            elif char == 'E' and enemy_count < max_enemies:
                enemies.append(Enemy(screen_x, screen_y))
                enemy_count += 1

# Create objects
player = Player()

restart_button = turtle.Turtle()
restart_button.penup()
restart_button.hideturtle()
restart_button.shape("restart.gif")

exit_button = turtle.Turtle()
exit_button.penup()
exit_button.hideturtle()
exit_button.shape("exit.gif")

next_level_button = turtle.Turtle()
next_level_button.penup()
next_level_button.hideturtle()
next_level_button.shape("nextlevel.gif")  # <- New button

# Controls
wn.listen()
wn.onkeypress(player.move_up, "Up")
wn.onkeypress(player.move_down, "Down")
wn.onkeypress(player.move_left, "Left")
wn.onkeypress(player.move_right, "Right")

# Setup Level 1
setup_maze(level_1)

# Start enemy movement
for enemy in enemies:
    wn.ontimer(enemy.change_direction, 250)

# Main game loop
while True:
    if game_running:
        for treasure in treasures:
            check_collision(player, treasure)
        for enemy in enemies:
            check_collision(player, enemy)
        wn.update()
    else:
        wn.update()
