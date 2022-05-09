import common as c
import schedule as sc
import time
import sys
import mealTime as mt
from pytimekr import pytimekr

try:
   print('---------------정상 실행----------------')
except:
   print('---------------실행 실패----------------')
   sys.exit()

# 실행
mt.mealTime()

# 무한 루프문
while True:
   sc.run_pending()
   time.sleep(1)

# now = datetime(2022, 5, 9, 11, 30)

#if t.clock():
#api.update_status('')

#팔로우한 계정 가져오기
# id = api.get_follower_ids(screen_name='nya_eum')
# create_friendship = api.create_friendship(id)

# for e in len(id):
# print(id[0], len(id))

# fid = id[0]

# #해당 계정 글 가져오기
# get_timeline = api.user_timeline(user_id=fid, count=1)
# print(get_timeline)

#json_data = j.loads(timeline)

#print(json_data['id'])

#api.create_favorites()

