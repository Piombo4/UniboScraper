import requests 
from bs4 import BeautifulSoup 
def simple_scraper(url): 
    response = requests.get(url) 
    if response.status_code == 200: 
        soup = BeautifulSoup(response.text, 'html.parser') 
        tbodies=soup.find_all("tbody")
        for body in tbodies:
            for tr in body.find_all("tr"):
                td = tr.find("td",class_="title")
                a = td.find("a",)
                #title = a.get_text()
                print(a)
        
    else: 
        print(f'Error: Failed to fetch {url}') 

def main():
    url = "https://corsi.unibo.it/magistrale/ingegneriainformatica/insegnamenti/piano/2023/5826/B21/000/2023"
    simple_scraper(url)
    print("\nFINITO\n")

if __name__ == "__main__":
    main()