import tweepy
import common as c
import json as j

auth = tweepy.OAuthHandler(
   c.API_KEY, c.API_KEY_SECRET, callback='oob'
)
auth.set_access_token(
   c.ACCESS_TOKEN, c.ACCESS_TOKEN_SECRET
)

api = tweepy.API(auth)

#글 작성 기능
#api.update_status('TEST')

#팔로우한 계정 가져오기
id = api.get_follower_ids(screen_name='nya_eum')

#for e in len(id):
print(id[0], len(id))

fid = id[0]

#해당 계정 글 가져오기
get_timeline = api.user_timeline(user_id=fid, count=1)
print(get_timeline)

#json_data = j.loads(timeline)

#print(json_data['id'])

#api.create_favorites()

