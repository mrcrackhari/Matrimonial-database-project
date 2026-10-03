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
            SELECT m.member_id,m.first_name,m.middle_name,m.last_name,g.gender,ms.status,c.city_name,o.occupation_name,m.annual_income FROM member_info m
            INNER JOIN gender g ON m.gender = g.id
            INNER JOIN marital_status ms ON m.marital_status = ms.id
            INNER JOIN city c ON m.city = c.id
            INNER JOIN occupations o ON m.occupation = o.id
            WHERE 
            ms.status = 'Never Married'
            AND m.annual_income > 500000
            AND (
            (g.gender = 'Male' AND ms.status = 'Never Married')
            OR (g.gender = 'Female' AND c.city_name = 'Pune') )
            AND NOT (o.occupation_name = 'Unemployed')
            ORDER BY m.annual_income DESC
            LIMIT 10;





""")


data = cursor.fetchall()

with open ("report_16_final_advanced_search.csv","w",newline="",encoding="utf-8") as file:
    writer=csv.DictWriter(
          file,
          fieldnames=[
              "member_id",
              "first_name",
              "middle_name",
              "last_name",
              "gender",
              "status",
              "city_name",
              "occupation_name",
              "annual_income"
               
        ]


    )



    writer.writeheader()
    writer.writerows(data)

print("Data export successed")

cursor.close()
con.close()