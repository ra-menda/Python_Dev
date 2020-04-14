inp = int(input())
h = inp // 3600
m = inp % 3600 // 60
s = inp % 60
print(f"{h}:{m}:{s}")
