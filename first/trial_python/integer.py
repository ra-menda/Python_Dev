#https://www.python-izm.com/basic/integer/

#四則演算
test_integer = 100
print("-------\n四則演算")
print("10を足すと" + str(test_integer + 10))
print("10を引くと" + str(test_integer - 10))
print("10をかけると" + str(test_integer * 10))
print("10で割ると"+ str(test_integer /10))

#数値変換
test_str = "100"

print("-------\n数値変換")
print(int(test_str) + 100)

#浮動小数点
test_str = "100.5"

print("-------\n浮動小数点")
print(float(test_str) + 100)

#複素数
test_complex = 100 + 5j

print("-------\n複素数計算")
print(test_complex)
print(test_complex.real)
print(test_complex.imag)