import requests


def call(data):
	tosswinner=data['tosswinner']
	tossdec=data['tossdec']
	if(data['tossch']!='true'):
		tosswinner=None
		tossdec=None
	API_KEY = {{ API_KEY }}
	token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey": API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
	mltoken = token_response.json()["access_token"]
	temp=data['venue'][0]
	temp=list(map(str.strip, temp.split(',')))
	city=temp[1]
	venue=temp[0]
	header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

	payload_scoring = {
		"input_data": [
			{
				"fields": [
					"id",
					"season",
					"city",
					"date",
					"team1",
					"team2",
					"toss_winner",
					"toss_decision",
					"result",
					"dl_applied",
					"winner",
					"win_by_runs",
					"win_by_wickets",
					"player_of_match",
					"venue",
					"umpire1",
					"umpire2",
					"umpire3",
					"winner_id",
					"team1_id",
					"team2_id",
					"toss_winner_id"
				],
				"values": [
					[
						1,
						None,
						city,
						None,
						data['team1'][0],
						data['team2'][0],
						data['tosswinner'][0],
						data['tossdec'][0],
						None,
						None,
						None,
						None,
						None,
						None,
						venue,
						data['umpire1'][0],
						data['umpire2'][0],
						data['umpire3'][0],
						None,
						None,
						None,
						None,
						None
					]
				]
			}
		]
	}
	response_scoring = requests.post('https://eu-gb.ml.cloud.ibm.com/ml/v4/deployments/70803dd9-2abc-421a-8320-6683b700f799/predictions?version=2021-08-31', json=payload_scoring, headers={'Authorization': 'Bearer ' + mltoken})
	response_scoring=response_scoring.json()
	winner=response_scoring['predictions'][0]
	winner=winner['values']
	win=winner[0]
	return win
