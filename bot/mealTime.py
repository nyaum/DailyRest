import common as c
import schedule as sc
from datetime import datetime

class mealTime():
   def breakfast():
      dt_now = datetime.now()
      result = dt_now.strftime("현재 시간은 %H시 %M분, 아침 시간입니다".encode('unicode-escape').decode())
      result = result.encode().decode('unicode-escape')
      c.api.update_status(result)

      try:
         print('아침 글 작성 완료')
      except:
         print('아침 글 작성 실패')

   sc.every().day.at("07:00:01").do(breakfast)

   def lunch():
      dt_now = datetime.now()
      result = dt_now.strftime("현재 시간은 %H시 %M분, 점심 시간입니다".encode('unicode-escape').decode())
      result = result.encode().decode('unicode-escape')
      c.api.update_status(result)

      try:
         print('점심 글 작성 완료')
      except:
         print('점심 글 작성 실패')

   sc.every().day.at("12:00:01").do(lunch)

   def dinner():
      dt_now = datetime.now()
      result = dt_now.strftime("현재 시간은 %H시 %M분, 저녁 시간입니다".encode('unicode-escape').decode())
      result = result.encode().decode('unicode-escape')
      c.api.update_status(result)

      try:
         print('저녁 글 작성 완료')
      except:
         print('저녁 글 작성 실패')
         
   sc.every().day.at("19:00:01").do(dinner)

   # 테스트 코드
   # def test():
   #    dt_now = datetime.now()
   #    result = dt_now.strftime("현재 시간은 %H시 %M분, test 시간입니다".encode('unicode-escape').decode())
   #    result = result.encode().decode('unicode-escape')
   #    c.api.update_status(result)

   # 스케쥴로 시간마다 실행
   # sc.every(1).seconds.do(nowtime)
   # sc.every().day.at("15:36:01").do(test)