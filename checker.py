import requests
import bs4

resp = requests.get('http://ketqua.net')

tree = bs4.BeautifulSoup(resp.text, 'html.parser')

tree.find_all(attrs = {'id': 'rs_0_0'})
result = tree.find_all(attrs = {'id': 'rs_0_0'})[0]

print(result.text)
    
