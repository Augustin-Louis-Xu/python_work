# 永久改变列表中元素的排列顺序，使其按照字母顺序排序
cars=['bmw','audi','toyota','subaru']
cars.sort()
print(cars)
# 反方向排序
cars.sort(reverse=True)
print(cars)
print('\n')
#使用sorted进行临时排序,同时不影响原来元素的排列位置
cars=['bmw','toyota','subaru','audi']
print('This is the original cars list:')
print(cars)
print('\nHere is the sorted list:')
print(sorted(cars))#可理解为向sorted传递cars
print('\nHere is the original list again:')
print(cars)#最后输出了原始的排列顺序
print(sorted(cars,reverse=True))#向sorted()递reverse=True
#倒着打印列表
print('\n')
cars=['bmw','audi','toyota','subaru']#反转列表元素的排序位置
cars.reverse()
print(cars)
cars.reverse()#虽然reverse为永久改变排序位置，但是再次调用即可恢复
print(cars)
print('\n')
#确定列表长度，也就是元素的个数
cars=['bmw','audi','toyota','subaru']
print(len(cars))

