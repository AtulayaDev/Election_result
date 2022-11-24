from os import listdir
import json
import re
import database

# process the files that was recently uploaded in election_html and save it to a data base

input_folder = './election_html'


party_name_mapper = {
    1 : "Nepali Congress",
    2 : "UML",
    3 : "Maoist",
    158 : "National Freedom Party",
    116 : "National Democratic Party",
    9999 : "Others" 
}

def main():
    # loop through all the html files in election_html 
    for input_file in listdir(input_folder):
        process_file(input_file)
        
def process_file(file : str):
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
            data['PartyName'] = party_name_mapper[party_data['PartyId']]
            data['TotalLead'] = party_data['TotLead']
            data['TotalWin'] = party_data['TotWin']
        
            
            save_data(data)


def save_data(data):
    print(data)
    # save the relevant data to a database like sqlite, pg , firebase , supabase etc .... 
     #! need to add that data file in list and execute this in code below i.e new=[#data value]
    pass

# database.add_data() #! need to add c.executemay(bala(new))
# database.data_main()

def get_date_time_from_file_name(file_name : str):
    date_val = re.findall(r'20[0-9]{2}-[0-9]{2}-[0-9]{2}' ,  file_name)[0]
    time_val = re.findall(r'[0-9]{2}\:[0-9]{2}\:[0-9]{2}' , file_name)[0]
    
    return {
        "date": date_val, 
        "time": time_val
    }
if __name__ == "__main__":
    main()