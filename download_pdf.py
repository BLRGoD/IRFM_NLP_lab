import requests

url = '''https://fstec.ru/files/61/----------/17/----------.pdf'''

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    'Referer': 'https://www.google.com/',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
}

r = requests.get(url, headers=headers, allow_redirects=True, verify=False, timeout=30)

open('met_recommendations.pdf', 'wb').write(r.content)
