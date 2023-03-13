import pymysql
import signup

host = "localhost"
user = "root"
password = "1234"
database = "quotes"

conn = pymysql.connect(host=host, user=user, password=password, database=database)
cur = conn.cursor()

print("""
Welcome to Quote-Hub
1. login
2. signup
""")

create = f"create table if not exists users (id tinyint auto_increment primary key, first_name varchar(15) not null, last_name varchar(15) not null, password varchar(15) not null, username varchar(15) unique);"
cur.execute(create)
create = f"create table if not exists quotes (id tinyint auto_increment not null primary key, user_id tinyint, category varchar(50) not null , quotes varchar(255) unique , author varchar(20));"
cur.execute(create)


while True:
    user = (input("Please enter login/signup user: ")).lower()
    if (user == "login") or (user == "1"):
        res = signup.login(cur)
        if (res == True):
            break
        
    elif (user == "signup") or (user == "2"):
        signup.signup(cur)
        conn.commit()
        
    else:
        print("please enter correct input")
    
conn.close()




