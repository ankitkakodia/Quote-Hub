# print("""
# 1. Add Quote
# 2. View Quote
# """)

# while True:
#     action = input("Enter action: ")
#     if (action == "1"):
def add_quote(cur,user_details,conn):
    while True:
        while True:
            print("Please choose category or Press 0 to go back:")
            select = f"select * from categories;"
            cur.execute(select)
            all_cat = cur.fetchall()
            all_cat_id = []
            for id,cat in all_cat:
                print(id,cat)
                all_cat_id.append(id)

            category_id = int(input("Enter category_id: "))
            if (category_id == 0):
                break
            elif category_id not in all_cat_id:
                print("Invalid category Id, please try again")
            else: break
        quote = input("Enter Quote or Press 0 to go back: ").strip()
        author = input("Enter author or Press 0 to go back: ").title().strip()
        if (category_id == "0") or (quote == "0") or (author == "0"):
            break
        

        select = f"select id,first_name,last_name from users where username = '{user_details[0][0]}'"
        cur.execute(select)
        out = cur.fetchall()
        user_id = out[0][0]
        user_full_name = f"{(out[0][1]).title()} {(out[0][2]).title()}"
        if (author == ""): 
            author = user_full_name
                        
        if (category_id == "") or (quote == ""):
            print("Category or Quote can't be empty, please insert again!!!")             
        else:
            select = f"select cat_name from categories where cat_id = {category_id} ;"
            cur.execute(select)
            category = cur.fetchall()[0][0]
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
            
                



                     

        

                
