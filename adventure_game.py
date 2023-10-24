import time

# Function to display the game introduction
def intro():
    print("Welcome to the Magical Forest Adventure!")
    print("You are on a quest to find the lost Crystal of Power in the magical forest.")
    print("Your journey begins now...")
    time.sleep(2)
    start_adventure()

# Function to start the adventure
def start_adventure():
    print("\nYou are standing at the edge of a dense, mystical forest.")
    print("You have two paths to choose from.")
    choice = input("Which path will you take? (left/right): ").lower()
    if choice == "left":
        print("You venture into the dark forest...")
        left_path()
    elif choice == "right":
        print("You follow the path to the right...")
        right_path()
    else:
        print("Invalid choice. Try again.")
        start_adventure()

# Function for the left path of the forest
def left_path():
    print("\nAs you walk deeper into the forest, you come across a talking tree.")
    print("The tree tells you that the Crystal of Power is hidden nearby.")
    choice = input("What will you do? (ask/ignore): ").lower()
    if choice == "ask":
        print("The talking tree shares a riddle to guide you.")
        print("Solve the riddle to find the crystal!")
        solve_riddle(1)  # Start with the first riddle
    elif choice == "ignore":
        print("You continue your journey deeper into the forest.")
        find_crystal()
    else:
        print("Invalid choice. Try again.")
        left_path()

# Function to solve a riddle and find the crystal
def solve_riddle(riddle_number):
    riddles = [
        {
            "question": "I'm not alive, but I can grow. I don't have lungs, but I need air. What am I?",
            "answer": "fire"
        },
        {
            "question": "I have keys but open no locks. I have space but no room. You can enter, but you can't go inside. What am I?",
            "answer": "keyboard"
        },
        {
            "question": "I am taken from a mine, and shut up in a wooden case, from which I am never released, and yet I am used by almost every person. What am I?",
            "answer": "pencil lead"
        }
    ]
    
    current_riddle = riddles[riddle_number - 1]
    guesses = 3  # Player has 3 chances to guess the riddle
    while guesses > 0:
        print(f"\nHere's the riddle: {current_riddle['question']}")
        user_answer = input(f"You have {guesses} chances left. Your answer: ").lower()
        if user_answer == current_riddle["answer"]:
            if riddle_number == len(riddles):
                print("Congratulations! You've solved the final riddle and found the Crystal of Power!")
                win()
            else:
                print("Congratulations! You've solved the riddle and found a clue to the next riddle.")
                solve_riddle(riddle_number + 1)  # Move to the next riddle
            break
        else:
            guesses -= 1
            if guesses > 0:
                print(f"Sorry, that's not correct. You have {guesses} chances left.")
            else:
                print("You've run out of chances. Keep searching for the crystal.")
                find_crystal()

# Function for continuing to search for the crystal in the left path
def find_crystal():
    print("\nYou continue deeper into the forest.")
    print("As you explore, you encounter a mischievous forest spirit.")
    choice = input("Will you try to befriend the spirit or avoid it? (befriend/avoid): ").lower()
    if choice == "befriend":
        print("You and the spirit become friends, and it leads you to the crystal!")
        win()
    elif choice == "avoid":
        print("You carefully avoid the spirit and keep searching for the crystal.")
        print("Your quest continues...")
        time.sleep(2)
        print("You find yourself lost in the forest.")
        game_over()
    else:
        print("Invalid choice. Try again.")
        find_crystal()

# Function for the right path of the forest
def right_path():
    print("\nYou follow the path to the right, and it leads to a complex maze.")
    print("The maze has multiple twists and turns.")
    print("You need to find your way through.")
    navigate_maze()

# Function to navigate the maze in the right path
def navigate_maze():
    print("\nYou find yourself in a labyrinth of passages and tunnels.")
    print("You must choose the correct path to reach the end of the maze.")
    print("Be careful; the wrong choice could lead you in circles!")
    choice = input("Which path will you take? (1/2/3): ")
    if choice == "3":
        print("You've found the exit of the maze! Well done.")
        win()
    else:
        print("You've taken the wrong path and are now lost in the maze.")
        game_over()

# Function to handle the game over scenario
def game_over():
    print("\nYou are lost in the mystical forest, and your quest comes to a tragic end.")
    print("Game Over! Try again?")
    play_again()

# Function to handle the win scenario
def win():
    print("\nCongratulations! You've found the Crystal of Power and completed your quest!")
    play_again()

# Function to prompt the player to play again or exit the game
def play_again():
    choice = input("Do you want to embark on another adventure? (yes/no): ").lower()
    if choice == "yes":
        intro()
    elif choice == "no":
        print("Thanks for playing!")
    else:
        print("Invalid choice. Try again.")
        play_again()

# Start the game by calling the intro function
intro()
