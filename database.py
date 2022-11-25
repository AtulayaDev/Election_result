import sqlite3


 

database_name = './election_result.db'
    

def create_connection():
    return sqlite3.connect(database_name)           
def data_main():          
 conn= sqlite3.connect('election_result.db')

 c=conn.cursor()
 c.execute('SELECT rowid, * FROM nepal')
 a= c.fetchall()
 for aa in a:
     print(aa)


 

 conn.commit() 
 conn.close()

# data_main()

def add_data(conn, table_name,  data : list): 
    c = conn.cursor()
    c.execute(f"""INSERT INTO {table_name} ('CreateDate' , 'CreateTime' , 'PartyId' ,  'PartyName' , 'TotalLead' ,  'TotalWin') 
    VALUES (?,?,?,?,?,?)""",data)
    conn.commit()
    
def create_table(conn , table_name):
    cur = conn.cursor()
    CREATE_TABLE_QUERY=f"""CREATE TABLE IF NOT EXISTS {table_name}(
                  PartyId INTEGER,
                  PartyName TEXT, 
                  TotalLead INTERGER, 
                  TotalWin INTEGER,
                  CreateDate TEXT,
                  CreateTime TEXT
            );"""
    cur.execute(CREATE_TABLE_QUERY)

    conn.commit()