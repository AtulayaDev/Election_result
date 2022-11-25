from os import listdir
import json
import re
import database

# needed variables for the program
input_folder = './election_html'
party_name_mapper = {
    1 : "Nepali Congress",
    2 : "UML",
    3 : "Maoist",
    158 : "National Freedom Party",
    116 : "National Democratic Party",
    9999 : "Others" 
}
table_name = 'nepal_result'
# things to execute before the main function 
conn = database.create_connection()
database.create_table(conn , table_name)
def main():
    
    for input_file in listdir(input_folder):
        process_file(input_file )
        
def process_file(file : str ):
    # open the file 
    date_and_time = get_date_time_from_file_name(file)
    data = { 
        "CreateDate": date_and_time['date'],
        "CreateTime" : date_and_time['time']
    }
    with open(f"{input_folder}/{file}", 'r') as f:
        file_data = json.loads(f.read())
    
        for party_data in file_data:
            
            data['PartyId'] = party_data['PartyId']
            try:
                data['PartyName'] = party_name_mapper[party_data['PartyId']]
            except: 
               data['PartyName'] = ''
            data['TotalLead'] = party_data['TotLead']
            data['TotalWin'] = party_data['TotWin']
        
            
            save_data(data)


def save_data(data : dict):
    data_tuple = tuple(data.values())
    database.add_data(conn , table_name ,  data_tuple)
    



def get_date_time_from_file_name(file_name : str):
    date_val = re.findall(r'20[0-9]{2}-[0-9]{2}-[0-9]{2}' ,  file_name)[0]
    time_val = re.findall(r'[0-9]{2}\:[0-9]{2}\:[0-9]{2}' , file_name)[0]
    
    return {
        "date": date_val, 
        "time": time_val
    }


if __name__ == "__main__": 
    main()
    # things to do after the main has ececuted 
    conn.close()