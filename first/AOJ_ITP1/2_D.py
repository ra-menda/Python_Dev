W,H,x,y,r = map(int,input().split())
if (x-r)>=0 and (x+r)<=W:
    if (y-r)>=0 and (y+r)<=H:
        print("Yes")
    else:
        print("No")
else:
    print("No")
