def login(cur):
            username = input("Username: ")
            password = input("Password: ")
            select = f"select username, password from users where username = '{username}' and password = '{password}';"
            cur.execute(select)
            login = cur.fetchall()
            if (len(login) == 0):
                print("Wrong Username/password or Please signup first!!")
                user = input("Please enter login/signup user: ")
            else :
                return ("Login Successfully!!!")
