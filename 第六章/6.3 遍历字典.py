#遍历所有的键值对
user_0 = {
    'username':'efermi',
    'first':'enrico',
    'last':'fermi',
    }
for key,value in user_0.items():
    print('\nkey:' + key)
    print('value:' + value)
#前面的一个例子
print('\n')
favorite_languages = {
    'jane':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',#此处加逗号是为了在下一行添加键值对。
    }#注意使用多行来定义字典时的格式。
for name,language in favorite_languages.items():
    print(name.title()+"'s favorite is " + language + '.')
#遍历字典中的所有键在使用字典中的部分信息时特别有用。
print('\n')
favorite_languages = {
    'jane':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',#此处加逗号是为了在下一行添加键值对。
    }#注意使用多行来定义字典时的格式。
for value in favorite_languages.values():#注意此处不同于使用字典所有信息的".items()"。
    print(value.title())
print('\n')
for name in favorite_languages.keys():#注意此处不同于使用字典所有信息的".items()"。
    print(name.title())
    #使用当前键来访问与之关联的值。
print('\n')
favorite_languages = {
    'jane':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',#此处加逗号是为了在下一行添加键值对。
    }#注意使用多行来定义字典时的格式。
friends = ['phil','sarah']
for name in favorite_languages.keys():#注意此处不同于使用字典所有信息的".items()"。
    print(name.title())
    if name in friends:
        print('Hi, ' + name.title() + 
        'I see your favorite language is ' + 
        favorite_languages[name].title() +
        '.')
#使用keys()确定某个人是否接受了检查，实际上keys()的作用是返回一个包含字典中所有键的列表。
print('\n')
favorite_languages = {
    'jane':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',#此处加逗号是为了在下一行添加键值对。
    }#注意使用多行来定义字典时的格式。
if 'erin' not in favorite_languages.keys(): #此行代码作用是核实'erin'是否在keys()返回的列表中。
    print('Erin, please take our poll!')
#按顺序遍历字典中的所有键
print('\n')
favorite_languages = {
    'jane':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',#此处加逗号是为了在下一行添加键值对。
    }#注意使用多行来定义字典时的格式。
for name in sorted(favorite_languages.keys()):
    print(name.title() + ', thank you for taking the poll.')
#遍历字典中的所有值
print('\n')
favorite_languages = {
    'jane':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',#此处加逗号是为了在下一行添加键值对。
    }#注意使用多行来定义字典时的格式。
print('以下的这些语言被提及：')

for value in favorite_languages.values():
    print(value.title())
    #可使用set语句来避免从字典中提取出来的值重复。
print('\n')
favorite_languages = {
    'jane':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',#此处加逗号是为了在下一行添加键值对。
    }#注意使用多行来定义字典时的格式。
print('以下的这些语言被提及：')
for language in set(favorite_languages.values()):
    print(language)
