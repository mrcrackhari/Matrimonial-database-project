import mysql.connector
import csv

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="matrimonial_website"
)

mycursor = mydb.cursor()


mycursor.execute("""
        SELECT distinct m.profile_code,m.first_name,m.middle_name,m.last_name,c.city_name,d.district_name,s.state_name,g.gender FROM member_info m
       JOIN gender g ON m.gender = g.id  JOIN city c ON m.city = c.id  JOIN district d ON m.district = d.id  JOIN state s ON m.state = s.id
       ORDER BY m.first_name DESC, m.last_name DESC; 
   
       """)

data = mycursor.fetchall()

with open("report_02_unique.csv", "w", newline="", encoding="utf-8") as file:

    writer = csv.writer(file)
    writer.writerow([
        "profile_code","first_name","middle_name","last_name","city_name","district_name","state_name","gender"
       
       
    ])


    for row in data:
        writer.writerow(row)

print("Data exported successfully")


mycursor.close()
mydb.close()