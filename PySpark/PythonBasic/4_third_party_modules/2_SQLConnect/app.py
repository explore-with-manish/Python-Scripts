import pyodbc

conn = pyodbc.connect(
    "Driver={SQL Server};"
    "Server=.\\SqlExpress;"
    "Database=Northwind;"
    "Trusted_Connection=yes;"
)

cursor = conn.cursor()
rows = cursor.execute("SELECT * FROM Northwind.dbo.Customers")

for row in rows:
    print(row)