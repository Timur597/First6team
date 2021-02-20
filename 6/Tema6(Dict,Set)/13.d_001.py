13 Задание
farm_2 = {"cow", "horse", "donkey", "cat", "dog"}
farm_1 = {"dog", "cat", "mouse", "sheep"}
farm_3 = farm_2.intersection_update (farm_1) #  не надо писать set
print (farm_2)
t = farm_1.difference_update (farm_2)
print (farm_1)
