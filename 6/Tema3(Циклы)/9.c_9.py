# 9 Задание
num=-100
num1=num
i=0
x=0
while num<=100:
	if (num%13==0) & (num%2==0):
		print(num,num**2)
		i=i+1
	num=num+1
print(i)

while num1<=100:
	if num1%2==1:
		x=x+1
		print(num1)
	num1=num1+7
print(x)