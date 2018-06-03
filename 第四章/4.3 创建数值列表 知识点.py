#函数range()
for value in range(1,5):
    print(value) #此处输出的确是1到4，没有打印5，原因在这里：python在我们指定的第一个值开始，在指定的第二个值后就停止了，所以我们看不到5.
print('\n')
for value in range(1,6):
    print(value)    #显然，这里输出的就是1到5了。
#使用list()创建数字列表
print("\t")
numbers=list(range(1,6))
print(numbers)
#以下示例中，函数range从2开始不断的加2，直至达到或超过11。
print('\n')
number=list(range(2,11,2))
print(number)
number=list(range(22222,11,-52))
print(number)
#使用函数range()几乎能创造任何需要的数字集合。
print('\n')
squares=[]
for value in range(1,11):
    square=value**2
    squares.append(square)#将遍历的每个数的平方值附加到列表的末尾，然后输出。
print(squares)
    #更高效的一种方法，立即赋值,但需要说明的是，使用临时变量更加易读，但在其他情况下却让代码变长。
squares=[]
for value in range(1,11):
	squares.append(value**2)
print(squares)
#对数字列表执行简单的统计计算
digits=[0,1,2,3,4,5,6,7,8,9,0]
print(min(digits))
print(max(digits))
print(sum(digits))
digits=list(range(1,101))
print(sum(digits))
#列表解析，创建列表解析将for循环和创建新元素的代码合并成一行，让所需生成列表squares的行数大大减少。
squares=[value**2 for value in range(1,11)]#注意，此时for语句后并没有冒号。
print(squares)
