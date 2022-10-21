price = input()
if len(price) <= 2:
    print(99)
else:
    num = int(price[-2:])
    if(num) >= 49:
        price = price[0:-2] + "99"
        print(price)
    else:
        a = int(price)-int(num)-1
        print(a)
        