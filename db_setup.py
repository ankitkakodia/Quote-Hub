import pymysql
from settings import *

conn = pymysql.connect(host=host, user=user, password=password,)
cur = conn.cursor()

cur.execute(f"drop database if exists {database}")
print("Database Deleted")
create_database = f"""create database {database} ;"""

cur.execute(create_database)
print("Database created")

cur.execute(f"""use {database};""")
print("use database")

create = f"create table users (id int auto_increment primary key, first_name varchar(15) not null, last_name varchar(15) not null, password varchar(128) not null, username varchar(15) unique);"
cur.execute(create)
print("User table created")
create = f"create table categories(cat_id int auto_increment primary key, cat_name varchar(50));"
cur.execute(create)
print("Categories table created")
create = f"create table quotes (id int auto_increment not null primary key, user_id int, category_id int not null, quotes varchar(255) unique , author varchar(20),foreign key (user_id) references users(id), foreign key (category_id) references categories(cat_id));"
cur.execute(create)
print("Quotes table created")
insert = f"insert into categories (cat_name) values ('Motivational'),('Funny'),('Sad'),('Love'),('Friendship'),('Political'),('Others');"
cur.execute(insert)
conn.commit()
print("Insert categories")


conn.close()