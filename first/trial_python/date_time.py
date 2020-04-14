#https://www.python-izm.com/basic/date_time/

import datetime
import calendar

#日付の取得

today = datetime.date.today()
todaydetail = datetime.datetime.today()

#今日の日付
print("-----------------")
print(today)
print(todaydetail)

#今日に日付：それぞれの値
print("-----------------")
print(today.year)
print(today.month)
print(today.day)
print(todaydetail.year)
print(todaydetail.month)
print(todaydetail.day)
print(todaydetail.hour)
print(todaydetail.minute)
print(todaydetail.second)
print(todaydetail.microsecond)
 
#日付のフォーマット
print("-----------------")
print(today.isoformat())
print("本日の日付は" + todaydetail.strftime("%Y/%m/%d %H:%M:%S"))

#明日の日付
print("明日の日付は" + str(todaydetail + datetime.timedelta(days=1)))
 
newyear = datetime.datetime(2010, 1, 1)
 
#2010年1月1日の一週間後
print("2010年1月1日の一週間後は" + str(newyear + datetime.timedelta(days=7)))
 
#2010年1月1日から今日までの日数
calc = todaydetail - newyear
 
#計算結果の戻り値は「timedelta」
print("2010年1月1日から今日までの日数：" + str(calc.days) + "日")

#うるう年の判定
print("2015年はうるう年か：" + str(calendar.isleap(2015)))
print("2016年はうるう年か：" + str(calendar.isleap(2016)))
print("2017年はうるう年か：" + str(calendar.isleap(2017)))
print("2010-2020の間にうるう年は何年あるか？")
print(str(calendar.leapdays(2010, 2020)) + "年")