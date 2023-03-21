import hashlib

def login(cur):
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    password = hashlib.sha512(password.encode())
    password = password.hexdigest()
    select = f"select username, password from users where username = '{username}' and password = '{password}';"
    cur.execute(select)
    user_details = cur.fetchall()
    
    if(len(user_details)):
        print("Login Successfully!!!")
        return True, user_details
    return None
            
def signup(cur):
    first_name = input("Please enter First name: ")
    last_name = input("Please enter Last name: ")
    username = input("Enter username: ")
    password = input("Enter Password: ")
    password = hashlib.sha512(password.encode())
    password = password.hexdigest()
    select = f"select username, password from users where username = '{username}';"
    cur.execute(select)
    user_details = cur.fetchall()
    
    if (len(user_details)==0):
        insert = f"insert into users (first_name,last_name,password,username) values('{first_name}','{last_name}','{password}','{username}');"
        cur.execute(insert)
        return True, (username, password)
    return None
            
