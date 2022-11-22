import requests
from datetime import datetime
import os
import time



# url for top party through election commision website


def wtf(page_content):
    today=datetime.now()
    output_folder = './election_html'
    if not os.path.exists(output_folder):
        os.mkdir(output_folder)

    
    with open(f"{output_folder}/res_{today}.html" , "w") as f:
        f.write(page_content)

def main():
    print("Starting sending request for election result ....")
    url="https://result.election.gov.np/JSONFiles/Election2079/Common/HoRPartyTop5.txt"
    response=requests.get(url)
    
    wtf(response.text)

 

if __name__ == '__main__':    
    while True:
        main()
        time.sleep(15 * 60)
