import pymysql
from settings import *

conn = pymysql.connect(host=host, user=user, password=password,)
cur = conn.cursor()

print("""
Welcome to Quote-Hub
1. login
2. signup
""")

cur.execute(f"drop database if exists {database}")
create_database = f"""create database if not exists {database} ;"""
cur.execute(create_database)

cur.execute(f"""use {database};""")



create = f"create table if not exists users (id int auto_increment primary key, first_name varchar(15) not null, last_name varchar(15) not null, password varchar(128) not null, username varchar(15) unique);"
cur.execute(create)
create = f"create table if not exists categories(cat_id int auto_increment primary key, cat_name varchar(50));"
cur.execute(create)
create = f"create table if not exists quotes (id int auto_increment not null primary key, user_id int, category_id int not null, quotes varchar(255) unique , author varchar(20),foreign key (user_id) references users(id), foreign key (category_id) references categories(cat_id));"
cur.execute(create)



conn.close()