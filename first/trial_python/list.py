#https://www.python-izm.com/basic/list/

#リストの基本
print('\n#リストの基本')
test_list_1 = ['Hello', '/', 'world', '.', 'com' , '!!!!!!']
print(test_list_1)
 
print('--------------------------------')
 

for i in test_list_1:
    print(i)

#要素の追加
print('\n#要素の追加')
test_list_1 = []
print(test_list_1)
 
print('--------------------------------')
 
test_list_1.append('python')
test_list_1.append('-')
test_list_1.append('izm')
test_list_1.append('.')
test_list_1.append('com')
 
print(test_list_1)

#インデックスを指定して追加

print('\n#インデックスを指定して追加')
test_list_1 = ['python', 'izm', 'com']
print(test_list_1)
 
print('--------------------------------')
 
test_list_1.insert(1, '-')
test_list_1.insert(3, '.')
 
print(test_list_1)
 
test_list_1.insert(0, 'http://www.')
 
print(test_list_1)

#要素の削除1
print('\n#要素の削除1')
test_list_1 = ['1', '2', '3', '2', '1']
print(test_list_1)
 
print('--------------------------------')
 
test_list_1.remove('2')
 
print(test_list_1)

#要素の削除2
print('\n#要素の削除2')

test_list_1 = ['1', '2', '3', '2', '1']
print(test_list_1)
 
print('--------------------------------')
 
print(test_list_1.pop(1))
print(test_list_1)
 
print(test_list_1.pop())
print(test_list_1)