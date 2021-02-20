#11 Задание не работает как надо
south_american_countries = ['Argentina', 'Bolivia', 'Brazil', 'Chile', 'Colombia', \
'Ecuador', 'Guyana', 'Paraguay', 'Peru', 'Suriname', 'Suriname', 'Uruguay', 'Venezuela']
a=south_american_countries
a.remove('Suriname')
print(a)
s=['Suriname']
a.intersection('Suriname')
print(a) # не возвращает

2 метод
x =south_american_countries = ['Argentina', 'Bolivia', 'Brazil', 'Chile', 'Colombia', \
  'Ecuador', 'Guyana', 'Paraguay', 'Peru', 'Suriname', 'Suriname', 'Uruguay', 'Venezuela']
x = set(south_american_countries)
print(list(x))