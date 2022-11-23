import sqlite3


CREATE_TABLE="CREATE TABLE Election (Id INTERGER PRIMARY KEY, PartyId INTEGER,PartyName TEXT, TotalLead INTERGER, TotalWin INTEGER;"
INSERT_TABLE="INSERT INTO Election (PartyId,PartyName,TotalLead,TotalWin) VALUES(,,,);"
def connect():
    return sqlite3.connect('data.db')


def create_tables(connection):
    with connection:
        connection.execute(CREATE_TABLE)
    
    

        
        