import tweepy
import datetime as dt
import sys
import key as k
import os

try:
    auth = tweepy.OAuthHandler(
    k.API_KEY, k.API_KEY_SECRET, callback='oob'
    )
    auth.set_access_token(
    k.ACCESS_TOKEN, k.ACCESS_TOKEN_SECRET
    )

    api = tweepy.API(auth)
    print("\n---------------------정상 실행---------------------")

except:
    print("\n---------------------실행 실패---------------------")
    sys.exit()

today = dt.datetime.now()
nowyear = today.strftime("%Y")

endyear = nowyear + '1231'
strftoday2 = today.strftime("%Y%m%d")
# strftoday2 = '20221231'

if endyear == strftoday2:
    nowyear = int(nowyear) + 1

strftoday = today.strftime("작성일 : %Y년 %m월 %d일 \n\n".encode('unicode-escape').decode())
strftoday = strftoday.encode().decode('unicode-escape')

def restart():
    os.execl(sys.executable, sys.executable, *sys.argv)