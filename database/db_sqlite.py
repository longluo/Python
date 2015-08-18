#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Database SQLite
# 2015-08-19 00:26:10

# 表是数据库中存放关系数据的集合，一个数据库里面通常都包含多个表，比如学生的表，班级的表，学校的表，等等。表和表之间通过外键关联。
# 要操作关系数据库，首先需要连接到数据库，一个数据库连接称为Connection；
# 连接到数据库后，需要打开游标，称之为Cursor，通过Cursor执行SQL语句，然后，获得执行结果。

import sqlite3
# 导入SQLite驱动:

conn = sqlite3.connect('test.db')

cursor = conn.cursor()

cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')

cursor.execute('insert into user (id, name) values (\'1\', \'Jack\')')

print cursor.rowcount

cursor.close()

conn.commit()

conn.close()



# SQL Query
conn = sqlite3.connect('test.db')

cursor = conn.cursor()

cursor.execute('select * from user where id=?', '1')

values = cursor.fetchall()

print values

cursor.close()

conn.close()












