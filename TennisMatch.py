import prompt
import random

def frange(*args):
    """
    Returns a float range: e.g., for i in range(0.1, 1.0, 0.1): print(i)
      prints the numbers .1, .2, .3, ... .9, 1.: 0.1 through 1.0 inclusive
    """
    start = 0.
    step  = 1.
    if len(args) == 1:
        stop = args[0]
    elif len(args) == 2:
        start,stop = args[0],args[1]
    elif len(args) == 3:
        start,stop,step = args[0],args[1],args[2]
    else:
        raise TypeError('frange expected 1-3 arguments, got ' + str(len(args)))
    if step == 0.:
        raise ValueError('frange step cannot be 0.')
    i = 0
    while True:
        curr = start + i*step
        if (step > 0. and curr > stop+.1*step) or (step < 0. and curr < stop-.1*step):
            return
        yield curr
        i += 1
        
        

def point_winner(percent_A_win_point):    
    x = random.random()
    if x <= percent_A_win_point:
        return 'A'
    else:
        return 'B'
    
def game_winner(percent_A_win_point):
    A_points=0
    B_points=0
    while True:
        if point_winner(percent_A_win_point) == 'A':
            A_points += 1
        else:
            B_points += 1
        if A_points >= 4 and A_points >= B_points + 2:
            return 'A'
        elif B_points >= 4 and B_points >= A_points +2:
            return 'B'
        if (A_points >= 4 and A_points >= B_points + 2) or (B_points >= 4 and B_points >= A_points +2):
            break
        
def A_win_stats(percent_A_win_point, play_function, times_to_play, trace=False, unit=None, suffix='s'):
    if play_function==game_winner:
        if trace==True:
            print('Playing',times_to_play,'games with percent_A_win_point =',percent_A_win_point)
        games=0
        A_win=0
        while True:
            games +=1
            if game_winner(percent_A_win_point) == 'A':
                A_win+=1
                if trace==True:
                    print(' game',games,'winner = A')
            else:
                if trace==True:
                    print(' game',games,'winner = B')
            if games==times_to_play:
                break
        if trace==True:
            print('A won',(A_win/games)*100,'percent of the games')
        return (A_win/games)*100
    if play_function==point_winner:
        if trace==True:
            print('Playing',times_to_play,'points with percent_A_win_point =',percent_A_win_point)
        games=0
        A_win=0
        while True:
            games +=1
            if point_winner(percent_A_win_point) == 'A':
                A_win+=1
                if trace==True:
                    print(' point',games,'winner = A')
            else:
                if trace==True:
                    print(' point',games,'winner = B')
            if games==times_to_play:
                break
        if trace==True:
            print('A won',(A_win/games)*100,'percent of the points')
        return (A_win/games)*100
    if play_function==set_winner:
        if trace==True:
            print('Playing',times_to_play,'sets with percent_A_win_point =',percent_A_win_point)
        games=0
        A_win=0
        while True:
            games +=1
            if set_winner(percent_A_win_point) == 'A':
                A_win+=1
                if trace==True:
                    print(' set',games,'winner = A')
            else:
                if trace==True:
                    print(' set',games,'winner = B')
            if games==times_to_play:
                break
        if trace==True:
            print('A won',(A_win/games)*100,'percent of the sets')
        return (A_win/games)*100
    if play_function==match_winner:
        if trace==True:
            print('Playing',times_to_play,'matches with percent_A_win_point =',percent_A_win_point)
        games=0
        A_win=0
        while True:
            games +=1
            if match_winner(percent_A_win_point) == 'A':
                A_win+=1
                if trace==True:
                    print(' match',games,'winner = A')
            else:
                if trace==True:
                    print(' match',games,'winner = B')
            if games==times_to_play:
                break
        if trace==True:
            print('A won',(A_win/games)*100,'percent of the matches')
        return (A_win/games)*100
    

def set_winner(percent_A_win_point):
    A_games=0
    B_games=0
    while True:
        if game_winner(percent_A_win_point) == 'A':
            A_games += 1
        else:
            B_games += 1
        if A_games >= 4 and A_games >= B_games + 2:
            return 'A'
        elif B_games >= 4 and B_games >= A_games +2:
            return 'B'
        if (A_games >= 4 and A_games >= B_games + 2) or (B_games >= 4 and B_games >= A_games +2):
            break    

def match_winner(percent_A_win_point):
    A_sets=0
    B_sets=0
    while True:
        if game_winner(percent_A_win_point) == 'A':
            A_sets += 1
        else:
            B_sets += 1
        if A_sets >= 4 and A_sets >= B_sets + 2:
            return 'A'
        elif B_sets >= 4 and B_sets >= A_sets +2:
            return 'B'
        if (A_sets >= 4 and A_sets >= B_sets + 2) or (B_sets >= 4 and B_sets >= A_sets +2):
            break   
         
min_percentage=prompt.for_float('Enter minimum percentage',default=0.45)
max_percentage=prompt.for_float('Enter maximum percentage',default=0.55)
step_percentage=prompt.for_float('Enter percentage step',default=0.01)
matches_to_play=prompt.for_int('Enter matches to play',default=1000)
for i in frange(min_percentage,max_percentage,step_percentage):
    winner = A_win_stats(i,match_winner,matches_to_play)
    print('with percent_A_win_point =',str(round(i*100,1))+'% A wins',str(round(winner,1))+'% of the matches')


    

