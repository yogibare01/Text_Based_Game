# commit change test

room = 20
alive = 'true'
"""

player_lives = 1
play_loc = 'ul'
dir_move = ''
death_message = 'You Died!'

def messages(room_name):
    message = ''
    if room_name == kids_room:
        message = input('You are now in the kids room. What would you like to do next? \n')
    elif room_name == hall_way:
        message = input('You are now in the hallway. What would you like to do next? \n')
    return message

def hit_wall(dir_wall):
    wall = ''
    if dir_wall == 'w':
        wall = 'North'
    elif dir_wall == 'a':
        wall = 'West'
    elif dir_wall == 'd':
        wall = 'East'
    elif dir_wall == 's':
        wall = 'South'
    message = str(input(f'You ran into the {wall} wall, try again: '))
    return message

play_move = str(input('Please choose a direction to move'))

while player_restart == 'y'

    while player_lives >= 1:

        while play_loc == 'ul':
            if play_move == 'u':
                hit_wall('u')
            else:
                print('moved right')
                play_loc = uc
                messages(hall_way)

    else:
        player_restart = input('Would you like to try again?\n')

else:
    print('Game Over')

print('end')

"""
vector = ''

def map(room):
    d = '-------------\n'
    e = '|   |   |   |\n'
    l = '| X |   |   |\n'
    c = '|   | X |   |\n'
    r = '|   |   | X |\n'
    o = '    | X |    \n'
    p = '    -----    \n'

    map = ''
    if room == 11:
        map = f'MAP\n{d}{e}{d}{e}{d}{l}{d}'
    if room == 12:
        map = f'MAP\n{d}{e}{d}{l}{d}{e}{d}'
    if room == 13:
        map = f'MAP\n{d}{l}{d}{e}{d}{e}{d}'
    if room == 20:
        map = f'MAP\n{d}{e}{d}{e}{d}{e}{d}{o}{p}'
    if room == 21:
        map = f'MAP\n{d}{e}{d}{e}{d}{c}{d}'
    if room == 22:
        map = f'MAP\n{d}{e}{d}{c}{d}{e}{d}'
    if room == 23:
        map = f'MAP\n{d}{c}{d}{e}{d}{e}{d}'
    if room == 31:
        map = f'MAP\n{d}{e}{d}{e}{d}{r}{d}'
    if room == 32:
        map = f'MAP\n{d}{e}{d}{r}{d}{e}{d}'
    if room == 33:
        map = f'MAP\n{d}{r}{d}{e}{d}{e}{d}'
    print(map)


def move(vector):
    global room
    w = 'w'
    a = 'a'
    s = 's'
    d = 'd'
    while alive == 'true':
        map(room)
        while room == 20:
            if vector == w:
                room += 1
                map(room)

            else:
                continue

        while room == 21:
            if vector == a:
                room -= 10
                map(room)
            if vector == s:
                print('The door is locked, you cannot escape.')
                continue



move(20)