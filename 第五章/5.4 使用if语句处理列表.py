#检查特殊元素
requested_toppings=['mushrooms','green peppers','extra cheese']
for requested_topping in requested_toppings:
    if requested_topping=='green peppers':
        print('sorry,we are out of green peppers right now.')
    else:
        print('Adding '+str(requested_topping)+'.')
print('\nFinished making your pizza.')
#确定列表不是空的。
requested_toppings=[]
if requested_toppings:#此处检查的列表若为空，则会返回False，执行else语句，否则将执行for循环。
    for requested_topping in requested_toppings:
        print('Adding '+requested_topping+'.')
        print('\nFinished making you pizza.')
    else:
        print('Are you sure your want a plain pizza.')
#使用多个列表
print('\n')
available_toppings=('mushrooms','olives','peperoni','extra chees')#如果配料是固定的，也可以用元组来存储。
requested_toppings=['mushrooms','french fries','extra chees']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print('Adding '+requested_topping+'.')
    else:
        print("Sorry,we don't have "+requested_topping+'.')
