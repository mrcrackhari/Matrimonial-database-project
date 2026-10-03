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
            SELECT f.food_pref AS Food_Preference ,COUNT(m.member_id) AS Member_count,AVG(m.annual_income) AS Average_income FROM member_info m
            INNER JOIN food f ON m.food_preference = f.id
            GROUP BY Food_Preference
            ORDER BY Member_count DESC,Average_income desc




""")


data = cursor.fetchall()

with open ("report_14_food_preferance_analysis.csv","w",newline="",encoding="utf-8") as file:
    writer=csv.DictWriter(
          file,
          fieldnames=[
              "Food_Preference",
              "Member_count",
              "Average_income"


              
          ]


    )



    writer.writeheader()
    writer.writerows(data)

print("Data export successed")

cursor.close()
con.close()