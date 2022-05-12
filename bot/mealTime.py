import common as c
import schedule as sc
import log

class mealTime():
   def breakfast():
      print("\n---------------------아침 글 작성 시작---------------------")
      result = c.today.strftime("현재 시간은 %H시 %M분, 아침 시간입니다".encode('unicode-escape').decode())
      result = result.encode().decode('unicode-escape')      
      breakfast_result = c.strftoday + result

      try:
         c.api.update_status(breakfast_result)
         print('\n---------------------아침 글 작성 완료---------------------')
      except Exception as e:
         print('\n---------------------아침 글 작성 실패---------------------')
         log.fail_log()

   sc.every().day.at("07:00:01").do(breakfast)

   def lunch():
      print("\n---------------------점심 글 작성 시작---------------------")
      result = c.today.strftime("현재 시간은 %H시 %M분, 점심 시간입니다".encode('unicode-escape').decode())
      result = result.encode().decode('unicode-escape')      
      lunch_result = c.strftoday + result

      try:
         c.api.update_status(lunch_result)
         print('\n---------------------점심 글 작성 완료---------------------')
      except Exception as e:
         print('\n---------------------점심 글 작성 실패---------------------')
         log.fail_log()

   sc.every().day.at("12:00:01").do(lunch)

   def dinner():
      print("\n---------------------저녁 글 작성 시작---------------------")
      result = c.today.strftime("현재 시간은 %H시 %M분, 저녁 시간입니다".encode('unicode-escape').decode())
      result = result.encode().decode('unicode-escape')
      dinner_result = c.strftoday + result
      
      try:
         c.api.update_status(dinner_result)
         print('\n---------------------저녁 글 작성 완료---------------------')
      except Exception as e:
         print('---------------------저녁 글 작성 실패---------------------')
         log.fail_log()
         
   sc.every().day.at("19:00:01").do(dinner)

   # 테스트 코드
   # def test():
   #    result = c.today.strftime("현재 시간은 %H시 %M분, test 시간입니다".encode('unicode-escape').decode())
   #    result = result.encode().decode('unicode-escape')
   #    c.api.update_status(result)

   # 스케쥴로 시간마다 실행
   # sc.every(1).seconds.do(nowtime)
   # sc.every().day.at("15:36:01").do(test)