#嘉宾名单
list=['Alice','Bob','Linda']
print("I want to request "+list[0]+','+list[1]+',and '+list[2]+' to go dinner\n')
#参考答案
names=['Alice','Bob','Linda']
for name in names:
    print('Invite '+name+' to dinner')
#修改嘉宾名单
print('\n')
names=['Alice','Bob','Linda']
for name in names:
    print('Invite '+name+' to dinner')
print(list[1].title()+" can't come to here,sorry ,so I invite my good friends-Tom to go this dinner.\n")
names=['Alice','Tom','Linda']
for name in names:
    print('Invite '+name+' to dinner.')
#添加嘉宾
print('\n')
names=['Alice','Tom','Linda']
for name in names:
    print('Invite '+name+' to dinner.')
print('I find a bigger table,so I request more people to dinner')#注意此处for语句的开头行间距，如果没有左对齐，会产生一系列的不同输出结果
names.insert(0,'Da ming')#插入人名，insert可以在列表中任意指定位置添加，只需要索引
names.insert(2,'Mary')
names.append('louis')#append语句默认在列表的末尾位置插入元素
print(names)
for people in names:
	print("Invite "+people+' to dinner')
#缩减名单
print('\n')
names=['Alice','Tom','Linda']
names.insert(0,'Da ming')#插入人名，insert可以在列表中任意指定位置添加，只需要索引
names.insert(2,'Mary')
names.append('louis')
for people in names:
	print("Invite "+people+' to dinner')
print("For the reason that the dinner I bought can't timely deliever, so I only can invite two people to dinner.")
name=names.pop()#暂定删除，以下为删除过程。
print('Sorry, My dear '+name.title()+",For the reason that the dinner I bought can't timely deliever, so I can't invite you to this dinner.")
name=names.pop()
print('Sorry, My dear '+name.title()+",For the reason that the dinner I bought can't timely deliever, so I can't invite you to this dinner.")
name=names.pop()
print('Sorry, My dear '+name.title()+",For the reason that the dinner I bought can't timely deliever, so I can't invite you to this dinner.")
name=names.pop()
print('Sorry, My dear '+name.title()+",For the reason that the dinner I bought can't timely deliever, so I can't invite you to this dinner.")
for name in names:
    print('Invite '+name+' to dinner.')
del names[0]#删除最后两位
del names[0]#删除最后两位
print(names)
print('I invite '+str(len(names))+' to have dinner ,'+'There are :'+str(names)+', Heihei, I eat with myself.')
