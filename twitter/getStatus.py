#!/usr/bin/env python

#Update your .twconfig file on this same directory
#with your own api keys and secrets
#Get them signing up at https://apps.twitter.com

#Install twitter module with 
#'pip install python-twitter' 

import configparser
import os
import sys
import json
import twitter

def jdefault(o):
    return o.__dict__
    #usage: print(json.dumps(string, default=jdefault))

def main():
	#Twitter status id to fetch
	statusId = '973464578708316161'

	try:
		sys.stdout.write('reading config file... ')
		config = configparser.RawConfigParser()
		config.read('.twconfig')
		print('success!')
	except:
		print('failed to read config file!')
		exit()
	try:
		sys.stdout.write('connecting to api... ')
		api = twitter.Api(consumer_key=config.get('keys', 'consumer_key'),
			consumer_secret=config.get('keys', 'consumer_secret'),
			access_token_key=config.get('keys', 'access_key'),
			access_token_secret=config.get('keys', 'access_secret'))
		print('success!')
	except Exception as e:
		print('failed to connect to twitter api!')
		print(e)
		exit()

	try:
		sys.stdout.write('fetching status %s... ' % statusId )
		status = api.GetStatus(statusId)
		print('success!')
	except:
		print('failed to get status!')
		exit()
	try:
		print('writing to file out.txt... ')
		with open(statusId + '.txt', 'w') as outfile:
			statusparsed = json.loads(str(status).encode())
			outfile.write(json.dumps(status, default=jdefault) + '\n')
			sys.stdout.write('Created at: ' + statusparsed['created_at'])
		outfile.closed
	except:
		print('failed writing to file!')
		exit()

if __name__ == "__main__":
	main()
