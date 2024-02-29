import requests 
from bs4 import BeautifulSoup
import concurrent.futures
class UniboScraper:
    def __init__(self, url):
        self.url =url
        
    def courseInformationPage(self,url):
        response = requests.get(url) 
        if response.status_code == 200: 
            soup = BeautifulSoup(response.text, 'html.parser') 
            div = soup.find("div",class_="text-wrap")
            if(div is None):
                return "Nessun virtuale trovato"
            else:   
                a = div.find("a") 
                return "Nessun virtuale trovato" if a is None else a.get("href")
    
    def startScraper(self): 
        response = requests.get(self.url) 
        if response.status_code == 200: 
            soup = BeautifulSoup(response.text, 'html.parser') 
            tbodies=soup.find_all("tbody")
            for body in tbodies:
                for tr in body.find_all("tr"):
                    td = tr.find("td",class_="title")
                    a = td.find("a")
                    if(a is None):
                        title = td.get_text().strip()

                    else:
                        title = a.get_text().strip()
                        courseInfo = a.get("href")
                        virtuale = self.courseInformationPage(courseInfo)
                        print(title + " -> " + virtuale)

        else: 
            print(f'Error: Failed to fetch {self.source_url}') 

if __name__ == '__main__':
    cc = UniboScraper('https://corsi.unibo.it/magistrale/ingegneriainformatica/insegnamenti/piano/2023/5826/B21/000/2023')
    cc.startScraper()