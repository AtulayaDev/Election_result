import bs4
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import os



# url for top party through election commision website


def main():

 url="https://result.election.gov.np/JSONFiles/Election2079/Common/HoRPartyTop5.txt"
 
 
 response=requests.get(url)

 page_content=response.text

#  with open('top_party.html','w') as f:
#     f.write(page_content)

 doc=BeautifulSoup(page_content,'html.parser')
 
 def wtf():

    # today = datetime.today().strftime("%Y-%m-%d")
    today=datetime.now()
    
    if not os.path.exists("./output_html"):
        os.mkdir('./output_html')

    if not os.path.exists(f'./output_html/{today}'):
            os.mkdir(f'./output_html/{today}')

    with open(f"./output_html/{today}/{today}.html" , "w") as f:
        f.write(page_content)

 return wtf()

if __name__ == '__main__':    
    main()



 


    



