# ------------------------------------
# PLEASE BE CAREFUL WITH THIS FILE 
# 	I included my api key and this code to show my process
#	this code does not need to be run as I have already collected and stored the data from the api requests shown
# Feel free to look at the data and play around with it and do things I haven't just don't mess with this file
# ------------------------------------

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
	print('requesting {}-th match. id: {}'.format(i, m['match_id']))
	
	# PLEASE DON'T UNCOMMENT AND RUN THIS - THE DATA IS ALREADY STORED IN THE TXT FILE IN THE SUBMISSION
	# i might delete the key upon submission so if you REALLY want to run this file comment out the current api call and uncomment the following line (api call without my api key) and uncomment the sleep line (because there is a rate limit - both per second and total calls cap)
	# API CALLS TO THIS KEY CHARGE ME so pls (again i might delete so i won't have to worry xd - but i kinda want to work on this more over the summer so probs not)
	r = requests.get('https://api.opendota.com/api/matches/{}?api_key=0510a91f-c1f5-49ec-9ff8-07f087283ad1'.format(m['match_id']))
	#r = requests.get('https://api.opendota.com/api/matches/{}'.format(m['match_id']))
	
	#print(type(r))
	# default write encodes to ascii and there are multiple unicode characters present in the data - sucks because it makes the file of data much larger (maybe there's some smart way to deal with this)
	f.write((r.text).encode('utf-8'))
	f.write('\n')
	print(r.text)
	#time.sleep(5)
	i += 1
	
print('processed {} matches'.format(i))
f.close()
