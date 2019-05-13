import json
import collections
import operator

class Match:
    def __init__(self, match, radiant_win):
        self.match = match
        self.radiant_win = radiant_win
        self.hero_picks = []


names = {}
with open('heroes.json') as file:
    data = json.load(file)
    for hero in data:
        names[hero['id']] = hero['localized_name']


def process_match(match):

    radiant_win = match['radiant_win']

    m = Match(match['match_id'], radiant_win)

    for pb in match['picks_bans']:
        if pb['is_pick']:
            m.hero_picks.append(names[pb['hero_id']])

    return m


with open('pob_match_data.txt', 'r', errors='replace') as file:
    matches = file.readlines()

processed = 0
errors = 0
processed_matches = []
for match in matches:
    match = json.loads(match)

    try:
        processed_matches.append(process_match(match))
        processed += 1
    except Exception as e:
        errors += 1
        #print("Error processing match. error {}\n".format(e))

print("Processed {} matches. Errors: {}".format(processed, errors))

print("\n\nPOBBISH MATCH STATISTICS\n")

won_matches = list(filter(lambda m : m.radiant_win, processed_matches))
print('Radiant won {} of the {} games.'.format(len(won_matches), len(processed_matches)))
print('\tOverall Winrate: {0:.2f}'.format(float(len(won_matches)/len(processed_matches) * 100)))

print("\nA few of my most played heroes:")
spec_matches = list(filter(lambda m : 'Spectre' in m.hero_picks, processed_matches))
print('Found {} games where Spectre was picked.'.format(len(spec_matches)))

drow_matches = list(filter(lambda m : 'Drow Ranger' in m.hero_picks, processed_matches))
print('Found {} games where Pob\'s team picked Drow Ranger.'.format(len(drow_matches)))

pa_matches = list(filter(lambda m : 'Phantom Assassin' in m.hero_picks, processed_matches))
print('Found {} games where Pob\'s team picked Phantom Assassin.'.format(len(pa_matches)))

print("\n\nTOTAL HERO STATS IN POBBISH'S MATCHES\n")

#hero_wins = collections.defaultdict(int)
hero_totals = collections.defaultdict(int)
hero_matches = collections.defaultdict(list)
for m in processed_matches:
    for hero in m.hero_picks:
        hero_totals[hero] += 1
        #if not match.pob_win:
            #hero_wins[hero] += 1
        hero_matches[hero].append(m.match)

#win_percent = collections.defaultdict(float)
#for k, v in hero_matches.items():
    #win_percent[k] = (v/hero_totals[k])

sorted_picks = collections.OrderedDict(sorted(hero_totals.items(), key=operator.itemgetter(1), reverse=True))

for k, v in sorted_picks.items():
    print("{} has been picked {} out of {} games in Pobbish's matches.".format(k, hero_totals[k], len(processed_matches)))
    print("\tOverall pick rate: {0:.2f}%".format(float(hero_totals[k]/len(processed_matches) * 100)))