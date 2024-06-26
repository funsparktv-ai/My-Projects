import random

class Room:
    def __init__(self, name, description, is_dark=False, has_monster=False, items=None):
        self.name = name
        self.description = description
        self.exits = {}
        self.items = items if items else []
        self.is_dark = is_dark
        self.has_monster = has_monster

    def enter_room(self):
        if self.is_dark:
            if random.random() < 0.5:
                print("It's pitch black in here. You can't see anything!")
            else:
                print("You hear faint whispers echoing in the darkness...")
        if self.has_monster:
            print("You sense a presence lurking nearby...")

class Player:
    def __init__(self, name, start_location):
        self.name = name
        self.current_location = start_location
        self.inventory = []
        self.health = 100

    def take_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            print("You have succumbed to the horrors. Game Over.")
            exit(0)
        else:
            print(f"You took {amount} damage! Your health is now {self.health}.")

def main_game_loop():
    # Define rooms and items
    rooms = {
        "start": Room("Start Room", "You wake up in a dimly lit room, with a cold draft brushing against your skin.", is_dark=True),
        "hallway": Room("Hallway", "You enter a long hallway lined with flickering candles. A chilling wind passes through."),
        "library": Room("Library", "The library is filled with ancient books, some of which seem to whisper as you pass by."),
        "crypt": Room("Crypt", "You descend into a dark crypt filled with ancient coffins and a faint smell of decay.", is_dark=True, has_monster=True),
        "dining": Room("Dining Hall", "The dining hall is adorned with cobweb-covered furniture and eerie portraits on the walls."),
        "kitchen": Room("Kitchen", "The kitchen is abandoned, with rusty knives and pots scattered around."),
        "exit": Room("Exit", "You've found the exit! Freedom is within your grasp.")
    }

    # Define room connections
    rooms["start"].exits = {"north": rooms["hallway"]}
    rooms["hallway"].exits = {"south": rooms["start"], "north": rooms["library"], "east": rooms["dining"], "west": rooms["kitchen"]}
    rooms["library"].exits = {"south": rooms["hallway"]}
    rooms["crypt"].exits = {"up": rooms["hallway"]}
    rooms["dining"].exits = {"west": rooms["hallway"]}
    rooms["kitchen"].exits = {"east": rooms["hallway"]}
    rooms["exit"].exits = {}  # No exits, final room

    # Add items to rooms
    rooms["hallway"].items = ["key"]
    rooms["library"].items = ["candle"]
    rooms["crypt"].items = ["ancient amulet"]
    rooms["dining"].items = ["silver fork", "rotten meat"]
    rooms["kitchen"].items = ["rusty knife", "old pot"]

    player = Player("Player1", rooms["start"])

    print("Welcome to the Horror Text Adventure Game!")
    print("Can you escape the haunted mansion?")
    print("Commands: north, south, east, west, up, down, look, search, inventory, quit\n")

    while True:
        print("\n" + "-"*50)
        print(player.current_location.name)
        print(player.current_location.description)
        player.current_location.enter_room()
        
        print("\nExits:", ", ".join(player.current_location.exits.keys()))
        
        command = input("\nEnter command: ").strip().lower()
        
        if command == "quit":
            print("Exiting game. Goodbye!")
            break
        elif command in player.current_location.exits:
            player.current_location = rooms[player.current_location.exits[command]]
        elif command == "look":
            print(player.current_location.description)
        elif command == "search":
            if player.current_location.items:
                print("You found the following items:")
                for item in player.current_location.items:
                    print("-", item)
                    player.inventory.append(item)
                player.current_location.items = []
            else:
                print("You found nothing of interest.")
        elif command == "inventory":
            if player.inventory:
                print("Inventory:")
                for item in player.inventory:
                    print("-", item)
            else:
                print("Your inventory is empty.")
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main_game_loop()
