#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Function Arguments
# 2015-07-21 14:12:18

def power(x):
	return x * x

print power(5), power(15)

def power(x, n):
	sum = 1
	while n > 0:
		n = n - 1
		sum = sum * x
	return sum

print power(5, 2), power(5, 5)

# Default Arguments
def power(x, n = 2):
	sum = 1
	while n > 0:
		n = n - 1
		sum = sum * x
	return sum

print power(6, 2), power(6, 5)

def enroll(name, gender):
	print 'name:', name
	print 'gender:', gender

print enroll('Frank', 'M')

def enroll(name, gender, age = 6, city = 'Shenzhen'):
	print 'name:', name
	print 'gender:', gender
	print 'age:', age
	print 'city:', city

print enroll('Lucy', 'F')
print enroll('Mary', 'F', 8)
print enroll('Adam', 'M', city='Beijing')

# Attention
def add_end(L=[]):
	L.append('END')
	return L

print add_end([1, 2, 3])
print add_end(['x', 'y', 'z'])

print add_end(), add_end(),


# 定义默认参数要牢记一点：默认参数必须指向不变对象！
def add_end(L = None):
	if L is None:
		L = []
	L.append('END')
	return L

print 
print add_end(), add_end()


# 可变参数

# 函数参数作为一个list或tuple传进来
def calc(numbers):
	sum = 0
	for n in numbers:
		sum = sum + n
	return sum

print calc([1, 2, 3]), calc([1, 3, 5, 7])


# 函数的参数改为可变参数
def calc(*numbers):
	sum = 0
	for n in numbers:
		sum = sum + n * n
	return sum

print calc(1, 2), calc()


# 关键字参数
# 关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict
def person(name, age, **kw):
	print 'name:', name, 'age:', age, 'other:', kw

print person('Frank', 99)
print person('Sunny', 25, city='Shenzhen')
print person('Mike', 30, gender='M', job='Engineer')

kw = {'city':'Beijing', 'job':'Engineer'}
print person('Jack', 36, city=kw['city'], job=kw['job'])

kw = {'city':'Beijing', 'job':'Engineer'}
print person('Jack', 35, **kw)

# 参数组合
def func(a, b, c = 0, *args, **kw):
	print 'a=', a, 'b=', b, 'c=', c, 'args=', args

print func(1, 2)
print func(1, 2, c =  3)
print func(1, 2, 3, 'a', 'b')
print func(1, 2, 3, 'a', 'b', x=99)



