from pydfs_lineup_optimizer import (
    get_optimizer,
    Site,
    Sport,
    TeamStack,
    CSVLineupExporter,
    PlayerFilter,
    AfterEachExposureStrategy,
    PositionsStack,
    PlayersGroup
)
import numpy as np
import pandas as pd
optimizer = get_optimizer(Site.DRAFTKINGS_CAPTAIN_MODE, Sport.FOOTBALL)

optimizer.load_players_from_csv(
    r'/Users/Alex/Desktop/Optimizer/DK_Showdown.csv'
)
df = pd.read_csv(
    r'/Users/Alex/Desktop/Optimizer/DK_Showdown.csv'
)
df.head()
# optimizer.restrict_positions_for_same_team(('RB', 'RB'))

for lineup in optimizer.optimize(
    n=15, max_exposure=(), # exposure_strategy=AfterEachExposureStrategy
):
    print(lineup)
    print(lineup.players)  # list of players
    print(lineup.fantasy_points_projection)
    print(lineup.salary_costs)
    print(lineup.ownerships)
optimizer.export('DK_Showdown_Results.csv')
optimizer.print_statistic()


