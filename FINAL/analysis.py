import json
import time
import requests

input_file = open('my_matches.json')
matches = json.load(input_file)
input_file.close()

print('loading {} matches\n'.format(len(matches)))

f = open('pob_match_data.txt', 'w')
i = 0
for m in matches:
	print('requesting match {}'.format(m['match_id']))
	r = requests.get('https://api.opendota.com/api/matches/{}?=api_key=0510a91f-c1f5-49ec-9ff8-07f087283ad1'.format(m['match_id']))
	print(type(r))
	f.write((r.text).encode('utf-8'))
	f.write('\n')
	print(r.text)
	#time.sleep(2)
	i += 1
	
print('processed {} matches'.format(i))
f.close()
