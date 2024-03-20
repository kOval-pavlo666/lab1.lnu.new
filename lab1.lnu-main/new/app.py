import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def scrape_links(url):
    response = requests.get(url)
    links = []
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        for span in soup.find_all('span', class_='value'):
            link = span.find('a')
            if link and link.get('href') and link.get('href').startswith('https://'):
                links.append(urljoin(base_url, link.get('href')))
    return links

def scrape_info(link, file):
    administration_link = link + "/about/administration"
    response = requests.get(administration_link)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        dean_office_section = soup.find('section', class_='dean-office')
        if dean_office_section:
    
            dean_office_info = dean_office_section.find_all('td')
            file.write(f"Faculty: {link}\n")
            for item in dean_office_info:
                file.write(item.text.strip() + '\n')
            file.write("\n")
        
   

base_url = "https://lnu.edu.ua"

url = "https://lnu.edu.ua/about/faculties/"

file_name = "dean_information.txt"

faculty_links = scrape_links(url)
with open(file_name, 'a', encoding='utf-8') as file:
    for faculty_link in faculty_links:
        
        scrape_info(faculty_link, file)
