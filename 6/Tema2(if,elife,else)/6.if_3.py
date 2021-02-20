#1 Метод
num = int ( input ('Введите число: ') )
if num > 0 and num < 21:
	print ('Разрешено')
if num > 57 and num < 100:
	print ('разрешено')
if num > 21 and num < 57:
	print ('Запрещено')
if num > 100 or num < 0:
	print ('запрещено')

# 2 Метод 
good = range (0, 21)
good2 = range (57,100)
c = 19
if c in good or c in good2:
	print ('good')
else:
	print ('bad')