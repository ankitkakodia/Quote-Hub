def login(cur):
    while True:
        username = input("Username: ")
        password = input("Password: ")
        select = f"select username, password from users where username = '{username}' and password = '{password}';"
        cur.execute(select)
        user_details = cur.fetchall()
        
        if (len(user_details) == 0):
            print("Wrong Username/password or Please signup first!!")
        else :
            print("Login Successfully!!!")
            return True, user_details
            
def signup(cur):
    while True:
        first_name = input("Please enter First name: ")
        last_name = input("Please enter Last name: ")
        username = input("Choose username: ")
        password = input("Choose password: ")
        select = f"select username, password from users where username = '{username}';"
        cur.execute(select)
        user_details = cur.fetchall()
        
        if (len(user_details)==0):
            insert = f"insert into users (first_name,last_name,password,username) values('{first_name}','{last_name}','{password}','{username}');"
            cur.execute(insert)
            return True, user_details
        else :
            print("Username Already exists, please try again!!!")
             



