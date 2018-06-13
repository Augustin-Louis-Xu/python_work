#5-8-9 以特殊的方式和管理员打招呼。
names=['Daming','David','Augustin','Admin','Obama']
if names: #添加if语句，检查用户列表是否为空，可尝试删除列表中的人名，则输出为“我们需要寻找用户！”
    for name in names:
        if name != 'Admin':
            print('Hello '+name+',thank you for logging in again.')
        else:
             print('Hello Admin,would you like to see a status report.')
else:
    print('We need to fand some users!')
#5-10 检查用户名
current_names=['Daming','David','Augustin','Admin','Obama']
new_users=['Daming','David','Mary','Jack','Anthony']
    #转换为小写。
lower_current_names=[item.lower() for item in current_names]
lower_new_users=[item.lower() for item in new_users]
    #检查名字是否重复，此时已经不区分大小写了。
print('\n')
for new_user in lower_new_users:
    if new_user in lower_current_names:
        print('You should logging in other names!')
    else:
        print('congratulations! '+new_user+' not be use for others!')
#5-11 序数
print('\n')
numbers=list(range(1,10))#在列表中存储数字
for number in numbers:
    if number == 1:
        print(str(number)+'st')
    elif number == 2:
        print(str(number)+'nd')
    elif number == 3:
        print(str(number)+'rd')
    else:
            print(str(number)+'th')
    #另一种方法在列表中存储数字
print('\n')
numbers=[]
for number in range(1,10):
    numbers.append(number)
print(numbers)    

     
