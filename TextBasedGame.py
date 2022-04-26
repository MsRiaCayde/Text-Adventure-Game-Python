# Ria Cayde Labbe
# A dictionary for the rooms in Mothership
# The dictionary links a room to other rooms as well as what items are in the room.


rooms = {
        'Central Hub': {'North': 'SciOps', 'East': 'MedBay', 'South': 'Engineering Bay', 'West': 'Bridge', 'text': 'Your panicked rush has begun while in the [Central Hub].\nThe gentle hum of the ship is slowly waining as you look around frantically.\nTo the north is the [SciOps Division], to the East is the [MedBay], to the south is the [Engineering Bay], and to the west is the [Bridge].'},
        'Engineering Bay': {'North': 'Central Hub', 'South': 'Red Matter Core', 'item': 'Laser Cutter', 'text': 'The [Engineering Bay] is a hot and muddled place. Your Chief Engineer scurries about, trying to figure out what is causing the gravity engines to dampen.\nAn assortment of tools lays across the halls,\nmost notably is the standard issue [Laser Cutter] that can help anyone in a pinch.\nThe [Central Hub] is to the north, and the [Red Matter Core] is to the south... Though you probably shouldnt go that way yet.'},
        'MedBay': {'West': 'Central Hub', 'item': 'MedGel', 'text': 'The [Medbay] is by far the cleanest area of the ship, you can not be too sure of what you might need\nbut your Medical expert suggests grabbing some [MedGel] in case of any potential injures.\nYou can only head back to the [Central Hub] in the west.'},
        'SciOps': {'East': 'Teleportation Division', 'South': 'Central Hub', 'West': 'Armory', 'item': 'Personal Shield Generator', 'text': '[SciOps] houses some of the most technologically advanced personnel on this ship, well,\noutside of the Diplomat on the [Bridge].\nYou head over to your designated locker and open it up.\nThere are a few photos and trinkets, but it also contains a [Personal Shield Generator] that might come in handy.\nHeading east will place you in the [Teleportation Division],\nheading west will put you in the [Armory], and heading south will return you to the [Central Hub].'},
        'Teleportation Division': {'West': 'SciOps', 'item': 'Interdimensional Pressure Suit', 'text': 'The Teleportation Division is your fastest way to travel,\nbut they also have a few [Interdimensional Pressure Suit]s that are sure to be needed to cross the rift thats opened in the Red Matter Core'},
        'Armory': {'East': 'SciOps', 'item': 'Pulse Blaster', 'text': 'The [Armory] has the pungent scent of metallic fluids and plasma residue. A few of the officers are preparing themselves and you should probably do the same.\nOver along the wall are several racks of [Pulse Blasters].\nYou can only head east from here which will put you back in [SciOps]'},
        'Bridge': {'East': 'Central Hub', 'item': 'Interdimensional Scissors', 'text': 'The [Bridge] houses your most curious guest, one who can help you with this issue. Set along the recesses of the area is a small room with The Diplomat inside.\nTheir body drips with ethereal darkness as it scuffles about its quarters, turning to speak to you as you arrive.\n"Take this with you... Youre going to need it."\nFloating effortlessly in the air above its palm is a pair of [Interdimensional Scissors].\nYou can return east and reach the [Bridge]'},
        'Red Matter Core': {'North': 'Engineering Bay', 'item': 'Colour Out of Space'}  # Villain
    }


def intro_loop():
    # Main Menu and Command List
    print('---------------------------------')
    print('Mothership Text Adventure Game')
    print('---------------------------------')
    print('You take upon the role of the captain on Mothership. During the midst of your journey the engines have noticeably began to shut down.\nYour Red Matter Core has exhibited significant power fluctuations\nover the past hour and now, what you can only guess to be an interdimensional portal, has opened up in the core.\nIt now lies on you to collect the [6] pieces of equipment from all over the ship that will needed to become the savior of this ship and your crew.')
    print('---------------------------------')
    print('Commands!')
    print('---------------------------------')
    print('Movement: go North, go East, go South, go West\n' + 'Add to Inventory: get [item name]\n' + 'Misc: exit')
    print('---------------------------------')


def player_room():
    print('*********************************')
    print('You are in the {}'.format(currentRoom))
    print('Inventory: {}'.format(playerInventory))
    print('*********************************')
    print(rooms[currentRoom].get('text'))
    print('*********************************')


def win_room():
    print('As you enter through the seemingly anomalous entrance, You are fully prepared to face the dangers ahead.\nCrossing over in to an alternate dimensional space is no easy feat, but the biggest challenge is the creature infront of you.\nPerched around your engine is a Color Out of Space, its form pulsating around the Red Matter Core as it drains its energy.\nYou take hold of your equipment and dredge forward towards core control systems. You steadily remove the Laser Cutter and use it so wire the core to collapse in onto itself, all whilst protecting yourself against the black goo forms that crawl ever closer towards you.\nOnce you have the systems set you know that time is short, and the portal you came through is gone.\nYou take the Interdimensional Scissors from your side and cut a whole in the fabric of reality only\nto wake up laying on the floor of the Red Matter Core with your crew cheering with excitement.\nCongratulations')
    exit()


def loss_room():
    print('As you enter through the seemingly anomalous entrance, fate itself seems to bar you from completing your tasks ahead.\nPerhaps next time you will bring forth the tools you need to be the saviour of your crew.')
    print('Your ship drifts endlessly into the void...\n' + 'Game Over')
    exit()


# Make adding item to inventory, with checking tif it was grabbed so that it can only be grabbed once
# Update if/elif/else commands to reflect rooms (just time consuming, not actually difficult)

# start player in Central Hub
currentRoom = 'Central Hub'
playerMove = ''
playerInventory = []
playerInventoryCount = 0
intro_loop()


while currentRoom != 'Exit':
    while currentRoom == 'Central Hub':
        player_room()
        playerMove = input('Enter command:\n')
        if playerMove not in ['go South', 'go south', 'Exit', 'exit', 'go North', 'go north', 'go East', 'go east', 'go West', 'go west']:
            print('ERROR: Invalid Command.')
        elif playerMove in ['Exit', 'exit']:
            currentRoom = 'Exit'
            print('Your ship drifts endlessly into the void...\n' + 'Game Over')
        elif playerMove in ['go South', 'go south']:
            currentRoom = 'Engineering Bay'
        elif playerMove in ['go North', 'go north']:
            currentRoom = 'SciOps'
        elif playerMove in ['go East', 'go east']:
            currentRoom = 'MedBay'
        elif playerMove in ['go West', 'go west']:
            currentRoom = 'Bridge'
    while currentRoom == 'Engineering Bay':
        player_room()
        playerMove = input('Enter Command:\n')
        if playerMove not in ['go North', 'go north', 'go South', 'go south', 'Exit', 'exit', 'Get Laser Cutter', 'get laser cutter', 'get Laser Cutter']:
            print('ERROR: Invalid Command.')
        elif playerMove in ['Exit', 'exit']:
            currentRoom = 'Exit'
            print('Your ship drifts endlessly into the void...\n' + 'Game Over')
        elif playerMove in ['go North', 'go north']:
            currentRoom = 'Central Hub'
        elif playerMove in ['go South', 'go south']:
            currentRoom = 'Red Matter Core'
        elif playerMove in ('Get Laser Cutter', 'get laser cutter', 'get Laser Cutter') and playerInventory.count(['Laser Cutter']) == 0:
            item = playerMove.title().split(' ', 1)
            playerInventory.append(item[1:])
            del item
            playerInventoryCount += 1
    while currentRoom == 'Red Matter Core':
        if playerInventoryCount == 6:
            win_room()
        else:
            loss_room()
    while currentRoom == 'MedBay':
        player_room()
        playerMove = input('Enter Command:\n')
        if playerMove not in ['go West', 'go west', 'Exit', 'exit', 'Get', 'get', 'Get MedGel', 'get medgel', 'get Medgel']:
            print('ERROR: Invalid Command.')
        elif playerMove in ['Exit', 'exit']:
            currentRoom = 'Exit'
            print('Your ship drifts endlessly into the void...\n' + 'Game Over')
        elif playerMove in ['go West', 'go west']:
            currentRoom = 'Central Hub'
        elif playerMove in ('Get MedGel', 'get medgel', 'get Medgel') and playerInventory.count(['Medgel']) == 0:
            item = playerMove.title().split(' ', 1)
            playerInventory.append(item[1:])
            del item
            playerInventoryCount += 1
    while currentRoom == 'SciOps':
        player_room()
        playerMove = input('Enter Command:\n')
        if playerMove not in ['go East', 'go east', 'go South', 'go south', 'go West', 'go west', 'Exit', 'exit', 'get Personal Shield Generator', 'get Personal Shield generator',
                              'get Personal shield generator', 'get personal shield generator']:
            print('ERROR: Invalid Command.')
        elif playerMove in ['Exit', 'exit']:
            currentRoom = 'Exit'
            print('Your ship drifts endlessly into the void...\n' + 'Game Over')
        elif playerMove in ['go East', 'go east']:
            currentRoom = 'Teleportation Division'
        elif playerMove in ['go South', 'go south']:
            currentRoom = 'Central Hub'
        elif playerMove in ['go West', 'go west']:
            currentRoom = 'Armory'
        elif playerMove in ('get Personal Shield Generator', 'get Personal Shield generator', 'get Personal shield generator', 'get personal shield generator') \
                and playerInventory.count(['Personal Shield Generator']) == 0:
            item = playerMove.title().split(' ', 1)
            playerInventory.append(item[1:])
            del item
            playerInventoryCount += 1
    while currentRoom == 'Armory':
        player_room()
        playerMove = input('Enter Command:\n')
        if playerMove not in ['go East', 'go east', 'Exit', 'exit', 'Get Pulse Blaster', 'get Pulse Blaster', 'get Pulse blaster', 'get pulse blaster']:
            print('ERROR: Invalid Command.')
        elif playerMove in ['Exit', 'exit']:
            currentRoom = 'Exit'
            print('Your ship drifts endlessly into the void...\n' + 'Game Over')
        elif playerMove in ['go East', 'go east']:
            currentRoom = 'SciOps'
        elif playerMove in ('Get Pulse Blaster', 'get Pulse Blaster', 'get Pulse blaster', 'get pulse blaster') and playerInventory.count(['Pulse Blaster']) == 0:
            item = playerMove.title().split(' ', 1)
            playerInventory.append(item[1:])
            del item
            playerInventoryCount += 1
    while currentRoom == 'Teleportation Division':
        player_room()
        playerMove = input('Enter Command:\n')
        if playerMove not in ['go West', 'go west', 'Exit', 'exit', 'Get Interdimensional Pressure Suit', 'get Interdimensional pressure suit', 'get Interdimensional Pressure suit',
                              'get interdimensional pressure suit']:
            print('ERROR: Invalid Command.')
        elif playerMove in ['Exit', 'exit']:
            currentRoom = 'Exit'
            print('Your ship drifts endlessly into the void...\n' + 'Game Over')
        elif playerMove in ['go West', 'go west']:
            currentRoom = 'SciOps'
        elif playerMove in ('Get Interdimensional Pressure Suit', 'get Interdimensional pressure suit', 'get Interdimensional Pressure suit', 'get interdimensional pressure suit') \
                and playerInventory.count(['Interdimensional Pressure Suit']) == 0:
            item = playerMove.title().split(' ', 1)
            playerInventory.append(item[1:])
            del item
            playerInventoryCount += 1
    while currentRoom == 'Bridge':
        player_room()
        playerMove = input('Enter Command:\n')
        if playerMove not in ['go East', 'go east', 'Exit', 'exit', 'Get Interdimensional Scissors', 'get Interdimensional scissors', 'get interdimensional scissors']:
            print('ERROR: Invalid Command.')
        elif playerMove in ['Exit', 'exit']:
            currentRoom = 'Exit'
            print('Your ship drifts endlessly into the void...\n' + 'Game Over')
        elif playerMove in ['go East', 'go east']:
            currentRoom = 'Central Hub'
        elif playerMove in ('Get Interdimensional Scissors', 'get Interdimensional scissors', 'get interdimensional scissors') and playerInventory.count(['Interdimensional Scissors']) == 0:
            item = playerMove.title().split(' ', 1)
            playerInventory.append(item[1:])
            del item
            playerInventoryCount += 1
