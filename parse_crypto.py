from bs4 import BeautifulSoup
import requests
import csv
import json
headers = {
    'accept': '*/*',
    'user-agent': 'Mozilla/5.0 (Linux; Android) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.109 Safari/537.36 CrKey/1.54.248666'
}
n = int(input('Enter how many pages of crypto do you want to parse '))
crypto_res_dict = {}
crypto_res_list = []
def parse_crypto(n):
    url = f'https://coinmarketcap.com/?page={n+1}'
    get_url = requests.get(url, headers=headers).text
    result = BeautifulSoup(get_url, 'html.parser')
    prices = result.tbody.find_all('tr')
    names_10 = result.tbody.find_all('tr')
    names_else = result.tbody.find_all('tr', class_='sc-1rqmhtg-0 jUUSMS')
    for name in names_10[:10]:
        name_res = list(name)[2].p.string
        price_res = list(name)[3].span.text
        crypto_res_dict[name_res] = price_res
        crypto_res_list.append({
            'Name of crypto': name_res,
            'Price of crypto': price_res,
        })
    for name in names_else:
        names_res = list(name)[2].find_all('span')[1]
        price_res = list(name)[3].span.text
        for name_res in names_res:
            crypto_res_dict[name_res.text] = price_res
            crypto_res_list.append({
                'Name of crypto': name_res.text,
                'Price of crypto': price_res,
            })
count = 1
for n in range(n):
    parse_crypto(n)
    print(f"Completed is {count}***")
    count += 1
with open(f'parse_crypto_pages{n+1}.csv', 'a', newline='', encoding='utf-8') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(
        (
            'Name of cryptocurrency',
            'Cost of cryptocurrency'
        )
    )
with open(f'parse_crypto_pages{n+1}.csv', 'a', newline='', encoding='utf-8') as file:
    writer = csv.writer(file, delimiter=';')
    for cur_name, cur_cost in crypto_res_dict.items():
        writer.writerow(
            (
                cur_name,
                cur_cost
            )
         )
with open(f"crypto_pages{n+1}.json", "w", encoding='utf-8') as file:
    json.dump(crypto_res_list, file, indent=4, ensure_ascii=False)
