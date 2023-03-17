import pymysql
import signup
import add_quote
import view_quotes

host = "localhost"
user = "root"
password = "1234"
database = "quotes"

conn = pymysql.connect(host=host, user=user, password=password, database=database)
cur = conn.cursor()

print("""
1. Add Quote
2. View Quote
3. Edit Quote
""")

while True:
    action = input("Enter action: ")
    username = "ankyvrm"
    if (action == "3"):
        select = f"select a.id as quote_id,a.quotes,a.author from quotes as a inner join users as b on a.user_id = b.id where b.username = '{username}';"
        cur.execute(select)
        user_quotes = cur.fetchall()
        # for i in cur.description:
        #     print(f"i[0]")
        for quote in user_quotes:
            print(f"{quote[0]}  {quote[1]}  {quote[2]}")
    quote_id = input("Please enter quote_id to select quote: ")

        