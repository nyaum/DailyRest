import tweepy

API_KEY = 'O9jwMCtaY0tiZmGhH1cSlTvbK'
API_KEY_SECRET = 'KtNrxiPXtHleWFliqghGZ5lQzKHtQon1dlksge9YODQgs9VU6F'
ACCESS_TOKEN = '1522436039729565696-qm2XxwZrELwOaspeg5MurR3O2BCAsL'
ACCESS_TOKEN_SECRET = 'GC1fBQocedFVPtzlkJRTLsOAEihfGm1ehixFQzMuNBbpX'

auth = tweepy.OAuthHandler(
   API_KEY, API_KEY_SECRET, callback='oob'
)
auth.set_access_token(
   ACCESS_TOKEN, ACCESS_TOKEN_SECRET
)

api = tweepy.API(auth)
