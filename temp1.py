print("Hello world")
print(2+4)
print(5-2)
print(3*4)
print(6/3)
print(7//3)
print(5 % 3)
print(22**10)

print("_"*5)
x = 5.0
thur = 8*x % 4
print("thur=", thur)
print("thur=%.2f" % thur)
print("thur={:.2f}".format(thur))
print(thur)
x, y, b = 2, 5, 8
func_2 = 2*x+7*y+b
print(func_2)

print("_"*50)
lst_1 = list(range(2, 70, 7))
print(lst_1)
print("the list length={}".format(len(lst_1)))
print("Maximum value={}".format(max(lst_1)))
print("Minimum value={}".format(min(lst_1)))

print("_"*50)
lst_2 = list(map(chr, range(90, 110)))
print(lst_2)
print("_"*50)
print("[3:6]->{}".format(lst_2[3:6]))
print("[-3:-1]->{}".format(lst_2[-3:-1]))
print("[-3:]->{}".format(lst_2[-3:]))
print("[:3]->{}".format(lst_2[:3]))
print("[:]->{}".format(lst_2[:]))
print("_"*50)
help(map)
print("_"*50)

print(lst_2)
print("_"*50)
print("[0:10:2]->{}".format(lst_2[0:10:2]))
print("[::3]->{}".format(lst_2[::3]))
print("[9:3:-2]->{}".format(lst_2[9:7:-2]))
print("[20:3:-2]->{}".format(lst_2[20:4:-2]))
print("[7::-2]->{}".format(lst_2[7::-2]))
print("[:3:-2]->{}".format(lst_2[:3:-2]))

print("_"*50)
print(lst_2)
print("_"*50)
lst_2[5] = "白羊"
print("lst_2[5]=白羊->{}".format(lst_2))
lst_3 = lst_2+["白羊"]*6
print("lst_2+[白羊]*6->{}".format(lst_3))
lst_3[9] = 2015
print("lst_3[13]=2015->{}".format(lst_3))
lst_3[-6:-3] = list(range(100, 104, 2))
print("lst_3[-6:-3]=list(range(100,104,2))->{}".format(lst_3))
lst_3[1:1] = [0, 0, 0, 12]
print("lst_none[1:1]=[0,0,0,12]->{}".format(lst_3))
del lst_3[-2:]
print("del lst_3[-2:]->{}".format(lst_3))

print("_"*50)
lst_s_2 = list(map(chr, range(100, 105)))
print(lst_s_2)
print("_"*50)
lst_s_2.append(96)
print("lst_s_2.append(99)->{}".format(lst_s_2))
lst_s_2.append(list(range(66, 80, 5)))
print("lst_s_2.append(list(range(50,80,5)))->{}".format(lst_s_2))
lst_spechars = ['*', ')', '*']
lst_s_2.extend(lst_spechars)
print("lst_s_2.extend(lst_spechars)->{}".format(lst_s_2))
print("lst_s_2.count('*')={}".format(lst_s_2.count('*')))
print("lst_s_2.index('e')={}".format(lst_s_2.index('e')))
lst_s_2.insert(2, [1000, 1400, 1500])
print("lst_s_2.insert(2,[1000,1200,1500])->{}".format(lst_s_2))
print("lst_s_2.pop(7)_popup->{}".format(lst_s_2.pop(7)))
print("lst_s_2.pop(7)_retention->{}".format(lst_s_2))
lst_s_2.remove('*')
print("lst_s_2.remove('*')_retention->{}".format(lst_s_2))
list_n_2 = [2, 56, 6, 85, 4, 7]
list_n_2.sort()
print("list_n_2.sort()->{}".format(list_n_2))

print("_"*50)
tuple_1=2,3,5,
print("tuple_1=2,3,5,->{}".format(tuple_1))
print("3*(20*3,)->{}".format(3*(34*3,)))
print("tuple((5,8,9))->{}".format(tuple((7,8,9))))
print("tuple([5,8,9])->{}".format(tuple([6,8,9])))

print("_"*50)
import random
items=[(0,[i for i in range(5)]),(1,[random.sample(list(range(100,200,2)),4)]),(2,'python')]
print("items->{}".format(items))
dic=dict(items)
print("dic=dict(items)->{}".format(dic))
print("dic[1]->{}".format(dic[1]))

print("_"*50)
print("len(dic)->{}".format(len(dic)))
dic[3]=(random.random(),random.uniform(200,400))
print("dic[3]=(random.random(),random.uniform(200,300))->{}".format(dic))
del dic[1]
print("del dic[1]->{}".format(dic))
print("3 in dic->{}".format(3 in dic))
print("5 in dic->{}".format(5 in dic))
print("dic.keys()->{}".format(dic.keys()))
print("dic.values()->{}".format(dic.values()))
print("dic.items()->{}".format(dic.items()))
print("_"*50)
print("list(dic.keys())->{}".format(list(dic.keys())))

print("_"*50)
for k,v in enumerate(dic.items()):
    print(k,v)

print("_"*50)
lst_A=list(range(6,70,3))
lst_B=list(range(200,350,35))
print("lst_A={},lst_B={}".format(lst_A,lst_B))
dic_2={0:lst_A,1:lst_B}
print("dic_2={}".format(dic_2))
print("_"*50)
dic_assignment=dic_2
print("dic_assignment={}".format(dic_assignment))
dic_2.clear()
print("dic_2.clear()->{}".format(dic_2))
print("dic_assignment={}".format(dic_assignment))
dic_2[5]=list(range(1,7,2))
print("dic_2[5]=list(range(1,9,2))->{}".format(dic_2))
dic_copy=dic_2.copy()
print("dic_copy=dic_2.copy()->{}".format(dic_copy))
dic_2[8]=[5,7]
print("dic_2[8]=[5,7]->{}".format(dic_2))
print("dic_copy={}".format(dic_copy))
dic_copy[5].remove(5)
print("dic_copy[5].remove(5)->{}".format(dic_copy))
dic_copy.setdefault(6,[77,99])
print("dic_copy.setdefault(6,[77,99])->{}".format(dic_copy))
dic_2.pop(5)
print("dic_2.pop(5)->{}".format(dic_2))
dic_update={8:[5,6,7,3,2],9:[3,2,33,55,66]}
print("dic_update={}".format(dic_update))
dic_2.update(dic_update)
print("dic_2.update(dic_update->{}".format(dic_2))
print("dic_2.get(9)->{}".format(dic_2.get(9)))
dic_2.popitem()
print("dic_2.popitem()->{}".format(dic_2))

dic_3={}.fromkeys([0,1,2,3,4,'A'])
print("dic_3={}"+".fromkeys([0,1,2,3,4,'A'])->{}".format(dic_3))

print("_"*50)
lst_s_3=list("Hello Python!")
print("lst_s_3=list(\"Hello Python!\")->{}".format(lst_s_3)) #"\" escape character
print("\"Hellow\"+\" Python!\"->{}".format("Hellow"+" Python!"))
print("\"+\".join(str(123456))->{}".format("+".join(str(123456))))
print("len(\"Hellow Python!\")->{}".format(len("Hellow Python!")))
coordinates="120.132007,30.300508,9.7"
print("coordinates.split(\",\")->{}".format(coordinates.split(",")))
print("eval(coordinates)->{}".format(eval(coordinates))) #通常用eval()方法将字符串，转换为对应数值形式；
print("\"Hello Python!\".lower()->{}".format("Hello Python!".lower()))
print("\"Hello Python!\".upper()->{}".format("Hello Python!".upper()))
print("\"Hello Python!\"[6:]->{}".format("Hello Python!"[6:]))
print("\"    Hello Python!    \".strip()->{}".format("    Hello Python!    ".strip()))
print("\"Hello Python!\".replace(\"Python\",\"Grasshopper\")->{}".format("Hello Python!".replace("Python","Grasshopper")))
hello_lst=list("Hello Python!")
hello_lst.sort()
print("hello_lst.sort()>{}".format(hello_lst))
print("\"Hello Python!\".find(\"Py\")->{}".format("Hello Python!".find("Py")))

print("_"*50)
format_str="Hello,%s and %s!"
values=("Python","Grasshopper")
new_str=format_str % values
print("new_str=format_str % values->{}".format(new_str))
format_str_2="Pi with three decimals:%.3f,and enter a value with percent sign:%.2f %%" #如果字符串里包含实际的%，则通过%%即两个百分号进行转义
from math import pi
new_str_2=format_str_2 % (pi,3.1415926535)
print("new_str_2=format_str_2 % (pi,3.1415926)->{}".format(new_str_2))


format_str_3="%10f,%10.2f,%.2f,%.5s,%.*s,%d,%x,%f"
new_str_3=format_str_3%(pi,pi,pi,"Hello Python!",5,"Hello Python!",52,52,pi)
print("{}".format(new_str_3))


from string import Template
s_template_1=Template("$x,glorious,$x!")
s_1=s_template_1.substitute(x="Python")
print("s_1=s_template_1.substitute(x=\"Python\")->{}".format(s_1))
s_template_2=Template("${x}thon is amazing!")
s_2=s_template_2.substitute(x="py")
print("s_2=s_template_2.substitute(x=\"py\")->{}".format(s_2))
s_template_3=Template("$x and $y are both amazing!")
substitute_dict=dict([('x','Python'),('y','Grasshopper')])
print("substitute_dict={}".format(substitute_dict))
s_3=s_template_3.substitute(substitute_dict)
print("s_3=s_template_3.substitute(substitute_dict)->{}".format(s_3))


import re
pattern_1='Python'
text="Hello Python!"
print("re.findall(pattern_1,text)->{}".format(re.findall(pattern_1,text)))
pattern_2='python'
print("re.findall(pattern_2,text)->{}".format(re.findall(pattern_2,text)))


print("re.findall('.ython','Hello Python!')->{}".format(re.findall('.ython','Hello Python!')))
print("re.findall('.ython','Hello gython!')->{}".format(re.findall('.ython','Hello gython!')))
print("re.findall('.ython','Hello gPython!')->{}".format(re.findall('.ython','Hello gPython!')))
print("re.findall('.ython','Hello Pthon!')->{}".format(re.findall('.ython','Hello Pthon!')))



print("re.findall(r'w?cadesign\.cn,w+\.cadesign\.cn','cadesign.cn,www.cadesign.cn')->{}".format(re.findall(r'w?cadesign\.cn,w+\.cadesign\.cn','cadesign.cn,www.cadesign.cn')))
print("re.findall(r'w{2}"+"\.cadesign\.cn','www.cadesign.cn')->{}".format(re.findall(r'w{2}\.cadesign\.cn','www.cadesign.cn')))
print("re.findall(r'w{1,3}"+"\.cadesign\.cn','www.cadesign.cn')->{}".format(re.findall(r'w{1,3}\.cadesign\.cn','www.cadesign.cn')))


print("re.findall('[Py]*thon!','Hello Python!')->{}".format(re.findall('[Py]*thon!','Hello Python!')))
print("re.findall('[Py]*thon!','Hello Pthon!')->{}".format(re.findall('[Py]*thon!','Hello Pthon!')))
print("re.findall('[Py]*thon!','Hello ython!')->{}".format(re.findall('[Py]*thon!','Hello ython!')))
print("re.findall('[Py]*thon!','Hello ython!')->{}".format(re.findall('[Py]*thon!','Hello thon!')))


print("re.findall('python|grasshopper','python')->{}".format(re.findall('python|grasshopper','python')))
print("re.findall('python|grasshopper','grasshopper')->{}".format(re.findall('python|grasshopper','grasshopper')))
print("re.findall('python|grasshopper','grasshopper and python')->{}".format(re.findall('python|grasshopper','grasshopper and python')))


print("re.findall('\d','number=10')->{}".format(re.findall('\d','number=10')))
print("re.findall('\D','number=10')->{}".format(re.findall('\D','number=10')))
print("re.findall('[^0-9]','number=10')->{}".format(re.findall('[^0-9]','number=10')))


print("re.findall('[a-z]','python')->{}".format(re.findall('[a-z]','python-3.0')))
print("re.search('[a-z]+','python')->{}".format(re.search('[a-z]+','python')))
if re.search('[a-z]+','python'):
    print("re.search('[a-z]+','python')->found it!")
print("re.split(',','Hello,,,,,,Python!')->{}".format(re.split(',','Hello,,,,,,Python!')))
print("re.sub('Python','Grasshopper','Hello Python!')->{}".format(re.sub('Python','Grasshopper','Hello Python!')))
pattern_compile=re.compile('Python')
print("pattern_compile.findall('Hello,,,,,,Python!')->{}".format(pattern_compile.findall('Hello,,,,,,Python!')))
if re.match('p','python'):
    print("re.match('p','python')->found it!")


print("\'python\'.find(\'python\')->{}".format('python'.find('python')))
print("\'python\'.find(\'thon\')->{}".format('python'.find('thon')))
print("\'python\'.find(\'a\')->{}".format('python'.find('a')))
print("\'p\' in \'python\'->{}".format('p' in 'python'))


print("\'Hello,,,,,,Python!\'.split(',')->{}".format( 'Hello,,,,,,Python!'.split(',')))
print("\'Hello Python!\'.replace(\'Python\',\'Grasshopper\')->{}".format( 'Hello Python!'.replace('Python','Grasshopper')))


match_1=re.match(r'www\.(.*)\..{3}','www.python.org')
print("match_1.gourp(1)->{}".format(match_1.group(1)))
print("match_1.start(1)->{}".format(match_1.start(1)))
print("match_1.end(1)->{}".format(match_1.end(1)))
print("match_1.span(1)->{}".format(match_1.span(1)))
match_2=re.match(r'www\.(.*)\.(.{3})','www.python.org')
print("match_2.group(1)->{}".format(match_2.group(1)))
print("match_2.group(2)->{}".format(match_2.group(2)))


lst=list(range(27,35,3))
print("lst={}".format(lst))
print("_"*50)
print("for i in lst:")
for i in lst:
    print(i)
print("for i in range(len(lst)):")
for i in range(len(lst)):
    print("idx={},val={}".format(i,lst[i]))
print("+"*50)
dic=dict(a=5,b=4,c=2,d=8)
print("dic={}".format(dic))
print("_"*50)
print("for k in dic:")
for k in dic:
    print(k)
print("for k,v in dic.items():")
for k,v in dic.items():
    print("key={},val={}".format(k,v))


x=1
while x<=100:
    print("x={}".format(x))
    x+=10;x*=2


x=1
while x<=100:
    print("x={}".format(x))
    x+=10
    if x>=50:break

import sys
print("sys.maxsize={}".format(sys.maxsize))
for i in range(sys.maxsize):
    print("i={}".format(i))
    i+=10
    if i>=30:break

topography_fp='./data/elevation.txt'
f=open(topography_fp,'r')
elevation_dat=[]
while True:
    line=f.readline()
    elevation_dat.append(line)
    if not line:break
f.close()
print("elevation_dat[:10]={}".format(elevation_dat[:10]))


import pandas as pd
elevation_df=pd.read_csv(topography_fp, delimiter = ",",header=None)
print(elevation_df)


lst_a=[0,1,2,4]
lst_b=['point_a','point_b','point_c','point_d']
zip_lst=zip(lst_a,lst_b)
print("zip_lst=zip(lst_a,lst_b)->{}".format(zip_lst))
print("dict(zip_lst)->{}".format(dict(zip_lst)))

zip_lst=zip(lst_a,lst_b)
for a,b in zip_lst:
    print(a,b)

zip_lst=zip(lst_a,lst_b)
a,b=zip(*zip_lst)
print("a={},b={}".format(a,b))


lst_a=[0,1,2,3]
lst_b=['point_a','point_b','point_c','point_d']
zip_lst=zip(lst_a,lst_b)
print("zip_lst=zip(lst_a,lst_b)->{}".format(zip_lst))
print("dict(zip_lst)->{}".format(dict(zip_lst)))

zip_lst=zip(lst_a,lst_b)
for a,b in zip_lst:
    print(a,b)

zip_lst=zip(lst_a,lst_b)
a,b=zip(*zip_lst)
print("a={},b={}".format(a,b))


print("[x*x for x in range(3,37,5) if x%2==0]->{}".format([x*x for x in range(5,45,6) if x%2==0]))
print("[(x,y) for x in range(3)for y in range(2)]->{}".format([(x,y) for x in range(3)for y in range(2)]))
print("[(x,y) for x,y in zip(range(3),range(2))]->{}".format([(x,y) for x,y in zip(range(3),range(2))]))
nested_list=[[a for a in range(1,10,3)],2,3,[b for b in range(60,100,7)],[[c for c in range(1100,2000,150)],3,9]]
print("[[a for a in range(1,10,3)],2,3,[b for b in range(60,100,7)],[[c for c in range(1000,2000,120)],3,9]]->{}".format(nested_list)) #嵌套列表推导式

flatten_lst = []

flatten_lst= lambda lst: [m for n_lst in lst for m in flatten_lst[n_lst]] if type(lst) is list else [lst] #展平列表常用，可以放置到单独的.py文件中调用。lambda函数后文阐述
print("flatten_lst(nested_list)->{}".format(flatten_lst(nested_list)))


x=10
if x<0:
    print('It is negative.')
elif x==0:
    print('Equal to zero.')
elif 0<x<10:
    print('Positive but smaller than 10')
else:
    print('Positive and larger than or equal to 10.')

x=y=[2,6,9]
z=[2,6,9]
print("x==y->{}".format(x==y))
print("x is y->{}".format(x is y))
print("x==z->{}".format(x==z))
print("x is z->{}".format(x is z))
print("x is not y->{}".format(x is not y))
print("x is not z->{}".format(x is not z))
print("id_x:{};id_y:{};id_z:{}".format(id(x),id(y),id(z))) #Memory Location

del x[2]
print("x={},y={},z={} after del x[2]".format(x,y,z))


x=[3,6,9]
print("3 in x->{}".format(3 in x))
print("0 in x->{}".format(0 in x))
print("3 not in x->{}".format(3 not in x))
print("0 not in x->{}".format(0 not in x))


a,b,c=0,10,16
if c>a and c<b:
    print('a<c<b')
else: print('a<c<b kidding!!!')


def simple_func(x,y):
    z=pow(x,2)+y
    return z
print("simple_func(3,7)->{}".format(simple_func(3,7)))
print("simple_func(7,3)->{}".format(simple_func(7,3)))
print("simple_func(y=7,x=3)->{}".format(simple_func(y=7,x=3)))


def fibonacci(s,count):
    fib_lst=[0,1]
    fib_part=[]
    if s==0 or s==1:
        fib_part[:]=fib_lst
        for i in range(count-2):
            fib_part.append(fib_part[-1]+fib_part[-2])
    else:
        while True:
            fib_lst[:]=[fib_lst[1],fib_lst[0]+fib_lst[1]]
            #print(fib_lst)
            if fib_lst[1]-s>=0:break
        fib_part[:]=fib_lst
        if abs(fib_lst[0]-s)>=abs(fib_lst[1]-s):
            for i in range(count-1):
                fib_part.append(fib_part[-1]+fib_part[-2])
            fib_part.pop(0)
        else:
            for i in range(count-2):
                fib_part.append(fib_part[-1]+fib_part[-2])
    return fib_part

print("fibonacci(6,9)->{}".format(fibonacci(6,9)))
print("fibonacci(7,9)->{}".format(fibonacci(7,9)))


def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(7))


class Bird:
    fly='Whirring' #美 /wɜːr/
    def __init__(self):
        self.hungry=True
    def eat(self):
        if self.hungry:
            print('Aaaah...')
            self.hungry=False
        else:
            print('No.Thanks!')

class Apodidae(Bird):  #/'æpədədi:/
    def __init__(self):
        super(Apodidae,self).__init__()
        self.sound='Squawk!' #美 /skwɔːk/
    def sing(self):
        print(self.sound)
swift=Apodidae()
print("swift.fly->{}".format(swift.fly))
print("swift.eat()->")
swift.eat()
print("swift.eat()->")
swift.eat()
print("swift.sing()->")
swift.sing()


blackswift=Apodidae()
scarceswift=Apodidae()
print("blackswift.sing()->")
blackswift.sing()
print("scarceswift.sing()->")
scarceswift.sing()


print("blackswift.fly->{}".format(blackswift.fly))
blackswift.fly='humming' #重新赋予实例的属性
print("blackswift.fly after redefining the blackswif's attribute->{}".format(blackswift.fly))
print("scarceswift.fly->{}".format(scarceswift.fly))


blackswift.sing()


help(Bird)


help(Apodidae)


class Fibs():
    def __init__(self):
        self.a=0
        self.b=1
    def __next__(self):  #实现迭代器的next方法
        self.a,self.b=self.b,self.a+self.b
        return self.a
    def __iter__(self): #实现迭代方法
        return self.__next__()


f=Fibs()
fa=[]
fb=[]
for i in range(9):
    fa.append(f.__next__())
print("fa={}".format(fa))
for i in range(5):
    fb.append(f.__next__())
print("fb={}".format(fb))


lst_d=list(range(3,20,2))
print("lst_d={}".format(lst_d))
print("_"*50)
lst_iter=iter(lst)
print("next(lst_iter)->{}".format(next(lst_iter)))
print("next(lst_iter)->{}".format(next(lst_iter)))
for i in lst_iter:
    print(i)
next(lst_iter)


lst_e=[list(range(3,21,3)),[3,8,67,list(range(5)),89]]
print("lst_e={}".format(lst_e))
print("_"*50)
flatten_lst=[]
for v_1 in lst_e:
    try:
        for v_2 in v_1:
            try:
                for v_3 in v_2:
                    flatten_lst.append(v_3)
            except TypeError:
                flatten_lst.append(v_2)
    except TypeError:
        flatten_lst.append(v_1)
print("flatten_lst={}".format(flatten_lst))


def flatten(lst):
    try:
        for n_lst in lst:
            for m in flatten(n_lst):
                yield m
    except TypeError:
        yield lst


print("list(flatten(lst_e))->{}".format(list(flatten(lst_e))))


flatten_lst=lambda lst:[m for n_lst in lst for m in flatten_lst[n_lst]] if type(lst) is list else [lst] #lambda 生成器方法


def infinite():
    n=0
    while True:
        yield 'num#'+str(n)
        n+=1


n=infinite()
print("next(n)->{}".format(next(n)))
print("next(n)->{}".format(next(n)))
print("next(n)->{}".format(next(n)))
print("[next(n) for i in range(5)]->{}".format([next(n) for i in range(5)]))


n=3
print("[[(2*pi*(2*(u/(n-1))-1),2*pi*(2*(v/(n-1))-1)) for u in range(n)] for v in range(n)]->{}".format([[(2*pi*(2*(u/(n-1))-1),2*pi*(2*(v/(n-1))-1)) for u in range(n)] for v in range(n)]))
print("_"*50)
print("([(2*pi*(2*(u/(n-1))-1),2*pi*(2*(v/(n-1))-1)) for u in range(n)] for v in range(n))->{}".format(([(2*pi*(2*(u/(n-1))-1),2*pi*(2*(v/(n-1))-1)) for u in range(n)] for v in range(n))))
gen=([(2*pi*(2*(u/(n-1))-1),2*pi*(2*(v/(n-1))-1)) for u in range(n)] for v in range(n))
print("next(gen)->{}".format(next(gen)))
print("next(gen)->{}".format(next(gen)))


def f_convert_a(x):
    try:
        return float(x)
    except:
        return x
print("f_convert_a('3.1415')->{}".format(f_convert_a('3.1415')))
print("f_convert_a('string')->{}".format(f_convert_a('string')))
print("f_convert_a(3,6,7)->{}".format(f_convert_a((3,6,7))))



def f_convert_b(x):
    try:
        return float(x)
    except ValueError:
        return x
print("f_convert_b('3.1415')->{}".format(f_convert_b('3.1415')))
print("f_convert_b('string')->{}".format(f_convert_b('string')))
print("f_convert_b(3,6,7)->{}".format(f_convert_b((3,6,7))))


def f_convert_c(x):
    try:
        return float(x)
    except ValueError:
        return x
    except TypeError:
        print(x,'TypeError')
print("f_convert_c('3.1415')->{}".format(f_convert_c('3.1415')))
print("f_convert_c('string')->{}".format(f_convert_c('string')))
print("f_convert_c(3,6,7)->{}".format(f_convert_c((3,6,7))))


def f_convert_d(x):
    try:
        return float(x)
    except (ValueError,TypeError):
        print(x,'ValueError or TypeError')
print("f_convert_d('3.1415')->{}".format(f_convert_d('3.1415')))
print("f_convert_d('string')->{}".format(f_convert_d('string')))
print("f_convert_d(3,6,7)->{}".format(f_convert_d((3,6,7))))


def f_convert_e(x):
    try:
        return float(x)
    except (ValueError,TypeError) as e:
        return print(x,e)
print("f_convert_e('3.1415')->{}".format(f_convert_e('3.1415')))
print("f_convert_e('string')->{}".format(f_convert_e('string')))
print("f_convert_e(3,6,7)->{}".format(f_convert_e((3,6,7))))


def f_convert_f(x):
    try:
        return float(x)
    except (ValueError,TypeError) as e:
        pass
print("f_convert_f('3.1415')->{}".format(f_convert_f('3.1415')))
print("f_convert_f('string')->{}".format(f_convert_f('string')))
print("f_convert_f(3,6,7)->{}".format(f_convert_f((3,6,7))))


def f_open_a(fp):
    try:
        f=open(fp,'r')
    except IOError as e:
        print('Unable to open',fp,':%s\n' %e)
    else:
        data=f.read()
        f.close
        return data
tryException_content=f_open_a("./data/tryException.txt")
print("tryException_content->{}".format(tryException_content))
f_open_a("./data/tryException_.txt")


def f_open_b(fp):
    try:
        f=open(fp,'r')
    except IOError as e:
        print('Unable to open',fp,':%s\n' %e)
    else:
        data=f.read()
        f.close()
        return data
    finally:
        print('done!')
f_open_b("./data/tryException.txt")


x=20
assert x>0
assert x<0