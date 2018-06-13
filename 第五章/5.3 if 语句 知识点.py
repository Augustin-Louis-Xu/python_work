#if-else语句
age=19
if age >= 18:
    print('You are old enough to vote!')
    print('Have you registered to vote yet?')
else:
    print('Sorry,you are too young to vote.')
    print('please registered to vote as soon as you turn 18!')
#if-elif-else语句 游乐场收费规则，四岁以下免费，4-18岁收费5美元，18岁以上收费10美元。
age=12
if age < 4:
    print('\nYou admission cost is $0.')
elif age < 18:
    print('\nYou admission cost is #5.')
else:
    print('\nYou admission cost is $10.')
    #一种更加简便的语句。
age=12
if age < 4:
    price=0
elif age < 18:
    price=4
else:
    price=8
print('\nYou admission cost is $'+str(price)+'.')
#使用多个elif语句
age=75
if age < 4:
    price=0
elif age < 18:
    price=4
elif age < 65:
    price=10
else:
    price=5#此添加的elif代码块实现了65岁以上老人的半价门票。
print('\nYou admission cost is $'+str(price)+'.')
#省略else代码块，python并不要求所有的if-elif结构后面必须有else代码块。
age=75
if age < 4:
    price=0
elif age < 18:
    price=4
elif age < 65:
    price=10
elif age >= 65:
    price=5#此添加的elif代码块实现了65岁以上老人的半价门票。
print('\nYou admission cost is $'+str(price)+'.')
#测试多个条件，不管前一个条件测试结果如何都将进行下一个条件的测试。但是以上语句只能测试一个条件。
requested_toppings=['mushrooms','extra chess']
if 'mushrooms' in requested_toppings:
    print('\nAdding mushrooms')
if 'pepperoni' in requested_toppings:
    print('Adding peperomi.')
if 'extra chess' in requested_toppings:
    print('Adding extra chess.')
print('\nFinished making your pizza.')
