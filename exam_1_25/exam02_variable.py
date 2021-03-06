# -*- coding: utf-8 -*-
"""exam02_variable.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Jrv9IQ-kJglD96iaaMwZCEd_HWF0h7ij

#변수

##숫자형

python에서의 변수 활용
"""

a = 10
b = 20
c = 'A'
PI = 3.1415

print(a)
print(type(a))
print(type(c))
print(type(PI))

"""####사칙연산"""

sum = a + b
print(sum)

sub = a - b
print(sub)

print(a * b)
div = a / b
print(div)

print(type(div))

"""몫 연산자"""

print(a // b)

"""나머지 연산자"""

print(a % b)

"""거듭제곱 연산자"""

print(3 ** 3)

"""##List"""

a = []
b = [1, 2, 3]
c = ['Life', 'is', "too", 'short']
d = [1, 2, 'Life', "is"]
e = [1, 2, ['life', 5]]

f = e[2][0:2]
print(f)

print(b[2])
print(d[2])
print(e[2][1])

print(b[-1])

a = [1,2,3,4,5]
b = a[0:3]
print(b)

b = a[:3]
print(b)

b = a[2:5]
print(b)

c = a[2:]
print(c)
d = a [2:4]
print(d)

a = [1,2,3]
b = [4,5,6]
c = a + b
print(c)   #c를 출력
""" 
여러줄 주석
"""

print(a[0] + b[0])

c = []
c.append(a[0] + b[0])
c.append(a[1] + b[1])
c.append(a[2] + b[2])
print(c)

print(a)
d = a * 3
print(d)
print(len(d))

print(a)
a[1] = 10
print(a)

print(a)
del a[1]
print(a)

print(a)
a.append(10)
print(a)

print(a)
a.append(2)
print(a)
a.sort()
print(a)

a.reverse()
print(a)

print(a.index(3))

a.insert(1,5)
print(a)

a.remove(3)
print(a)

print(a)
b = a.pop()
print(a)
print(b)

b = a.pop(1)
print(a)
print(b)

a = [1,2,3,4,5,1,2,1,1]
print(a.count(1))

print(a)
a.extend([10,11])
print(a)

a = a + [12, 13]
print(a)

a += [14, 15]
print(a)

number = 1
number += 1 # number = number + 1
print(number)

"""##String"""

hello = "Hello"
print(hello)

a = ['H', 'e', 'l', 'l', 'o']
print(a)

print(hello[2])
print(a[2])

print(type(a))
print(type(hello))

str_a = hello[:4]
print(str_a)

str_b = hello[1:]
print(str_b)

str_c = 'world'
print(str_c)

str_d = "'Python is very easy'"
print(str_d)

food = "Python's favorite food is perl"
print(food)

food = "Python's favorite food is perl"
print(food)

food = 'Python\'s favorite food is perl'
print(food)

head = "Pyhton"
tail = "is fun"
str_head_tail = head + ' ' + tail
print(str_head_tail)
print(head,tail)

a = "hobby"
print(a.count('b'))

a = 'Python is the best choice'
print(a.find('o'))

print(",".join('abcd'))

s = ' hi '
print(s.lstrip() + 'there')
print(s.rstrip() + 'there')
print(s.strip() + 'there')
print(s)

a = 'Life is too short'
b = a.replace("Life", "Your leg")
print(a)
print(b)

str_list = a.split()
print(str_list)
print(type(str_list))

str_list = a.split('i')
print(str_list)
print(type(str_list))

b = "영희,90,100,80"
str_list = b.split(',')
print(str_list)
sum = int(str_list[1]) + int(str_list[2]) + int(str_list[3])
print(sum)

"""##Tuple"""

t1 = ()
t2 = (1,)
t3 = (1,2,3)

print(t2 + t3)

t2 = t2 + t3
print(t2)

# t3[1] = 10

"""##Dictionary"""

dic = {'name':'pey', 'phone':'0119993323',
       'birth':'1118'}

list_a = ['pey', '0119993323', '1118']

print(list_a[0])
print(dic['name'])

dic['phone'] = '01029993323'
print(dic)

dic['id'] = 'peypey'
print(dic)

dic[1] = '0192222222'
print(dic)

del dic[1]
print(dic)

dic = {3:[1,2,3]}
print(dic[3])
# dic = {[1,2,3]:3}

job = {'김연아':'피겨스케이팅', '류현진':'야구',
       '손흥민':'축구','귀도':'파이썬'}
print(job)

print(job['류현진'])

print(job.keys())

print(job['귀도'])

print(job.values())

print(job.items())

print(job['손흥민'])
print(job.get('손흥민'))

print('박지성' in job)

print('류현진' in job)
print('축구' in job)

print('축구' in job.keys())

print(job)

print(type(job))

"""##Set"""

s = set([1,2,3,3])
print(type(s))
print(s)

s1 = set([1,2,3,4,5,6,7,8])
s2 = set([5,6,7,8,9,10,11,12])

intersection = s1 & s2
print(intersection)

#s1[1]

print(s1.intersection(s2))

union = s1 | s2
print(union)

print(s1.union(s2))

difference = s1 - s2
print(difference)
print(s1.difference(s2))

difference = s2 - s1
print(difference)
print(s2.difference(s1))

list_a = [1,2,3,1,2,5,6,7,3,4,5]
list_unique = list(set(list_a))
print(list_unique)

s1 = set([1,2,3,4,5,6,7,8])
print(s1)
s1.add(9)
print(s1)

s1.update([13,14])
print(s1)

s1.remove(4)
print(s1)

"""논리연산자"""

print(type(True))
print(True and False)
print(True or False)
print(True & False)
print(True | False)
print(not True)
print(2 | 5)
print(2 or 5)
print(0 or 5)
print(0 and 5)

a = 10
print(a >= 0)

a = -10
if a > 0 or a == 0:
    a = a
else :
    a = -a 
print(a)

"""##비교 연산자"""

a = 10
b = 10
c = 20
print(a == b)
print(a == c)
print(a < b)
print(a > b)
print(a <= b)  
print(a >= b)
#print(a => b)
print(a != b)

"""##대입연산자"""

a = 10
a = a + 1
print(a)

a += 1
print(a)

a -= 1
print(a)

a *= 2
print(a)

a //= 2
print(a)

"""#이해 안되도 됨"""

a = [1,2,3]
print(a)
print(id(a))

b = a
print(b)
print(id(b))

print(a == b)
print(a is b)

b[1] = 4
print(a)

b = a[:]
b[1] = 2
print(a)
print(b)

print(a == b)
print(a is b)

print(id(a))
print(id(b))

a, b, c = 10, 20, 30
print(a)
print(b)
print(c)

a = b = 'python'
print(a)
print(b)
print(a is b)

a = 10
b = 20

c = a
a = b
b = c
print(a)
print(b)

a, b = b, a
print(a)
print(b)