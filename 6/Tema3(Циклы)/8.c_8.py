1 Метод
num = int (input ('Введите число от 100 до 999: ') )
if num > 100 and num < 999:
	while True:
		print ('Это число трехзначное')
		break
if num > 0 and num % 2 == 0:
	while True:
		print ('Это число положительное и чётное')
		break
if num % 31 == 0:
	while True:
		print ('Это число делится на 31 без остатка')
		break
if num > 100 and num % 17 == 0 or num > 150 and num == 13 ** 2:
	while True:
		print ('Это число больше 100 и оно делится на 17 без остатка или это число больше 150 и равно 13 ** 2')
		break

2 Метод

a = 600
while  a <= 600:
# 1
	if a > 99 and a < 1000:
		print('число трёхзначное')
	else:
		print("число не трёхзначное")
# 2
	if a > (-1):
		print('число положительное')
	else:
		print('число не положительное')
	if a % 2 == 0:
		print('число чётное')
	else:
		print('число не чётное')
# 3
	if a % 31:
		print('число делится на 31 без остатка')
	else:
		print('число не делится на 31 без остатка')
# 4
	if a > 100:
		print ('число больше 100')
	else:
		print('число не больше 100')
	if a % 17:
	     print ('число делится на 17')
	else:
		print('число не делится на 17')
	if a > 150: 
		print ('число больше 150')
	else:
		print('число не больше 150')
	if a == 13**2:
		print ('число равно на 13**2')
	else:
		print('число не равно на 13**2')
		break
print(a)

3 Метод

num = 100
if(num < 1000 and num > 99):
    print("It's a 3 digit number")
else:
    print("is not a 3 digit number")

#3. Is it EVEN or ODD number?
if (num // 2) != 0:
    print("100 in an EVEN number")
else:
    print("100 is an ODD number")

#4 Can 100 be divided by 31 without remainder
if (num % 17) != 0 or (num > 150) and (num == 13**2):
    print(num)