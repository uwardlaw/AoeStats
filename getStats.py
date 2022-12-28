import requests
import json
import pprint

data = {}

#for pageNumber in range(20):
#    params={'leaderboard':'rm_2v2', 'page': pageNumber+1}
#    data[pageNumber] = requests.get("https://aoe4world.com/api/v0/games", params=params).json()

#with open('2v2_rm.json', 'w') as out:
#     json.dump(data,out)

with open('2v2_rm.json') as inFile:
    data = json.load(inFile)

teamCount = {}
civCount = {}

total = 0

for page in data.values():
    for game in page.get('games'):
        for team in game.get('teams'):
            t1 = team[0]['player']['civilization']
            t2 = team[1]['player']['civilization']

            if t1 not in civCount:
                civCount[t1] = 1
            else:
                civCount[t1] = civCount[t1] + 1

            if t2 not in civCount:
                civCount[t2] = 1
            else:
                civCount[t2] = civCount[t2] + 1

            pair = ' '.join(sorted([t1, t2]))
            if pair not in teamCount:
                teamCount[pair] = 1
            else:
                teamCount[pair] = teamCount[pair] + 1
            total = total + 1

print('total: ' + str(total))
for pair in sorted(teamCount, key=teamCount.get, reverse=True):
    print(pair, teamCount[pair], '{:.1%}'.format(teamCount[pair]/total))

print()
for civ in sorted(civCount, key=civCount.get, reverse=True):
    print(civ, civCount[civ], '{:.1%}'.format(civCount[civ]/(total*2)))

