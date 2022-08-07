# Chris Bare
# A dictionary for the simplified dragon text game
# The dictionary links a room to other rooms.
rooms = {
        'Great Hall': {'South': 'Bedroom'},
        'Bedroom': {'North': 'Great Hall', 'East': 'Cellar'},
        'Cellar': {'West': 'Bedroom'}
        }

player_alive = True
player_continue = True
current_room = 'Great Hall'
last_room = []

# A welcome message to the player
print('Welcome to the game!')

# Loop to check if player is alive
while player_alive == True:

    # Loop to check if player wants to continue playing
    while player_continue == True:

        # Outputs current room at beginning of each loop while player wants to continue playing
        print(f'You are currently in the {current_room}')

        # checks to see if current room is exit, asks player if they really want to quit
        if current_room == 'exit':
            continue_prompt = str(input(f'Are you sure you want to exit?\nEnter y to exit\nEnter n to return to {last_room[-1]}\n'))

            # If player enters y, turns player_continue False, leads to GAME OVER message
            if continue_prompt == 'y':
                player_continue = False
                continue

            # If the player enters n, they're sent back to the room they were in before they entered the exit
            if continue_prompt == 'n':
                player_continue = True
                current_room = last_room[-1]

            # Repeats the "Are you sure...?" loop if an invalid input is entered
            else:
                print('Invalid input, try again:\n')
                continue

        # If player is in any room other than the exit, adds the current room to list of previous rooms
        # then outputs available moves from rooms dictionary
        else:
            last_room.append(current_room)
            print('Available moves:')
            for move,room in rooms[current_room].items():
                print('To go to the ' + room + ', enter ' + move)
            print('To leave the game, enter exit')

            # Assigns user input as a string to user_command (command) variable
            user_command = str(input('Which direction would you like to move?\n'))

            # Checks for exit first, goes to exit room, prompts "Are you sure...?" loop
            if user_command == 'exit':
                current_room = 'exit'

            # Then checks if command is valid in rooms dictionary,
            # If valid, prints move confirmation message and changes current_room variable
            elif user_command in rooms[current_room]:
                print(f'You moved {user_command}')
                current_room = rooms[current_room].get(user_command)

            # If invalid, prints message and restarts loop, Asks which way to move again
            else:
                print('Invalid input, try again.')

    # GAME OVER message if user chooses not to continue playing (player_continue = False)
    else:
        print('You exited the game successfully\nThank you for playing\nGAME OVER')
        break

# GAME OVER message if player dies (player_alive = False)
else:
    print('You Died\nGAME OVER')


"""
Assignment Instructions, do not delete below this line
develop code to meet the required functionality, by prompting the player to enter commands to move between the rooms or exit the game. 
To achieve this, you must develop the following:
A gameplay loop that includes:
    Output that displays the room the player is currently in
    Decision branching that tells the game how to handle the different commands. 
        The commands can be to either move between rooms (such as go North, South, East, or West) or exit.
    If the player enters a valid “move” command, the game should use the dictionary to move them into the new room.
    If the player enters “exit,” the game should set their room to a room called “exit.”
    If the player enters an invalid command, the game should output an error message to the player (input validation).
    A way to end the gameplay loop once the player is in the “exit” room

TIP: Use the pseudocode or flowchart that you designed in Step #4 of Project One to help you develop your code.

As you develop, you should debug your code to minimize errors and enhance functionality.
After you have developed all of your code, be sure to run the code to test and make sure it is working correctly.
    What happens if the player enters a valid direction? Does the game move them to the correct room?
    What happens if the player enters an invalid direction? Does the game provide the correct output?
    Can the player exit the game?
"""