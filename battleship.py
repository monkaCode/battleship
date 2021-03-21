# coding=utf8
import os
from random import randint
from playsound import playsound
import warnings

os.system("cls")
warnings.filterwarnings("ignore")

users = 0
colorUser1 = "User color aren't specified yet."
win = False
shipamount = 15
xaxisl = 1
xaxisr = 1
yaxisu = 1
yaxisd = 1

class Colors:
        GREEN = "\033[92m"
        BLUE = "\u001b[34;1m"
        RED = "\u001b[31;1m"
        CYAN = "\u001b[36;1m"
        YELLOW = "\u001b[33m"
        GRAY = "\033[90m"
        ENDC = "\033[0m"

class TypeOfMessage:
    Info = f"[{Colors.BLUE}INFO{Colors.ENDC}] "
    Error = f"[{Colors.RED}ERROR{Colors.ENDC}] "
    Input = f"[{Colors.YELLOW}INPUT{Colors.ENDC}] "
    Hit = f"[{Colors.GREEN}HIT{Colors.ENDC}] "
    NoHit = f"[{Colors.RED}NO HIT{Colors.ENDC}] "
    GameOver = f"[{Colors.YELLOW}GAME OVER{Colors.ENDC}] "


class User:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.ships = [[["███████", "███████", "███████"], ["███████", "███████", "███████"], ["███████", "███████", "███████"], ["███████", "███████", "███████"], ["███████", "███████", "███████"], ["███████", "███████", "███████"], ["███████", "███████", "███████"], ["███████", "███████", "███████"]], [["███████", "███████", "███████"], ["███████", "███████", "███████"], ["███████", "███████", "███████"], ["███████", "███████", "███████"], ["███████", "███████", "███████"], ["███████", "███████", "███████"], ["███████", "███████", "███████"], ["███████", "███████", "███████"]], [["███████", "███████", "███████"], ["███████", "███████", "███████"], ["███████", "███████", "███████"], ["███████", "███████", "███████"], ["███████", "███████", "███████"], ["███████", "███████", "███████"], ["███████", "███████", "███████"], ["███████", "███████", "███████"]], [["███████", "███████", "███████"], ["███████", "███████", "███████"], ["███████", "███████", "███████"], ["███████", "███████", "███████"], ["███████", "███████", "███████"], ["███████", "███████", "███████"], ["███████", "███████", "███████"], ["███████", "███████", "███████"]], [["███████", "███████", "███████"], ["███████", "███████", "███████"], ["███████", "███████", "███████"], ["███████", "███████", "███████"], ["███████", "███████", "███████"], ["███████", "███████", "███████"], ["███████", "███████", "███████"], ["███████", "███████", "███████"]], [["███████", "███████", "███████"], ["███████", "███████", "███████"], ["███████", "███████", "███████"], ["███████", "███████", "███████"], ["███████", "███████", "███████"], ["███████", "███████", "███████"], ["███████", "███████", "███████"], ["███████", "███████", "███████"]], [["███████", "███████", "███████"], ["███████", "███████", "███████"], ["███████", "███████", "███████"], ["███████", "███████", "███████"], ["███████", "███████", "███████"], ["███████", "███████", "███████"], ["███████", "███████", "███████"], ["███████", "███████", "███████"]], [["███████", "███████", "███████"], ["███████", "███████", "███████"], ["███████", "███████", "███████"], ["███████", "███████", "███████"], ["███████", "███████", "███████"], ["███████", "███████", "███████"], ["███████", "███████", "███████"], ["███████", "███████", "███████"]]]
        self.playground = [[["███████", "███████", "███████"], ["███████", "███████", "███████"], ["███████", "███████", "███████"], ["███████", "███████", "███████"], ["███████", "███████", "███████"], ["███████", "███████", "███████"], ["███████", "███████", "███████"], ["███████", "███████", "███████"]], [["███████", "███████", "███████"], ["███████", "███████", "███████"], ["███████", "███████", "███████"], ["███████", "███████", "███████"], ["███████", "███████", "███████"], ["███████", "███████", "███████"], ["███████", "███████", "███████"], ["███████", "███████", "███████"]], [["███████", "███████", "███████"], ["███████", "███████", "███████"], ["███████", "███████", "███████"], ["███████", "███████", "███████"], ["███████", "███████", "███████"], ["███████", "███████", "███████"], ["███████", "███████", "███████"], ["███████", "███████", "███████"]], [["███████", "███████", "███████"], ["███████", "███████", "███████"], ["███████", "███████", "███████"], ["███████", "███████", "███████"], ["███████", "███████", "███████"], ["███████", "███████", "███████"], ["███████", "███████", "███████"], ["███████", "███████", "███████"]], [["███████", "███████", "███████"], ["███████", "███████", "███████"], ["███████", "███████", "███████"], ["███████", "███████", "███████"], ["███████", "███████", "███████"], ["███████", "███████", "███████"], ["███████", "███████", "███████"], ["███████", "███████", "███████"]], [["███████", "███████", "███████"], ["███████", "███████", "███████"], ["███████", "███████", "███████"], ["███████", "███████", "███████"], ["███████", "███████", "███████"], ["███████", "███████", "███████"], ["███████", "███████", "███████"], ["███████", "███████", "███████"]], [["███████", "███████", "███████"], ["███████", "███████", "███████"], ["███████", "███████", "███████"], ["███████", "███████", "███████"], ["███████", "███████", "███████"], ["███████", "███████", "███████"], ["███████", "███████", "███████"], ["███████", "███████", "███████"]], [["███████", "███████", "███████"], ["███████", "███████", "███████"], ["███████", "███████", "███████"], ["███████", "███████", "███████"], ["███████", "███████", "███████"], ["███████", "███████", "███████"], ["███████", "███████", "███████"], ["███████", "███████", "███████"]]]
        self.shipsalive = shipamount

print(f"┌────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐")
print(f"│ {Colors.BLUE}██████╗        ████╗    ████████████╗ ████████████╗ ██╗        ████████╗{Colors.RED}   ████████╗ ██╗     ██╗ ██╗ ███████╗ {Colors.ENDC} │")
print(f"│ {Colors.BLUE}██╔══██╗      ██╔═██╗        ██╔════╝      ██╔════╝ ██║        ██╔═════╝{Colors.RED}  ███╔═════╝ ██║     ██║ ██║ ██╔═══██╗{Colors.ENDC} │")
print(f"│ {Colors.BLUE}██║   ██╗    ██╔╝  ██╗       ██║           ██║      ██║        ██║      {Colors.RED} ███╔╝       ██║     ██║ ██║ ██║   ██║{Colors.ENDC} │")
print(f"│ {Colors.BLUE}███████╔╝    ████████║       ██║           ██║      ██║        ██████╗  {Colors.RED}  ██████╗    ██████████║ ██║ ███████╔╝{Colors.ENDC} │")
print(f"│ {Colors.BLUE}██╔═══██╗   ██╔═════██╗      ██║           ██║      ██║        ██╔═══╝  {Colors.RED}      ████╗  ██╔═════██║ ██║ ██╔════╝ {Colors.ENDC} │")
print(f"│ {Colors.BLUE}██║  ██╔╝   ██║     ██║      ██║           ██║      ██║        ██║      {Colors.RED}        ███╗ ██║     ██║ ██║ ██║      {Colors.ENDC} │")
print(f"│ {Colors.BLUE}██████╔╝   ██╔╝      ██╗     ██║           ██║      █████████╗ ████████╗{Colors.RED} █████████╔╝ ██║     ██║ ██║ ██║      {Colors.ENDC} │")
print(f"│ {Colors.BLUE}╚═════╝    ╚═╝       ╚═╝     ╚═╝           ╚═╝      ╚════════╝ ╚═══════╝{Colors.RED} ╚════════╝  ╚═╝     ╚═╝ ╚═╝ ╚═╝      {Colors.ENDC} │")
print(f"└────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘\n")


u1 = User("", "")
u2 = User("", "")

def createUser():
    try:
        name = input(f"{TypeOfMessage.Input}Type in your name: ")
    except:
        print(f"{TypeOfMessage.Error}An error occured. Please try it again.")
        createUser()
        return
    
    def UC():
        colorInput = input(f"{TypeOfMessage.Input}Type in your favorite color ({Colors.GREEN}██ green{Colors.ENDC}, {Colors.BLUE}██ blue{Colors.ENDC}, {Colors.RED}██ red{Colors.ENDC}, {Colors.YELLOW}██ yellow{Colors.ENDC}, {Colors.CYAN}██ cyan{Colors.ENDC}): ").lower()
        global users
        global colorUser1
        if users == 0:
            colorUser1 = colorInput
        elif colorInput == colorUser1:
            print(f"{TypeOfMessage.Error}Your Opponent has already picked this color.")
            UC()
            return
        if colorInput == "green":
            UC.color = Colors.GREEN
            users += 1
        elif colorInput == "blue":
            UC.color = Colors.BLUE
            users += 1
        elif colorInput == "red":
            UC.color = Colors.RED
            users += 1
        elif colorInput == "yellow":
            UC.color = Colors.YELLOW
            users += 1
        elif colorInput == "cyan":
            UC.color = Colors.CYAN
            users += 1
        else:
            print(f"{TypeOfMessage.Error}You must type one of these colors: ")
            UC()
            return
    UC()
    if users == 1:
        global u1
        u1 = User(name, UC.color)
        print(f"{TypeOfMessage.Info}User {u1.color}{u1.name}{Colors.ENDC} was created.\n")
    elif users == 2:
        global u2
        u2 = User(name, UC.color)
        print(f"{TypeOfMessage.Info}User {u2.color}{u2.name}{Colors.ENDC} was created.\n")
    

createUser()
createUser()

input(f"{TypeOfMessage.Info}Press ENTER to start the game...")

os.system("cls")

def createShip(user, error):

    os.system("cls")

    print()
    print()
    print()
    print(f"        ┌───────────────────────────────────────────────────────────────────────────────┐")
    print(f"        │         1        2        3        4        5        6        7        8      │")
    print(f"        │                                                                               │")
    print(f"        │      {user.ships[0][0][0]}  {user.ships[0][1][0]}  {user.ships[0][2][0]}  {user.ships[0][3][0]}  {user.ships[0][4][0]}  {user.ships[0][5][0]}  {user.ships[0][6][0]}  {user.ships[0][7][0]}   │")
    print(f"        │  A   {user.ships[0][0][1]}  {user.ships[0][1][1]}  {user.ships[0][2][1]}  {user.ships[0][3][1]}  {user.ships[0][4][1]}  {user.ships[0][5][1]}  {user.ships[0][6][1]}  {user.ships[0][7][1]}   │")
    print(f"        │      {user.ships[0][0][2]}  {user.ships[0][1][2]}  {user.ships[0][2][2]}  {user.ships[0][3][2]}  {user.ships[0][4][2]}  {user.ships[0][5][2]}  {user.ships[0][6][2]}  {user.ships[0][7][2]}   │")
    print(f"        │                                                                               │")
    print(f"        │      {user.ships[1][0][0]}  {user.ships[1][1][0]}  {user.ships[1][2][0]}  {user.ships[1][3][0]}  {user.ships[1][4][0]}  {user.ships[1][5][0]}  {user.ships[1][6][0]}  {user.ships[1][7][0]}   │")
    print(f"        │  B   {user.ships[1][0][1]}  {user.ships[1][1][1]}  {user.ships[1][2][1]}  {user.ships[1][3][1]}  {user.ships[1][4][1]}  {user.ships[1][5][1]}  {user.ships[1][6][1]}  {user.ships[1][7][1]}   │")
    print(f"        │      {user.ships[1][0][2]}  {user.ships[1][1][2]}  {user.ships[1][2][2]}  {user.ships[1][3][2]}  {user.ships[1][4][2]}  {user.ships[1][5][2]}  {user.ships[1][6][2]}  {user.ships[1][7][2]}   │")
    print(f"        │                                                                               │")
    print(f"        │      {user.ships[2][0][0]}  {user.ships[2][1][0]}  {user.ships[2][2][0]}  {user.ships[2][3][0]}  {user.ships[2][4][0]}  {user.ships[2][5][0]}  {user.ships[2][6][0]}  {user.ships[2][7][0]}   │") 
    print(f"        │  C   {user.ships[2][0][1]}  {user.ships[2][1][1]}  {user.ships[2][2][1]}  {user.ships[2][3][1]}  {user.ships[2][4][1]}  {user.ships[2][5][1]}  {user.ships[2][6][1]}  {user.ships[2][7][1]}   │")
    print(f"        │      {user.ships[2][0][2]}  {user.ships[2][1][2]}  {user.ships[2][2][2]}  {user.ships[2][3][2]}  {user.ships[2][4][2]}  {user.ships[2][5][2]}  {user.ships[2][6][2]}  {user.ships[2][7][2]}   │")
    print(f"        │                                                                               │")
    print(f"        │      {user.ships[3][0][0]}  {user.ships[3][1][0]}  {user.ships[3][2][0]}  {user.ships[3][3][0]}  {user.ships[3][4][0]}  {user.ships[3][5][0]}  {user.ships[3][6][0]}  {user.ships[3][7][0]}   │")
    print(f"        │  D   {user.ships[3][0][1]}  {user.ships[3][1][1]}  {user.ships[3][2][1]}  {user.ships[3][3][1]}  {user.ships[3][4][1]}  {user.ships[3][5][1]}  {user.ships[3][6][1]}  {user.ships[3][7][1]}   │")
    print(f"        │      {user.ships[3][0][2]}  {user.ships[3][1][2]}  {user.ships[3][2][2]}  {user.ships[3][3][2]}  {user.ships[3][4][2]}  {user.ships[3][5][2]}  {user.ships[3][6][2]}  {user.ships[3][7][2]}   │")
    print(f"        │                                                                               │")
    print(f"        │      {user.ships[4][0][0]}  {user.ships[4][1][0]}  {user.ships[4][2][0]}  {user.ships[4][3][0]}  {user.ships[4][4][0]}  {user.ships[4][5][0]}  {user.ships[4][6][0]}  {user.ships[4][7][0]}   │")
    print(f"        │  E   {user.ships[4][0][1]}  {user.ships[4][1][1]}  {user.ships[4][2][1]}  {user.ships[4][3][1]}  {user.ships[4][4][1]}  {user.ships[4][5][1]}  {user.ships[4][6][1]}  {user.ships[4][7][1]}   │")
    print(f"        │      {user.ships[4][0][2]}  {user.ships[4][1][2]}  {user.ships[4][2][2]}  {user.ships[4][3][2]}  {user.ships[4][4][2]}  {user.ships[4][5][2]}  {user.ships[4][6][2]}  {user.ships[4][7][2]}   │")
    print(f"        │                                                                               │")
    print(f"        │      {user.ships[5][0][0]}  {user.ships[5][1][0]}  {user.ships[5][2][0]}  {user.ships[5][3][0]}  {user.ships[5][4][0]}  {user.ships[5][5][0]}  {user.ships[5][6][0]}  {user.ships[5][7][0]}   │")
    print(f"        │  F   {user.ships[5][0][1]}  {user.ships[5][1][1]}  {user.ships[5][2][1]}  {user.ships[5][3][1]}  {user.ships[5][4][1]}  {user.ships[5][5][1]}  {user.ships[5][6][1]}  {user.ships[5][7][1]}   │")
    print(f"        │      {user.ships[5][0][2]}  {user.ships[5][1][2]}  {user.ships[5][2][2]}  {user.ships[5][3][2]}  {user.ships[5][4][2]}  {user.ships[5][5][2]}  {user.ships[5][6][2]}  {user.ships[5][7][2]}   │")
    print(f"        │                                                                               │")
    print(f"        │      {user.ships[6][0][0]}  {user.ships[6][1][0]}  {user.ships[6][2][0]}  {user.ships[6][3][0]}  {user.ships[6][4][0]}  {user.ships[6][5][0]}  {user.ships[6][6][0]}  {user.ships[6][7][0]}   │")
    print(f"        │  G   {user.ships[6][0][1]}  {user.ships[6][1][1]}  {user.ships[6][2][1]}  {user.ships[6][3][1]}  {user.ships[6][4][1]}  {user.ships[6][5][1]}  {user.ships[6][6][1]}  {user.ships[6][7][1]}   │")
    print(f"        │      {user.ships[6][0][2]}  {user.ships[6][1][2]}  {user.ships[6][2][2]}  {user.ships[6][3][2]}  {user.ships[6][4][2]}  {user.ships[6][5][2]}  {user.ships[6][6][2]}  {user.ships[6][7][2]}   │")
    print(f"        │                                                                               │")
    print(f"        │      {user.ships[7][0][0]}  {user.ships[7][1][0]}  {user.ships[7][2][0]}  {user.ships[7][3][0]}  {user.ships[7][4][0]}  {user.ships[7][5][0]}  {user.ships[7][6][0]}  {user.ships[7][7][0]}   │")
    print(f"        │  H   {user.ships[7][0][1]}  {user.ships[7][1][1]}  {user.ships[7][2][1]}  {user.ships[7][3][1]}  {user.ships[7][4][1]}  {user.ships[7][5][1]}  {user.ships[7][6][1]}  {user.ships[7][7][1]}   │")
    print(f"        │      {user.ships[7][0][2]}  {user.ships[7][1][2]}  {user.ships[7][2][2]}  {user.ships[7][3][2]}  {user.ships[7][4][2]}  {user.ships[7][5][2]}  {user.ships[7][6][2]}  {user.ships[7][7][2]}   │")
    print(f"        │                                                                               │")
    print(f"        └───────────────────────────────────────────────────────────────────────────────┘\n\n\n")

    print(error)

    global newShipPlace
    newShip = input(f"{TypeOfMessage.Input}Create a ship: ").lower()
    if len(newShip) != 2:
        createShip(user, f"{TypeOfMessage.Error}Incorrect Input. Try something like D{randint(1,8)} or H{randint(1,8)}.")
        return
    nSl = newShip[0]
    try:
        nSn = int(newShip[1])
    except:
        createShip(user, f"{TypeOfMessage.Error}Incorrect Input. Try something like D{randint(1,8)} or H{randint(1,8)}.")
        return
    if nSn > 8:
        createShip(user, f"{TypeOfMessage.Error}The number of the ship must be from 1-8.")
        return
    if nSl == "a":
        if user.ships[0][nSn-1][0] == f"{user.color}█  █  █{Colors.ENDC}":
            createShip(user,f"{TypeOfMessage.Error}You have already placed a ship on this field.")
            return
        else:
            yd = 1
            yu = 1
            xl = 1
            xr = 1
            newShipPlace = [0, nSn-1]
            if newShipPlace[0] == 0:
                yd = 0
            elif newShipPlace[0] == 7:
                yu = 0
            if newShipPlace[1] == 0:
                xl = 0
            elif newShipPlace[1] == 7:
                xr = 0
            if user.ships[newShipPlace[0]-yd][newShipPlace[1]][0] == f"{user.color}█  █  █{Colors.ENDC}" or user.ships[newShipPlace[0]+yu][newShipPlace[1]][0] == f"{user.color}█  █  █{Colors.ENDC}" or user.ships[newShipPlace[0]][newShipPlace[1]-xl][0] == f"{user.color}█  █  █{Colors.ENDC}" or user.ships[newShipPlace[0]][newShipPlace[1]+xr][0] == f"{user.color}█  █  █{Colors.ENDC}":
                createShip(user,f"{TypeOfMessage.Error}This ship is too close to an another one.")
                return
            else:
                user.ships[0][nSn-1][0] = f"{user.color}█  █  █{Colors.ENDC}"
                user.ships[0][nSn-1][1] = f"{user.color}███████{Colors.ENDC}"
                user.ships[0][nSn-1][2] = f"{user.color} █████ {Colors.ENDC}"
    elif nSl == "b":
        if user.ships[1][nSn-1][0] == f"{user.color}█  █  █{Colors.ENDC}":
            createShip(user, f"{TypeOfMessage.Error}You have already placed a ship on this field.")
            return
        else:
            yd = 1
            yu = 1
            xl = 1
            xr = 1
            newShipPlace = [1, nSn-1]
            if newShipPlace[0] == 0:
                yd = 0
            elif newShipPlace[0] == 7:
                yu = 0
            if newShipPlace[1] == 0:
                xl = 0
            elif newShipPlace[1] == 7:
                xr = 0
            if user.ships[newShipPlace[0]-yd][newShipPlace[1]][0] == f"{user.color}█  █  █{Colors.ENDC}" or user.ships[newShipPlace[0]+yu][newShipPlace[1]][0] == f"{user.color}█  █  █{Colors.ENDC}" or user.ships[newShipPlace[0]][newShipPlace[1]-xl][0] == f"{user.color}█  █  █{Colors.ENDC}" or user.ships[newShipPlace[0]][newShipPlace[1]+xr][0] == f"{user.color}█  █  █{Colors.ENDC}":
                createShip(user,f"{TypeOfMessage.Error}This ship is too close to an another one.")
                return
            else:
                user.ships[1][nSn-1][0] = f"{user.color}█  █  █{Colors.ENDC}"
                user.ships[1][nSn-1][1] = f"{user.color}███████{Colors.ENDC}"
                user.ships[1][nSn-1][2] = f"{user.color} █████ {Colors.ENDC}"
    elif nSl == "c":
        if user.ships[2][nSn-1][0] == f"{user.color}█  █  █{Colors.ENDC}":
            createShip(user, f"{TypeOfMessage.Error}You have already placed a ship on this field.")
            return
        else:
            yd = 1
            yu = 1
            xl = 1
            xr = 1
            newShipPlace = [2, nSn-1]
            if newShipPlace[0] == 0:
                yd = 0
            elif newShipPlace[0] == 7:
                yu = 0
            if newShipPlace[1] == 0:
                xl = 0
            elif newShipPlace[1] == 7:
                xr = 0
            if user.ships[newShipPlace[0]-yd][newShipPlace[1]][0] == f"{user.color}█  █  █{Colors.ENDC}" or user.ships[newShipPlace[0]+yu][newShipPlace[1]][0] == f"{user.color}█  █  █{Colors.ENDC}" or user.ships[newShipPlace[0]][newShipPlace[1]-xl][0] == f"{user.color}█  █  █{Colors.ENDC}" or user.ships[newShipPlace[0]][newShipPlace[1]+xr][0] == f"{user.color}█  █  █{Colors.ENDC}":
                createShip(user,f"{TypeOfMessage.Error}This ship is too close to an another one.")
                return
            else:
                user.ships[2][nSn-1][0] = f"{user.color}█  █  █{Colors.ENDC}"
                user.ships[2][nSn-1][1] = f"{user.color}███████{Colors.ENDC}"
                user.ships[2][nSn-1][2] = f"{user.color} █████ {Colors.ENDC}"
    elif nSl == "d":
        if user.ships[3][nSn-1][0] == f"{user.color}█  █  █{Colors.ENDC}":
            createShip(user, f"{TypeOfMessage.Error}You have already placed a ship on this field.")
            return
        else:
            yd = 1
            yu = 1
            xl = 1
            xr = 1
            newShipPlace = [3, nSn-1]
            if newShipPlace[0] == 0:
                yd = 0
            elif newShipPlace[0] == 7:
                yu = 0
            if newShipPlace[1] == 0:
                xl = 0
            elif newShipPlace[1] == 7:
                xr = 0
            if user.ships[newShipPlace[0]-yd][newShipPlace[1]][0] == f"{user.color}█  █  █{Colors.ENDC}" or user.ships[newShipPlace[0]+yu][newShipPlace[1]][0] == f"{user.color}█  █  █{Colors.ENDC}" or user.ships[newShipPlace[0]][newShipPlace[1]-xl][0] == f"{user.color}█  █  █{Colors.ENDC}" or user.ships[newShipPlace[0]][newShipPlace[1]+xr][0] == f"{user.color}█  █  █{Colors.ENDC}":
                createShip(user,f"{TypeOfMessage.Error}This ship is too close to an another one.")
                return
            else:
                user.ships[3][nSn-1][0] = f"{user.color}█  █  █{Colors.ENDC}"
                user.ships[3][nSn-1][1] = f"{user.color}███████{Colors.ENDC}"
                user.ships[3][nSn-1][2] = f"{user.color} █████ {Colors.ENDC}"
    elif nSl == "e":
        if user.ships[4][nSn-1][0] == f"{user.color}█  █  █{Colors.ENDC}":
            createShip(user, f"{TypeOfMessage.Error}You have already placed a ship on this field.")
            return
        else:
            yd = 1
            yu = 1
            xl = 1
            xr = 1
            newShipPlace = [4, nSn-1]
            if newShipPlace[0] == 0:
                yd = 0
            elif newShipPlace[0] == 7:
                yu = 0
            if newShipPlace[1] == 0:
                xl = 0
            elif newShipPlace[1] == 7:
                xr = 0
            if user.ships[newShipPlace[0]-yd][newShipPlace[1]][0] == f"{user.color}█  █  █{Colors.ENDC}" or user.ships[newShipPlace[0]+yu][newShipPlace[1]][0] == f"{user.color}█  █  █{Colors.ENDC}" or user.ships[newShipPlace[0]][newShipPlace[1]-xl][0] == f"{user.color}█  █  █{Colors.ENDC}" or user.ships[newShipPlace[0]][newShipPlace[1]+xr][0] == f"{user.color}█  █  █{Colors.ENDC}":
                createShip(user,f"{TypeOfMessage.Error}This ship is too close to an another one.")
                return
            else:
                user.ships[4][nSn-1][0] = f"{user.color}█  █  █{Colors.ENDC}"
                user.ships[4][nSn-1][1] = f"{user.color}███████{Colors.ENDC}"
                user.ships[4][nSn-1][2] = f"{user.color} █████ {Colors.ENDC}"
    elif nSl == "f":
        if user.ships[5][nSn-1][0] == f"{user.color}█  █  █{Colors.ENDC}":
            createShip(user, f"{TypeOfMessage.Error}You have already placed a ship on this field.")
            return
        else:
            yd = 1
            yu = 1
            xl = 1
            xr = 1
            newShipPlace = [5, nSn-1]
            if newShipPlace[0] == 0:
                yd = 0
            elif newShipPlace[0] == 7:
                yu = 0
            if newShipPlace[1] == 0:
                xl = 0
            elif newShipPlace[1] == 7:
                xr = 0
            if user.ships[newShipPlace[0]-yd][newShipPlace[1]][0] == f"{user.color}█  █  █{Colors.ENDC}" or user.ships[newShipPlace[0]+yu][newShipPlace[1]][0] == f"{user.color}█  █  █{Colors.ENDC}" or user.ships[newShipPlace[0]][newShipPlace[1]-xl][0] == f"{user.color}█  █  █{Colors.ENDC}" or user.ships[newShipPlace[0]][newShipPlace[1]+xr][0] == f"{user.color}█  █  █{Colors.ENDC}":
                createShip(user,f"{TypeOfMessage.Error}This ship is too close to an another one.")
                return
            else:
                user.ships[5][nSn-1][0] = f"{user.color}█  █  █{Colors.ENDC}"
                user.ships[5][nSn-1][1] = f"{user.color}███████{Colors.ENDC}"
                user.ships[5][nSn-1][2] = f"{user.color} █████ {Colors.ENDC}"
    elif nSl == "g":
        if user.ships[6][nSn-1][0] == f"{user.color}█  █  █{Colors.ENDC}":
            createShip(user, f"{TypeOfMessage.Error}You have already placed a ship on this field.")
            return
        else:
            yd = 1
            yu = 1
            xl = 1
            xr = 1
            newShipPlace = [6, nSn-1]
            if newShipPlace[0] == 0:
                yd = 0
            elif newShipPlace[0] == 7:
                yu = 0
            if newShipPlace[1] == 0:
                xl = 0
            elif newShipPlace[1] == 7:
                xr = 0
            if user.ships[newShipPlace[0]-yd][newShipPlace[1]][0] == f"{user.color}█  █  █{Colors.ENDC}" or user.ships[newShipPlace[0]+yu][newShipPlace[1]][0] == f"{user.color}█  █  █{Colors.ENDC}" or user.ships[newShipPlace[0]][newShipPlace[1]-xl][0] == f"{user.color}█  █  █{Colors.ENDC}" or user.ships[newShipPlace[0]][newShipPlace[1]+xr][0] == f"{user.color}█  █  █{Colors.ENDC}":
                createShip(user,f"{TypeOfMessage.Error}This ship is too close to an another one.")
                return
            else:
                user.ships[6][nSn-1][0] = f"{user.color}█  █  █{Colors.ENDC}"
                user.ships[6][nSn-1][1] = f"{user.color}███████{Colors.ENDC}"
                user.ships[6][nSn-1][2] = f"{user.color} █████ {Colors.ENDC}"
    elif nSl == "h":
        if user.ships[7][nSn-1][0] == f"{user.color}█  █  █{Colors.ENDC}":
            createShip(user, f"{TypeOfMessage.Error}You have already placed a ship on this field.")
            return
        else:
            yd = 1
            yu = 1
            xl = 1
            xr = 1
            newShipPlace = [7, nSn-1]
            if newShipPlace[0] == 0:
                yd = 0
            elif newShipPlace[0] == 7:
                yu = 0
            if newShipPlace[1] == 0:
                xl = 0
            elif newShipPlace[1] == 7:
                xr = 0
            if user.ships[newShipPlace[0]-yd][newShipPlace[1]][0] == f"{user.color}█  █  █{Colors.ENDC}" or user.ships[newShipPlace[0]+yu][newShipPlace[1]][0] == f"{user.color}█  █  █{Colors.ENDC}" or user.ships[newShipPlace[0]][newShipPlace[1]-xl][0] == f"{user.color}█  █  █{Colors.ENDC}" or user.ships[newShipPlace[0]][newShipPlace[1]+xr][0] == f"{user.color}█  █  █{Colors.ENDC}":
                createShip(user,f"{TypeOfMessage.Error}This ship is too close to an another one.")
                return
            else:
                user.ships[7][nSn-1][0] = f"{user.color}█  █  █{Colors.ENDC}"
                user.ships[7][nSn-1][1] = f"{user.color}███████{Colors.ENDC}"
                user.ships[7][nSn-1][2] = f"{user.color} █████ {Colors.ENDC}"
    else:
        createShip(user, f"{TypeOfMessage.Error}The letter of the ship must be from A-H.")
        return

def createShipPart(user, error, xl, xr, yu, yd):
    os.system("cls")

    print()
    print()
    print()
    print(f"        ┌───────────────────────────────────────────────────────────────────────────────┐")
    print(f"        │         1        2        3        4        5        6        7        8      │")
    print(f"        │                                                                               │")
    print(f"        │      {user.ships[0][0][0]}  {user.ships[0][1][0]}  {user.ships[0][2][0]}  {user.ships[0][3][0]}  {user.ships[0][4][0]}  {user.ships[0][5][0]}  {user.ships[0][6][0]}  {user.ships[0][7][0]}   │")
    print(f"        │  A   {user.ships[0][0][1]}  {user.ships[0][1][1]}  {user.ships[0][2][1]}  {user.ships[0][3][1]}  {user.ships[0][4][1]}  {user.ships[0][5][1]}  {user.ships[0][6][1]}  {user.ships[0][7][1]}   │")
    print(f"        │      {user.ships[0][0][2]}  {user.ships[0][1][2]}  {user.ships[0][2][2]}  {user.ships[0][3][2]}  {user.ships[0][4][2]}  {user.ships[0][5][2]}  {user.ships[0][6][2]}  {user.ships[0][7][2]}   │")
    print(f"        │                                                                               │")
    print(f"        │      {user.ships[1][0][0]}  {user.ships[1][1][0]}  {user.ships[1][2][0]}  {user.ships[1][3][0]}  {user.ships[1][4][0]}  {user.ships[1][5][0]}  {user.ships[1][6][0]}  {user.ships[1][7][0]}   │")
    print(f"        │  B   {user.ships[1][0][1]}  {user.ships[1][1][1]}  {user.ships[1][2][1]}  {user.ships[1][3][1]}  {user.ships[1][4][1]}  {user.ships[1][5][1]}  {user.ships[1][6][1]}  {user.ships[1][7][1]}   │")
    print(f"        │      {user.ships[1][0][2]}  {user.ships[1][1][2]}  {user.ships[1][2][2]}  {user.ships[1][3][2]}  {user.ships[1][4][2]}  {user.ships[1][5][2]}  {user.ships[1][6][2]}  {user.ships[1][7][2]}   │")
    print(f"        │                                                                               │")
    print(f"        │      {user.ships[2][0][0]}  {user.ships[2][1][0]}  {user.ships[2][2][0]}  {user.ships[2][3][0]}  {user.ships[2][4][0]}  {user.ships[2][5][0]}  {user.ships[2][6][0]}  {user.ships[2][7][0]}   │") 
    print(f"        │  C   {user.ships[2][0][1]}  {user.ships[2][1][1]}  {user.ships[2][2][1]}  {user.ships[2][3][1]}  {user.ships[2][4][1]}  {user.ships[2][5][1]}  {user.ships[2][6][1]}  {user.ships[2][7][1]}   │")
    print(f"        │      {user.ships[2][0][2]}  {user.ships[2][1][2]}  {user.ships[2][2][2]}  {user.ships[2][3][2]}  {user.ships[2][4][2]}  {user.ships[2][5][2]}  {user.ships[2][6][2]}  {user.ships[2][7][2]}   │")
    print(f"        │                                                                               │")
    print(f"        │      {user.ships[3][0][0]}  {user.ships[3][1][0]}  {user.ships[3][2][0]}  {user.ships[3][3][0]}  {user.ships[3][4][0]}  {user.ships[3][5][0]}  {user.ships[3][6][0]}  {user.ships[3][7][0]}   │")
    print(f"        │  D   {user.ships[3][0][1]}  {user.ships[3][1][1]}  {user.ships[3][2][1]}  {user.ships[3][3][1]}  {user.ships[3][4][1]}  {user.ships[3][5][1]}  {user.ships[3][6][1]}  {user.ships[3][7][1]}   │")
    print(f"        │      {user.ships[3][0][2]}  {user.ships[3][1][2]}  {user.ships[3][2][2]}  {user.ships[3][3][2]}  {user.ships[3][4][2]}  {user.ships[3][5][2]}  {user.ships[3][6][2]}  {user.ships[3][7][2]}   │")
    print(f"        │                                                                               │")
    print(f"        │      {user.ships[4][0][0]}  {user.ships[4][1][0]}  {user.ships[4][2][0]}  {user.ships[4][3][0]}  {user.ships[4][4][0]}  {user.ships[4][5][0]}  {user.ships[4][6][0]}  {user.ships[4][7][0]}   │")
    print(f"        │  E   {user.ships[4][0][1]}  {user.ships[4][1][1]}  {user.ships[4][2][1]}  {user.ships[4][3][1]}  {user.ships[4][4][1]}  {user.ships[4][5][1]}  {user.ships[4][6][1]}  {user.ships[4][7][1]}   │")
    print(f"        │      {user.ships[4][0][2]}  {user.ships[4][1][2]}  {user.ships[4][2][2]}  {user.ships[4][3][2]}  {user.ships[4][4][2]}  {user.ships[4][5][2]}  {user.ships[4][6][2]}  {user.ships[4][7][2]}   │")
    print(f"        │                                                                               │")
    print(f"        │      {user.ships[5][0][0]}  {user.ships[5][1][0]}  {user.ships[5][2][0]}  {user.ships[5][3][0]}  {user.ships[5][4][0]}  {user.ships[5][5][0]}  {user.ships[5][6][0]}  {user.ships[5][7][0]}   │")
    print(f"        │  F   {user.ships[5][0][1]}  {user.ships[5][1][1]}  {user.ships[5][2][1]}  {user.ships[5][3][1]}  {user.ships[5][4][1]}  {user.ships[5][5][1]}  {user.ships[5][6][1]}  {user.ships[5][7][1]}   │")
    print(f"        │      {user.ships[5][0][2]}  {user.ships[5][1][2]}  {user.ships[5][2][2]}  {user.ships[5][3][2]}  {user.ships[5][4][2]}  {user.ships[5][5][2]}  {user.ships[5][6][2]}  {user.ships[5][7][2]}   │")
    print(f"        │                                                                               │")
    print(f"        │      {user.ships[6][0][0]}  {user.ships[6][1][0]}  {user.ships[6][2][0]}  {user.ships[6][3][0]}  {user.ships[6][4][0]}  {user.ships[6][5][0]}  {user.ships[6][6][0]}  {user.ships[6][7][0]}   │")
    print(f"        │  G   {user.ships[6][0][1]}  {user.ships[6][1][1]}  {user.ships[6][2][1]}  {user.ships[6][3][1]}  {user.ships[6][4][1]}  {user.ships[6][5][1]}  {user.ships[6][6][1]}  {user.ships[6][7][1]}   │")
    print(f"        │      {user.ships[6][0][2]}  {user.ships[6][1][2]}  {user.ships[6][2][2]}  {user.ships[6][3][2]}  {user.ships[6][4][2]}  {user.ships[6][5][2]}  {user.ships[6][6][2]}  {user.ships[6][7][2]}   │")
    print(f"        │                                                                               │")
    print(f"        │      {user.ships[7][0][0]}  {user.ships[7][1][0]}  {user.ships[7][2][0]}  {user.ships[7][3][0]}  {user.ships[7][4][0]}  {user.ships[7][5][0]}  {user.ships[7][6][0]}  {user.ships[7][7][0]}   │")
    print(f"        │  H   {user.ships[7][0][1]}  {user.ships[7][1][1]}  {user.ships[7][2][1]}  {user.ships[7][3][1]}  {user.ships[7][4][1]}  {user.ships[7][5][1]}  {user.ships[7][6][1]}  {user.ships[7][7][1]}   │")
    print(f"        │      {user.ships[7][0][2]}  {user.ships[7][1][2]}  {user.ships[7][2][2]}  {user.ships[7][3][2]}  {user.ships[7][4][2]}  {user.ships[7][5][2]}  {user.ships[7][6][2]}  {user.ships[7][7][2]}   │")
    print(f"        │                                                                               │")
    print(f"        └───────────────────────────────────────────────────────────────────────────────┘\n\n\n")

    print(error)
    newShipPart = input(f"{TypeOfMessage.Input}Create a ship: ").lower()
    if len(newShipPart) != 2:
        createShipPart(user, f"{error}\n{TypeOfMessage.Error}Incorrect Input. Try something like D{randint(1,8)} or H{randint(1,8)}.", xl, xr, yu, yd)
        return
    nSPl = newShipPart[0]
    try:
        nSPn = int(newShipPart[1])
    except:
        createShipPart(user, f"{error}\n{TypeOfMessage.Error}Incorrect Input. Try something like D{randint(1,8)} or H{randint(1,8)}.", xl, xr, yu, yd)
        return
    if nSPn > 8:
        createShipPart(user, f"{error}\n{TypeOfMessage.Error}The number of the ship must be from 1-8.", xl, xr, yu, yd)
        return
    if nSPl == "a":
        newShipPartPlace = [0, nSPn-1]
    elif nSPl == "b":
        newShipPartPlace = [1, nSPn-1]
    elif nSPl == "c":
        newShipPartPlace = [2, nSPn-1]
    elif nSPl == "d":
        newShipPartPlace = [3, nSPn-1]
    elif nSPl == "e":
        newShipPartPlace = [4, nSPn-1]
    elif nSPl == "f":
        newShipPartPlace = [5, nSPn-1]
    elif nSPl == "g":
        newShipPartPlace = [6, nSPn-1]
    elif nSPl == "h":
        newShipPartPlace = [7, nSPn-1]

    global yaxisu
    global yaxisd
    global xaxisl
    global xaxisr

    if newShipPartPlace == [newShipPlace[0]-yu, newShipPlace[1]]:
        user.ships[newShipPartPlace[0]][nSPn-1][0] = f"{user.color}█  █  █{Colors.ENDC}"
        user.ships[newShipPartPlace[0]][nSPn-1][1] = f"{user.color}███████{Colors.ENDC}"
        user.ships[newShipPartPlace[0]][nSPn-1][2] = f"{user.color} █████ {Colors.ENDC}"
        xaxisl = 0
        xaxisr = 0
        yaxisu += 1
    elif newShipPartPlace == [newShipPlace[0]+yd, newShipPlace[1]]:
        user.ships[newShipPartPlace[0]][nSPn-1][0] = f"{user.color}█  █  █{Colors.ENDC}"
        user.ships[newShipPartPlace[0]][nSPn-1][1] = f"{user.color}███████{Colors.ENDC}"
        user.ships[newShipPartPlace[0]][nSPn-1][2] = f"{user.color} █████ {Colors.ENDC}"
        xaxisl = 0
        xaxisr = 0
        yaxisd += 1
    elif newShipPartPlace == [newShipPlace[0], newShipPlace[1]-xl]:
        user.ships[newShipPartPlace[0]][nSPn-1][0] = f"{user.color}█  █  █{Colors.ENDC}"
        user.ships[newShipPartPlace[0]][nSPn-1][1] = f"{user.color}███████{Colors.ENDC}"
        user.ships[newShipPartPlace[0]][nSPn-1][2] = f"{user.color} █████ {Colors.ENDC}"
        yaxisu = 0
        yaxisd = 0
        xaxisl += 1
    elif newShipPartPlace == [newShipPlace[0], newShipPlace[1]+xr]:
        user.ships[newShipPartPlace[0]][nSPn-1][0] = f"{user.color}█  █  █{Colors.ENDC}"
        user.ships[newShipPartPlace[0]][nSPn-1][1] = f"{user.color}███████{Colors.ENDC}"
        user.ships[newShipPartPlace[0]][nSPn-1][2] = f"{user.color} █████ {Colors.ENDC}"
        yaxisu = 0
        yaxisd = 0
        xaxisr += 1
    else:
        createShipPart(user, f"{error}\n{TypeOfMessage.Error}The ship part must connect to another part.", xl, xr, yu, yd)

def updateShips(user):
    os.system("cls")

    print()
    print()
    print()
    print(f"        ┌───────────────────────────────────────────────────────────────────────────────┐")
    print(f"        │         1        2        3        4        5        6        7        8      │")
    print(f"        │                                                                               │")
    print(f"        │      {user.ships[0][0][0]}  {user.ships[0][1][0]}  {user.ships[0][2][0]}  {user.ships[0][3][0]}  {user.ships[0][4][0]}  {user.ships[0][5][0]}  {user.ships[0][6][0]}  {user.ships[0][7][0]}   │")
    print(f"        │  A   {user.ships[0][0][1]}  {user.ships[0][1][1]}  {user.ships[0][2][1]}  {user.ships[0][3][1]}  {user.ships[0][4][1]}  {user.ships[0][5][1]}  {user.ships[0][6][1]}  {user.ships[0][7][1]}   │")
    print(f"        │      {user.ships[0][0][2]}  {user.ships[0][1][2]}  {user.ships[0][2][2]}  {user.ships[0][3][2]}  {user.ships[0][4][2]}  {user.ships[0][5][2]}  {user.ships[0][6][2]}  {user.ships[0][7][2]}   │")
    print(f"        │                                                                               │")
    print(f"        │      {user.ships[1][0][0]}  {user.ships[1][1][0]}  {user.ships[1][2][0]}  {user.ships[1][3][0]}  {user.ships[1][4][0]}  {user.ships[1][5][0]}  {user.ships[1][6][0]}  {user.ships[1][7][0]}   │")
    print(f"        │  B   {user.ships[1][0][1]}  {user.ships[1][1][1]}  {user.ships[1][2][1]}  {user.ships[1][3][1]}  {user.ships[1][4][1]}  {user.ships[1][5][1]}  {user.ships[1][6][1]}  {user.ships[1][7][1]}   │")
    print(f"        │      {user.ships[1][0][2]}  {user.ships[1][1][2]}  {user.ships[1][2][2]}  {user.ships[1][3][2]}  {user.ships[1][4][2]}  {user.ships[1][5][2]}  {user.ships[1][6][2]}  {user.ships[1][7][2]}   │")
    print(f"        │                                                                               │")
    print(f"        │      {user.ships[2][0][0]}  {user.ships[2][1][0]}  {user.ships[2][2][0]}  {user.ships[2][3][0]}  {user.ships[2][4][0]}  {user.ships[2][5][0]}  {user.ships[2][6][0]}  {user.ships[2][7][0]}   │") 
    print(f"        │  C   {user.ships[2][0][1]}  {user.ships[2][1][1]}  {user.ships[2][2][1]}  {user.ships[2][3][1]}  {user.ships[2][4][1]}  {user.ships[2][5][1]}  {user.ships[2][6][1]}  {user.ships[2][7][1]}   │")
    print(f"        │      {user.ships[2][0][2]}  {user.ships[2][1][2]}  {user.ships[2][2][2]}  {user.ships[2][3][2]}  {user.ships[2][4][2]}  {user.ships[2][5][2]}  {user.ships[2][6][2]}  {user.ships[2][7][2]}   │")
    print(f"        │                                                                               │")
    print(f"        │      {user.ships[3][0][0]}  {user.ships[3][1][0]}  {user.ships[3][2][0]}  {user.ships[3][3][0]}  {user.ships[3][4][0]}  {user.ships[3][5][0]}  {user.ships[3][6][0]}  {user.ships[3][7][0]}   │")
    print(f"        │  D   {user.ships[3][0][1]}  {user.ships[3][1][1]}  {user.ships[3][2][1]}  {user.ships[3][3][1]}  {user.ships[3][4][1]}  {user.ships[3][5][1]}  {user.ships[3][6][1]}  {user.ships[3][7][1]}   │")
    print(f"        │      {user.ships[3][0][2]}  {user.ships[3][1][2]}  {user.ships[3][2][2]}  {user.ships[3][3][2]}  {user.ships[3][4][2]}  {user.ships[3][5][2]}  {user.ships[3][6][2]}  {user.ships[3][7][2]}   │")
    print(f"        │                                                                               │")
    print(f"        │      {user.ships[4][0][0]}  {user.ships[4][1][0]}  {user.ships[4][2][0]}  {user.ships[4][3][0]}  {user.ships[4][4][0]}  {user.ships[4][5][0]}  {user.ships[4][6][0]}  {user.ships[4][7][0]}   │")
    print(f"        │  E   {user.ships[4][0][1]}  {user.ships[4][1][1]}  {user.ships[4][2][1]}  {user.ships[4][3][1]}  {user.ships[4][4][1]}  {user.ships[4][5][1]}  {user.ships[4][6][1]}  {user.ships[4][7][1]}   │")
    print(f"        │      {user.ships[4][0][2]}  {user.ships[4][1][2]}  {user.ships[4][2][2]}  {user.ships[4][3][2]}  {user.ships[4][4][2]}  {user.ships[4][5][2]}  {user.ships[4][6][2]}  {user.ships[4][7][2]}   │")
    print(f"        │                                                                               │")
    print(f"        │      {user.ships[5][0][0]}  {user.ships[5][1][0]}  {user.ships[5][2][0]}  {user.ships[5][3][0]}  {user.ships[5][4][0]}  {user.ships[5][5][0]}  {user.ships[5][6][0]}  {user.ships[5][7][0]}   │")
    print(f"        │  F   {user.ships[5][0][1]}  {user.ships[5][1][1]}  {user.ships[5][2][1]}  {user.ships[5][3][1]}  {user.ships[5][4][1]}  {user.ships[5][5][1]}  {user.ships[5][6][1]}  {user.ships[5][7][1]}   │")
    print(f"        │      {user.ships[5][0][2]}  {user.ships[5][1][2]}  {user.ships[5][2][2]}  {user.ships[5][3][2]}  {user.ships[5][4][2]}  {user.ships[5][5][2]}  {user.ships[5][6][2]}  {user.ships[5][7][2]}   │")
    print(f"        │                                                                               │")
    print(f"        │      {user.ships[6][0][0]}  {user.ships[6][1][0]}  {user.ships[6][2][0]}  {user.ships[6][3][0]}  {user.ships[6][4][0]}  {user.ships[6][5][0]}  {user.ships[6][6][0]}  {user.ships[6][7][0]}   │")
    print(f"        │  G   {user.ships[6][0][1]}  {user.ships[6][1][1]}  {user.ships[6][2][1]}  {user.ships[6][3][1]}  {user.ships[6][4][1]}  {user.ships[6][5][1]}  {user.ships[6][6][1]}  {user.ships[6][7][1]}   │")
    print(f"        │      {user.ships[6][0][2]}  {user.ships[6][1][2]}  {user.ships[6][2][2]}  {user.ships[6][3][2]}  {user.ships[6][4][2]}  {user.ships[6][5][2]}  {user.ships[6][6][2]}  {user.ships[6][7][2]}   │")
    print(f"        │                                                                               │")
    print(f"        │      {user.ships[7][0][0]}  {user.ships[7][1][0]}  {user.ships[7][2][0]}  {user.ships[7][3][0]}  {user.ships[7][4][0]}  {user.ships[7][5][0]}  {user.ships[7][6][0]}  {user.ships[7][7][0]}   │")
    print(f"        │  H   {user.ships[7][0][1]}  {user.ships[7][1][1]}  {user.ships[7][2][1]}  {user.ships[7][3][1]}  {user.ships[7][4][1]}  {user.ships[7][5][1]}  {user.ships[7][6][1]}  {user.ships[7][7][1]}   │")
    print(f"        │      {user.ships[7][0][2]}  {user.ships[7][1][2]}  {user.ships[7][2][2]}  {user.ships[7][3][2]}  {user.ships[7][4][2]}  {user.ships[7][5][2]}  {user.ships[7][6][2]}  {user.ships[7][7][2]}   │")
    print(f"        │                                                                               │")
    print(f"        └───────────────────────────────────────────────────────────────────────────────┘\n\n\n")

def setShips(user):
    input(f"{TypeOfMessage.Info}The following page should only see {user.color}{user.name}{Colors.ENDC}...")
    global xaxisl
    global xaxisr
    global yaxisu 
    global yaxisd
    createShip(user, f"{TypeOfMessage.Info}Large ship (5 ship parts):")
    createShipPart(user, f"{TypeOfMessage.Info}Large ship (5 ship parts):", xaxisl, xaxisr, yaxisu, yaxisd)
    createShipPart(user, f"{TypeOfMessage.Info}Large ship (5 ship parts):", xaxisl, xaxisr, yaxisu, yaxisd)
    createShipPart(user, f"{TypeOfMessage.Info}Large ship (5 ship parts):", xaxisl, xaxisr, yaxisu, yaxisd)
    createShipPart(user, f"{TypeOfMessage.Info}Large ship (5 ship parts):", xaxisl, xaxisr, yaxisu, yaxisd)
    xaxisl = 1
    xaxisr = 1
    yaxisu = 1
    yaxisd = 1
    createShip(user, f"{TypeOfMessage.Info}Big ship (4 ship parts):")
    createShipPart(user, f"{TypeOfMessage.Info}Big ship (4 ship parts):", xaxisl, xaxisr, yaxisu, yaxisd)
    createShipPart(user, f"{TypeOfMessage.Info}Big ship (4 ship parts):", xaxisl, xaxisr, yaxisu, yaxisd)
    createShipPart(user, f"{TypeOfMessage.Info}Big ship (4 ship parts):", xaxisl, xaxisr, yaxisu, yaxisd)
    xaxisl = 1
    xaxisr = 1
    yaxisu = 1
    yaxisd = 1
    createShip(user, f"{TypeOfMessage.Info}Medium ship (3 ship parts):")
    createShipPart(user, f"{TypeOfMessage.Info}Medium ship (3 ship parts):", xaxisl, xaxisr, yaxisu, yaxisd)
    createShipPart(user, f"{TypeOfMessage.Info}Medium ship (3 ship parts):", xaxisl, xaxisr, yaxisu, yaxisd)
    xaxisl = 1
    xaxisr = 1
    yaxisu = 1
    yaxisd = 1
    createShip(user, f"{TypeOfMessage.Info}Small ship (2 ship parts):")
    createShipPart(user, f"{TypeOfMessage.Info}Small ship (2 ship parts):", xaxisl, xaxisr, yaxisu, yaxisd)
    xaxisl = 1
    xaxisr = 1
    yaxisu = 1
    yaxisd = 1
    createShip(user, f"{TypeOfMessage.Info}Mini ship (1 ship part):")
    updateShips(user)
    input(f"{TypeOfMessage.Info}Press ENTER to continue...")
    os.system("cls")

setShips(u1)
setShips(u2)

def update(usertarget):
    os.system("cls")

    print()
    print()
    print()
    print(f"        ┌───────────────────────────────────────────────────────────────────────────────┐")
    print(f"        │         1        2        3        4        5        6        7        8      │")
    print(f"        │                                                                               │")
    print(f"        │      {usertarget.playground[0][0][0]}  {usertarget.playground[0][1][0]}  {usertarget.playground[0][2][0]}  {usertarget.playground[0][3][0]}  {usertarget.playground[0][4][0]}  {usertarget.playground[0][5][0]}  {usertarget.playground[0][6][0]}  {usertarget.playground[0][7][0]}   │")
    print(f"        │  A   {usertarget.playground[0][0][1]}  {usertarget.playground[0][1][1]}  {usertarget.playground[0][2][1]}  {usertarget.playground[0][3][1]}  {usertarget.playground[0][4][1]}  {usertarget.playground[0][5][1]}  {usertarget.playground[0][6][1]}  {usertarget.playground[0][7][1]}   │")
    print(f"        │      {usertarget.playground[0][0][2]}  {usertarget.playground[0][1][2]}  {usertarget.playground[0][2][2]}  {usertarget.playground[0][3][2]}  {usertarget.playground[0][4][2]}  {usertarget.playground[0][5][2]}  {usertarget.playground[0][6][2]}  {usertarget.playground[0][7][2]}   │")
    print(f"        │                                                                               │")
    print(f"        │      {usertarget.playground[1][0][0]}  {usertarget.playground[1][1][0]}  {usertarget.playground[1][2][0]}  {usertarget.playground[1][3][0]}  {usertarget.playground[1][4][0]}  {usertarget.playground[1][5][0]}  {usertarget.playground[1][6][0]}  {usertarget.playground[1][7][0]}   │")
    print(f"        │  B   {usertarget.playground[1][0][1]}  {usertarget.playground[1][1][1]}  {usertarget.playground[1][2][1]}  {usertarget.playground[1][3][1]}  {usertarget.playground[1][4][1]}  {usertarget.playground[1][5][1]}  {usertarget.playground[1][6][1]}  {usertarget.playground[1][7][1]}   │")
    print(f"        │      {usertarget.playground[1][0][2]}  {usertarget.playground[1][1][2]}  {usertarget.playground[1][2][2]}  {usertarget.playground[1][3][2]}  {usertarget.playground[1][4][2]}  {usertarget.playground[1][5][2]}  {usertarget.playground[1][6][2]}  {usertarget.playground[1][7][2]}   │")
    print(f"        │                                                                               │")
    print(f"        │      {usertarget.playground[2][0][0]}  {usertarget.playground[2][1][0]}  {usertarget.playground[2][2][0]}  {usertarget.playground[2][3][0]}  {usertarget.playground[2][4][0]}  {usertarget.playground[2][5][0]}  {usertarget.playground[2][6][0]}  {usertarget.playground[2][7][0]}   │") 
    print(f"        │  C   {usertarget.playground[2][0][1]}  {usertarget.playground[2][1][1]}  {usertarget.playground[2][2][1]}  {usertarget.playground[2][3][1]}  {usertarget.playground[2][4][1]}  {usertarget.playground[2][5][1]}  {usertarget.playground[2][6][1]}  {usertarget.playground[2][7][1]}   │")
    print(f"        │      {usertarget.playground[2][0][2]}  {usertarget.playground[2][1][2]}  {usertarget.playground[2][2][2]}  {usertarget.playground[2][3][2]}  {usertarget.playground[2][4][2]}  {usertarget.playground[2][5][2]}  {usertarget.playground[2][6][2]}  {usertarget.playground[2][7][2]}   │")
    print(f"        │                                                                               │")
    print(f"        │      {usertarget.playground[3][0][0]}  {usertarget.playground[3][1][0]}  {usertarget.playground[3][2][0]}  {usertarget.playground[3][3][0]}  {usertarget.playground[3][4][0]}  {usertarget.playground[3][5][0]}  {usertarget.playground[3][6][0]}  {usertarget.playground[3][7][0]}   │")
    print(f"        │  D   {usertarget.playground[3][0][1]}  {usertarget.playground[3][1][1]}  {usertarget.playground[3][2][1]}  {usertarget.playground[3][3][1]}  {usertarget.playground[3][4][1]}  {usertarget.playground[3][5][1]}  {usertarget.playground[3][6][1]}  {usertarget.playground[3][7][1]}   │")
    print(f"        │      {usertarget.playground[3][0][2]}  {usertarget.playground[3][1][2]}  {usertarget.playground[3][2][2]}  {usertarget.playground[3][3][2]}  {usertarget.playground[3][4][2]}  {usertarget.playground[3][5][2]}  {usertarget.playground[3][6][2]}  {usertarget.playground[3][7][2]}   │")
    print(f"        │                                                                               │")
    print(f"        │      {usertarget.playground[4][0][0]}  {usertarget.playground[4][1][0]}  {usertarget.playground[4][2][0]}  {usertarget.playground[4][3][0]}  {usertarget.playground[4][4][0]}  {usertarget.playground[4][5][0]}  {usertarget.playground[4][6][0]}  {usertarget.playground[4][7][0]}   │")
    print(f"        │  E   {usertarget.playground[4][0][1]}  {usertarget.playground[4][1][1]}  {usertarget.playground[4][2][1]}  {usertarget.playground[4][3][1]}  {usertarget.playground[4][4][1]}  {usertarget.playground[4][5][1]}  {usertarget.playground[4][6][1]}  {usertarget.playground[4][7][1]}   │")
    print(f"        │      {usertarget.playground[4][0][2]}  {usertarget.playground[4][1][2]}  {usertarget.playground[4][2][2]}  {usertarget.playground[4][3][2]}  {usertarget.playground[4][4][2]}  {usertarget.playground[4][5][2]}  {usertarget.playground[4][6][2]}  {usertarget.playground[4][7][2]}   │")
    print(f"        │                                                                               │")
    print(f"        │      {usertarget.playground[5][0][0]}  {usertarget.playground[5][1][0]}  {usertarget.playground[5][2][0]}  {usertarget.playground[5][3][0]}  {usertarget.playground[5][4][0]}  {usertarget.playground[5][5][0]}  {usertarget.playground[5][6][0]}  {usertarget.playground[5][7][0]}   │")
    print(f"        │  F   {usertarget.playground[5][0][1]}  {usertarget.playground[5][1][1]}  {usertarget.playground[5][2][1]}  {usertarget.playground[5][3][1]}  {usertarget.playground[5][4][1]}  {usertarget.playground[5][5][1]}  {usertarget.playground[5][6][1]}  {usertarget.playground[5][7][1]}   │")
    print(f"        │      {usertarget.playground[5][0][2]}  {usertarget.playground[5][1][2]}  {usertarget.playground[5][2][2]}  {usertarget.playground[5][3][2]}  {usertarget.playground[5][4][2]}  {usertarget.playground[5][5][2]}  {usertarget.playground[5][6][2]}  {usertarget.playground[5][7][2]}   │")
    print(f"        │                                                                               │")
    print(f"        │      {usertarget.playground[6][0][0]}  {usertarget.playground[6][1][0]}  {usertarget.playground[6][2][0]}  {usertarget.playground[6][3][0]}  {usertarget.playground[6][4][0]}  {usertarget.playground[6][5][0]}  {usertarget.playground[6][6][0]}  {usertarget.playground[6][7][0]}   │")
    print(f"        │  G   {usertarget.playground[6][0][1]}  {usertarget.playground[6][1][1]}  {usertarget.playground[6][2][1]}  {usertarget.playground[6][3][1]}  {usertarget.playground[6][4][1]}  {usertarget.playground[6][5][1]}  {usertarget.playground[6][6][1]}  {usertarget.playground[6][7][1]}   │")
    print(f"        │      {usertarget.playground[6][0][2]}  {usertarget.playground[6][1][2]}  {usertarget.playground[6][2][2]}  {usertarget.playground[6][3][2]}  {usertarget.playground[6][4][2]}  {usertarget.playground[6][5][2]}  {usertarget.playground[6][6][2]}  {usertarget.playground[6][7][2]}   │")
    print(f"        │                                                                               │")
    print(f"        │      {usertarget.playground[7][0][0]}  {usertarget.playground[7][1][0]}  {usertarget.playground[7][2][0]}  {usertarget.playground[7][3][0]}  {usertarget.playground[7][4][0]}  {usertarget.playground[7][5][0]}  {usertarget.playground[7][6][0]}  {usertarget.playground[7][7][0]}   │")
    print(f"        │  H   {usertarget.playground[7][0][1]}  {usertarget.playground[7][1][1]}  {usertarget.playground[7][2][1]}  {usertarget.playground[7][3][1]}  {usertarget.playground[7][4][1]}  {usertarget.playground[7][5][1]}  {usertarget.playground[7][6][1]}  {usertarget.playground[7][7][1]}   │")
    print(f"        │      {usertarget.playground[7][0][2]}  {usertarget.playground[7][1][2]}  {usertarget.playground[7][2][2]}  {usertarget.playground[7][3][2]}  {usertarget.playground[7][4][2]}  {usertarget.playground[7][5][2]}  {usertarget.playground[7][6][2]}  {usertarget.playground[7][7][2]}   │")
    print(f"        │                                                                               │")
    print(f"        └───────────────────────────────────────────────────────────────────────────────┘\n\n\n")

def play():

    def move(user, usertarget, error):

        os.system("cls")
        global win

        print()
        print()
        print()
        print(f"        ┌───────────────────────────────────────────────────────────────────────────────┐")
        print(f"        │         1        2        3        4        5        6        7        8      │")
        print(f"        │                                                                               │")
        print(f"        │      {usertarget.playground[0][0][0]}  {usertarget.playground[0][1][0]}  {usertarget.playground[0][2][0]}  {usertarget.playground[0][3][0]}  {usertarget.playground[0][4][0]}  {usertarget.playground[0][5][0]}  {usertarget.playground[0][6][0]}  {usertarget.playground[0][7][0]}   │")
        print(f"        │  A   {usertarget.playground[0][0][1]}  {usertarget.playground[0][1][1]}  {usertarget.playground[0][2][1]}  {usertarget.playground[0][3][1]}  {usertarget.playground[0][4][1]}  {usertarget.playground[0][5][1]}  {usertarget.playground[0][6][1]}  {usertarget.playground[0][7][1]}   │")
        print(f"        │      {usertarget.playground[0][0][2]}  {usertarget.playground[0][1][2]}  {usertarget.playground[0][2][2]}  {usertarget.playground[0][3][2]}  {usertarget.playground[0][4][2]}  {usertarget.playground[0][5][2]}  {usertarget.playground[0][6][2]}  {usertarget.playground[0][7][2]}   │")
        print(f"        │                                                                               │")
        print(f"        │      {usertarget.playground[1][0][0]}  {usertarget.playground[1][1][0]}  {usertarget.playground[1][2][0]}  {usertarget.playground[1][3][0]}  {usertarget.playground[1][4][0]}  {usertarget.playground[1][5][0]}  {usertarget.playground[1][6][0]}  {usertarget.playground[1][7][0]}   │")
        print(f"        │  B   {usertarget.playground[1][0][1]}  {usertarget.playground[1][1][1]}  {usertarget.playground[1][2][1]}  {usertarget.playground[1][3][1]}  {usertarget.playground[1][4][1]}  {usertarget.playground[1][5][1]}  {usertarget.playground[1][6][1]}  {usertarget.playground[1][7][1]}   │")
        print(f"        │      {usertarget.playground[1][0][2]}  {usertarget.playground[1][1][2]}  {usertarget.playground[1][2][2]}  {usertarget.playground[1][3][2]}  {usertarget.playground[1][4][2]}  {usertarget.playground[1][5][2]}  {usertarget.playground[1][6][2]}  {usertarget.playground[1][7][2]}   │")
        print(f"        │                                                                               │")
        print(f"        │      {usertarget.playground[2][0][0]}  {usertarget.playground[2][1][0]}  {usertarget.playground[2][2][0]}  {usertarget.playground[2][3][0]}  {usertarget.playground[2][4][0]}  {usertarget.playground[2][5][0]}  {usertarget.playground[2][6][0]}  {usertarget.playground[2][7][0]}   │") 
        print(f"        │  C   {usertarget.playground[2][0][1]}  {usertarget.playground[2][1][1]}  {usertarget.playground[2][2][1]}  {usertarget.playground[2][3][1]}  {usertarget.playground[2][4][1]}  {usertarget.playground[2][5][1]}  {usertarget.playground[2][6][1]}  {usertarget.playground[2][7][1]}   │")
        print(f"        │      {usertarget.playground[2][0][2]}  {usertarget.playground[2][1][2]}  {usertarget.playground[2][2][2]}  {usertarget.playground[2][3][2]}  {usertarget.playground[2][4][2]}  {usertarget.playground[2][5][2]}  {usertarget.playground[2][6][2]}  {usertarget.playground[2][7][2]}   │")
        print(f"        │                                                                               │")
        print(f"        │      {usertarget.playground[3][0][0]}  {usertarget.playground[3][1][0]}  {usertarget.playground[3][2][0]}  {usertarget.playground[3][3][0]}  {usertarget.playground[3][4][0]}  {usertarget.playground[3][5][0]}  {usertarget.playground[3][6][0]}  {usertarget.playground[3][7][0]}   │")
        print(f"        │  D   {usertarget.playground[3][0][1]}  {usertarget.playground[3][1][1]}  {usertarget.playground[3][2][1]}  {usertarget.playground[3][3][1]}  {usertarget.playground[3][4][1]}  {usertarget.playground[3][5][1]}  {usertarget.playground[3][6][1]}  {usertarget.playground[3][7][1]}   │")
        print(f"        │      {usertarget.playground[3][0][2]}  {usertarget.playground[3][1][2]}  {usertarget.playground[3][2][2]}  {usertarget.playground[3][3][2]}  {usertarget.playground[3][4][2]}  {usertarget.playground[3][5][2]}  {usertarget.playground[3][6][2]}  {usertarget.playground[3][7][2]}   │")
        print(f"        │                                                                               │")
        print(f"        │      {usertarget.playground[4][0][0]}  {usertarget.playground[4][1][0]}  {usertarget.playground[4][2][0]}  {usertarget.playground[4][3][0]}  {usertarget.playground[4][4][0]}  {usertarget.playground[4][5][0]}  {usertarget.playground[4][6][0]}  {usertarget.playground[4][7][0]}   │")
        print(f"        │  E   {usertarget.playground[4][0][1]}  {usertarget.playground[4][1][1]}  {usertarget.playground[4][2][1]}  {usertarget.playground[4][3][1]}  {usertarget.playground[4][4][1]}  {usertarget.playground[4][5][1]}  {usertarget.playground[4][6][1]}  {usertarget.playground[4][7][1]}   │")
        print(f"        │      {usertarget.playground[4][0][2]}  {usertarget.playground[4][1][2]}  {usertarget.playground[4][2][2]}  {usertarget.playground[4][3][2]}  {usertarget.playground[4][4][2]}  {usertarget.playground[4][5][2]}  {usertarget.playground[4][6][2]}  {usertarget.playground[4][7][2]}   │")
        print(f"        │                                                                               │")
        print(f"        │      {usertarget.playground[5][0][0]}  {usertarget.playground[5][1][0]}  {usertarget.playground[5][2][0]}  {usertarget.playground[5][3][0]}  {usertarget.playground[5][4][0]}  {usertarget.playground[5][5][0]}  {usertarget.playground[5][6][0]}  {usertarget.playground[5][7][0]}   │")
        print(f"        │  F   {usertarget.playground[5][0][1]}  {usertarget.playground[5][1][1]}  {usertarget.playground[5][2][1]}  {usertarget.playground[5][3][1]}  {usertarget.playground[5][4][1]}  {usertarget.playground[5][5][1]}  {usertarget.playground[5][6][1]}  {usertarget.playground[5][7][1]}   │")
        print(f"        │      {usertarget.playground[5][0][2]}  {usertarget.playground[5][1][2]}  {usertarget.playground[5][2][2]}  {usertarget.playground[5][3][2]}  {usertarget.playground[5][4][2]}  {usertarget.playground[5][5][2]}  {usertarget.playground[5][6][2]}  {usertarget.playground[5][7][2]}   │")
        print(f"        │                                                                               │")
        print(f"        │      {usertarget.playground[6][0][0]}  {usertarget.playground[6][1][0]}  {usertarget.playground[6][2][0]}  {usertarget.playground[6][3][0]}  {usertarget.playground[6][4][0]}  {usertarget.playground[6][5][0]}  {usertarget.playground[6][6][0]}  {usertarget.playground[6][7][0]}   │")
        print(f"        │  G   {usertarget.playground[6][0][1]}  {usertarget.playground[6][1][1]}  {usertarget.playground[6][2][1]}  {usertarget.playground[6][3][1]}  {usertarget.playground[6][4][1]}  {usertarget.playground[6][5][1]}  {usertarget.playground[6][6][1]}  {usertarget.playground[6][7][1]}   │")
        print(f"        │      {usertarget.playground[6][0][2]}  {usertarget.playground[6][1][2]}  {usertarget.playground[6][2][2]}  {usertarget.playground[6][3][2]}  {usertarget.playground[6][4][2]}  {usertarget.playground[6][5][2]}  {usertarget.playground[6][6][2]}  {usertarget.playground[6][7][2]}   │")
        print(f"        │                                                                               │")
        print(f"        │      {usertarget.playground[7][0][0]}  {usertarget.playground[7][1][0]}  {usertarget.playground[7][2][0]}  {usertarget.playground[7][3][0]}  {usertarget.playground[7][4][0]}  {usertarget.playground[7][5][0]}  {usertarget.playground[7][6][0]}  {usertarget.playground[7][7][0]}   │")
        print(f"        │  H   {usertarget.playground[7][0][1]}  {usertarget.playground[7][1][1]}  {usertarget.playground[7][2][1]}  {usertarget.playground[7][3][1]}  {usertarget.playground[7][4][1]}  {usertarget.playground[7][5][1]}  {usertarget.playground[7][6][1]}  {usertarget.playground[7][7][1]}   │")
        print(f"        │      {usertarget.playground[7][0][2]}  {usertarget.playground[7][1][2]}  {usertarget.playground[7][2][2]}  {usertarget.playground[7][3][2]}  {usertarget.playground[7][4][2]}  {usertarget.playground[7][5][2]}  {usertarget.playground[7][6][2]}  {usertarget.playground[7][7][2]}   │")
        print(f"        │                                                                               │")
        print(f"        └───────────────────────────────────────────────────────────────────────────────┘\n\n\n")

        print(error)

        shoot = input(f"[{user.color}{user.name}'s TURN{Colors.ENDC}] Where do u want to shoot on {usertarget.color}{usertarget.name}'s{Colors.ENDC} playground?: ")
        if len(shoot) != 2:
            move(user, usertarget, f"{TypeOfMessage.Error}Incorrect Input. Try something like D{randint(1,8)} or H{randint(1,8)}.")
            return
        nSl = shoot[0]
        try:
            nSn = int(shoot[1])
        except:
            move(user, usertarget, f"{TypeOfMessage.Error}Incorrect Input. Try something like D{randint(1,8)} or H{randint(1,8)}.")
            return
        if nSn > 8:
            move(user, usertarget, f"{TypeOfMessage.Error}The number of the ship must be from 1-8.")
            return
        if nSl == "a":
            if usertarget.ships[0][nSn-1][0] == f"{usertarget.color}█  █  █{Colors.ENDC}":
                usertarget.ships[0][nSn-1][0] = f"{usertarget.color} █████ {Colors.ENDC}"
                usertarget.playground[0][nSn-1][0] = f"{usertarget.color} █████ {Colors.ENDC}"
                usertarget.playground[0][nSn-1][1] = f"{usertarget.color}███████{Colors.ENDC}"
                usertarget.playground[0][nSn-1][2] = f"{usertarget.color}█  █  █{Colors.ENDC}"
                usertarget.shipsalive -= 1
                playsound("explosion.mp3")
                if usertarget.shipsalive == 0:
                    win = True
                    update(usertarget)
                    return
                else:
                    move(user, usertarget, f"{TypeOfMessage.Hit}You hit a ship part of {usertarget.color}{usertarget.name}'s{Colors.ENDC} ship army. [{usertarget.color}{usertarget.shipsalive}{Colors.ENDC}/{shipamount}] remaining.")
                    return
            elif usertarget.ships[0][nSn-1][0] == f"{usertarget.color} █████ {Colors.ENDC}" or usertarget.playground[0][nSn-1][0] == f"{Colors.GRAY}██   ██{Colors.ENDC}":
                move(user, usertarget, f"{TypeOfMessage.Error}You already hit on this field. Try again an other field:")
                return
            else:
                usertarget.playground[0][nSn-1][0] = f"{Colors.GRAY}██   ██{Colors.ENDC}"
                usertarget.playground[0][nSn-1][1] = f"{Colors.GRAY}  ███  {Colors.ENDC}"
                usertarget.playground[0][nSn-1][2] = f"{Colors.GRAY}██   ██{Colors.ENDC}"
                update(usertarget)
                input(f"{TypeOfMessage.NoHit}You don't have hit a ship part of {usertarget.color}{usertarget.name}'s{Colors.ENDC} ship army...")
        elif nSl == "b":
            if usertarget.ships[1][nSn-1][0] == f"{usertarget.color}█  █  █{Colors.ENDC}":
                usertarget.ships[1][nSn-1][0] = f"{usertarget.color} █████ {Colors.ENDC}"
                usertarget.playground[1][nSn-1][0] = f"{usertarget.color} █████ {Colors.ENDC}"
                usertarget.playground[1][nSn-1][1] = f"{usertarget.color}███████{Colors.ENDC}"
                usertarget.playground[1][nSn-1][2] = f"{usertarget.color}█  █  █{Colors.ENDC}"
                usertarget.shipsalive -= 1
                playsound("explosion.mp3")
                if usertarget.shipsalive == 0:
                    win = True
                    update(usertarget)
                    return
                else:
                    move(user, usertarget, f"{TypeOfMessage.Hit}You hit a ship part of {usertarget.color}{usertarget.name}'s{Colors.ENDC} ship army. [{usertarget.color}{usertarget.shipsalive}{Colors.ENDC}/{shipamount}] remaining.")
                    return
            elif usertarget.ships[1][nSn-1][0] == f"{usertarget.color} █████ {Colors.ENDC}" or usertarget.playground[1][nSn-1][0] == f"{Colors.GRAY}██   ██{Colors.ENDC}":
                move(user, usertarget, f"{TypeOfMessage.Error}You already hit on this field. Try again an other field:")
                return
            else:
                usertarget.playground[1][nSn-1][0] = f"{Colors.GRAY}██   ██{Colors.ENDC}"
                usertarget.playground[1][nSn-1][1] = f"{Colors.GRAY}  ███  {Colors.ENDC}"
                usertarget.playground[1][nSn-1][2] = f"{Colors.GRAY}██   ██{Colors.ENDC}"
                update(usertarget)
                input(f"{TypeOfMessage.NoHit}You don't have hit a ship part of {usertarget.color}{usertarget.name}'s{Colors.ENDC} ship army...")
        elif nSl == "c":
            if usertarget.ships[2][nSn-1][0] == f"{usertarget.color}█  █  █{Colors.ENDC}":
                usertarget.ships[2][nSn-1][0] = f"{usertarget.color} █████ {Colors.ENDC}"
                usertarget.playground[2][nSn-1][0] = f"{usertarget.color} █████ {Colors.ENDC}"
                usertarget.playground[2][nSn-1][1] = f"{usertarget.color}███████{Colors.ENDC}"
                usertarget.playground[2][nSn-1][2] = f"{usertarget.color}█  █  █{Colors.ENDC}"
                usertarget.shipsalive -= 1
                playsound("explosion.mp3")
                if usertarget.shipsalive == 0:
                    win = True
                    update(usertarget)
                    return
                else:
                    move(user, usertarget, f"{TypeOfMessage.Hit}You hit a ship part of {usertarget.color}{usertarget.name}'s{Colors.ENDC} ship army. [{usertarget.color}{usertarget.shipsalive}{Colors.ENDC}/{shipamount}] remaining.")
                    return
            elif usertarget.ships[2][nSn-1][0] == f"{usertarget.color} █████ {Colors.ENDC}" or usertarget.playground[2][nSn-1][0] == f"{Colors.GRAY}██   ██{Colors.ENDC}":
                move(user, usertarget, f"{TypeOfMessage.Error}You already hit on this field. Try again an other field:")
                return
            else:
                usertarget.playground[2][nSn-1][0] = f"{Colors.GRAY}██   ██{Colors.ENDC}"
                usertarget.playground[2][nSn-1][1] = f"{Colors.GRAY}  ███  {Colors.ENDC}"
                usertarget.playground[2][nSn-1][2] = f"{Colors.GRAY}██   ██{Colors.ENDC}"
                update(usertarget)
                input(f"{TypeOfMessage.NoHit}You don't have hit a ship part of {usertarget.color}{usertarget.name}'s{Colors.ENDC} ship army...")
        elif nSl == "d":
            if usertarget.ships[3][nSn-1][0] == f"{usertarget.color}█  █  █{Colors.ENDC}":
                usertarget.ships[3][nSn-1][0] = f"{usertarget.color} █████ {Colors.ENDC}"
                usertarget.playground[3][nSn-1][0] = f"{usertarget.color} █████ {Colors.ENDC}"
                usertarget.playground[3][nSn-1][1] = f"{usertarget.color}███████{Colors.ENDC}"
                usertarget.playground[3][nSn-1][2] = f"{usertarget.color}█  █  █{Colors.ENDC}"
                usertarget.shipsalive -= 1
                playsound("explosion.mp3")
                if usertarget.shipsalive == 0:
                    win = True
                    update(usertarget)
                    return
                else:
                    move(user, usertarget, f"{TypeOfMessage.Hit}You hit a ship part of {usertarget.color}{usertarget.name}'s{Colors.ENDC} ship army. [{usertarget.color}{usertarget.shipsalive}{Colors.ENDC}/{shipamount}] remaining.")
                    return
            elif usertarget.ships[3][nSn-1][0] == f"{usertarget.color} █████ {Colors.ENDC}" or usertarget.playground[3][nSn-1][0] == f"{Colors.GRAY}██   ██{Colors.ENDC}":
                move(user, usertarget, f"{TypeOfMessage.Error}You already hit on this field. Try again an other field:")
                return
            else:
                usertarget.playground[3][nSn-1][0] = f"{Colors.GRAY}██   ██{Colors.ENDC}"
                usertarget.playground[3][nSn-1][1] = f"{Colors.GRAY}  ███  {Colors.ENDC}"
                usertarget.playground[3][nSn-1][2] = f"{Colors.GRAY}██   ██{Colors.ENDC}"
                update(usertarget)
                input(f"{TypeOfMessage.NoHit}You don't have hit a ship part of {usertarget.color}{usertarget.name}'s{Colors.ENDC} ship army...")
        elif nSl == "e":
            if usertarget.ships[4][nSn-1][0] == f"{usertarget.color}█  █  █{Colors.ENDC}":
                usertarget.ships[4][nSn-1][0] = f"{usertarget.color} █████ {Colors.ENDC}"
                usertarget.playground[4][nSn-1][0] = f"{usertarget.color} █████ {Colors.ENDC}"
                usertarget.playground[4][nSn-1][1] = f"{usertarget.color}███████{Colors.ENDC}"
                usertarget.playground[4][nSn-1][2] = f"{usertarget.color}█  █  █{Colors.ENDC}"
                usertarget.shipsalive -= 1
                playsound("explosion.mp3")
                if usertarget.shipsalive == 0:
                    win = True
                    update(usertarget)
                    return
                else:
                    move(user, usertarget, f"{TypeOfMessage.Hit}You hit a ship part of {usertarget.color}{usertarget.name}'s{Colors.ENDC} ship army. [{usertarget.color}{usertarget.shipsalive}{Colors.ENDC}/{shipamount}] remaining.")
                    return
            elif usertarget.ships[4][nSn-1][0] == f"{usertarget.color} █████ {Colors.ENDC}" or usertarget.playground[4][nSn-1][0] == f"{Colors.GRAY}██   ██{Colors.ENDC}":
                move(user, usertarget, f"{TypeOfMessage.Error}You already hit on this field. Try again an other field:")
                return
            else:
                usertarget.playground[4][nSn-1][0] = f"{Colors.GRAY}██   ██{Colors.ENDC}"
                usertarget.playground[4][nSn-1][1] = f"{Colors.GRAY}  ███  {Colors.ENDC}"
                usertarget.playground[4][nSn-1][2] = f"{Colors.GRAY}██   ██{Colors.ENDC}"
                update(usertarget)
                input(f"{TypeOfMessage.NoHit}You don't have hit a ship part of {usertarget.color}{usertarget.name}'s{Colors.ENDC} ship army...")
        elif nSl == "f":
            if usertarget.ships[5][nSn-1][0] == f"{usertarget.color}█  █  █{Colors.ENDC}":
                usertarget.ships[5][nSn-1][0] = f"{usertarget.color} █████ {Colors.ENDC}"
                usertarget.playground[5][nSn-1][0] = f"{usertarget.color} █████ {Colors.ENDC}"
                usertarget.playground[5][nSn-1][1] = f"{usertarget.color}███████{Colors.ENDC}"
                usertarget.playground[5][nSn-1][2] = f"{usertarget.color}█  █  █{Colors.ENDC}"
                usertarget.shipsalive -= 1
                playsound("explosion.mp3")
                if usertarget.shipsalive == 0:
                    win = True
                    update(usertarget)
                    return
                else:
                    move(user, usertarget, f"{TypeOfMessage.Hit}You hit a ship part of {usertarget.color}{usertarget.name}'s{Colors.ENDC} ship army. [{usertarget.color}{usertarget.shipsalive}{Colors.ENDC}/{shipamount}] remaining.")
                    return
            elif usertarget.ships[5][nSn-1][0] == f"{usertarget.color} █████ {Colors.ENDC}" or usertarget.playground[5][nSn-1][0] == f"{Colors.GRAY}██   ██{Colors.ENDC}":
                move(user, usertarget, f"{TypeOfMessage.Error}You already hit on this field. Try again an other field:")
                return
            else:
                usertarget.playground[5][nSn-1][0] = f"{Colors.GRAY}██   ██{Colors.ENDC}"
                usertarget.playground[5][nSn-1][1] = f"{Colors.GRAY}  ███  {Colors.ENDC}"
                usertarget.playground[5][nSn-1][2] = f"{Colors.GRAY}██   ██{Colors.ENDC}"
                update(usertarget)
                input(f"{TypeOfMessage.NoHit}You don't have hit a ship part of {usertarget.color}{usertarget.name}'s{Colors.ENDC} ship army...")
        elif nSl == "g":
            if usertarget.ships[6][nSn-1][0] == f"{usertarget.color}█  █  █{Colors.ENDC}":
                usertarget.ships[6][nSn-1][0] = f"{usertarget.color} █████ {Colors.ENDC}"
                usertarget.playground[6][nSn-1][0] = f"{usertarget.color} █████ {Colors.ENDC}"
                usertarget.playground[6][nSn-1][1] = f"{usertarget.color}███████{Colors.ENDC}"
                usertarget.playground[6][nSn-1][2] = f"{usertarget.color}█  █  █{Colors.ENDC}"
                usertarget.shipsalive -= 1
                playsound("explosion.mp3")
                if usertarget.shipsalive == 0:
                    win = True
                    update(usertarget)
                    return
                else:
                    move(user, usertarget, f"{TypeOfMessage.Hit}You hit a ship part of {usertarget.color}{usertarget.name}'s{Colors.ENDC} ship army. [{usertarget.color}{usertarget.shipsalive}{Colors.ENDC}/{shipamount}] remaining.")
                    return
            elif usertarget.ships[6][nSn-1][0] == f"{usertarget.color} █████ {Colors.ENDC}" or usertarget.playground[6][nSn-1][0] == f"{Colors.GRAY}██   ██{Colors.ENDC}":
                move(user, usertarget, f"{TypeOfMessage.Error}You already hit on this field. Try again an other field:")
                return
            else:
                usertarget.playground[6][nSn-1][0] = f"{Colors.GRAY}██   ██{Colors.ENDC}"
                usertarget.playground[6][nSn-1][1] = f"{Colors.GRAY}  ███  {Colors.ENDC}"
                usertarget.playground[6][nSn-1][2] = f"{Colors.GRAY}██   ██{Colors.ENDC}"
                update(usertarget)
                input(f"{TypeOfMessage.NoHit}You don't have hit a ship part of {usertarget.color}{usertarget.name}'s{Colors.ENDC} ship army...")
        elif nSl == "h":
            if usertarget.ships[7][nSn-1][0] == f"{usertarget.color}█  █  █{Colors.ENDC}":
                usertarget.ships[7][nSn-1][0] = f"{usertarget.color} █████ {Colors.ENDC}"
                usertarget.playground[7][nSn-1][0] = f"{usertarget.color} █████ {Colors.ENDC}"
                usertarget.playground[7][nSn-1][1] = f"{usertarget.color}███████{Colors.ENDC}"
                usertarget.playground[7][nSn-1][2] = f"{usertarget.color}█  █  █{Colors.ENDC}"
                usertarget.shipsalive -= 1
                playsound("explosion.mp3")
                if usertarget.shipsalive == 0:
                    win = True
                    update(usertarget)
                    return
                else:
                    move(user, usertarget, f"{TypeOfMessage.Hit}You hit a ship part of {usertarget.color}{usertarget.name}'s{Colors.ENDC} ship army. [{usertarget.color}{usertarget.shipsalive}{Colors.ENDC}/{shipamount}] remaining.")
                    return
            elif usertarget.ships[7][nSn-1][0] == f"{usertarget.color} █████ {Colors.ENDC}" or usertarget.playground[7][nSn-1][0] == f"{Colors.GRAY}██   ██{Colors.ENDC}":
                move(user, usertarget, f"{TypeOfMessage.Error}You already hit on this field. Try again an other field:")
                return
            else:
                usertarget.playground[7][nSn-1][0] = f"{Colors.GRAY}██   ██{Colors.ENDC}"
                usertarget.playground[7][nSn-1][1] = f"{Colors.GRAY}  ███  {Colors.ENDC}"
                usertarget.playground[7][nSn-1][2] = f"{Colors.GRAY}██   ██{Colors.ENDC}"
                update(usertarget)
                input(f"{TypeOfMessage.NoHit}You don't have hit a ship part of {usertarget.color}{usertarget.name}'s{Colors.ENDC} ship army...")
        else:
            move(user, usertarget, f"{TypeOfMessage.Error}The letter of the ship must be from A-H.")
            return

    while win == False:
        move(u1, u2, "")
        if win == False:
            move(u2, u1, "")
        else:
            return

play()

if u1.shipsalive == 0:
    print(f"{TypeOfMessage.GameOver}{u2.color}{u2.name}{Colors.ENDC} wins!")
    playsound("win.mp3")
elif u2.shipsalive == 0:
    print(f"{TypeOfMessage.GameOver}{u1.color}{u1.name}{Colors.ENDC} wins!")
    playsound("win.mp3")

input(f"{TypeOfMessage.Info}Press any key to exit...")
