def signup(cur):
    while True:
        first_name = input("Please enter First name: ")
        last_name = input("Please enter Last name: ")
        username = input("Choose username: ")
        password = input("Choose password: ")
        select = f"select username from users where username = '{username}';"
        cur.execute(select)
        usernames = cur.fetchall()
        
        if (len(usernames)==0):
            insert = f"insert into users (first_name,last_name,password,username) values('{first_name}','{last_name}','{password}','{username}');"
            cur.execute(insert)
            # conn.commit()
            return ("Signup Successfully")
            
        else :
             print("Username Already exists, please login!!!")
             signup.login(cur)
