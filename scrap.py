from bs4 import BeautifulSoup
import requests
import json
import time


url='https://goldprice.org/cryptocurrency-price'
header={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'}

crypto_dic={}

def obtain_data():
    """    Obtain data of cryptocurrencies from a website and store it in a file.

    It sends a GET request to the specified URL with the given headers and then parses the response using BeautifulSoup.
    It then extracts cryptocurrency data from the parsed HTML and stores it in a dictionary, which is then written to a file in JSON format.
    """

    response=requests.get(url, headers=header)
    
    soup=BeautifulSoup(response.text, 'lxml')

    cryptocurrencies=soup.find('div', class_='view-cryptocurrency-index').find('tbody').find_all('tr')

    with open("data.txt", 'w') as f:
        f.write('')

    i=1;
    for cryptocurrency in cryptocurrencies:
        
        cryptocurrency_name=cryptocurrency.find('td', class_='views-field-field-crypto-proper-name').a.text.strip()
        cryptocurrency_curr_price=cryptocurrency.find('td', class_='views-field-field-crypto-price').text.strip()
        cryptocurrency_change_per=cryptocurrency.find('td', class_='views-field-field-crypto-price-change-pc-24h').text.strip()
        cryptocurrency_market_cap=cryptocurrency.find('td', class_='views-field-field-market-cap').text.strip()
        crypto_dic[cryptocurrency_name]={"curr_price": cryptocurrency_curr_price, "change_in_24hr": cryptocurrency_change_per, "market_cap": cryptocurrency_market_cap}
    
    with open("data.txt", 'w') as f:
        json.dump(crypto_dic, f)
        


if __name__=='__main__':
    obtain_data()
    
  
       
