from yahoo_oauth import OAuth2
import yahoo_fantasy_api as yfa

# print(OAuth2.__file__)

# connect to yahoo api
sc = OAuth2(None, None, from_file='oauth2.json')

# get game object

gm = yfa.Game(sc, 'nfl')

leagues = gm.league_ids()

# print(leagues)

# get league object
lg = gm.to_league('406.l.763037')

# statCat = lg.stat_categories()

# print(statCat)

settings = lg.settings()

print(settings)


# teams = lg.teams()

# print(teams)

# #print(lg)

# # get team key
# teamkey = lg.team_key()

# # get team object
# team = lg.to_team(teamkey)

# # get team roster
# roster = team.roster()

# print(roster)