import requests
from bs4 import BeautifulSoup

baseurl = "https://webscraper.io"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
}

producttitles = []
productlinks = []

r = requests.get("https://webscraper.io/test-sites/e-commerce/allinone/phones", headers=headers)
print(r.status_code)
soup = BeautifulSoup(r.content, 'lxml')
a_tag = soup.find('a', class_='title', title="Sony Xperia")
if a_tag:
    title_value = a_tag.get('title')
    print("Title attribute:", title_value)
else:
    print("No matching tag found")

# productlist = soup.find_all('a', class_='title')
# for item in productlist:
#     producttitles.append(item.text.strip())
#     productlinks.append(baseurl + item['href'])

# lst = []


# for link in productlinks:
#     r = requests.get(link, headers=headers)
#     soup = BeautifulSoup(r.content, 'lxml')
    
    
#     name = soup.find('h4', class_="title card-title")
#     review = soup.find('p', class_='review-count')
#     price = soup.find('h4', class_="price float-end pull-right")
#     color_dropdown = soup.find('select', {'aria-label': 'color'})
#     colors = [option.text.strip() for option in color_dropdown.find_all('option') if option['value']] if color_dropdown else []
   
    
#     product_details = {
#         'name': name.text.strip() if name else None,
#         'review': review.text.strip() if review else None,
#         'colors': colors,
#         'price': price.text.strip() if price else None
#     }
    
    
#     lst.append(product_details)


# for product in lst:
#     print(product)
