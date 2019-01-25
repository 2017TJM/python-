#列表的方式需要查找名字段,字典就可以避免这个缺点
bob ={'name':'Bob Smith','age':42,'pay':30000,'job':'dev'}
sue ={'name':'Sue Jones','age':45,'pay':40000,'job':'hdw'}

name_pay =bob['name'],sue['pay']
print(name_pay)

print(bob['name'].split()[-1])
sue['pay']*=1.10
print(sue['pay'])


#其他建立字典的方法
bob =dict(name='Bob Smith',age=42,pay=30000,job='dev')
sue=dict(name='Sue Jones',age=45,pay=40000,job='hdw')
print(bob,sue)


#一次一个字段的填写



sue ={}
sue['name']='Sue Jones'
sue['age']=42
sue['pay']=40000
sue['job']='hdw'
print(sue)

#用zip函数将名/值列表链在一起
names=['name','age','pay','job']
values=['Sue Jones',45,40000,'hdw']
print(dict(list(zip(names,values))))


#通过键序列和所有键的可选初值创建字典（便于初始化空字典）

fields=('name','age','job','pay')

record =dict.fromkeys(fields,'?')
print(record)

people =[bob,sue] #应用列表

print(people)

for person in people:
    print(person['name'],person['pay'],sep=',')#所有名字和薪水


for person in people:
    if person['name']=='Bob Smith':   #获取特定人的薪水
        print(person['pay'])

#收集姓名
names = [person['name'] for  person in people]
print(names)
#同上生成式，map,lambda (收集姓名)
print(list(map((lambda x:x['name']),people)))

#汇总薪水
print(sum(person['pay'] for person in people))

print(sum(list(map((lambda x:x['pay']),people))))

#类似SQL的查询
a_name=[rec['name'] for rec in people if rec['age']==42]
print(a_name)

a_age=[(rec['age']**2 if rec['age']>=44 else rec['age']) for rec in people]
print(a_age)

G=(rec['name'] for rec in people if rec['age']>=42)
print(next(G))

G=((rec['age']**2  if rec['age']>=44 else rec['age'])for rec in people)
#print(next(G))
print(G.__next__())


for person in people:
    print(person['name'].split()[-1])
    person['pay']*=1.10
    print(person['pay'])



#嵌套结构
#通过把字典，列表，元组嵌套在另一个字典中，呈现出一种更为结构化的记录
bob2={'name':{'first':'Bob','last':'Smith'},
      'age':42,
       'job':['software','writing'],
       'pay':(40000,50000)}

#由于这条记录包含嵌套结构，索引两次就可以访问到两层深的数据
print(bob2['name'])#bob全名
print(bob2['name']['last'])#bob姓氏
print(bob2['pay'][1])

#使用通常的对象操作来获取或者改变嵌套的数据

for job in bob2['job']:#bob的所有工作
    print(job)
print(bob2['job'][-1])#bob的最近的工作

bob2['job'].append('janitor')
print(bob2)

#字典的字典

bob = dict(name='Bob Smith',age=42,pay=30000,job='dev')
sue =dict(name='Sue Jones',age=45,pay=40000,job='hdw')

print(bob)

db={}
db['bob']=bob #引用字典的字典
db['sue']=sue
print(db)
print(db['bob']['name']) #获取bob 的名字
db['sue']['pay']=50000   #改变sue的薪水
print(db['sue']['pay'])
print(db['sue'])
print(db)

import pprint
pprint.pprint(db)


#逐条记录地访问数据库，可以使用字典的迭代器
for key in  db:
    print(key,'=>',db[key]['name'])


for key in  db:
    print(key,'=>',db[key]['pay'])


#访问所有的对象，使用键索引
for key in db:
    print(db[key]['name'].split()[-1])
    db[key]['pay']*=1.10
    print(db[key]['pay'])


#直接访问
for record in db.values():
    print(record['name'])

x=[db[key]['name']for  key in  db]
print(x)

x= [rec['name'] for rec in db.values()]
print(x)

#新增加数据

db['tom']=dict(name='Tom',age=50,job=None,pay=0)
print(db)

print(list(db.keys()))
print(len(db))
print([rec['age'] for rec in db.values()])
print([rec['name'] for rec in db.values() if  rec['age']>=45])

