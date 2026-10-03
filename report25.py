import mysql.connector
import csv 

con= mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "matrimonial_website"
)

cursor = con.cursor(dictionary = True)

cursor.execute("""
            SELECT c.city_name AS city , o.occupation_name AS Occupation , COUNT(m.member_id) AS Member_count, AVG(m.annual_income) AS Average_income FROM member_info m
            INNER JOIN city c ON m.city = c.id
            INNER JOIN occupations o ON m.occupation = o.id
            GROUP BY city , Occupation
            ORDER BY Member_count DESC , Average_income DESC LIMIT 10





""")


data = cursor.fetchall()

with open (" report_15_top_city_occupation.csv","w",newline="",encoding="utf-8") as file:
    writer=csv.DictWriter(
          file,
          fieldnames=[
                "city",
                "Occupation",
                "Member_count",
                "Average_income"


              
          ]


    )



    writer.writeheader()
    writer.writerows(data)

print("Data export successed")

cursor.close()
con.close()