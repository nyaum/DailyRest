import tweepy
import datetime as dt

API_KEY = 'O9jwMCtaY0tiZmGhH1cSlTvbK'
API_KEY_SECRET = 'KtNrxiPXtHleWFliqghGZ5lQzKHtQon1dlksge9YODQgs9VU6F'
ACCESS_TOKEN = '1522436039729565696-qm2XxwZrELwOaspeg5MurR3O2BCAsL'
ACCESS_TOKEN_SECRET = 'GC1fBQocedFVPtzlkJRTLsOAEihfGm1ehixFQzMuNBbpX'

REST_AUTH_KEY = 'w7Ycwo9qcSFEoKkPtsvvg1ww8vxweOXvChmlMql3HZxutjR%2FYbmn7vWJONRUy25Zozng3hSvyKOGMM5glY%2BRWw%3D%3D'

auth = tweepy.OAuthHandler(
   API_KEY, API_KEY_SECRET, callback='oob'
)
auth.set_access_token(
   ACCESS_TOKEN, ACCESS_TOKEN_SECRET
)

api = tweepy.API(auth)

today = dt.datetime.now()
nowyear = today.strftime("%Y")
strftoday = today.strftime("작성일 : %Y년 %m월 %d일 \n\n".encode('unicode-escape').decode())
strftoday = strftoday.encode().decode('unicode-escape')
