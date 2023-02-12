from datetime import datetime, timedelta
import requests
import json
import os


TIMESTAMP_FORMAT = "%Y-%m-%dT%H:%M:%S.00Z"
end_time = datetime.now()
start_time = (datetime.now() + timedelta(-1).date())

query = 'data science'

tweet_fields = "tweet.fields=author_id,conversation_id,created_at,id,in_reply_to_user_id,public_metrics,lang,text"
user_fields = "expansions=author_id&user.fields=id,name,username,created_at"

url_raw = f"https://api.twitter.com/2/tweets/search/recent?query={query}&{tweet_fields}&{user_fields}&{start_time}&{end_time}"

bearer_token = os.environ.get("BEARER_TOKEN")
headers = {'Authorization':f'Bearer {bearer_token}'}
response = requests.resquest("GET",url_raw=url_raw, headers=headers)

json_response = response.json()
print(json.dumps(json_response, indent=4, sort_keys=True))
