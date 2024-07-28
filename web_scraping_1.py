from bs4 import BeautifulSoup
import requests
from lxml import html
import pandas as pd

url = "https://en.wikipedia.org/wiki/List_of_largest_companies_by_revenue"


# Make an HTTP GET request to fetch the page content
response = requests.get(url)
response.raise_for_status()  # Ensure the request was successful

# Parse the page content with lxml
tree = html.fromstring(response.content)

# Use the XPath to locate the table
table = tree.xpath('/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/table[1]')

# Check if the table was found
if table:
    # Convert the table to a string
    table_html = html.tostring(table[0]).decode('utf-8')
    
    # Use pandas to read the HTML table
    dfs = pd.read_html(table_html)
    
    if dfs:
        df = dfs[0]
        
    else:
        print("No tables found in the HTML.")
else:
    print("Table not found")

print(df)

df1 = df.drop('State-owned',axis=1)
print(df1)
