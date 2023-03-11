import pymysql
import signup
import login

host = "localhost"
user = "root"
password = "1234"
database = "quotes"

conn = pymysql.connect(host=host, user=user, password=password, database=database)
cur = conn.cursor()



# user = "ankitkk"
# pwd = "ankit1234"
# select = f"select * from users where username = '{user}';"
# cur.execute(select)
# out = cur.fetchall()
# print(len(out))


# print(out[0][4], out[0][3])




print("Welcome to Quote-Hub")

user = input("Please enter login/signup user: ")

create = f"create table if not exists users (id tinyint auto_increment primary key, first_name varchar(15) not null, last_name varchar(15) not null, password varchar(15) not null, username varchar(15) unique);"
cur.execute(create)
create = f"create table if not exists quotes (id tinyint auto_increment not null primary key, user_id tinyint, category varchar(50) not null , quotes varchar(255) unique , author varchar(20));"
cur.execute(create)

while True:
    if (user == "login"):
        login.login(cur)
        conn.commit()
        conn.close()
        
    elif (user == "signup"):
        signup.signup(cur)
        conn.commit()
        conn.close()
    elif (user != "login") or (user != "signup"):
        user = input("Try again, enter login/signup user: ")





