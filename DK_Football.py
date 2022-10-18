from pydfs_lineup_optimizer import (
    get_optimizer,
    Site,
    Sport,
    TeamStack,
    CSVLineupExporter,
    PlayerFilter,
    AfterEachExposureStrategy,
    PositionsStack,
)
import numpy as np
import pandas as pd
optimizer = get_optimizer(Site.DRAFTKINGS, Sport.FOOTBALL)

optimizer.load_players_from_csv(
    r'/Users/Alex/Desktop/Optimizer/DKSalaries.csv'
)
df = pd.read_csv(
    r'/Users/Alex/Desktop/Optimizer/DKSalaries.csv'
)
df.head()

optimizer.add_stack(PositionsStack(['QB', 'WR', ('WR', 'TE')]))
# optimizer.set_min_salary_cap(49500)
# optimizer.add_stack(TeamStack(2, for_positions=['QB', 'WR', 'TE']))
# optimizer.add_stack(PositionsStack(['QB', ('WR', 'TE')])) # Stack QB with either WR or TE
# optimizer.force_positions_for_opposing_team(('TE', 'WR'))
# optimizer.restrict_positions_for_same_team(('RB', 'RB'))
# optimizer.restrict_positions_for_same_team(('RB', 'WR'))
# optimizer.restrict_positions_for_same_team(('TE', 'WR'))
# optimizer.restrict_positions_for_same_team(('TE', 'RB'))
# optimizer.restrict_positions_for_same_team(('RB', 'TE'))
# optimizer.restrict_positions_for_same_team(('QB', 'D'), ('RB', 'D'))

for lineup in optimizer.optimize(
    n=15, max_exposure=(.35), # exposure_strategy=AfterEachExposureStrategy
):
    print(lineup)
    print(lineup.players)  # list of players
    print(lineup.fantasy_points_projection)
    print(lineup.salary_costs)
optimizer.export('result.csv')
optimizer.print_statistic()


