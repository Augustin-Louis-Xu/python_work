#4-10
my_foods=['pizza','falafel','carrot cake']
friend_foods=my_foods[:]
my_foods.append('cannoli')
friend_foods.append('ice cream')
print('\nMy favorite foods is:')
print(my_foods)
print("\nMy friend's favorite is:")
print(friend_foods)
print('\nThe first three items in the list are:')
print(my_foods[:3])#前三个
print('\nThe items from the middle of the list is:')
print(my_foods[1:4])#中间三个
print('\nThe last three items in the list is:')
print(my_foods[1:])#最后三个
#4-11
pizzas=['pan ','thick style','california Style']
friend_pizzas=pizzas[:]#创建副本
pizzas.append('Thick style')
friend_pizzas.append('Take and Bake Style')
print('\nMy favorite pizzas are:')
print(pizzas)
print("\nMy friend' favorite pizzas are:")
print(friend_pizzas)
print('\n')
for pizza in friend_pizzas:
	 print(pizza.upper())
#4-12
print('\t')
my_foods=['pizza','falafel','carrot cake']
friend_foods=my_foods[:]
my_foods.append('cannoli')
friend_foods.append('ice cream')
for food in my_foods:
	print(food.title())
print('\n')
for food in friend_foods:
	print(food.title())
