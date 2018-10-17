####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Team9' # Only 10 chars displayed.
strategy_name = 'EnemyBetray?'
strategy_description = 'Checks previous move'
    
def move(my_history, their_history, my_score, their_score):
    turn = len(my_history)
    index = turn - 1
    enemyBetrays = False
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    
    Make my move.
    Returns 'c' or 'b'. 
    '''

    # my_history: a string with one letter (c or b) per round that has been played with this opponent.
    # their_history: a string of the same length as history, possibly empty. 
    # The first round between these two players is my_history[0] and their_history[0].
    # The most recent round is my_history[-1] and their_history[-1].
    
    # Analyze my_history and their_history and/or my_score and their_score.
    # Decide whether to return 'c' or 'b'.
    if turn == 1 or turn == 2 or turn == 3 or turn == 4 or turn == 0:
        return 'c'
    elif turn == 6:
        return 'b'
    elif turn == 7:
        if 'b' in their_history[0:6]:
            enemyBetrays = True
            return 'b'
        elif 'c' == their_history[6]:
            enemyBetrays = False
            return 'b'
        else:
            enemyBetrays = False
            return 'b'
    else:
        if enemyBetrays == True:
            if their_history[index:] == 'c':
                return 'b'
            elif their_history[index-1:] == 'cc':
                return 'c'
            else:
                return 'b'
        else:
            if their_history[index:] == 'c':
                return 'c'
            else:
                return 'b'