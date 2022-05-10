import tweepy
import datetime as dt
import sys
import key as k

try:
    auth = tweepy.OAuthHandler(
    k.API_KEY, k.API_KEY_SECRET, callback='oob'
    )
    auth.set_access_token(
    k.ACCESS_TOKEN, k.ACCESS_TOKEN_SECRET
    )

    api = tweepy.API(auth)
    print("---------------정상 실행---------------")

except:
    print("---------------실행 실패---------------")
    sys.exit()

today = dt.datetime.now()
nowyear = today.strftime("%Y")
strftoday = today.strftime("작성일 : %Y년 %m월 %d일 \n\n".encode('unicode-escape').decode())
strftoday = strftoday.encode().decode('unicode-escape')
