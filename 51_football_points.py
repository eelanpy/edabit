# 51_football_points:

def football_pnts(wins,draws,loses):
    points_wins = wins * 3
    points_draws = draws * 1
    points_loses = 0
    counter = points_wins + points_draws + points_loses
    print(counter)

football_pnts(5,0,2)