num=[]
for i in range(100):
    num.append(i)

for i in num:
    if num%100==0:
        print('100の倍数')
    
    if num%5==0:
        print('5の倍数である')
