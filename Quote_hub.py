import pymysql
import signup
import add_quote
import view_quotes
from settings import *


conn = pymysql.connect(host=host, user=user, password=password, database=database)
cur = conn.cursor()

print("""
Welcome to Quote-Hub
1. login
2. signup
""")

while True:
    user = (input("Please enter login/signup user: ")).lower()
    if (user == "login") or (user == "1"):
        user_logged_in, user_details = signup.login(cur)
        username = user_details[0][0]
        if (user_logged_in == True):
            # add_quote.add_quote(cur,user_details,conn)
            break         
    elif (user == "signup") or (user == "2"):
        signup_complete, user_details = signup.signup(cur)
        conn.commit()
        if (signup_complete == True):
            break
    else:
        print("please enter correct input")

while True:
    print("""
    1. Add Quote
    2. View Quote
    3. Edit Quote
    """)
    action = input("Enter action: ")
    if (action == "1"):
        add_quote.add_quote(cur,user_details,conn)
    elif (action == "2"):
        view_quotes.view_quotes(cur)
    elif (action == "0"):
        print("Thanks")
        break
    else:
        print("Invalid Action, Try Again!!!!")


conn.close()




