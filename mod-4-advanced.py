'''Module 4: Individual Programming Assignment 1'''

def relationship_status(from_member, to_member, social_graph):
    from_following = social_graph[from_member]['following']

    if to_member in from_following:
        return "follower"
    else:
        to_following = social_graph[to_member]['following']

        if from_member in to_following:
            return "followed by"
        else:
            if to_member in from_following and from_member in to_following:
                return "friends"
            else:
                return "no relationship"
            
users = ["@bongolpoc", "@joaquin", "@chums", "@jobenilagan", "@joeilagan", "@eeebeee"]

social_graph = { 
    "@bongolpoc":{"first_name":"Joselito", "last_name":"Olpoc", "following":[ ] }, 
    "@joaquin": {"first_name":"Joaquin", "last_name":"Gonzales", "following":[ "@chums","@jobenilagan" ] }, 
    "@chums" : {"first_name":"Matthew", "last_name":"Uy", "following":[ "@bongolpoc","@rudyang","@joeilagan" ] }, 
    "@jobenilagan":{"first_name":"Joben", "last_name":"Ilagan", "following":[ "@eeebeee","@jobenilagan","@chums","@joaquin" ] }, 
    "@joeilagan":{"first_name":"Joe", "last_name":"Ilagan", "following":[ "@eeebeee","@jobenilagan","@chums" ] }, 
    "@eeebeee": {"first_name":"Elizabeth", "last_name":"Ilagan", "following":[ "@jobenilagan","@joeilagan" ] }, 
}

def tic_tac_toe(board):
    a = len(board)
    x='X'
    o='O'
    count=0
    b=False
    
    for i in range(0,a):
        
        if board[i].count(x)==a:
            b=True
            return(x)
            break
        elif board[i].count(o)==a:
            b=True
            return(o)
            break
        else:
            continue
    
    count=0    
    for j in range (0,a):
        
        if (x in board[j][j])==True:
            count+=1
        elif (o in board[j][j])==True:
            count-=1
        else:
            continue
        
        if count==a:
            b=True
            return(x)
            break
        elif abs(count)==a:
            b=True
            return(o)
            break
        else:
            continue
    
    count=0
    for f in range (0,a):
        
        if (x in board[a-1-f][f])==True:
            count+=1
        elif (o in board[a-1-f][f])==True:
            count-=1
        else:
            continue
        
        if count==a:
            b=True
            return(x)
            break
        elif abs(count)==a:
            b=True
            return(o)
            break
        else:
            continue
            
    
    for d in range (0,a):
        count=0
        for e in range (0,a):
            if (x in board[e][d])==True:
                count+=1
            elif (o in board[e][d])==True:
                count-=1
            else:
                continue
        if count==a:
            b=True
            return (x)
            break
        elif abs(count)==a:
            b=True
            return(o)
            break
        else:
            continue
        
    if b==False:
        return('NO WINNER')

def eta(first_stop, second_stop):
    route_map = {
        ("upd", "admu"): {"travel_time_mins": 10},
        ("admu", "dlsu"): {"travel_time_mins": 35},
        ("dlsu", "upd"): {"travel_time_mins": 55}
    }

    stops = list(route_map.keys())

    if (first_stop, second_stop) not in stops:
        raise ValueError("Invalid stops entered or no valid route between the stops.")

    total_time = 0
    current_stop = first_stop

    while current_stop != second_stop:
        for stop1, stop2 in stops:
            if stop1 == current_stop:
                total_time += route_map[(stop1, stop2)]['travel_time_mins']
                current_stop = stop2
                break
        else:
            raise ValueError("No valid route found between the stops.")

    return total_time

while (True):
    print("\nSelect a Function")
    print("[1] Relationship Status")
    print("[2] Tic Tac Toe")
    print("[3] ETA")

    select = None

    while (True):
        select = int(input(">> "))
        if not(select <= 3 and select >= 1):
            print("\n[SYSTEM]: Please input a number from the available options.")
        else:
            break
    if select == 1:
        print("\nYou've selected Relationship Status.")
        from_member = input("Enter the first user: ")
        to_member = input("Enter the second user: ")
    
        if from_member in users and to_member in users:
            from_first_name = social_graph[from_member]['first_name']
            from_last_name = social_graph[from_member]['last_name']
            to_first_name = social_graph[to_member]['first_name']
            to_last_name = social_graph[to_member]['last_name']
            result = relationship_status(from_member, to_member, social_graph)

        if result == "follower":
            print(f"\n{from_first_name} {from_last_name} is {to_first_name} {to_last_name}'s {result}.")
        elif result == "followed by":
            print(f"\n{from_first_name} {from_last_name} is {result} {to_first_name} {to_last_name}.")
        elif result == "friends":
            print(f"\n{from_first_name} {from_last_name} and {to_first_name} {to_last_name} are {result}.")
        elif result == "no relationship":
            print(f"\n{from_first_name} {from_last_name} and {to_first_name} {to_last_name} have {result}.")
        else:
            print("Invalid input. Please ensure that both users exist.")

    elif select == 2:
       while True:
        current_board = [[' ' for _ in range(3)] for _ in range(3)]  # Creating an empty 3x3 board
        print("Let's play Tic Tac Toe!")
        print("Player 1: X | Player 2: O")
        players = ['X', 'O']
        winner = 'NO WINNER'

        for turn in range(9):  # Maximum number of moves in a 3x3 board
            current_player = players[turn % 2]  # Alternating players

            print("\nCurrent Board:")
            for row in current_board:
                print(' '.join(row))

        while True:
            try:
                row, col = map(int, input(f"Player '{current_player}', enter row and column number (0-2) separated by space: ").split())
                if current_board[row][col] == ' ':  # Checking if the cell is empty
                    current_board[row][col] = current_player
                    break
                else:
                    print("That cell is already taken. Try again.")
            except (ValueError, IndexError):
                print("Invalid input. Please enter valid row and column numbers.")

        winner = tic_tac_toe(current_board)
        if winner != 'NO WINNER':
            break

        print("\nFinal Board:")
        for row in current_board:
            print(' '.join(row))

        if winner != 'NO WINNER':
            print(f"Player '{winner}' wins!")
        else:
            print("It's a tie!")

    elif select == 3:
        print("\nYou've selected ETA.")
        while True:
            first_stop = input("Enter your first stop: ")
            second_stop = input("Enter your second stop: ")

            try:
                total_time = eta(first_stop, second_stop)
                print(f"\nThe estimated time of arrival (ETA) is {total_time} minutes.")
                break
            except ValueError as e:
                print(str(e))
                break

    print("\nInitiate program execution once more?")
    print("[1] Yes")
    print("[2] No")
        
    while (True):
        select_option = int(input(">> "))
        if not(select_option <= 2 and select_option >= 1):
            print("\nPlease input a number from the available options.")
        else:
            break

    if select_option == 2:
        break


