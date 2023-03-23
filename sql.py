import os
import pandas as pd
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Ladenposse3",
  database="bincom"
)

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM sys.polling_unit")
myresult = mycursor.fetchall()
print(myresult)

df=pd.DataFrame()
for x in myresult:
    df2=pd.DataFrame(list(x)).T
    df=pd.concat([df,df2])
df.to_html('templates/sql-data.html')