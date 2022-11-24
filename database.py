import sqlite3


 

# INSERT_TABLE="INSERT INTO Election (PartyId,PartyName,TotalLead,TotalWin) VALUES(?,?,?,?);"

CREATE_TABLE="""CREATE TABLE nepal(
                  PartyId INTEGER,
                  PartyName TEXT, 
                  TotalLead INTERGER, 
                  TotalWin INTEGER
            );"""
            
            
def data_main():          
 conn= sqlite3.connect('election_result.db')

 c=conn.cursor()
 c.execute('SELECT rowid, * FROM nepal')
 a= c.fetchall()
 for aa in a:
     print(aa)


 #  c.execute(CREATE_TABLE) no idea how to not run this code.

 # c.execute(INSERT_TABLE)

 conn.commit() 

 conn.close()

data_main()

def add_data(PartyId,PartyName,TotalLead,TotalWin): #!here i can add list or create list funtion
    conn= sqlite3.connect('election_result.db')
    c=conn.cursor()
    
    c.execute("INSERT INTO nepal VALUES (?,?,?,?)",(PartyId,PartyName,TotalLead,TotalWin))#!in this part i can add list
    
    conn.commit()
    conn.close()
    
    
#! eg





