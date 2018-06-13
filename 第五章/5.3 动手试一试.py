#5-3 外星人的颜色
alien_color='green'
if alien_color is 'green':
    print('Congratulations,You get 5 points areadly.')
alien_color='red'
if alien_color is 'green':
    print('Congratulations,You get 5 points areadly.')#未通过测试没有输出。
#5-4 外星人的颜色
alien_color='red'
if alien_color is 'green':
    print('Congratulations,You get 5 points areadly because you shot aliens.')
else:
    print('Congratulations,You get 10 points areadly.')#执行else.
alien_color='green'
if alien_color is 'green':
    print('Congratulations,You get 5 points areadly because you shot aliens.')
else:
    print('Congratulations,You get 10 points areadly.')#执行if.
    #另一种表述,同时用到了测试多个条件的if语句。
alien_color='red'
if alien_color == 'green':
    print('Congratulations,You get 5 points areadly because you shot aliens.')
if alien_color != 'green':
    print('Congratulations,You get 10 points areadly.')
#5-5 外星人的颜色
alien_color='green'
if alien_color is 'green':#为绿色。
    print('\nCongratulations,You get 5 points areadly .')
elif alien_color == 'yellow':
    print('\nCongratulations,You get 10 points areadly.')
else:
    print('\nCongratulations,You get 145 points areadly.')
alien_color='yellow' #为黄色。
if alien_color is 'green':
    print('\nCongratulations,You get 5 points areadly .')
elif alien_color == 'yellow':
    print('\nCongratulations,You get 10 points areadly.')
else:
    print('\nCongratulations,You get 145 points areadly.')
alien_color='green'
if alien_color is 'red':#为红色
    print('\nCongratulations,You get 5 points areadly .')
elif alien_color == 'yellow':
    print('\nCongratulations,You get 10 points areadly.')
else:
    print('\nCongratulations,You get 15 points areadly.')
#5-6 人生的不同阶段
age=65
if age < 2:
    print('He is a baby')
elif age < 4:
    print('He is taking a toldder.')
elif age < 13:
    print('He is a child.')
elif age < 20:
    print('He is a adolescent.')
elif age < 65:
    print('He is a an adult.')
else:
    print('\nHe is a the aged.')
#5-7 喜欢的水果
favorite_fruits=['bananas','apple','pear']
if 'bananas' in favorite_fruits:
    print('\nyou really like bananas!')
if 'apple' in favorite_fruits:
    print('\nYou really like apple!')
if 'grape' in favorite_fruits:
    print('\nYou really like grape!')
if 'pear' in favorite_fruits:
    print('\nYou really like prea!')
if 'mango' in favorite_fruits:
    print('\nYou really like mango!')
