from pydfs_lineup_optimizer.solvers.mip_solver import MIPSolver
from pydfs_lineup_optimizer import __version__
print('Version',__version__
)
from pydfs_lineup_optimizer import (
    get_optimizer,
    Site,
    Sport,
    TeamStack,
    CSVLineupExporter,
    PlayerFilter,
    AfterEachExposureStrategy,
    PositionsStack,
    solvers
)
import numpy as np
import pandas as pd

optimizer = get_optimizer(Site.FANDUEL, Sport.FOOTBALL, solver=MIPSolver)


optimizer.load_players_from_csv(
    r"FanDuel-NFL.csv")
# PlayerFilter(from_value=15),  # use only players with points >= 5
# PlayerFilter(from_value=2, filter_by='efficiency'),  # and efficiency(points/salary) >= 2
# PlayerFilter(from_value=2000, filter_by='salary'),  # and salary >= 3000
# optimizer.player_pool.exclude_teams(['Seattle Mariners'])
df = pd.read_csv(
    r"FanDuel-NFL.csv"
)
df.head()

# optimizer.add_stack(PositionsStack((["QB", "WR", ("WR", "TE")]))) or ((["QB", "WR", "TE"]))
# optimizer.add_stack(PositionsStack(['QB', ('WR', 'TE')]) or (PositionsStack(['QB', 'WR', ('WR', 'TE')])))
# optimizer.set_min_salary_cap(49200)
# optimizer.set_max_repeating_players(7)
# optimizer.restrict_positions_for_same_team(("RB", "RB"), ("QB", "RB"))
# optimizer.force_positions_for_opposing_team(('QB', 'WR'))
# optimizer.restrict_positions_for_opposing_team(['D'], ['RB', 'WR', 'TE'])
for lineup in optimizer.optimize(
    n=150,
    max_exposure=(), randomness=True):
    print(lineup)
    print(lineup.players)  # list of players
    print(lineup.fantasy_points_projection)
    print(lineup.salary_costs)
    print(lineup.ownerships)
optimizer.print_statistic()
optimizer.export("result.csv")

