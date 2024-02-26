import requests 
from bs4 import BeautifulSoup 
def simple_crawler(url): 

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
            print(link.get('href'))
            simple_crawler(str(link.get('href')))

        #print(f'Title: {title} Content: {content}') 

# Additional data extraction and processing can be added here 

    else: 

        print(f'Error: Failed to fetch {url}') 

def main():
    simple_crawler("https://www.unibo.it/sitoweb/antonio.natali/didattica")
if __name__ == "__main__":
    main()