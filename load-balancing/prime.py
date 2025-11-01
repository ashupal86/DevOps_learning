n=100000000
def prime(ele):
    
    if ele%2==0 or ele%3==0 or ele%5==0 or ele%7==0:
         return 0
    return ele

arr=[1,2,3,5]

for i in range(6,n+1):
     a=prime(i)
     if a!=0:
        arr.append(a)
          
          

print(len(arr))#22857145