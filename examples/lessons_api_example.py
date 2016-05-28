# Run with Python 3
import json
import requests
import pylab
import pandas as pd
import matplotlib.pyplot as plt

'''This example is made to be simple and useful. 
It demonstrates how to get lessons data via StepicAPI and why it can be useful.'''

# 1. Get your keys at https://stepic.org/oauth2/applications/ (client type = confidential,
# authorization grant type = client credentials)
client_id = "Put yours here"
client_secret = "Put yours here"

# 2. Get a token
auth = requests.auth.HTTPBasicAuth(client_id, client_secret)
resp = requests.post('https://stepic.org/oauth2/token/',
                     data={'grant_type': 'client_credentials'},
                     auth=auth
                     )
token = json.loads(resp.text)['access_token']

# 3. Call API (https://stepic.org/api/docs/) using this token.
# Example:
api_url = 'https://stepic.org/api/lessons'
lessons = json.loads(requests.get(api_url, headers={'Authorization': 'Bearer '+ token}).text)

lessons_data_frame = pd.DataFrame(lessons['lessons'])

passed = lessons_data_frame['passed_by'].values
time_to_complete = lessons_data_frame['time_to_complete'].values
views = lessons_data_frame['viewed_by'].values

pylab.subplot (3, 1, 1)
pylab.xlabel('time (s)')
pylab.ylabel('Viewed this')
pylab.bar (time_to_complete, views)
pylab.title ("Comparison of viewed/passed")

pylab.subplot (3, 1, 2)
pylab.xlabel('time (s)')
pylab.ylabel('Passed this')
pylab.bar (time_to_complete, passed)

pylab.subplot (3, 1, 3)
pylab.xlabel('time (s)')
pylab.ylabel('Quited this')
pylab.bar (time_to_complete, views-passed)
pylab.savefig('quit.png')
