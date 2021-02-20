1 ЗАДАНИЕ
1 МЕТОД
lang = "Rust"
languages = ["go","mo","do","Rust","fo","bo"]
c = "This languages in list"
i = 0
while languages [i] != lang:     #как я понял while всегда надо писать не равно,а после через else выводить равенство.
	print ("bad")
	i = i + 1
else:
	print (c)
	
2 МЕТОД
lang = "Rust"
languages = ["go","mo","do","Rust","fo","bo"]
c = "This languages in list"
for i in range (0, 5):
	if languages [i] == lang:
		print (c) 
	else:
		print ("жопа")	