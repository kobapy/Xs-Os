import random
import sys
import time

# GameField
# u1|u2|u3
# m1|m2|m3
# l1|l2|l3

gameField = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
u1 = gameField[0][0]
u2 = gameField[0][1]
u3 = gameField[0][2]
m1 = gameField[1][0]
m2 = gameField[1][1]
m3 = gameField[1][2]
l1 = gameField[2][0]
l2 = gameField[2][1]
l3 = gameField[2][2]
crosses = "x"
noughts = "○"

# For judging input values
player_select_list = ["1", "2"]
point = 0
input_number_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
input_item = 0
turn_action_record = [0]
j = 0


def game_view():
    """Game Field Drawing

    Draw the game screen on the CLI.
    """
    print(u1, u2, u3)
    print(m1, m2, m3)
    print(l1, l2, l3)


def my_turn(my_point: int, player_turn: int):
    """Player Turn Action

    A function where the player selects a number, checks if the number is valid, 
    and then passes the value to the draw function.

    Args:
        my_point: An integer where to mark on the game field.
        player_turn: An integer indicating the first / second attack.
    """
    global j, input_item
    time.sleep(0.5)
    print("Your turn.")
    time.sleep(0.2)
    print("Please enter the place to put it from 1-9.")
    while my_point in turn_action_record:
        if j == 1:
            print("Already entered place.")
        input_item = input("> ")
        while input_item not in input_number_list:
            print("Please enter only numbers from 1 to 9.")
            input_item = input("> ")
        my_point = int(input_item)
        j = 1
    j = 0
    if my_point not in turn_action_record:
        turn_action_record.append(my_point)
        draw(my_point, player_turn)


def enemy_turn(enemy_point: int, player_turn: int):
    """Enemy Turn Action

    A function of game progress on the computer side.

    Args:
        enemy_point: An integer where to mark on the game field.
        player_turn: An integer indicating the first / second attack.
    """
    time.sleep(0.5)
    print("AI turn.")
    while enemy_point in turn_action_record:
        enemy_point = random.randint(1, 9)
    if enemy_point not in turn_action_record:
        turn_action_record.append(enemy_point)
        draw(enemy_point, player_turn)


def draw(point: int, player_turn: int):
    """Game Action

    Substitute x or ○ in the game field list.
    In addition, a victory judgment is made.

    Args:
        point: An integer where to mark on the game field.
        player_turn: An integer indicating the first / second attack.
    """
    global u1, u2, u3, m1, m2, m3, l1, l2, l3
    global item
    item = ""
    # Turn
    if player_turn == 0:
        item = crosses
    elif player_turn == 1:
        item = noughts
    # Game Parts Drawing
    if point == 1:
        u1 = item
    elif point == 2:
        u2 = item
    elif point == 3:
        u3 = item
    elif point == 4:
        m1 = item
    elif point == 5:
        m2 = item
    elif point == 6:
        m3 = item
    elif point == 7:
        l1 = item
    elif point == 8:
        l2 = item
    elif point == 9:
        l3 = item
    else:
        print("ERROR")
    game_view()
    # winning decision
    if u1 == u2 == u3 == item:
        win_judge(item)
    elif m1 == m2 == m3 == item:
        win_judge(item)
    elif l1 == l2 == l3 == item:
        win_judge(item)
    elif u1 == m1 == l1 == item:
        win_judge(item)
    elif u2 == m2 == l2 == item:
        win_judge(item)
    elif u3 == m3 == l3 == item:
        win_judge(item)
    elif u1 == m2 == l3 == item:
        win_judge(item)
    elif u3 == m2 == l1 == item:
        win_judge(item)


# WIN messages
def win_judge(item: str):
    """WIN messages

    Display a victory message and end the game.

    Args:
        item = A character string that stores x or ○.
    """
    time.sleep(0.5)
    if item == crosses:
        print("x WIN")
        sys.exit()
    elif item == noughts:
        print("○ WIN")
        sys.exit()


# Game Opening
print("Welcome to Tic-tac-toe!")
time.sleep(0.5)
input_item = input("Enter 1 for the first move and 2 for the second move:")
while input_item not in player_select_list:
    print("Please enter 1 or 2.")
    input_item = input("> ")
turn = int(input_item)
if turn == 1:
    print("You are the first player.")
elif turn == 2:
    print("You are the Second player.")
else:
    print("Please enter the valid value.")
    sys.exit()
print("1|2|3")
print("4|5|6")
print("7|8|9")
print("Enter the location and the corresponding number.")
time.sleep(1.0)
print("----------------")
game_view()

# Game progression
for i in range(1, 6):
    player_turn = 0
    time.sleep(0.5)
    print("TURN:" + str(i))
    if turn == 1:
        my_turn(point, player_turn)
    elif turn == 2:
        enemy_turn(point, player_turn)
    if i == 5:
        print("DRAW")
        sys.exit()
    player_turn = 1
    if turn == 1:
        enemy_turn(point, player_turn)
    elif turn == 2:
        my_turn(point, player_turn)
