# print("""
#     1. Add Quote
#     2. View Quote
#     """)

# 
#     action = (input("Enter action: ")).strip()
#     if (action == "2"):
def view_quotes(cur):
        print("1.Search by Category: Press 1\n \
              2.Search by Author: Press 2\n \
              3.Search by words: Press 3\n \
              Press 0 for Exit")
        search = input("Search: ").strip()
        # if (search == "0"):
        #     break
        if (search == "1"):
                select = f"select * from categories;"
                cur.execute(select)
                all_cat = cur.fetchall()
                all_cat_id = []
                for id, cat in all_cat:
                    print(id, cat)
                    all_cat_id.append(id)
                
                print("Please choose category or Press 0 to go back:")
                category_id = input("Enter category_id: ").strip()
                if (category_id == ""):
                    select = f"select quotes, author from quotes;"
                    cur.execute(select)
                    all_quotes = cur.fetchall()
                    count = 0
                    if (len(all_quotes)==0):
                        print(f"Quotes do not exist.")
                        # break
                    else:
                        for quote in all_quotes:
                            count += 1
                            print(f"{count}.{quote[0]}\n{' '*len(quote[0])}-by {quote[1].title()}")
                elif int(category_id) not in all_cat_id:
                    print("Invalid category Id, please try again")
                else:
                    # select = f"select cat_name from categories where cat_id = {category_id};"
                    # cur.execute(select)
                    # category = cur.fetchall()[0][0]
                # category = input("Enter Category or Press 0 to go Back: ").strip()
                    select = f"select quotes, author from quotes where category_id = {category_id};"
                    cur.execute(select)
                    quotes_by_cat = cur.fetchall()
                    count = 0
                    if (len(quotes_by_cat)==0):
                        print(f"No Result found for {category_id}")
                        # break
                    else:
                        for quote in quotes_by_cat:
                            count += 1
                            print(f"{count}.{quote[0]}\n{' '*len(quote[0])}-by {quote[1].title()}")
                        # break
                    
        elif (search == "2"):
            
                author = input("Enter Author or Press 0 to go Back: ").strip()
                select = f"select quotes, author from quotes where author like '%{author}%';"
                cur.execute(select)
                quotes_by_aut = cur.fetchall()
                count = 0
                
                # if (author == "0"):
                #     break
                if (len(quotes_by_aut)==0):
                    print("Author not found, Please enter correct Author")
                else:
                    for quote in quotes_by_aut:
                        count += 1
                        print(f"{count}.{quote[0]}\n{' '*len(quote[0])}-by {quote[1].title()}")
                    # break

        elif (search == "3"):
            
                words = input("Enter words or Press 0 to go Back: ").strip()
                select = f"select quotes, author from quotes where quotes like '%{words}%';"
                cur.execute(select)
                quotes_by_words = cur.fetchall()
                count = 0

                # if (words =="0"):
                #     break
                if (len(quotes_by_words)==0):
                    print("No result found, Please enter correct words")
                else:
                    for quote in quotes_by_words:
                        count += 1
                        print(f"{count}.{quote[0]}\n{' '*len(quote[0])}-by {quote[1].title()}")
                    # break    
        else:
            print("Please provide correct action")  
            
