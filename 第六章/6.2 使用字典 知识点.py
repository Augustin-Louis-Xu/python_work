#一个简单的字典
alien_0 = {'color':'green','points':'5'}
print(alien_0['color'])
print(alien_0['points'])
    #如果玩家射杀了外星人时，运行这段代码，你将会获得如下的提示点数。
alien_0 = {'color':'green','points':'5'}
new_points = alien_0['points']
print('You just earned ' + str(new_points) + ' points!')
#添加键-值对
alien_0 = {'color':'green','points':'5'}
print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
print(alien_0['y_position'])#注意输出的键——值对应排列顺序与添加顺序可能不一致，python只关心键和值的关联关系，不关心添加顺序。
#先创建一个空字典，在存储大量用户数据以及编写能够自动生成大量的键——值对的代码时，通常都先建立一个空字典。
alien_0 = {}
alien_0['color'] = 'green'
alien_0['point'] = '5'
print(alien_0)
#修改字典中的值
alien_0 = {'color':'Green'}
print('The alien is ' + alien_0['color'] + '.')
alien_0['color'] = 'Yellow'#此处修改了外星人的颜色。
print('The alien is ' + alien_0['color'] + '.')
#追踪外星人的位置
alien_0 = {'x_position':0,'y_position':25,'speed':'slow'}#注意此处将x_position定义为了整形数，0与‘0’会导致不同的输出结果，要特别注意。
print('Original x_position is ' + str(alien_0['x_position']) + '.')
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
alien_0['x_position'] = alien_0['x_position'] + x_increment#外星人的更新位置。
print('New x_position is ' + str(alien_0['x_position']) + '.')
