#使用for循环打印数字1~20。
for value in range(1,21):
    print(value)
#用for循环将创建列表的包含的1~100000打印出来，如果输出时间过长，就按ctrl+c终止。
for value in range(1,1001):
	print(value)
value=[value for value in range(1,1001)]
print(value)
#计算1~1000000的和。
list=range(1,100001)
print(sum(list))
#通过指定第三个参数来打印出1~20的奇数。
values=[value for value in range(1,21,2)]
for value in  values:
    print(value)
print('\n')
   #另一种方法
for value in range(1,21,2):
     print(value)
print('\n')
#创建一个列表包含3~30中能被3整除的数字，再用for循环打印出来。
list=[value for value in range(3,31,3)]
for value in list:
	print(value)
   #另一中方法
list=[]
for value in range(1,11):
    values=value*3
    list.append(values)
print(list)
#创建一个列表，将1~10的立方打印出来。
list=[]
for value in range(1,11):
	lists=value**3
	list.append(lists)
	print(list)
#使用列表解析生成一个列表，其中包含前十个整数的立方。
print('\n')
list=[value**3 for value in range(1,11)]
print(list)
