#列表适用于程序运行期间可能变化的数据，但元组是用来存储不可变的值，不可变的列表称为元组。
dimensions=('200','50')#此处表明这个矩形的长宽是固定数值，不能修改，注意区别于列表的是用括号来标时。若接上dimensions[0]=250，将会抱错。
print(dimensions[0])
print(dimensions[1])
#遍历元组中的所有值。
dimensions=(200,50)
for dimension in dimensions:
	print(dimension)
#虽然不能修改元组的值，但却可以给存储元组的变量重新赋值。
dimensions=(200,50)
print('\nOriginal dimensions:')
for dimension in dimensions:
	print(dimension)
dimensions=(300,200)
print('\nModifield dimensions:')
for dimension in dimensions:
	print(dimension)
