10 Задание
1 Метод не фрозит, можно изменить
set1 = set ()
i = 0
while i < 10:
	i = i + 1
	num = int ( input ( "Введите любое число от 1 до 10: " ) )
	set1 . add (num)
print (set1)

2 метод
set1 = set ()
for x in range ( 1 ,11 ) :
	x = int (input ("Введите любое число от 1 до 10: ") )
	set1.add(x)
	print (tuple (set1))