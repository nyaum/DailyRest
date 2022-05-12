import common as c
import requests
import datetime as dt
from datetime import datetime
from bs4 import BeautifulSoup
import urllib.parse as urlparse
import schedule as sc
import key as k
import log

class rest():
    def rest():
        print("\n---------------------휴일 글 작성 시작---------------------")
        def print_whichday(year, month, day) :
            r = ['월요일', '화요일', '수요일', '목요일', '금요일', '토요일', '일요일']
            aday = dt.date(year, month, day)
            bday = aday.weekday()
            return r[bday]

        def get_request_query(url, operation, params, serviceKey):
            params = urlparse.urlencode(params)
            request_query = url + '/' + operation + '?' + params + '&' + 'serviceKey' + '=' + serviceKey
            return request_query
            
        diffresult = []

        for month in range(1,13):
            if month < 10:
                month = '0' + str(month)
            else:
                month = str(month)

            mykey = k.REST_AUTH_KEY
            url = 'http://apis.data.go.kr/B090041/openapi/service/SpcdeInfoService'
            operation = 'getRestDeInfo'
            year = c.nowyear
            
            params = {'solYear':year, 'solMonth':month}

            request_query = get_request_query(url, operation, params, mykey)
            req = requests.get(request_query)

            if True == req.ok:
                soup = BeautifulSoup(req.content, 'lxml')

                item = soup.findAll('item')
            
            for i in item:

                day = int(i.locdate.string[-2:])
                weekname = print_whichday(int(year), int(month), day)

                day = datetime.strptime(i.locdate.get_text(), "%Y%m%d")
                # result = day.strftime("%m월 %d일".encode('unicode-escape').decode())
                # result = result.encode().decode('unicode-escape')
                # today = dt.datetime.now()
                diff = day - c.today
                
                # print(i.datename.string, ':', result, weekname, '입니다')
                if diff.days > 0:
                    diffresult.append('다음 공휴일인 ' + i.datename.string + '까지 ' + str(diff.days+1) + '일 남았습니다.')
                elif diff.days == 0:
                    diffresult.append('오늘은 ' + i.datename.string + ' 입니다.')

        # strftoday = today.strftime("작성일 : %Y년 %m월 %d일 \n\n".encode('unicode-escape').decode())
        # strftoday = strftoday.encode().decode('unicode-escape')

        write = c.strftoday + diffresult[0]

        try:
            c.api.update_status(write)
            print('\n---------------------휴일 디데이 글 작성 완료---------------------')
        except Exception as e:
            print('\n---------------------휴일 디데이 글 작성 실패---------------------')
            log.fail_log()

    sc.every().day.at("00:05:00").do(rest)