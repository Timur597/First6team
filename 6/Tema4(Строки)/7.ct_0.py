# 1 Метод ,надо подумать, можно доработать думаю
# a = 'ну что начнемс ребята КОДИТЬ НА ЯЗЫКЕ PYTHON'
# print (a [0:3].upper () + " " + a [4:].lowwer () )

# 2 Метод рабочий
# txt = 'первое второе третье четвертое пятое шестое седьмое восьмое'
# txt1 = len (txt)
# lower_text = txt.lower ()
# upper_text = txt.upper ()
# cut_len = txt1 - (txt1 // 2)
# printlen = lower_text [:cut_len] + upper_text [cut_len:]   #:cut левая первая часть предложения.cut: правая значит.
# print (printlen)

# 3 Похожий пример, работает но не так как надо
pred = 'УЧИТЕЛЯ В НАШЕЙ ШКОЛЕ ДОВОЛЬНО СУРОВЫ, ведь кто если не мы ,а если не мы то кто!'
r = len (pred)
lowwer_q = r.lower()
upper_q = r.upper()
t = r - (r // 2)
printT = lowwer_q[: t] + upper_q[t :]
print (printT)

# 4 Похожий пример
# txt='УЧИТЕЛЯ В НАШЕЙ ШКОЛЕ ДОВОЛЬНО СУРОВЫ, ведь кто если не мы ,а если не мы то кто!'
# txt1= len(txt)
# cut_len= txt1-(txt1//2) #Если мы делим кол-во букв на 2,то лучше всего делать с округлением в меньшую сторону.
# lower_case= txt.lower()
# upper_case= txt.upper()
# printT=lower_case[0: cut_len] + upper_case[cut_len :]
# print(printT)

# 3 Метод
# x = 'первое второе третье четвертое'
# y = 'пятое шестое седьмое восьмое'
# print (x. upper(),y.lower())
 
 # 4 Метод
# txt='УЧИТЕЛЯ В НАШЕЙ ШКОЛЕ ДОВОЛЬНО СУРОВЫ, ведь кто если не мы ,а если не мы то кто!'
# d = txt.split()
# r = len(d)
# for i in range (r // 2):
# 	print (d[i].upper(), end="")
# s = r - r // 2
# while s < r:
#  	print (d[s].lower(), end="")
#  	s=s+1