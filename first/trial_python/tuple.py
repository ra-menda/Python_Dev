#https://www.python-izm.com/basic/tuple/

import datetime

#関数定義
def get_today():
 
    today = datetime.datetime.today()
    value = (today.year, today.month, today.day)
 
    return value
 
 
test_tuple = get_today()
 
print(test_tuple)
print(test_tuple[0])
print(test_tuple[1])
print(test_tuple[2])