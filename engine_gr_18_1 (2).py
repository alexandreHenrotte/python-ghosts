#-*- coding: utf-8 -*-

from typing import OrderedDict
import blessed, math, os, time
term = blessed.Terminal()

#Structure de données
number_magic = {10 :[[2,7], [14,7],
                    [1,2],
                    [14,8],
                    [6,2], 
                    [6,8],
                    [9,2],
                    [2,8]], 
                30:[[12,2], 
                    [8,2],
                    [8,7],
                    [2,2]],   
                50:[[13,14], 
                    [2,5],
                    [5,8],
                    [14,5]],
                100:[[8,6], 
                    [2,6]],
                500:[[7,8], 
                     [4,2]]
                }

player_1 = {"ghost" : [{"number_magic":int, "position": [int,int]} ,{}], 
        "number_magic" : int,
        "apparition" : (), 
        }

player_2 = {"ghost" : [{"number_magic":int, "position":[int,int]},{}], 
        "number_magic" : int,
        "apparition" : ()
        }
board_dictionnary = {20:20}

# the different functions used in the game
def read_file (file):
    '''returns dictionary of magic, dictonary's board and change the dictionary of player with spawn localisation and wich is changed with the file
    
    Parameters
    -----------
    file = file with information for the board

    Returns 
    --------
    magic_dictionnary, board dictionnary, players_dictionnary 
    
    Version 
    -------
    spécification : Michaëla Palanac (v1 : 15/02/2023)
    
    implémentation : Michaëla Palanac (v1 : 05/03/2023)
                    Michaëla Palanac (v2 : 20/03/2023)
    '''

    fh = open(file,'r') 
    lines = fh.readlines ()

    map = lines[1].split(" ")
    x = int(map[0])
    y = int(map[1])
    spawn_1 = lines[3].split(" ")
    x_1 = int(spawn_1[1])
    y_1 = spawn_1[2].split('\n')
    y_1 = int(y_1[0])
    spawn_1 = (x_1,y_1)

    spawn_2 = lines [4].split(" ")
    x_2 = int(spawn_2[1])
    y_2 = spawn_2[2].split('\n')
    y_2 = int(y_2[0])
    spawn_2 = (x_2,y_2)
    
    magic = lines [6:]
    data = []
    for elements in magic : 
        b = elements.split('\n')
        data.append(b)
    
    data_b = []
    for elements in data : 
        for i in elements : 
            del elements[0]
            data_b.append(i)
    
    data_c = []
    for elements in data_b : 
        f = elements.split(" ")
        data_c.append(f)
    
    data_d = []
    for elements in data_c : 
        for i in elements :
            g = int(i)
            data_d.append(g)
    
    number_magic = {}
    number_magic[10]= []
    ind10 = []
    for i in range(len(data_d)): 
        if data_d[i]== 10 :
            ind10.append(i)
    for i in ind10 : 
        g = data_d[i] 
        p = data_d[i-2]
        m = data_d[i-1]
        v = [p,m]
        number_magic[10].append(v)
        
    number_magic[30]= []
    ind30 = []
    for i in range(len(data_d)): 
        if data_d[i]== 30 :
            ind30.append(i)
    for i in ind30 : 
        g = data_d[i] 
        p = data_d[i-2]
        m = data_d[i-1]
        v = [p,m]
        number_magic[30].append(v)

    number_magic[50]= []
    ind50 = []
    for i in range(len(data_d)): 
        if data_d[i]== 50 :
            ind50.append(i)
    for i in ind50 : 
        g = data_d[i] 
        p = data_d[i-2]
        m = data_d[i-1]
        v = [p,m]
        number_magic[50].append(v)
        
    number_magic[100]= []
    ind100 = []
    for i in range(len(data_d)): 
        if data_d[i]== 100 :
            ind100.append(i)
    for i in ind100 : 
        g = data_d[i] 
        p = data_d[i-2]
        m = data_d[i-1]
        v = [p,m]
        number_magic[100].append(v)
            
            
    
    number_magic[500]= []
    ind500 = []
    for i in range(len(data_d)): 
        if data_d[i]== 500 :
            ind500.append(i)
    for i in ind500 : 
        g = data_d[i] 
        p = data_d[i-2]
        m = data_d[i-1]
        v = [p,m]
        number_magic[500].append(v)
    
    board_dictionnary = {"largeur" : x,"hauteur" : y}
    
    player_1 = {"ghost" : [{"number_magic":100, "position": [int,int]} ,{}], 
        "number_magic" : int,
        "apparition" : (spawn_1), 
        }

    player_2 = {"ghost" : [{"number_magic":100, "position":[int,int]},{}], 
        "number_magic" : int,
        "apparition" : (spawn_2)
        }
    return number_magic, board_dictionnary, player_1, player_2

def board(player_1, player_2, number_magic, board_dictionnary):
    """affiche the board with the magic points and the ghost and spawn of each player
    Parameters
    ----------
    player_1: the first player's dictionnary
    player_2: the second player's dictionnary
    number_magic: the magic points dictionnary

    Version
    -------
    Specification:  Palanac Michaela (V. 10/03/23)
                    Van Kerm Zélie (v.2 24/03/23)
    Implementation: Palanac Michaela (v.1 11/03/2023)
                    Palanac Michaela (v. 24/03/23)
                    Van Kerm Zélie (v. 24/03/23)
                    Van Kerm Zélie (v. 26/03/23)
                    Palanac Michaëla (v. 27/03/2023)


    """
    import blessed, random, time
    term = blessed.Terminal()

    print(term.home + term.clear + term.hide_cursor)

    #define position of the symbol
    x=0
    y=0
    
    #numbers on top
    print("  ", end='')
    for n in range(1,21):
        if n<=9:
            print(" " + str(n)+ " ", end='')
        else:
            print(" " + str(n), end='')
    print()
    for x in range(1,board_dictionnary[0]+1):
    #numbers on the side
        if x<=9:
            print(' ' + str(x), end='')
        else:
            print(str(x), end='')
    
        for y in range(1, board_dictionnary[1]+1):
        #conditions numbers for a checkerboard
            if (x+y)%2 == 0:
                print(term.on_purple + '   ' + term.normal, end='')
            else:
                print(term.on_pink + '   ' + term.normal, end='')
            
        print()

    #add the magic points
    for e in number_magic:
        for a in range (len(number_magic[e])):
            magic_bag = number_magic[e][a]
            if e == 10:
                print(term.red_on_yellow + term.move_xy(magic_bag[0]*3-1, magic_bag[1]+1) + ' 10')
            elif e == 30:
                print(term.move_xy(magic_bag[0]*3-1, magic_bag[1]+1) + ' 30')
            elif e == 50:
                print(term.move_xy(magic_bag[0]*3-1, magic_bag[1]+1) + ' 50')
            elif e == 100:
                print(term.move_xy(magic_bag[0]*3-1, magic_bag[1]+1) + '100')
            elif e == 500:
                print(term.move_xy(magic_bag[0]*3-1, magic_bag[1]+1) + '500')

    #add the spawn of each player. player 1: blue and player 2: red
    spawn_1 = player_1["apparition"]
    print(term.move_xy(spawn_1[0]*3-1, spawn_1[1]+1) + term.on_cyan + '   ')
    spawn_2 = player_2["apparition"]
    print(term.move_xy(spawn_2[0]*3-1, spawn_2[1]+1) + term.on_red + '   ')

    #add each player's ghost
    for g in range(len(player_1["ghost"])):
        ghost_1 = player_1["ghost"][g]["position"]
        if player_1['ghost'][g]['number_magic'] > 10:
            print(term.on_cyan + term.move_xy(ghost_1[0]*3-1, ghost_1[1]+1) + '👻 ')
        else:
            print(term.on_darkblue + term.move_xy(ghost_1[0]*3-1, ghost_1[1]+1) + '👻 ')

    for p in range(len(player_2["ghost"])):
        ghost_2 = player_2["ghost"][p]['position']
        if player_2['ghost'][p]['number_magic'] > 10:
            print(term.on_red + term.move_xy(ghost_2[0]*3-1, ghost_2[1]+1) + '👻 ')
        else:
            print(term.on_darkred + term.move_xy(ghost_2[0]*3-1, ghost_2[1]+1) + '👻 ')

    #magic of each olayer on the side of the board
    print(term.normal + term.move_xy(21*3,1) + term.darkblue + 'magic player 1: ' + str(player_1['number_magic']))
    print(term.normal + term.move_xy(21*3,2) + term.darkred +  'magic player 2: ' + str(player_2['number_magic']))
    print(term.move_xy(21, 24))

def get_human_orders(player) :
    """The ordre of the player
    Parameter:
    ---------
    players_id: the dictionary with the player (dict)
    board: the board with the information (dict)
    player: the player who play

    Return
    ------
    action: orders choose by the player (str)

    Version:
    -------
    Spécification: Naomi Amedegnato (v.1 09/03/23)
    Implémentation: Naomi Amedegnato (v.1 09/03/23)
    """
    action = input("What order you want to do %s ? " %player)
    return action

def verify_order(action):
    """checks if the same position r1-c1 is not reused in several orders

    Parameters 
    ---
    action : the order of the player (str)

    Returns 
    ---
    order : the order without duplicate positions r1-c1 (str)

    Version 
    ---
    specification : Alexandra Rousselle (23/03/2023)
    implementation :Alexandra Rousselle (v1 25/03/2023)
                    Alexandra Rousselle (v2 27/03/2023)
    """
    order_2 = action.split(' ')
    dic_order = {}
    positions = []
    for elem in order_2:
        position = elem.split(':')
        coordinates = position[0].split('-')
        coordinate = []
        for values in coordinates:
            coordinate.append(int(values))
        if coordinate not in positions:
            positions.append(coordinate)
            dic_order[elem] = coordinate
    order = []
    for orders in dic_order:
        order.append(orders)
    return order

def read_order(order, player):
    """read the orders and call the functions of each game phases. 
    Parameters
    ----------
    order: the order of the player
    player: the player who wants to execute the order
    
    Version
    -------
    Specification: Zélie Van Kerm (v.1 17/03/23)
    Implementation: Zélie Van Kerm (v.1 17/03/23)
                    Zélie Van Kerm (v.2 20/03/23)
    """
    new_order = verify_order(order)
    for element in new_order: 
        if ':x' in element:
            attack(element, player_1, player_2)
        elif ':@' in element:
            shift_ghost(element, player)
        elif ':$' in element:
            take_magic(number_magic, player, order)
        elif 'ghost' in element:
            create_ghost(player)
        elif ':+' in element:
            regenerate_ghost (element, player)

def get_distance(pos1_x,pos1_y,pos2_x,pos2_y):
    """Calculate the range between two points on the Map

    Parameters
    ----------
    pos1_x : position x from start (int)
    pos1_y : position y from start (int)
    pos2_x : position x from finish (int)
    pos2_y : position y from finish (int)

    Return
    ------
    range : range between first and last position (int)

    Version
    -------
    Specification :  Naomi Amedegnato (v.1 09/03/23)
    Implementation : Naomi Amedegnato (v.1.09/03/23)
    """
    if pos1_x > pos2_x:
        range_x = pos1_x-pos2_x
    else:
        range_x = pos2_x-pos1_x

    if pos1_y >= pos2_y:
        range_y = pos1_y-pos2_y
    else:
        range_y = pos2_y-pos1_y

    if range_x > range_y:
        range = range_x
    else:
        range = range_y

    return range

def create_ghost (player) :
    """makes a ghost appear on the set if there is not a ghost yet  
    Parameters 
    ---
    player : the player who wants to play by making his ghosts appear (dict)
    
    Returns
    ---
    player['ghost'] : new player dictionnary containing ghosts information (list of dict) 
    
    Raises
    ---
    If there is a ghost yet 

    Version
    ---
    specification : Alexandra Rousselle (06/03/2023)
    implementation : Alexandra Rousselle (08/03/2023)
    """
    position = list(player["apparition"])
    other_ghost = {"number_magic": 100, "position": position}
    check_ghost = is_there_a_ghost(player, position)
    if check_ghost == False :
        if player["number_magic"]>=300:
            player['ghost'].append(other_ghost)
            return player['ghost']
        else :
            print('you do not have enough money and your ghost dictionary is staying %s'%player)
    else :
        print('there is someone yet and your ghost dictionary is staying %s'%player)

def take_magic(number_magic, player, order):
    """takes the magic source by increasing the magic points of the player 

    Parameters 
    ---
    number_magic : the number of magic in each case (dict)
    player : the player who wants to play with its magic points in the game and the list of its ghost that we want to see (dict)
    order : order of the player (str)

    Returns 
    ---
    magic : magic points of the player (int)

    Version 
    ---
    specification : Alexandra Rousselle (13/03/2023)
    implementation : Alexandra Rousselle (23/03/2023)
    """
    coordinates = []
    for element in order:
        if ':$' in element:
            index = element.index(':$') #after autorisation of using index()
            a, b = map(int, element[:index].split('-'))
            coordinates.append([a, b])
    #Verify if the ghost's position is in the ghost position dictionary and if it corresponds to a position of a magic point
    magic_points = 0
    for element in range(0, len(player['ghost'])):
        for numbers in number_magic:
            for coordinates in number_magic[numbers]:
                for position in coordinates:
                    if position == player['ghost'][element]["position"] and position == coordinates:
                        magic_points += numbers
                        number_magic[numbers].remove(coordinates)
    player["number_magic"] += magic_points
    magic = player["number_magic"]
    return magic
            
def is_there_a_ghost(player, position) : 
    """check if there is already a ghost at a position 

    Parameters 
    ---
    player : the player who wants to play with its appearance in the game and the list of its ghost that we want to see (dict)
    position : position to consider (list)

    Returns
    ---
    is_there_a_ghost : True or False

    Version 
    ---
    specification : Alexandra Rousselle (03/03/2023)
                    Zélie Van Kerm (v.2 20/03/23)
                    Alexandra Rousselle (v.3 21/03/2023)
    implementation :Alexandra Rousselle (v.1 03/03/2023)
                    Zélie Van Kerm (v.2 20/03/23)
                    Alexandra Rousselle (v.3 21/03/2023)
    """
    for element in range (len(player['ghost'])):
        if position == player['ghost'][element]["position"]:
            return True
    return False 

def find_ghost(position, player):
    """ see if there is a ghost on a specific place and return the index of the ghost from one of the player's list of ghost
    Parameters
    ----------
    position: the position where we want to check if there is a ghost or not (list)
    player: the player's dictionary containing the list of his ghost (dict)
    
    Returns
    -------
    x: the index of the ghost (int)
    -99: if there is no ghost on the position(int)

    Version
    -------
    Specification: Zélie Van Kerm (v.1 17/03/23)
    Implementation: Zélie Van Kerm (v.1 17/03/23)
    """
    for x in player:
        if position == player['ghost'][x]['position']:
            return(x) 
    return(-99)

def shift_ghost (order, player) : 
    """move the place of ghosts 
    Parameters: 
    —----------
    order: the order of the player (list)
    player: dictonary of the player who play (dict)
    
    Returns : 
    —---------
    new_place_of_ghosts(dict)
    

    Version
    -------
    Spécification : Annie Muyengango Ineza (v.1 16/02/23)
                    Naomi Amedegnato (v.2 09/03/23)
    
    Implémentation : Naomi Amedegnato (v.3 20/03/23)
    """
    coordinates = []
    for element in order:
            if ':@' in element:
                index = element.index(':@')
                a, b = map(int, element[:index].split('-'))
                c, d = map(int, element[index+2:].split('-'))
                coordinates.append([[a, b], [c, d]])
    for element in coordinates:
        start_position=element[0]
        position=element[1]
        start_row= start_position[0]
        start_column= start_position[1]
        final_row=position[0]
        final_column=position[1]
        #print(final_row, final_column)
        if get_distance(start_row, start_column, final_row, final_column) >= 2:
                print('vous ne pouvez pas vous déplacer')
        else: 
            if is_there_a_ghost(player, [c,d]) == False:
                for ghost in player['ghost'] : 
                    row=ghost['position'][0]
                    column=ghost['position'][1]
                    if int(start_row) == row and int(start_column) == column :
                        ghost['position'][0]=int(final_row)
                        ghost['position'][1]= int(final_column)
    return player

def attack(order, player_1, player_2):
    """
    Parameters
    ----------
    order: the part of the order for the attack including the position of the attacker ghost and the postion where the attack will be executed(str)
    player_1: the first's player dictionary(dict)
    player_2: the second's player dictionary (dict)

    Return
    -------
    (the players' dictionnary)

    Version
    --------
    Specification: Alexandra Rousselle (v.1 16/02/23)
                    Zélie Van Kerm (v.2 13/03/23)
    Implementation: Zélie Van Kerm (v.1 13/03/23)
                    Zélie Van Kerm (v.2 17/03/23)
                    Zélie Van Kerm (v.3 19/03/23)

    """
    #separate the code to get the positions of the attacker and attacker
    position = order.split (':x')
    attacker_position = position[0].split('-')
    attacked_position = position[1].split('-')
    
    #see if the position of the attack is next to the position of the attacker and not ferther
    if get_distance(attacker_position[0], attacker_position[1], attacked_position[0], attacked_position[1]) >1:
        print ('your reach is not long enough')
    else:
        #see which ghost is making the attack, if there is a ghost to attack. Then give or get magic from player or ghost
        index_attacker= find_ghost(attacker_position, player_1['ghost'])
        index_attacked= find_ghost(attacked_position, player_2['ghost'])

        if index_attacker >=0 and index_attacked >=0:
            player_1['number_magic']+=10
            player_2['ghost'][index_attacked]['number_magic']-=10
        
        index_attacker= find_ghost(attacker_position, player_2['ghost'])
        index_attacked= find_ghost(attacked_position, player_1['ghost'])

        if index_attacker >=0 and index_attacked >=0:
            player_2['number_magic']+=10
            player_1['ghost'][index_attacked]['number_magic']-=10

def regenerate_ghost (player, order):

    """"buy magic for the ghost with the player’s money
    Parametre:
    ------------
    player : the player who want to add magic to his ghost (dict) 
    order: the order for regenerate the ghost (str)
    
    Return :
    -------
    (player's dictionnary)

    Version:
    --------
    Specification: Zélie Van Kerm (v.1 16/02/23)
                   Annie Muyengango Ineza (v.2 24/03/23)
    implémentation: Annie Muyengango Ineza (v.1 17/03/23)
                    Annie Muyengango Ineza (v.2 24/03/23)
    
    """
    data = order.split(':+')
    ghost_position = data[0].split('-')
    magic =data[1]
    if player ['number_magic'] < magic*2 :
        print('you do not have enough money')
    else:
        index = find_ghost(ghost_position, player)

        if index == -99:
            print('there is no ghost on this position')
        else:
            if player['ghost'][index]['number_magic'] == 100:
                print('your ghost still has all his magic')
            elif player['ghost'][index]['number_magic'] + magic > 100:
                maximum = 100 - player['ghost'][index]['number_magic']
                print('you cannot add that much magic to your ghost, your maximum is %s.' %maximum)
            else: 
                player['ghost'][index]['number_magic'] += magic

def delete_ghost(player): 
            for a in range(len(player['ghost'])):
                if a < len(player['ghost']) and player['ghost'][a]["number_magic"] == 0:
                    player['ghost'].remove(player['ghost'][a])
                    return(delete_ghost(player))
            else:
                return 

#AI function-------------------------------------------------------------------------------------------------------------------------------------------------------------------
def disponible_place (player, position, board_dictionnary) : 
    """Returns in a list disponible places 

    Parameters
    ---
    player : player's dictionary which contains the position of the ghost, his apparition on the board and his magic points (dict)
    position : position to consider (list)
    board_dictionnary : dictionnary with the size of the board (dict)

    Returns
    ---
    places : list of free places to go for the AI player (list)

    Version 
    ---
    spécification : Annie Munyengango (v1 20/03/2023)
                    Alexandra Rousselle (v2 22/03/2023)
    implementation : Alexandra Rousselle (23/03/2023)
    """
    places = []
    [a,b] = position
    board_width = board_dictionnary['largeur']
    board_height = board_dictionnary['hauteur']
    #East position
    position = [a,b+1]
    if position != list(player['apparition']) and is_there_a_ghost(player, position) == False :
        if b < board_height:
            places.append([a,b+1])
    #South East position 
    position = [a+1,b+1]
    if position != list(player['apparition']) and is_there_a_ghost(player, position) == False :
        if a < board_width and b < board_height:
            places.append([a+1,b+1])
    #South position
    position = [a+1,b]
    if position != list(player['apparition']) and is_there_a_ghost(player, position) == False :
        if a < board_width:
            places.append([a+1,b])
    #South West position 
    position = [a+1,b-1]
    if position != list(player['apparition']) and is_there_a_ghost(player, position) == False :
        if b > 1 and a < board_width:
            places.append([a+1,b-1])
    #West position
    position = [a,b-1]
    if position != list(player['apparition']) and is_there_a_ghost(player, position) == False :
        if b > 1:
            places.append([a,b-1]) 
    #North West position
    position = [a-1,b-1]
    if position != list(player['apparition']) and is_there_a_ghost(player, position) == False :
        if a > 1 and b > 1:
            places.append([a-1,b-1])
#North position 
    position = [a-1,b]
    if position != list(player['apparition']) and is_there_a_ghost(player, position) == False :
        if a > 1:
            places.append([a-1,b]) 
    #North East position
    position = [a-1,b+1]
    if position != list(player['apparition']) and is_there_a_ghost(player, position) == False :
        if a > 1 and b < board_height:
            places.append([a-1,b+1])                                         
    if len(places) == 0:
        places.append([a,b])
    return places

#Both functions are possible 
def ghost_around (position_ghost_AI, player):
    """""
    return to a list of ghosts around the AI 

    Parameters 
    ----------
    position_ghost_AI : postion of ghosts of AI (list)
    player : the player who is playing (dict)

    Return 
    ------
    ghosts : list of ghosts around the AI (list)

    Version 
    --------
    spécification : Annie Munyengango ( v1 20/03/2023)
                    Alexandra Rousselle (v2 25/03/2023)
    Implémentation: Naomi Amedegnato (v.2 22/03/23)
                    Alexandra Rousselle (v3 25/03/2023)
    """
    ghost=[]
    for element in range(0, len(player["ghost"])): 
        r=player['ghost'][element]['position'][0]
        c=player['ghost'][element]['position'][1]
    if [r+1,c] == position_ghost_AI:
        ghost.append([r,c])
    elif [r+1,c-1] == position_ghost_AI:
        ghost.append([r,c])
    elif [r,c-1] == position_ghost_AI:
        ghost.append([r,c])
    elif [r-1,c-1] == position_ghost_AI:
        ghost.append([r,c])
    elif [r-1,c] == position_ghost_AI:
        ghost.append([r,c])
    elif [r-1,c+1] == position_ghost_AI:
        ghost.append([r,c])
    elif [r,c+1] == position_ghost_AI:
        ghost.append([r,c])
    elif [r+1,c+1] == position_ghost_AI:
        ghost.append([r,c])
    return ghost

def find_ghost(player_1, player_2, group):
    """Find if there is a ghost near the ghost of the player

    Parameters 
    ---
    player_1 : first player's dictionary which contains the position of the ghost, his apparition on the board and his magic points (dict)
    player_2 : second player's dictionary which contains the position of the ghost, his apparition on the board and his magic points (dict)
    group : group of the player 1 or 2 
    
    Returns 
    ---
    positions : position of the ghost (list of lists)

    Version 
    ---
    specification : Alexandra Rousselle (19/03/2023)
    implementation : Alexandra Rousselle (21/03/2023)
    """ 
    positions = []
    if group == 1 :
        for element in range(0, len(player_1['ghost'])) : 
            a = player_1['ghost'][element]["position"][0]
            b = player_1['ghost'][element]["position"][1]
            for element in range(0, len(player_2['ghost'])) : 
                    c = player_2['ghost'][element]["position"][0]
                    d = player_2['ghost'][element]["position"][1]
                    #East position
                    if [c,d] == [a,b+1]:
                        positions += [c,d]
                    #South East position 
                    elif [c,d] == [a+1,b+1]:
                        positions += [c,d]
                    #South position
                    elif [c,d] == [a+1,b]:
                        positions += [c,d]
                    #South west position
                    elif [c,d] == [a+1,b-1]:
                        positions += [c,d]
                    #West position 
                    elif [c,d] == [a,b-1]:
                        positions += [c,d]
                    #North west position
                    elif [c,d] == [a-1,b-1]:
                        positions += [c,d]
                    #North position
                    elif [c,d] == [a-1,b]:
                        positions += [c,d]
                    #North east position 
                    elif [c,d] == [a-1,b+1]:
                        positions += [c,d]
            return positions
    if group == 2:
        for element in range(0, len(player_2['ghost'])) : 
            a = player_2['ghost'][element]["position"][0]
            b = player_2['ghost'][element]["position"][1]
            for element in range(0, len(player_1['ghost'])) : 
                    c = player_1['ghost'][element]["position"][0]
                    d = player_1['ghost'][element]["position"][1]
                    #East position
                    if [c,d] == [a,b+1]:
                        positions += [c,d]
                    #South East position 
                    elif [c,d] == [a+1,b+1]:
                        positions += [c,d]
                    #South position
                    elif [c,d] == [a+1,b]:
                        positions += [c,d]
                    #South west position
                    elif [c,d] == [a+1,b-1]:
                        positions += [c,d]
                    #West position 
                    elif [c,d] == [a,b-1]:
                        positions += [c,d]
                    #North west position
                    elif [c,d] == [a-1,b-1]:
                        positions += [c,d]
                    #North position
                    elif [c,d] == [a-1,b]:
                        positions += [c,d]
                    #North east position 
                    elif [c,d] == [a-1,b+1]:
                        positions += [c,d]
            return positions

def move_IA (number_magic, player_1, player_2, position_ghost_IA, group):
    """Choose the minimal distance between the ghost, the magic, ennemy's ghost
    Parameters:
    ----------
    number_magic: the dictionnary with the information of the magic (dict)
    player_1: the first's player dictionary(dict)
    player_2: the second's player dictionary (dict) 
    position_ghost_IA: the position of the IA (list)
    group: the player (int)

    Return:
    position_to_go: the position the ghost want to go (list)

    Version:
    --------
    specification : Alexandra Rousselle et Naomi Amedegnato (25/03/2023)
    implémentation : Alexandra Rousselle (v1 27/03/2023)
    """
    move={'magic':[],
          'ghost':[]}
    [a,b]=position_ghost_IA
    if group==1:
        for element in range(len(player_2['ghost'])):
            row=player_2['ghost'][element]['position'][0]
            column=player_2['ghost'][element]['position'][1]
            for x in number_magic:
                for element in number_magic[x]:
                    row_magic=number_magic[x][element][0]
                    column_magic=number_magic[x][element][1]
                    #To have the distance between the ghosts and the AI ghost, then add ghost's position to the move dictionary and the distance
                    ghost_distance = get_distance(a,b,row, column)
                    move['ghost'].append({'initial_position':[row,column], 'distance': ghost_distance})
                    #To have the distance between the magic points and the AI ghost, then add magic points's position to the move dictionary and the distance
                    magic_distance = get_distance(a,b,row_magic, column_magic)
                    move['magic'].append({'initial_position':[row_magic,column_magic], 'distance': magic_distance})
                    #To reasearch the minimal distance in the ghost and the magic dictionaries by fixing the first distance as a supposed minimal distance  
                    distance_min = move['magic'][0]['distance']
                    for element in move:
                        for index in move[element]:
                            if index['distance'] < distance_min:
                                distance_min = index['distance']
                                position_to_go = index['initial_postion']
        return position_to_go
    if group == 2:
        for element in range(len(player_1['ghost'])):
            row=player_1['ghost'][element]['position'][0]
            column=player_1['ghost'][element]['position'][1]
            for x in number_magic:
                for element in number_magic[x]:
                    row_magic=number_magic[x][element][0]
                    column_magic=number_magic[x][element][1]
                    #To have the distance between the ghosts and the AI ghost, then add ghost's position to the move dictionary and the distance
                    ghost_distance = get_distance(a,b,row, column)
                    move['ghost'].append({'initial_position':[row,column], 'distance': ghost_distance})
                    #To have the distance between the magic points and the AI ghost, then add magic points's position to the move dictionary and the distance
                    magic_distance = get_distance(a,b,row_magic, column_magic)
                    move['magic'].append({'initial_position':[row_magic,column_magic], 'distance': magic_distance})
                    #To reasearch the minimal distance in the ghost and the magic dictionaries 
                    distance_min = move['magic'][0]['distance']
                    for element in move:
                        for index in move[element]:
                            if index['distance'] < distance_min:
                                distance_min = index['distance']
                                position_to_go = index['initial_postion']
        return position_to_go

def move_ghost_AI(position_to_go, position_ghost_AI, player):
    """move the ghost to the position
    
    Parameters 
    ---
    position_to_go : the minimal position to go to, calculated by the distance function (list)
    position_ghost_AI : the actual position of the AI ghost (list)
    player : player's dictionary which contains the position of the ghost, his apparition on the board and his magic points (dict)

    Returns 
    ---
    move_order : order to move (str)

    Spécification: Alexandra Rousselle (v1 25/03/2023)
    Implémentation : Alexandra Rousselle (v1 27/03/2023)
    """
    #the function is not finished  
    [a,b]=position_ghost_AI
    [c,d]= position_to_go
    move_order = ''
    f = a+1
    g = a-1
    h = b+1
    i = b-1
    for numbers in number_magic:
            for coordinates in number_magic[numbers]:
                if position_to_go == coordinates :
                    #align with the line 
                    while not a==c:
                        #go north
                        if a>c :
                            if is_there_a_ghost(player,position_ghost_AI)==False:
                                g-=1 #jusqu'à ce que g = c 
                                move_order+= str(a)+'-'+str(b)+':@'+str(g+1)+'-'+str(b)+' '
                        #go south
                        if c>a and is_there_a_ghost(player,position_ghost_AI)==False:
                                f+=1 #jusqu'à ce que f = c
                                move_order+= str(a)+'-'+str(b)+':@'+str(f-1)+'-'+str(b)+' '
                        #align with the column
                        while not b==d:
                            #go to west
                            if b>d and is_there_a_ghost(player,position_ghost_AI)==False:
                                i-=1 #jusqu'à ce que i = d
                                move_order+= str(c)+'-'+str(b)+':@'+str(c)+'-'+str(i+1)+' '
                            #go to east
                            if d>b and is_there_a_ghost(player,position_ghost_AI)==False:
                                h+=1 #jusqu'à ce que h = d
                                move_order+= str(c)+'-'+str(b)+':@'+str(c)+'-'+str(h-1)+' '
                    return move_order
    #if the position to go is the ghost's position, stop before 
    for element in range(0, len(player['ghost'])):
        if position_to_go == player['ghost'][element]["position"]:
                    #align with the line 
                    while not a==c:
                        #go north
                        if a>c :
                            if is_there_a_ghost(player,position_ghost_AI)==False:
                                g-=1 #jusqu'à ce que g = c 
                                move_order+= str(a)+'-'+str(b)+':@'+str(g+1)+'-'+str(b)+' '
                        #go south
                        if c>a and is_there_a_ghost(player,position_ghost_AI)==False:
                                f+=1 #jusqu'à ce que f = c
                                move_order+= str(a)+'-'+str(b)+':@'+str(f-1)+'-'+str(b)+' '
                        #align with the column
                        while not b==d:
                            #go to west
                            if b>d and is_there_a_ghost(player,position_ghost_AI)==False:
                                i-=1 #jusqu'à ce que i = d
                                move_order+= str(c)+'-'+str(b)+':@'+str(c)+'-'+str(i+1)+' '
                            #go to east
                            if d>b and is_there_a_ghost(player,position_ghost_AI)==False:
                                h+=1 #jusqu'à ce que h = d
                                move_order+= str(c)+'-'+str(b)+':@'+str(c)+'-'+str(h-1)+' '
                    return move_order

"""def main_IA (player, number_magic, board_dictionnary):
    """"""The main fonction of the IA which returns orders 
    Parameters
    ---
    player: the number of the player (int)
    number_magic: the dictionary with the information of the magic (dict)
    board_dictionnary : dictionnary with the size of the board (dict)

    Returns
    ---
    order : string with the orders generated by the IA (str)
    
    Version
    ---
    Spécification: Naomi Amedegnato (v.1 19/03/23)
                    Alexandra Rousselle (v2 25/03/2023)
    Implémentation : Alexandra Rousselle (v1 25/03/2023)
    """
    

#"main function of the AI"
def get_AI_orders(player_1, player_2, number_magic, player_id):
    """Return orders of AI.
    
    Parameters
    ----------
    game: game data structure (dict)
    player_id: player id of AI (int)

    Returns
    -------
    orders: orders of AI (str)
    
    """

    orders = ''
    if player_id == 1:
        for e in range(len(player_1['ghost'])):
            position_ghost_AI = player_1['ghost'][e]['position']
            positions = disponible_place(player_1, position_ghost_AI, board_dictionnary)
            position_to_go = positions[0]
            orders = move_ghost_AI(position_to_go, position_ghost_AI, player_1)
    elif player_id == 2:
        for e in range(len(player_1['ghost'])):
            position_ghost_AI = player_2['ghost'][e]['position']
            positions = disponible_place(player_2, position_ghost_AI, board_dictionnary)
            position_to_go = positions[0]
            orders = move_ghost_AI(position_to_go, position_ghost_AI, player_2)
    return orders

# main function
def play_game(map_file, group_1, type_1, group_2, type_2):
    """Play a game.
    
    Parameters
    ----------
    map_path: path of map file (str)
    group_1: group of player 1 (int)
    type_1: type of player 1 (str)
    group_2: group of player 2 (int)
    type_2: type of player 2 (str)
    
    Notes
    -----
    Player type is either 'human', 'AI' or 'remote'.
    
    If there is an external referee, set group id to 0 for remote player.
    
    Version
    -------
    Implementation: Zélie Van Kerm (v.1 10/03/23)
                    Zélie Van Kerm (v.2 20/03/23)
    """
    """number_magic, board_dictionnary, player_1, player_2 = read_file(map_file)"""
    
    # create connection, if necessary
    if type_1 == 'remote':
        connection = create_connection(group_2, group_1)
    elif type_2 == 'remote':
        connection = create_connection(group_1, group_2)
    
    #ajouter le plateau
    
    board(player_1, player_2, number_magic)

    #loop of the game, 200 turns maximum
    while turn <= 10:
    
        #get orders of player 1 if human and notify them to player 2, if necessary
        if type_1 == 'human':
            order_1 = get_human_orders(player_1)
            if type_2 == 'remote':
                notify_remote_orders(connection, orders)
            read_order(order_1)
            
        #get orders of player 2 if human and notify them to player 1, if necessary
        elif type_2 == 'human':
            order_2 = get_human_orders(player_2)
            if type_1 == 'remote':
                notify_remote_orders(connection, orders)
            read_order(order_2)

        
        # get orders of player 1 and notify them to player 2, if necessary
        if type_1 == 'remote':
            orders = get_remote_orders(connection)
        else:
            orders = get_AI_orders(player_1, player_2, number_magic, 1)
            if type_2 == 'remote':
                notify_remote_orders(connection, orders)
        read_order(orders)
        
        # get orders of player 2 and notify them to player 1, if necessary
        if type_2 == 'remote':
            orders = get_remote_orders(connection)
        else:
            orders = get_AI_orders(player_1, player_2, number_magic, 2)
            if type_1 == 'remote':
                notify_remote_orders(connection, orders)
        read_order(orders)
        
        
        #enlever les dictionnaire des fantömes qui n'ont plus de vie
        delete_ghost(player_1)
        delete_ghost(player_2)

        #check if any player lost
        points_1 = 0
        points_2 = 0
        #conditions in case the code didin't deleted a ghost without magic's dictionnary
        for e in range (len(player_1['ghost'])):
            if player_1['ghost'][e]['number_magic'] == 0 : 
                points_1 += 1
        
        for e in range (len(player_1['ghost'])):
            if player_1['ghost'][e]['number_magic'] == 0 : 
                points_2 += 1
        
        if points_1 == len(player_1["ghost"]):
            if points_2 != len(player_2["ghost"]):
                print('Game over, player 2 is the winner')
            else:
                print('Game over, no winner')
        else:
            if points_2 == (len(player_2["ghost"])):
                print('Game over, player 1 is the winner')

        #actualize the board game
        board(player_1, player_2, number_magic)

        #check if any player lost
        if player_1['ghost']==[] and player_2['ghost']==[]:
            print('Game over, no winner')
        elif player_1['ghost']==[]:
            print('Game over, player 2 is the winner')
        elif player_2['ghost']==[]:
            print('Game over, player 1 is the winner')
        

        player_1 ['number_magic']+= len(player_1['ghost'])
        player_2 ['number_magic']+= len (player_2['ghost'])

        turn +=1
    
    #the loop ended, we reached 200 turns without any dead players
    """Sépcification: Naomi Amedegnato (v.1 22/02/23)
    Implémentation: Naomi Amedegnato (v.1 22/02/23)
                    Naomi Amedegnato (v.2 23/02/23)
                    Naomi Amedegnato (v.3 14/03/23)
                    Zélie Van Kerm (v.4 20/03/23)
    """
    points_1 = 0
    points_2 = 0
    for x in player_1["ghost"]:
        for number_magic in x['number_magic']:
            if number_magic < 100:
                points_2 += number_magic
    for x in player_2["ghost"]:
        for number_magic in x['number_magic']:
            if number_magic < 100:
                points_1 += number_magic

    if points_1 < points_2:
        print('the player 2 is the winner!')
    if points_2 < points_1:
        print('the player 1 is the winner!')
    
    if points_1 == points_2:
        if player_1['number magic'] > player_2['number magic'] :
            print('the player 1 is the winner!')
        if player_2['number magic'] > player_1['number magic'] :
            print('the player 2 is the winner!')


    # close connection, if necessary
    if type_1 == 'remote' or type_2 == 'remote':
        close_connection(connection)
        
"""Module providing remote play features for UNamur programmation project (INFOB132).

Sockets are used to transmit orders on local or remote machines.
Firewalls or restrictive networks settings may block them.  

More details on sockets: https://docs.python.org/2/library/socket.html.

Author: Benoit Frenay (benoit.frenay@unamur.be).

"""

import socket
import struct
import time

def create_server_socket(local_port, verbose):
    """Creates a server socket.
    
    Parameters
    ----------
    local_port: port to listen to (int)
    verbose: True if verbose (bool)
    
    Returns
    -------
    socket_in: server socket (socket.socket)
    
    """
    
    socket_in = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_in.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # deal with a socket in TIME_WAIT state

    if verbose:
        print(' binding on local port %d to accept a remote connection' % local_port)
    
    try:
        socket_in.bind(('', local_port))
    except:
        raise IOError('local port %d already in use by your group or the referee' % local_port)
    socket_in.listen(1)
    
    if verbose:
        print('   done -> can now accept a remote connection on local port %d\n' % local_port)
        
    return socket_in


def create_client_socket(remote_IP, remote_port, verbose):
    """Creates a client socket.
    
    Parameters
    ----------
    remote_IP: IP address to send to (int)
    remote_port: port to send to (int)
    verbose: True if verbose (bool)
    
    Returns
    -------
    socket_out: client socket (socket.socket)
    
    """

    socket_out = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_out.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # deal with a socket in TIME_WAIT state
    
    connected = False
    msg_shown = False
    
    while not connected:
        try:
            if verbose and not msg_shown:
                print(' connecting on %s:%d to send orders' % (remote_IP, remote_port))
                
            socket_out.connect((remote_IP, remote_port))
            connected = True
            
            if verbose:
                print('   done -> can now send orders to %s:%d\n' % (remote_IP, remote_port))
        except:
            if verbose and not msg_shown:
                print('   connection failed -> will try again every 100 msec...')
                
            time.sleep(.1)
            msg_shown = True
            
    return socket_out
    
    
def wait_for_connection(socket_in, verbose):
    """Waits for a connection on a server socket.
    
    Parameters
    ----------
    socket_in: server socket (socket.socket)
    verbose: True if verbose (bool)
    
    Returns
    -------
    socket_in: accepted connection (socket.socket)
    
    """
    
    if verbose:
        print(' waiting for a remote connection to receive orders')
        
    socket_in, remote_address = socket_in.accept()
    
    if verbose:
        print('   done -> can now receive remote orders from %s:%d\n' % remote_address)
        
    return socket_in            


def create_connection(your_group, other_group=0, other_IP='127.0.0.1', verbose=False):
    """Creates a connection with a referee or another group.
    
    Parameters
    ----------
    your_group: id of your group (int)
    other_group: id of the other group, if there is no referee (int, optional)
    other_IP: IP address where the referee or the other group is (str, optional)
    verbose: True only if connection progress must be displayed (bool, optional)
    
    Returns
    -------
    connection: socket(s) to receive/send orders (dict of socket.socket)
    
    Raises
    ------
    IOError: if your group fails to create a connection
    
    Notes
    -----
    Creating a connection can take a few seconds (it must be initialised on both sides).
    
    If there is a referee, leave other_group=0, otherwise other_IP is the id of the other group.
    
    If the referee or the other group is on the same computer than you, leave other_IP='127.0.0.1',
    otherwise other_IP is the IP address of the computer where the referee or the other group is.
    
    The returned connection can be used directly with other functions in this module.
            
    """
    
    # init verbose display
    if verbose:
        print('\n[--- starts connection -----------------------------------------------------\n')
        
    # check whether there is a referee
    if other_group == 0:
        if verbose:
            print('** group %d connecting to referee on %s **\n' % (your_group, other_IP))
        
        # create one socket (client only)
        socket_out = create_client_socket(other_IP, 42000+your_group, verbose)
        
        connection = {'in':socket_out, 'out':socket_out}
        
        if verbose:
            print('** group %d successfully connected to referee on %s **\n' % (your_group, other_IP))
    else:
        if verbose:
            print('** group %d connecting to group %d on %s **\n' % (your_group, other_group, other_IP))

        # create two sockets (server and client)
        socket_in = create_server_socket(42000+your_group, verbose)
        socket_out = create_client_socket(other_IP, 42000+other_group, verbose)
        
        socket_in = wait_for_connection(socket_in, verbose)
        
        connection = {'in':socket_in, 'out':socket_out}

        if verbose:
            print('** group %d successfully connected to group %d on %s **\n' % (your_group, other_group, other_IP))
        
    # end verbose display
    if verbose:
        print('----------------------------------------------------- connection started ---]\n')

    return connection

def bind_referee(group_1, group_2, verbose=False):
    """Put a referee between two groups.
    
    Parameters
    ----------
    group_1: id of the first group (int)
    group_2: id of the second group (int)
    verbose: True only if connection progress must be displayed (bool, optional)
    
    Returns
    -------
    connections: sockets to receive/send orders from both players (dict)
    
    Raises
    ------
    IOError: if the referee fails to create a connection
    
    Notes
    -----
    Putting the referee in place can take a few seconds (it must be connect to both groups).
        
    connections contains two connections (dict of socket.socket) which can be used directly
    with other functions in this module.  connection of first (second) player has key 1 (2).
            
    """
    
    # init verbose display
    if verbose:
        print('\n[--- starts connection -----------------------------------------------------\n')

    # create a server socket (first group)
    if verbose:
        print('** referee connecting to first group %d **\n' % group_1)        

    socket_in_1 = create_server_socket(42000+group_1, verbose)
    socket_in_1 = wait_for_connection(socket_in_1, verbose)

    if verbose:
        print('** referee succcessfully connected to first group %d **\n' % group_1)        
        
    # create a server socket (second group)
    if verbose:
        print('** referee connecting to second group %d **\n' % group_2)        

    socket_in_2 = create_server_socket(42000+group_2, verbose)
    socket_in_2 = wait_for_connection(socket_in_2, verbose)

    if verbose:
        print('** referee succcessfully connected to second group %d **\n' % group_2)        
    
    # end verbose display
    if verbose:
        print('----------------------------------------------------- connection started ---]\n')

    return {1:{'in':socket_in_1, 'out':socket_in_1},
            2:{'in':socket_in_2, 'out':socket_in_2}}


def close_connection(connection):
    """Closes a connection with a referee or another group.
    
    Parameters
    ----------
    connection: socket(s) to receive/send orders (dict of socket.socket)
    
    """
    
    # get sockets
    socket_in = connection['in']
    socket_out = connection['out']
    
    # shutdown sockets
    socket_in.shutdown(socket.SHUT_RDWR)    
    socket_out.shutdown(socket.SHUT_RDWR)
    
    # close sockets
    socket_in.close()
    socket_out.close()
    
    
def notify_remote_orders(connection, orders):
    """Notifies orders to a remote player.
    
    Parameters
    ----------
    connection: sockets to receive/send orders (dict of socket.socket)
    orders: orders to notify (str)
        
    Raises
    ------
    IOError: if remote player cannot be reached
    
    """

    # deal with null orders (empty string)
    if orders == '':
        orders = 'null'
    
    # send orders
    try:
        tosend = struct.pack(f"!h{len(orders)}s", len(orders), orders.encode())
        connection['out'].sendall(tosend)
    except:
        raise IOError('remote player cannot be reached')


def get_remote_orders(connection):
    """Returns orders from a remote player.

    Parameters
    ----------
    connection: sockets to receive/send orders (dict of socket.socket)
        
    Returns
    ----------
    player_orders: orders given by remote player (str)

    Raises
    ------
    IOError: if remote player cannot be reached
            
    """
    # receive orders    
    try:
        toreceive = struct.unpack("!h", connection['in'].recv(2))[0]
        orders = connection['in'].recv(toreceive).decode()
    except:
        raise IOError('remote player cannot be reached')
        
    # deal with null orders
    if orders == 'null':
        orders = ''
        
    return orders
map = read_file ('file.txt')
#play_game('file.txt', 1, 'human', 2, 'AI')
