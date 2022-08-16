# Chris Bare

# importing time module for dramatic effect later
import time

# rooms dictionary rebuilt to include map and story elements as well as more rooms
rooms = {
    'entryway':
        {'Map': f'MAP\n'
                f'_____________\n'
                f':   :   :   |\n'
                f'|- -+- -+- -|\n'
                f'|   |   |   :\n'
                f'|- -+---+- -|\n'
                f'|   :   :   |\n'
                f'----+- -+----\n'
                f'    | X |    \n'
                f'    -----    \n',
         'Inspect':
             'You\'re at the front doorway.\n'
             'Just a door to your North,\na wall to the East and West,\nand a full moon beaming down on your back.',
         'Items':
             [],
         'Moves':
             {'North': 'foyer',
              'South': 'exit'}},
    'foyer':
        {'Map': f'MAP\n'
                f'_____________\n'
                f':   :   :   |\n'
                f'|- -+- -+- -|\n'
                f'|   |   |   :\n'
                f'|- -+---+- -|\n'
                f'|   : X :   |\n'
                f'----+- -+----\n'
                f'    |   |    \n'
                f'    -----    \n',
         'Inspect':
             'The architect must have thought this would be a fancy addition.\n'
             'You hear a loud growl emanating from the north wall in this room',
         'Items':
             [],
         'Moves':
             {'East': 'study',
              'South': 'entryway',
              'West': 'kitchen'}},
    'kitchen':
        {'Map': f'MAP\n'
                f'_____________\n'
                f':   :   :   |\n'
                f'|- -+- -+- -|\n'
                f'|   |   |   :\n'
                f'|- -+---+- -|\n'
                f'| X :   :   |\n'
                f'----+- -+----\n'
                f'    |   |    \n'
                f'    -----    \n',
         'Inspect':
             'It looks like someone was here recently.\nThe pizza rolls are still warm.',
         'Items':
             ['pizza rolls'],
         'Moves':
             {'North': 'gym',
              'East': 'foyer'}},
    'gym':
        {'Map': f'MAP\n'
                f'_____________\n'
                f':   :   :   |\n'
                f'|- -+- -+- -|\n'
                f'| X |   |   :\n'
                f'|- -+---+- -|\n'
                f'|   :   :   |\n'
                f'----+- -+----\n'
                f'    |   |    \n'
                f'    -----    \n',
         'Inspect':
             'The owner left a mess in the gym.\n'
             'Better pick up the exercise bands so nobody trips on them.\n'
             'there\'s that growling again. Now it\'s coming from the East wall',
         'Items':
             ['band'],
         'Moves':
             {'North': 'guest bedroom',
              'South': 'kitchen'}},
    'guest bedroom':
        {'Map': f'MAP\n'
                f'_____________\n'
                f': X :   :   |\n'
                f'|- -+- -+- -|\n'
                f'|   |   |   :\n'
                f'|- -+---+- -|\n'
                f'|   :   :   |\n'
                f'----+- -+----\n'
                f'    |   |    \n'
                f'    -----    \n',
         'Inspect':
             'Just a normal bedroom... But there\'s a draft coming from the West wall.',
         'Items':
             ['handle'],
         'Moves':
             {'East': 'hallway',
              'South': 'gym',
              'West': 'wall maybe'}},
    'hallway':
        {'Map': f'MAP\n'
                f'_____________\n'
                f':   : X :   |\n'
                f'|- -+- -+- -|\n'
                f'|   |   |   :\n'
                f'|- -+---+- -|\n'
                f'|   :   :   |\n'
                f'----+- -+----\n'
                f'    |   |    \n'
                f'    -----    \n',
         'Inspect':
             '',
         'Items':
             [],
         'Moves':
             {'East': 'bathroom',
              'South': 'boss arena',
              'West': 'guest bedroom'}},
    'bathroom':
        {'Map': f'MAP\n'
                f'_____________\n'
                f':   :   : X |\n'
                f'|- -+- -+- -|\n'
                f'|   |   |   :\n'
                f'|- -+---+- -|\n'
                f'|   :   :   |\n'
                f'----+- -+----\n'
                f'    |   |    \n'
                f'    -----    \n',
         'Inspect':
             'Nice looking bathroom with the pieces of a chewed up belt in the floor',
         'Items':
             ['belt'],
         'Moves':
             {'South': 'master bedroom',
              'West': 'hallway'}},
    'master bedroom':
        {'Map': f'MAP\n'
                f'_____________\n'
                f':   :   :   |\n'
                f'|- -+- -+- -|\n'
                f'|   |   | X :\n'
                f'|- -+---+- -|\n'
                f'|   :   :   |\n'
                f'----+- -+----\n'
                f'    |   |    \n'
                f'    -----    \n',
         'Inspect':
             'The master bedroom as a draft in the East wall.\n',
         'Items':
             [],
         'Moves':
             {'North': 'bathroom',
              'East': 'wall probably',
              'South': 'study'}},
    'study':
        {'Map': f'MAP\n'
                f'_____________\n'
                f':   :   :   |\n'
                f'|- -+- -+- -|\n'
                f'|   |   |   :\n'
                f'|- -+---+- -|\n'
                f'|   :   : X |\n'
                f'----+- -+----\n'
                f'    |   |    \n'
                f'    -----    \n',
         'Inspect':
             'Not many homes have a study any more.\n'
             'This one also has a working flintlock pistol.\n'
             'It could be useful if only you could find powder and bullets.',
         'Items':
             ['flintlock'],
         'Moves':
             {'North': 'master bedroom',
              'West': 'foyer'}},
    'boss arena':
        {'Map': f'MAP\n'
                f'_____________\n'
                f':   :   :   |\n'
                f'|- -+- -+- -|\n'
                f'|   | X |   :\n'
                f'|- -+---+- -|\n'
                f'|   :   :   |\n'
                f'----+- -+----\n'
                f'    |   |    \n'
                f'    -----    \n',
         'Inspect':
             'Welcome to the boss arena.\n'
             'You can finally see that the growl is that of a werewolf.\n'
             'On the bright side, it\'s asleep in the corner which buys you time\n'
             'If you think you have all the correct items, enter get\n'
             'If you need more time, run by moving to another room.',
         'Items':
             ['possible death'],
         'Moves':
             {'North': 'hallway'}},
    'wall maybe':
        {'Map': f'MAP\n'
                f'________________\n'
                f'|  :   :   :   |\n'
                f'|  |- -+- -+- -|\n'
                f'|  |   |   |   :\n'
                f'|  |- -+---+- -|\n'
                f'|  |   :   :   |\n'
                f'|  ----+- -+----\n'
                f'|  : X |   |    \n'
                f'------------    \n',
         'Inspect':
             'You moved through a secret passage in the wall\n'
             'into a small room to the West of the entryway\n'
             'It\'s cold, damp, and almost pitch black,\n'
             'but A dim light from the passage shows a small open canister of black powder\n'
             'This might be useful with a firearm and some bullets',
         'Items':
             ['gunpowder'],
         'Moves':
             {'West': 'guest bedroom'}},
    'wall probably':
        {'Map': f'MAP\n'
                f'_____________\n'
                f':   :   :   |\n'
                f'|- -+- -+- -|---\n'
                f'|   |   |   :  |\n'
                f'|- -+---+- -|  |\n'
                f'|   :   :   |  |\n'
                f'----+- -+----  |\n'
                f'    |   | X :  |\n'
                f'    ------------\n',
         'Inspect':
             'You moved through a secret passage in the wall\n'
             'into a small room to the East of the entryway\n'
             'It\'s cold, damp, and almost pitch black,\n'
             'but A dim light from the passage shows the glimmer of something metalic\n'
             'They\'re bullets that seem to be made of silver\n'
             'This might be useful with a firearm and some bullets',
         'Items':
             ['bullets'],
         'Moves':
             {'East': 'master bedroom'}}}

# Assigning variables
# Booleans for alive and continue to keep loops working while true
player_alive = True
player_continue = True

# Starting on the entryway/porch
current_room = 'entryway'

# initialize user inventory list
user_items = []

# initialized choice variable
choice = ''


def hud(current_room):
    # prints a divider, a map, the name of the room, items in room, and user inventory
    print('--------------------------------------')
    print(rooms[current_room]['Map'])
    print(f'You are in the {current_room}')
    if len(rooms[current_room]['Items']) > 0:
        print(f'Items in this room:')
        print(rooms[current_room]['Items'])
    else:
        print('There are no items in this room')
    if len(user_items) > 0:
        print(f'Player Inventory:\n{user_items}')
    else:
        print(f'Player Inventory:\nEMPTY')


# main gameplay loop. Main boolean executes if player wants to continue.
while player_continue == True:

    # Next level boolean executes if player is alive.
    if player_alive == True:

        # HUD prints at the beginning of each loop and is based on current room
        hud(current_room)

        # Asks for main action choice based on context of room
        if len(rooms[current_room]['Items']) > 0:
            choice = input('What would you like to do?\nYou can move, get, inspect, or exit').lower()
        else:
            choice = input('What would you like to do?\nYou can move, inspect, or exit').lower()

        # if player chooses exit, continue prompt loop executes to give them a second chance.
        while choice == 'exit':
            continue_prompt = str(input(f'Are you sure you want to exit?\nEnter y to exit\nEnter n to continue'))
            if continue_prompt == 'y':
                player_continue = False
                break
            elif continue_prompt == 'n':
                player_continue = True
                break
            else:
                print('Invalid input, try again:\n')

        # if player chooses move, the move loop executes to ask which direction
        while choice == 'move':
            print('Available moves:')
            for move, room in rooms[current_room]['Moves'].items():
                print('To go to the ' + room + ', enter ' + move)
            move = rooms[current_room]['Moves'].get(input('choose a direction').title(), 'invalid move')
            if move != 'invalid move':
                current_room = move
                break
            else:
                print('Invalid move, try again')
                continue

        # Inspect reads commentary about the room if any exists.
        if choice == 'inspect':
            print(rooms[current_room]['Inspect'])

        # 'get' gets the item from the room and puts it in player inventory except
        # in boss arena in which 'get' begins the final boss battle.
        if choice == 'get':
            if current_room == 'boss arena':
                print('You picked up the beasts paw to try to sneak the exit key from its grasp.')
                time.sleep(3)
                print('Although it was a heavy sleeper this entire time, it now hungers for your flesh.')
                time.sleep(3)
                print('You do what you can to get away, but it jumps between you and the exit.')
                time.sleep(3)
                print('The fight for your life has begun!')
                time.sleep(3)
                if 'bullets' and 'flintlock' and 'gunpowder' in user_items:
                    print('While traversing the halls of this home, you gathered the parts to build\n'
                          'a working weapon against just such a creature, The flintlock pistol with black powder,\n'
                          'a scrap of your shirt for patching, and silver bullets.\n'
                          'You draw the weapon, cock the hammer,\n'
                          'and..... \n')
                    time.sleep(6)
                    print('CLICK, TSSSS... The powder was damp from being open in the secret room too long!\n'
                          'The spark from the flint was enough to confuse it for a second, but\n'
                          'You feel the overwhelming sense of dread overtaking you because this was your last hope!')
                    time.sleep(6)
                    print('OR WAS IT?!!!!')
                    time.sleep(3)
                    if 'handle' and 'band' in user_items:
                        print('You remember the other items you picked up from around the house.\n'
                              'Like a cross between Underworld and McGuiver, you fashion together a slingshot\n'
                              'from the exercise band, slingshot handle, and another piece of belt.\n'
                              'you then shoot one of the silver bullets at the beast.')
                        time.sleep(2)
                        print('Headshot! It falls to the floor with a loud thud. You\'re relieved and begin walking\n'
                              'to the exit.')
                        time.sleep(10)
                        print('You see it arise from the corner of your eye. You merely stunned it,\n'
                              'now you need to think fast!')
                        time.sleep(2)
                        print('What will you do?!')
                        time.sleep(2)
                        print(
                            'There was nothing you could do. You\'ve all seen the movies. Werewolves are insanely fast')
                        time.sleep(2)
                        print(
                            'The werewolf grabs you by the backpack and throws you at the exit door, breaking the straps')
                        time.sleep(10)
                        if 'pizza rolls' in user_items:
                            print('You\'re nearly knocked out, but not eaten. What could have happened?')
                            time.sleep(3)
                            print('As soon as you get your bearings, you notice that the Werewolf prefers pizza rolls')
                            time.sleep(3)
                            print('The werewolf turns human. He explains that the pizza rolls were his and\n'
                                  'he made them shortly before going into his gaming room which he calls the\n'
                                  '"Boss Arena", Then he turned due to lack of pizza rolls.')
                            time.sleep(3)
                            print('You start to ask due to confusion, but he explains before you get the chance.\n'
                                  'His lycanthropy is treated using pizza rolls. No one knows why, but he has to\n'
                                  'snack on pizza rolls during full moons or he will turn and kill everything he can.')
                            time.sleep(3)
                            print(
                                'He goes on to explain that the issue tonight was that he was busy on an online game\n'
                                'and forgot to go to the air fryer to get the pizza rolls in time.\n'
                                'by the time he realized he was changing, it was too late, so he injected himself\n'
                                'with a heavy sedative to buy time and hoped a cloud would cover the moon.\n'
                                'as you know, that didn\'t happen, but you saved the day.\n'
                                'You ask if it would have just been easier if you just brought the pizza rolls.\n'
                                'He explains that he would have probably not ripped the bag if not for the frustration\n'
                                'caused by the other items... He thanks you and you are on your way.')
                            player_continue = False
                        else:
                            print('You awaken to being eaten alive feet first.')
                            player_alive = False
                    else:
                        print('You run for the door, the werewolf guts you with a single swipe through the abdomen')
                        player_alive = False
                else:
                    print(
                        'You were fully unprepared for this battle. You run around for a few seconds like a Scooby Doo\n'
                        'episode, but the werewolf isn\'t a person in a mask. It eats you alive as you try to fight it off.')
                    time.sleep(3)
                    print('You should have used the chance to go back and look for the other items.')
                    player_alive = False
            elif len(rooms[current_room]['Items']) > 0:
                user_items.append(rooms[current_room]['Items'][0])
                rooms[current_room]['Items'].pop()
                print(f'You picked up the {user_items[-1]}.')
            else:
                print('There are no items in this room')
    else:
        print('You Died\nThank you for playing\nGAME OVER')
        break
else:
    print('Thank you for playing\nGAME OVER')

# Code is written so that the affirmative of the loop leads to the win condition, most everything in 'else'
# is either an invalid entry, death, or game over message.
