# 6-7 在列表中存储字典
information_1 = {
    'first_name':'Xu',
    'last_name':'Lingling',
    'age':'30',
    'city':'Shenzhen'
    }
information_2 = {
    'first_name':'Xu',
    'last_name':'Kunkun',
    'age':'28',
    'city':'Shenzhen'
    }
information_3 = {
     'first_name':'Xu',
    'last_name':'Peipei',
    'age':'26',
    'city':'Jiaxing'
    }
information = [information_1,information_2,information_3]
for info in information:
    print (info)
# 6-8 在列表中存储字典
WHITE = {'type':'小狗',
    '所有者':'Guoji'
    }
YELLOW = {'type':'小猫',
    '所有者':'Peipei'
    }
GREEN = {'type':'水牛',
    '所有者':'Kunkun'
    }
pets = [WHITE,YELLOW,GREEN]
for pet in pets:
    print(pet)
#6-9 在字典中存储列表
favorite_palces = {
    '钢炮':['巴黎','波兰','堪培拉'],
    '阿昕':['深圳','广州','无锡'],
    '雪石':['自习室','图书馆','自习室'],
    '国际':['阳光沙滩']
    }
for name,palces in favorite_palces.items():
    if len(palces) >1:
        print('\n' + name + "'s favorite palces are:")
    else:
        print('\n' + name + "'s favorite palce is:")
    for palce in palces:
        print('\t'+ palce.title())
#6-10 喜欢的数字
number = {
    'Linda' : ['8','7','4','4'],
    'Daming' : ['7','5','6'], 
    'Jack' : ['6','5','8'],
    'Mary' : ['5','2','1'],
    'Augustin' : ['2','5','7','8','9','10'],
    }
print("Linda's favorite number is :")
for numbers in number['Linda']:
     print(numbers) 
print("Daming's favorite number is :")
for numbers in number['Daming']:
     print(numbers)
print("Jack's favorite number is :")
for numbers in number['Jack']:
     print(numbers)
print("Mary's favorite number is :")
for numbers in number['Mary']:
     print(numbers)
print("Augustin's favorite number is :") 
for numbers in number['Augustin']:
     print(numbers)
#6-11 城市
print('\n')
cities = {
    'Beijing' : {
        'country': 'China',
        'population' : '21.73 million',
        'fact' : 'It is the capital of china',
    },
        'Shengzhen' : {
        'country': 'China',
        'population' : '12.5283 million',
        'fact' : 'It is the special economic zone',
    },
        'Xinyang' : {
        'country': 'China',
        'population' : '8.85 million',
        'fact' : 'Possess many beautiful landscapes is the most obvious characteristic of Xingyang',
    },
    } 
for name,info in cities.items():
    print (name + ':' + '\n' + '\t' + 'country : ' + info['country'])
    print ('\t' + 'population:' + info['population'])
    print ('\t' + 'fact:' + info['fact']) 

 
 
 
 
 
 
 
 
 
 
 
