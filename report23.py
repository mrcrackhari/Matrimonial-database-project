import mysql.connector
import csv

con = mysql.connector.connect(

    host = "localhost",
    user = "root",
    password = "",
    database = "matrimonial_website"
)

cursor = con.cursor(dictionary = True)

cursor.execute("""

                 SELECT s.state_name as State , COUNT(m.member_id) as Member_Count,AVG(m.height) as Average_height,AVG(m.annual_income) as Average_income FROM member_info m
                 INNER JOIN state s ON m.state = s.id 
                 GROUP BY State
                 ORDER BY Member_Count DESC 


""")

data = cursor.fetchall()

with open ("report_13_state_statistics.csv","w",newline="",encoding="utf-8") as file:
    writer = csv.DictWriter(
        file,
        fieldnames=[

                    "State",
                    "Member_Count",
                    "Average_height",
                    "Average_income"

        ]
    )

    writer.writeheader()
    writer.writerows(data)

print("Data  exported successfully.")

cursor.close()
con.close()