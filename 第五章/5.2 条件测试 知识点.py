#一个简单列子
cars=['audi','bmw','subaru','toyota']
for car in cars:
    if car == 'bmw':#此处为检查变量的值与特定值是否相等
        print(car.upper())
    else:
        print(car.title()) 
    #car='Audi',car.lower() == 'audi',此处将返回True,函数Lower()不会改变存储在变量car中的值，因此在比较时不会影响原来的变量。

requested_topping='mushrooms'
if requested_topping!='anchovies':
    print('\nHold the anchovies')
answer=17
if answer != 42:#在这里输入的答案是17，不是42.
    print('\nThat is not the correct answer,please try again!')
#检查多个条件，可使用and或者or将测试条件合二为一。
    #age_0=21,age_1=18,age_0>=21 and age_1>=21,此处将返回Flase.
    #age_0=21,age_1=18,age_0>=21 or  age_1>=21,此处将返回Ture ,使用or检查条件只需要一个条件满足即可.
#检查特定值是否包含在列表中。requested_topping=['mushrooms','onions','pineapple'],'mushrooms' in requested_toppings 此处返回True.
#检查特定值是否不包含在列表中。
banned_users=['andrew','caroline','david']
user='marie'
if user not in banned_users:
    print('\n'+user.title()+',you can post a response if you wish.')
#布尔表达式 它是条件表达式的一种别名，返回的结果为True或者False,是一种高效的方式。

