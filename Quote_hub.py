import pymysql
host = "localhost"
user = "root"
password = "1234"
database = "quotes"

conn = pymysql.connect(host=host, user=user, password=password, database=database)
cur = conn.cursor()


user = "ankitkk"
select = f"select * from users where username = '{user}';"
cur.execute(select)
out = cur.fetchall()
print(out)




print("Welcome to Quote-Hub")

user = input("Please enter login/signup user: ")

# create = f"create table if not exists users (id tinyint auto_increment primary key, first_name varchar(15) not null, last_name varchar(15) not null, password varchar(15) not null, username varchar(15) unique);"
                    # cur.execute(create)
while True:
    if (user == "login"):
        username = input("Username: ")
        password = input("Password: ")
        break   

    elif (user == "signup"):
        def signup():
            while True:
                first_name = input("Please enter First name: ")
                last_name = input("Please enter Last name: ")
                username = input("Choose username: ")
                password = input("Choose password: ")
                select = f"select username from users where username = '{username}';"
                cur.execute(select)
                usernames = cur.fetchall()
                if (username == (usernames[0][0])):
                    print ("Username Already exists, try again!!!")
                else:
                    insert = f"insert into users (first_name,last_name,password,username) values('{first_name}','{last_name}','{password}','{username}');"
                    cur.execute(insert)
                    print ("Signup Successfully")
                    break
    elif (user != "login") or (user != "signup"):
        user = input("Try again, enter login/signup user: ")



