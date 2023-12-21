from gurobipy import Model, GRB, quicksum
import pandas as pd

# Cleaned dataset with pre-calculated performance metric
data_path = '/Users/niharikapatil/Documents/Academics/Fall Semester 2023/DABP/Final Project/data/final_merged.csv' #Replace data path here
players_data = pd.read_csv(data_path)

#Constraint variables
team_var = '131' #FC Barcelona
budget_var = 150000000
attack_needed = 1
defender_needed = 1
midfield_needed = 1
players_to_be_excluded = []
player_to_be_included = []

#Constants to enable decision for more than one team
TEAMS = [team_var] 
POSITIONS = players_data['position'].unique()
BUDGET = {team_var: budget_var}
NEEDS = {team_var: {"Attack": attack_needed, "Midfield": midfield_needed, "Defender": defender_needed}}

# Initialize the Gurobi model
model = Model("FootballTeamTransfersOptimization")


# OPTIGUIDE DATA CODE GOES HERE


#Exclude team player
if players_to_be_excluded:
    players_data = players_data[~players_data['player_id'].isin(players_to_be_excluded)]

# Decision variables: xij for each player i and team j
x = {}
for i in players_data['player_id']:
    for j in TEAMS:
        x[(i, j)] = model.addVar(vtype=GRB.BINARY, name=f"x_{i}_{j}")

# Update model to integrate new variables
model.update()

# Objective function - Maximise performance and value to team, minimise cost
obj = quicksum(players_data.loc[players_data['player_id'] == i, 'market_value_in_eur'].iloc[0] *
               players_data.loc[players_data['player_id'] == i, 'normalised_performance_score'].iloc[0] * x[(i, j)]
               for i in players_data['player_id'] for j in TEAMS) - \
      quicksum(players_data.loc[players_data['player_id'] == i, 'market_value_in_eur'].iloc[0] * x[(i, j)]
               for i in players_data['player_id'] for j in TEAMS)
model.setObjective(obj, GRB.MAXIMIZE)

# Constraints
for j in TEAMS:

    # Budget constraints
    model.addConstr(quicksum(players_data.loc[players_data['player_id'] == i, 'market_value_in_eur'].iloc[0] * x[(i, j)]
                             for i in players_data['player_id']) <= BUDGET[j], name=f"Budget_{j}")

    # Team needs
    for k in POSITIONS:
        model.addConstr(quicksum(players_data.loc[(players_data['player_id'] == i) & (players_data['position'] == k), 'normalised_performance_score'].iloc[0] * x[(i, j)]
                                 for i in players_data['player_id'] if not players_data[(players_data['player_id'] == i) & (players_data['position'] == k)].empty) >= NEEDS[j][k], name=f"Need_{j}_{k}")

# One team per player constraint
for i in players_data['player_id']:
    model.addConstr(quicksum(x[(i, j)] for j in TEAMS) <= 1, name=f"OneTeam_{i}")

# Solve the model
model.optimize()
m = model


# OPTIGUIDE CONSTRAINT CODE GOES HERE

# Solve
m.update()
model.optimize()


team_player_dict = {}

for v in model.getVars():
    if v.x > 0:  # If the player is chosen in the solution
    
        print(v.varName, "=", v.x)
        # Extracting i and j from the variable name
        _, player_id, team_id = v.varName.split('_')

        team_id = int(team_id)
        player_id = int(player_id)

        # Check if the team is already in the dictionary
        if team_id in team_player_dict:
            # If yes, append the player to the existing team's list
            team_player_dict[team_id].append(player_id)
        else:
            # If not, create a new entry with the player in a new list
            team_player_dict[team_id] = [player_id]
       


for team in team_player_dict.keys():
    print(team)
    selected_players = players_data[players_data['player_id'].isin(team_player_dict[team])]
    print(selected_players[['player_id', 'name', 'position', 'normalised_performance_score', 'market_value_in_eur']])

