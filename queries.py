import psycopg2

try:
    conn = psycopg2.connect("dbname='donut_tycoon' user='Austin' host='localhost'")
    cursor = conn.cursor()
except:
    print("I am unable to connect to the database")

def getAll(table):
    cursor.execute("SELECT * FROM {0}".format(table))
    out = cursor.fetchall()
    return out

def getWhere(table, col, val):
    cursor.execute("SELECT * FROM {0} WHERE {1} = {2}".format(table, col, val))
    out = cursor.fetchall()
    return out
