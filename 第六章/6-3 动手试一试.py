#6-4 词汇表
vocabulary = {
    'print':'打印出指定的内容\n',       
    '=':'等号右边的值赋给等号左边的变量\n',
    '==':'一种表示两个变量相等的逻辑表达式\n',
    'pop()':'删除列汇中某个元素，需要在括号中加入删除元素在列表中的位置数字\n',
    'sort()':'永久性的按照字母为列表中的元素排序\n',
    'sorted()':'短暂的进行排序',
    'set()':'提取列表中的不同元素，过滤重复元素',
    }
for key in vocabulary.keys():
    print(key + ":\n\t" + vocabulary[key])
#6-5 河流
River = {'Nile':'Egypt',
    'Amazon':'Brazil',
    'Yangtze River':'China',
    }
for river in River.keys():
    print('The ' + river + ' runs through ' + River[river] +'.')
for river in River.keys():
    print(river)
for river in River.keys():
    print(River[river])
#6-6 调查
favorite_languages = {
    'jane':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',#此处加逗号是为了在下一行添加键值对。
    }#注意使用多行来定义字典时的格式。
List_of_users = ['jane','sarah','edward','phil','Louis']
for name in List_of_users:#注意变量名的命名规则。
    if  name in favorite_languages.keys():
        print(name.title() + ', Thanks for you take in this check !')
    else:
        print(name.title() + ', Please take in this checking ,Thank you!')
    
        
