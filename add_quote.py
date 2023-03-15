# print("""
# 1. Add Quote
# 2. View Quote
# """)

# while True:
#     action = input("Enter action: ")
#     if (action == "1"):
def add_quote(cur,user_details,conn):
    while True:
        category = (input("Enter category: ")).title()
        quote = input("Enter Quote: ")
        author = input("Enter author: ").title()
        # username = user_details[0][0]
        

        select = f"select id,first_name,last_name from users where username = '{user_details[0][0]}'"
        cur.execute(select)
        out = cur.fetchall()
        user_id = out[0][0]
        user_full_name = f"{(out[0][1]).title()} {(out[0][2]).title()}"
        if (author == ""): 
            author = user_full_name
                        
        if (category == "") or (quote == ""):
            print("Category or Quote can't be empty, please insert again!!!")             
        else:
            quote = conn.escape(quote)
            select = f"select quotes from quotes where quotes = {quote};"
            cur.execute(select)
            quotes = cur.fetchall()

            if (len(quotes) ==0):
                insert = f"insert into quotes (category, quotes, user_id, author) values ('{category}', {quote},{user_id},'{author}');"
                cur.execute(insert)
                conn.commit()
                print("Quote Added Successfully")
                return True
            else:
                print("Quote already available, Please add new quote!!!")
            
                



                     

        

                
