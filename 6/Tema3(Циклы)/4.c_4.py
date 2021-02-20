4 ЗАДАНИЕ
1 Метод
languages = ["go","mo","do","Rust","fo","bo"]
i = 0
while languages [i] != 6:
	print (i, languages [i])
	i = i + 1      #Выдает ошибку индексации

2 Метод
languages = ["go","mo","do","Rust","fo","bo"]
for i in range (0, 6):
	print(i, languages [i])


3 Метод
languages = ["go","mo","do","Rust","fo","bo"]
for i, languages in enumerate ( ["go","mo","do","Rust","fo","bo"] ):
	print (i, languages)