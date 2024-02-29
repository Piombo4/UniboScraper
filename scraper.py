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
                a = td.find("a")
                if(a is None):
                    title = td.get_text().strip()

                else:
                    title = a.get_text().strip()
                    courseInfo = a.get("href")
                    virtuale = courseInformationPage(courseInfo)
                    print(title + " -> " + virtuale)

        
    else: 
        print(f'Error: Failed to fetch {url}') 
def courseInformationPage(url):
    response = requests.get(url) 
    if response.status_code == 200: 
        soup = BeautifulSoup(response.text, 'html.parser') 
        div = soup.find("div",class_="text-wrap")
        if(div is None):
            return "Nessun virtuale trovato"
        else:   
            a = div.find("a") 
            return "Nessun virtuale trovato" if a is None else a.get("href")
def main():
    url = "https://corsi.unibo.it/magistralecu/Giurisprudenza-Bologna/insegnamenti/piano/2023/9232/000/000/2023"
    simple_scraper(url)
    print("\nFINITO\n")

if __name__ == "__main__":
    main()