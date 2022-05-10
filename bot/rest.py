import common as c
import requests
import datetime as dt
from datetime import datetime
from bs4 import BeautifulSoup
import urllib.parse as urlparse
import schedule as sc

class rest():
    def rest():
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

            mykey = "w7Ycwo9qcSFEoKkPtsvvg1ww8vxweOXvChmlMql3HZxutjR%2FYbmn7vWJONRUy25Zozng3hSvyKOGMM5glY%2BRWw%3D%3D"
            url = 'http://apis.data.go.kr/B090041/openapi/service/SpcdeInfoService'
            operation = 'getRestDeInfo'
            year = 2022
            
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
                today = dt.datetime.now()
                diff = day - today
                
                # print(i.datename.string, ':', result, weekname, '입니다')
                if diff.days > 0:
                    diffresult.append('다음 공휴일인 ' + i.datename.string + '까지 ' + str(diff.days+1) + '일 남았습니다.')

        strftoday = today.strftime("작성일 : %Y년 %m월 %d일 \n\n".encode('unicode-escape').decode())
        strftoday = strftoday.encode().decode('unicode-escape')

        write = strftoday + diffresult[0]
        c.api.update_status(write)

        try:
            print('휴일 디데이 글 작성 완료')
        except:
            print('휴일 디데이 글 작성 실패')

    sc.every().day.at("00:00:01").do(rest)