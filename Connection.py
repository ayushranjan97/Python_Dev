# import os
# command = "echo cmd_working"  #The command needs to be a string
# os.system(command)
import snowflake.connector
import pandas as pd


# Gets the version
conn = snowflake.connector.connect(
user='AyushRanjan',
password='Ayush@123',
account='kg14021.ap-south-1.aws'
)
print("Connection established successfully")
cur=conn.cursor()
try:
    sql = 'SELECT * FROM "TRAINING"."PERSONAL"."COVID_MASTER_DATA" LIMIT 10'
    cur.execute(sql)
    df1=pd.DataFrame(cur)
    print(df1)
finally:
    cur.close()
    conn.close()