#有时候需要将一系列的字典储存在列表中或者将列表作为值储存在字典中，就需要用到嵌套。
#在列表中存储字典。
alien_0 = {'color':'green','points': 5 }
alien_1 = {'color':'yellow','points': 10}
alien_2 = {'color':'red','points': 15}
aliens = [alien_0,alien_1,alien_2]
for alien in aliens:
    print(alien)
    #创建30个外星人。
print('\n ')
aliens = []
for alien in range(30):
    new_alien = {'color':'green','points': 5}
    aliens.append(new_alien)
for alien in aliens[:5]:
    print(alien)
print('...')
print('Total number of aliens: ' + str(len(aliens)))
    #在python看来每个外星人都是独立的，我们可以改变其颜色。
print('\n ')
aliens = []
for alien in range(30):
    new_alien = {'color':'green','points': 5}
    aliens.append(new_alien)
for alien in aliens[:3]:#使用了切片
    if alien['color'] == 'green':
        alien['color'] = 'red'
        alien['points'] = 10
for alien in aliens[:5]:
    print(alien)
print('...')
    #经常需要在列表中包含大量的字典，例如存储众多用户的用户信息。
#在字典中存储列表，更有利于存储多方位信息。
pizza = {
    'crust':'thick',
    'toppings':['mushroom','extra chess'],
    }
print("You ordered a " + pizza['crust'] + '-crust pizza' + " with the following toppings:")
for topping in pizza['toppings']:
    print('\t'+topping)
    #每一个键都可以嵌套列表
favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah':['c'],
    'edward':['ruby','go'],
    'phil': ['pyhton','haskell'],
    }
for name,languages in favorite_languages.items(): #.items()可以调用字典的键值对。
    if len(languages) > 1:
        print('\n' + name.title()+"'s favorite languages are:")
        for language in languages:
            print('\t' + language.title())
    else:
        print('\n' + name.title()+"'s favorite languages is:")
        print('\t' + language.title())
#在字典中存储字典。
users = {
    'Lingling': {
        'first': 'Xu',
        'last': 'Lingling',
        'location': 'GUANGDONG SHENZHEN',
        },
    'Kunkun': {
        'first': 'Xu',
        'last': 'Kunkun',
        'location': 'HENAN XINGYANG',
        },
    'Peipei': {
        'first': 'Xu',
        'last': 'Peipei',
        'location': 'ZHEJIANG TONGXIANG',
        },    
  
    }
for username,user_info in users.items():
    print('\nUsername is: ' + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']
    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())
