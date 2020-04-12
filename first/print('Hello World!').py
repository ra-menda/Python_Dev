#参考サイト　https://www.python-izm.com/basic/string/

print('python-izm')
print("python-izm")

test_str = """
test_1
test_2
"""
print(test_str)

test_str = 'python'
test_str = test_str + '_'
test_str += 'izm'
print(test_str)

test_str = '012'
test_str += '345'
test_str += '678'
test_str += '9'
print(test_str)
#繰り返し
test_str ='012'*3
print(test_str)
#追加
test_integer = 100
print(str(test_integer)+'円')
#変更
test_str ='python-izm'
print(test_str.replace('izm','ism'))
#分割
test_str = 'python-izm'
print(test_str.split('-'))
#桁そろえ
test_str = '1234'
print(test_str.rjust(10,'0'))
print(test_str.rjust(10,'!'))

print(test_str.zfill(10))
print(test_str.zfill(3))
#検索
test_str = 'python-izm'
print(test_str.startswith('python'))
print(test_str.startswith('izm'))

test_str = 'python-izm'
print('z' in test_str)
print('s' in test_str)
#大文字小文字変換
test_str ='Python-Izm.Com'
print(test_str.upper())
print(test_str.lower())

#先頭末尾削除
print('---------------------')
test_str = '    python-izm.com'
print(test_str)
test_str = test_str.lstrip()
print(test_str)
test_str = test_str.lstrip('python')
print(test_str)
print('------------------------')
test_str = 'python-izm.com'
print(test_str+'/')
test_str = test_str.rstrip()
print(test_str+'/')
test_str=test_str.rstrip("com")
print(test_str)