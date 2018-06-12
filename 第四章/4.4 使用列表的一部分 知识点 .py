#切片
players=['charles','martina','michael','florence','eli']
print(players[0:3])
print(players[0:])
print(players[:4])
print(players[-3:])
#遍历切片
players=['charles','martina','michael','florence','eli']
print('Here are the first three players on our team:')
for player in players[:3]:
    print (player.title())#切片非常有作用，比如说在退出游戏时，可以将其分数加入一个列表中，然后将列表降序排列，最后用切片输出可以得到最高的三个得分。还可以用切片批量处理数据。
#复制列表
my_foods=['pizza','falafel','carrot cake']
friend_foods=my_foods[:]#注意，此处是添加了一个副本列表，一下会核实存在两个列表。
my_foods.append('cannoli')
friend_foods.append('ice cream')
print('\nMy favorite foods is:')
print(my_foods)
print("\nMy friend's favorite is:")
print(friend_foods)
  #以下演示在不使用切片的情乱下，简单的赋值，是不会得到两个列表的，两个变量指向同一个列表。
my_foods=['pizza','falafel','carrot cake']
friend_foods=my_foods
my_foods.append('cannoli')
friend_foods.append('ice cream')
print('\nMy favorite foods is:')
print(my_foods)
print("\nMy friend's favorite is:")
print(friend_foods)
print('\n')
