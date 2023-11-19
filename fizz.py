num=[]
for i in range(100):
    num.append(i)

for i in num:
    if i%100==0:
        print(str(i)+'は100の倍数')
    
    if i%5==0:
        print(str(i)+'は5の倍数である')
    if i%10==0:
        print(str(i)+'は10の倍数')
        
        
