import pyodbc

conn = pyodbc.connect('DRIVER={ODBC Driver 11 for SQL Server};SERVER=dbsep1612;DSN=UHN_Reporting;DATABASE=UHN_Reporting;UID=cvikas10;PWD=May2019#;Trusted_Connection=yes;')
cursor = conn.cursor()
for row in cursor.tables():
    print (row.table_name)