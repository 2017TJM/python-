#list记录两条数据
#list中数据分别是人名，年龄，月薪，工作领域
bob=['Bob Smith',42,30000,'software']
sue =['Sue Jones',45,40000,'hardware']
print("bob={0}\n,sue={1}\n".format(bob,sue))

#通过指定位置索引进行访问
#访问list对象中的第一个元素（人名）
print(bob[0])
print(sue[0])


#通过空格来分割姓名字段，然后获取最后部分
#可以通过改变月薪在列表中的相应字段来给某人加薪
print(bob[0].split()[-1])#Bob的姓什么
sue[2]*=1.25#给sue加薪25%
print(sue)

#数据库列表
#前面代码只是创建了两个变量，不是一个数据库，为了将前面数据存储在一起，将他们放入一个列表中
#可以再定义一个列表存储他们
people =[bob,sue]
#直接打印输出
print(people)

for person in people:
    #for循环打印输出
    print(person)

#现在people就是我们的数据库
#可以通过相对位置来获取特定记录
#或者通过循环一次处理一条记录

print(people[1][0])

for person in people:
    print(person[0].split()[-1])#姓
   #print(person[2])
    person[2]*=1.20   #涨20%薪水

#检查薪水
for person in people:print(person[2])
#收集薪水用list和for
pays =[person[2] for person in people]

print(pays)

#收集薪水用map lambda

pays =map(lambda x: x[2],people)
print(list(pays))

#生成器表达式,sum为内建表达式
print(sum(person[2]for person in people))


#向数据库中添加记录，用append,extend
people.append(['Tom',50,0,None])
print(people)
print(len(people))
print(people[-1][0])


#用range函数将字段名和其对应位置关联
NAME,AGE,PAY =range(3)#0,1,2
bob =['Bob Smith',42,10000]
print(bob[NAME])
a=PAY,bob[PAY]
print(a)

#元组列表
bob=[['name','Bob Smith'],['age',42],['pay',10000]]
sue=[['name','Sue Jones'],['age',45],['pay',20000]]

people=[bob,sue]
print(people)
for person in people:
    print(person[0][1],person[2][1])


#收集姓名
print([person[0][1] for person in people])

for person in people:
    print(person[0][1].split()[-1])
    person[2][1]*=1.10 #增加10%薪水
    print(person[2])


#拆开元组中名/值对
for person in people:
    for(name,value) in person:
        if name=='name':  #寻找特定字段
            print(value)

#或者其他方法，通过自己写一个函数
def field(record,label):
    for(fname,fvalue)in record:
        if fname==label: #根据名字寻找字段
            return fvalue

print(field(bob,'name'))#打印姓名
print(field(bob,'pay'))#打印所有薪水
print(field(sue,'pay'))#打印姓名
print("----------------------------")
for rec in people:
    print(field(rec,'name'))#打印所有姓名
    print(field(rec, 'age'))  # 打印所有年龄
    print(field(rec, 'pay'))  # 打印薪资


