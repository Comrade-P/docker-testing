import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import pyfiglet
from colorama import Fore, Style

hi = pyfiglet.figlet_format("COMRADE__END POINTS_______TRACKER", font="slant")
print(Fore.WHITE + hi + Style.RESET_ALL)
print(Fore.RED + "*" * 50 + Style.RESET_ALL)


site = input(Fore.WHITE+"Enter the TARGET URL...>>>>>"+Style.RESET_ALL)


response = requests.get(site, timeout=10)


if response.status_code == 200:
    print(Fore.RED+f"\nSuccessfully fetched: {site}\n"+Style.RESET_ALL)
    
    
    soup = BeautifulSoup(response.text, "html.parser")
    
    
    parsed_url = urlparse(site)
    base_url = f"{parsed_url.scheme}://{parsed_url.netloc}"

    endpoints = set()
    
    
    for link in soup.find_all('a'):
        comrade_find_href = link.get('href')  
        if comrade_find_href:  
            full_url = urljoin(base_url, comrade_find_href)  
            endpoints.add(full_url) 
    
    
    print(Fore.WHITE+f"Found {len(endpoints)} ,endpoints:\n"+Style.RESET_ALL)
    print(Fore.RED+"\n".join(sorted(endpoints))+Style.RESET_ALL)

else:
    print(Fore.RED+f"Failed to fetch {site}, status code: {response.status_code}"+Style.RESET_ALL)





#want to make a docker file of this guide me i want to learn iam an beginner