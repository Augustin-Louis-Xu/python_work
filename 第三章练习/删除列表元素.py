#删除后不可用
motorcycles=['one','two','threee']#python中的列表用中括号来表示，并且用逗号隔开每个元素。
del motorcycles[0]
print(motorcycles)

#删除后可以继续使用已经删除的元素..pop()用来弹出寨顶云元素，相当于删除列表的末尾元素。
motorcycles=['one','two','three']
motorcycles_poped=motorcycles.pop()#将弹出的值村存储到变量中
print('\n'+motorcycles_poped)#核实将弹出的元素赋值到新变量中
print(motorcycles)#核实删除的末尾元素

#应用：编程打出最新购买的摩托车，假设列表中的摩托车元素是按照先后顺序购买的
motorcycles=['one','two','three','four','end']
print('\n'+motorcycles[2])
print(motorcycles)
last_owned=motorcycles.pop()
print('The last motorcycle I owend was '+last_owned.title()+'.'+'\n')

#pop默认弹出末尾，想要弹出其他列表元素只需要指定元素位置即可
motorcycles=['one','two','three','four','end']
delete=motorcycles.pop(2)
print(delete)
print(motorcycles)
print("\n")

#加入不知道元素位于列表的位置，可与根据值来删除，此外：remove语句也可以继续使用移除元素的值
motorcycles=['one','two','three','four','end']
print(motorcycles)
motorcycles.remove('three')#此处让python知道目标元素位于列表什么位置，并且删除该元素
print(motorcycles)
print('\n')

#应用：remove为据值删除，使用remove语句删除”one“摩托车，说出放弃购买此种摩托车的原因
motorcycles=['one','two','three','four','end']
s='one'
motorcycles.remove(s)
print(motorcycles)
print('One reson I give up was that '+s.title()+' is too expensive .')



