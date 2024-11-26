#check whether the given number is a Armstrong or not. 153 ,

num=int(input('enter a number '))
sum=0
temp=num
while temp>0:
    numb=temp%10
    sum+=numb**3
    temp//=10
if num==sum:
    print(f'{num} is Armstrong number' )
else:
     print(f'{num} is not Armstrong number' )
