# Chris Bare
#A dictionary for the simplified dragon text game
#The dictionary links a room to other rooms.
rooms = {
        'Great Hall': {'South': 'Bedroom'},
        'Bedroom': {'North': 'Great Hall', 'East': 'Cellar'},
        'Cellar': {'West': 'Bedroom'}
    }
curr_room = ''
player_move = ''
player_move = str(input('Which way would you like to move?, \n'))

def move(butt):
    global curr_room
    curr_room = rooms[butt]
    print(curr_room)

while (user_input.lower() != 'exit'):
    print(curr_room)
    butt = str(input('Which way would you like to move?, \n'))
    move(butt)
else:
    print('Thank you for playing. Game Over')








"""
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