# Importing Packages
import sqlite3
import pandas as pd

db = sqlite3.connect('movies.db')

cursor = db.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS movies (id INT, Movie_Name VARCHAR(30), Lead_Actor VARCHAR(30), Lead_Actress VARCHAR(30), Director_Name VARCHAR(30) ,Year_Of_Release INT)")

ids = [1,2,3,4]
movies = ["Bahubali","Chhichhore","RRR","Vikram"]
heros = ["Parbas","Sushant Singh Rajput","Ram Charan","Kamal Haasan"]
heroines = ["Anushka","Shraddha Kapoor","Alia Bhat","Gayathrie Shankar"]
directors = ["S. S. Rajamouli","Nitesh Tiwari","S. S. Rajamouli","Lokesh Kanagaraj"]
years = ["2015","2019","2022","2022"]

columns = ["ID","Movie_Name","Lead_Actor","Lead_Actress","Director_Name","Year_Of_Release"]

for id,movie,hero,heroine,director,year in zip(ids,movies,heros,heroines,directors,years):
    cursor.execute('''INSERT INTO movies(id, Movie_Name, Lead_Actor, Lead_Actress, Director_Name,Year_Of_Release) VALUES({},"{}","{}","{}","{}",{})'''.format(id,movie,hero,heroine,director,year))

query = """SELECT * from movies"""
cursor.execute(query)
records = cursor.fetchall()

print(pd.DataFrame(records,columns = columns),"\n")


query = """SELECT * from movies where Lead_Actor = 'Ram Charan'"""
cursor.execute(query)
records = cursor.fetchall()

print(pd.DataFrame(records,columns = columns))
