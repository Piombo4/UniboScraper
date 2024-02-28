import requests 
from bs4 import BeautifulSoup 
visited = {}
def simple_scraper(url): 
    if(len(visited)>5):
        
        return
# Send HTTP request to the URL 
    response = requests.get(url) 


# Check if the request was successful (status code 200) 

    if response.status_code == 200: 

# Parse HTML content with BeautifulSoup 

        soup = BeautifulSoup(response.text, 'html.parser') 

# Extract and print relevant information (modify as needed) 

        title = soup.title.text 
        content = soup.get_text(strip=False).replace("\t","").replace("  ","").replace("\v","")
        prec = ""
        for element in content:
            if(element != "\n" or prec!="\n"):
                print(element, end='')
            prec = element
        
        for link in soup.find_all('a'):
            linkRef = link.get("href")
            hashLink = hash(linkRef)
            if(str(linkRef).startswith("http")):
                if(visited.get(hashLink)== None):
                    visited[hashLink] = linkRef
                    simple_scraper(linkRef)
        
        #print(f'Title: {title} Contendt: {content}') 

# Additional data extraction and processing can be added here 

    else: 

        print(f'Error: Failed to fetch {url}') 

def main():
    url = "https://www.unibo.it/sitoweb/antonio.natali/didattica"
    visited[hash(url)] = url
    simple_scraper(url)
    print("\nFINITO\n")
  

if __name__ == "__main__":
    main()